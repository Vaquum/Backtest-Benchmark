from __future__ import annotations

import argparse
from datetime import datetime, timezone
import gc
from hashlib import sha256
import json
import os
from pathlib import Path
import resource
import sys
import time
import traceback

EVENT_PREFIX = '@@BENCH_EVENT@@'


def event(name: str):
    print(EVENT_PREFIX + json.dumps({'event': name, 'worker_perf_counter_ns': time.perf_counter_ns()}), flush=True)


def peak_rss_bytes():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == 'darwin' else raw * 1024)


def main() -> int:
    event('ready')
    parser = argparse.ArgumentParser(description='One isolated candidate worker; use python -m bench for orchestration')
    parser.add_argument('--engine', required=True)
    parser.add_argument('--prepared', type=Path, required=True)
    parser.add_argument('--prepared-sha256', required=True)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--environment-manifest', type=Path, required=True)
    parser.add_argument('--benchmark-code-manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mode', choices=('preflight', 'measure'), default='preflight')
    parser.add_argument('--warm-repeats', type=int, default=9)
    parser.add_argument('--diagnostic-core', action='store_true')
    args = parser.parse_args()
    if args.warm_repeats < 1:
        raise ValueError('warm-repeats must be positive')
    args.output.mkdir(parents=True, exist_ok=False)
    report = {'schema_version': 1, 'engine': args.engine, 'mode': args.mode,
              'started_utc': datetime.now(timezone.utc).isoformat(), 'status': 'starting',
              'timing_samples': [], 'core_diagnostic_samples': [],
              'measurement_policy': 'Untimed preflight precedes independent fresh timed worker; each timed result is checked outside its timed region'}
    report_path = args.output / 'worker.json'

    def persist():
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')

    try:
        from bench.provenance import THREAD_ENV, verify_source_install, runtime_environment, verify_import_location
        if any(os.environ.get(name) != '1' for name in THREAD_ENV):
            raise ValueError('Every declared native thread limit must be fixed to one before worker startup')
        root = Path(__file__).resolve().parents[1]
        code_manifest = json.loads(args.benchmark_code_manifest.read_text())
        for relative, expected_hash in code_manifest.items():
            if sha256((root / relative).read_bytes()).hexdigest() != expected_hash:
                raise ValueError(f'Benchmark code changed during the campaign: {relative}')
        report['benchmark_code_manifest_sha256'] = sha256(args.benchmark_code_manifest.read_bytes()).hexdigest()
        start = time.perf_counter_ns()
        report['provenance'] = verify_source_install(args.engine, root, args.environment_manifest)
        report['source_verification_ms'] = (time.perf_counter_ns() - start) / 1e6
        if sha256(args.prepared.read_bytes()).hexdigest() != args.prepared_sha256:
            raise ValueError('Prepared-input byte hash differs from the orchestrator declaration')
        import numpy as np
        from bench.adapters import create_adapter
        from bench.api import UnsupportedContract
        from bench.contract import Contract, assert_parity, reference_result, result_summary, save_result
        from bench.data import array_digest

        start = time.perf_counter_ns()
        with np.load(args.prepared, allow_pickle=False) as loaded:
            data = {name: loaded[name] for name in loaded.files}
        input_digest = array_digest(data)
        contract = Contract.from_dict(json.loads(args.contract.read_text()))
        report['prepared_load_ms'] = (time.perf_counter_ns() - start) / 1e6
        report['prepared_arrays_sha256'] = input_digest
        report['contract'] = contract.to_dict()
        start = time.perf_counter_ns()
        expected = reference_result(data, contract)
        report['oracle_ms'] = (time.perf_counter_ns() - start) / 1e6
        save_result(args.output / 'oracle.npz', expected)
        start = time.perf_counter_ns()
        adapter = create_adapter(args.engine, data, contract)
        report['adapter_prepare_ms'] = (time.perf_counter_ns() - start) / 1e6
        report['provenance']['observed_candidate_imports'] = verify_import_location(args.engine)
        report['engine_scope'] = adapter.engine_scope
        report['settings'] = adapter.settings
        report['output_observation'] = adapter.output_observation
        report['rank_against_full_engine'] = adapter.settings.get('rank_against_full_engine', True)
        report['runtime'] = runtime_environment()
        try:
            from threadpoolctl import threadpool_info
            report['runtime']['threadpools'] = threadpool_info()
            if any(row.get('num_threads', 1) > 1 for row in report['runtime']['threadpools']):
                raise ValueError('A loaded native threadpool exceeds the fixed one-thread protocol')
        except ModuleNotFoundError:
            report['runtime']['threadpools'] = 'threadpoolctl unavailable; environment limits retained'

        def execute(run, extract, phase, destination):
            # Collection is outside the interval; within-call allocations and any
            # collections they trigger remain part of the engine's real work.
            gc.collect()
            cpu_start, start = time.process_time_ns(), time.perf_counter_ns()
            native = run()
            executed, cpu_executed = time.perf_counter_ns(), time.process_time_ns()
            actual = extract(native)
            summary = result_summary(actual, contract)
            finish, cpu_finish = time.perf_counter_ns(), time.process_time_ns()
            provisional = {'phase': phase, 'engine_ms': (executed - start) / 1e6,
                           'extraction_common_ms': (finish - executed) / 1e6,
                           'full_common_ms': (finish - start) / 1e6,
                           'engine_cpu_ms': (cpu_executed - cpu_start) / 1e6,
                           'full_common_cpu_ms': (cpu_finish - cpu_start) / 1e6}
            if args.mode == 'measure':
                destination.append(provisional)
            parity = assert_parity(actual, expected, contract)
            parity['actual_result_arrays_sha256'] = array_digest(
                {name: getattr(actual, name) for name in actual.__dataclass_fields__
                 if getattr(actual, name) is not None})
            if array_digest(data) != input_digest:
                raise AssertionError('Candidate modified the prepared market/signal arrays')
            provisional['parity'] = parity
            provisional['admitted'] = True
            return actual, summary, parity

        actual, summary, parity = execute(adapter.run, adapter.extract, 'first', report['timing_samples'])
        report.update(summary=summary, parity=parity, status='verified')
        report['peak_rss_bytes_after_first'] = peak_rss_bytes()
        event('first_valid')
        save_result(args.output / 'actual.npz', actual)
        persist()
        if args.mode == 'measure':
            for repetition in range(args.warm_repeats):
                execute(adapter.run, adapter.extract, f'warm-{repetition + 1}', report['timing_samples'])
                persist()
        report['peak_rss_bytes_after_full_calls'] = peak_rss_bytes()
        if args.diagnostic_core and adapter.core is not None:
            report['core_diagnostic_scope'] = adapter.core.scope
            phases = ['first'] + ([f'warm-{number + 1}' for number in range(args.warm_repeats)] if args.mode == 'measure' else [])
            for phase in phases:
                execute(adapter.core.run, adapter.core.extract, phase, report['core_diagnostic_samples'])
                persist()
        report['peak_rss_bytes_final'] = peak_rss_bytes()
        report['rss_scope'] = 'Process lifetime high-water memory, including imports, validation, all repetitions, and optional separately labeled core diagnostics; Linux KiB converted to bytes, macOS bytes unchanged'
        report['status'] = 'verified'
        persist()
        event('complete')
        return 0
    except Exception as error:
        name = type(error).__name__
        if name == 'UnsupportedContract':
            status = 'unsupported_contract'
        elif name == 'AdapterUnavailable':
            status = 'adapter_unavailable'
        elif isinstance(error, (ModuleNotFoundError, ImportError)):
            status = 'unavailable'
        elif isinstance(error, AssertionError):
            status = 'parity_failed'
        else:
            status = 'error'
        report.update(status=status, error=f'{name}: {error}', traceback=traceback.format_exc(),
                      timings_admitted=False, peak_rss_bytes_final=peak_rss_bytes())
        persist()
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
