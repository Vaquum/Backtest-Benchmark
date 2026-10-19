from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import selectors
import signal
import statistics
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENGINES = ['limen', 'backtrader', 'vectorbt', 'backtesting_py', 'bt', 'qstrader']
EVENT_PREFIX = '@@BENCH_EVENT@@'


def run_process(command, cwd: Path, environment: dict, directory: Path, timeout: float) -> dict:
    directory.mkdir(parents=True, exist_ok=False)
    launch = time.perf_counter_ns()
    child = subprocess.Popen(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, start_new_session=True)
    events, timed_out, buffered = {}, False, b''
    selector = selectors.DefaultSelector()
    selector.register(child.stdout, selectors.EVENT_READ)
    with (directory / 'stdout.log').open('wb') as log:
        while selector.get_map():
            elapsed = (time.perf_counter_ns() - launch) / 1e9
            if elapsed > timeout and not timed_out:
                timed_out = True
                try:
                    os.killpg(child.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            if timed_out and elapsed > timeout + 2:
                # A descendant retaining the pipe must not block the parent
                # forever, even when its original worker has already exited.
                for key in list(selector.get_map().values()):
                    selector.unregister(key.fileobj)
                    key.fileobj.close()
                if child.poll() is None:
                    child.kill()
                break
            for key, _ in selector.select(timeout=0.1):
                chunk = os.read(key.fileobj.fileno(), 65536)
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                log.write(chunk)
                log.flush()
                buffered += chunk
                while b'\n' in buffered:
                    line, buffered = buffered.split(b'\n', 1)
                    text = line.decode('utf-8', errors='replace')
                    if text.startswith(EVENT_PREFIX):
                        try:
                            name = json.loads(text[len(EVENT_PREFIX):])['event']
                            events.setdefault(name, (time.perf_counter_ns() - launch) / 1e6)
                        except (ValueError, KeyError):
                            pass
        returncode = child.wait()
    selector.close()
    record = {'command': command, 'returncode': returncode, 'timed_out': timed_out,
              'process_wall_ms': (time.perf_counter_ns() - launch) / 1e6,
              'launch_to_ready_ms': events.get('ready'),
              'launch_to_first_valid_ms': events.get('first_valid'),
              'parent_observed_events_ms': events, 'stdout_path': str(directory / 'stdout.log'),
              'startup_scope': 'Parent observed process launch to worker ready event, before scientific/engine imports; IPC scheduling is included',
              'first_valid_scope': 'Process launch through source verification, imports, input load, independent oracle, first engine call, extraction and successful parity'}
    (directory / 'process.json').write_text(json.dumps(record, indent=2) + '\n')
    return record


def aggregate_cases(cases: list[dict]) -> list[dict]:
    rows = []
    for case in cases:
        workers = [item['worker'] for item in case['measurements']
                   if item.get('worker', {}).get('status') == 'verified' and item['process']['returncode'] == 0]
        complete = (case['preflight_status'] == 'verified'
                    and len(workers) == case.get('requested_processes', 0) and bool(workers))
        row = {'engine': case['engine'], 'strategy': case['strategy'],
               'status': 'verified' if complete else case['preflight_status'] if not case['measurements'] else 'incomplete_measurements',
               'rank_against_full_engine': case.get('rank_against_full_engine', False),
               'independent_processes': len(workers),
               'equity_samples': case.get('preflight', {}).get('worker', {}).get('parity', {}).get('equity_samples_checked'),
               'fills_checked': case.get('preflight', {}).get('worker', {}).get('parity', {}).get('fills_checked'),
               'first_full_common_ms_median': None, 'warm_full_common_ms_median': None,
               'warm_engine_ms_median': None, 'warm_extraction_common_ms_median': None,
               'warm_full_common_cpu_ms_median': None, 'peak_rss_bytes_median': None,
               'launch_to_ready_ms_median': None, 'launch_to_first_valid_ms_median': None,
               'warm_full_common_ms_samples': [], 'first_full_common_ms_samples': [],
               'warm_process_medians_ms': [], 'relative_to_limen_warm_full_common': None,
               'warm_process_median_ms_min': None, 'warm_process_median_ms_max': None,
               'warm_full_common_call_ms_min': None, 'warm_full_common_call_ms_max': None,
               'first_full_common_ms_min': None, 'first_full_common_ms_max': None,
               'warm_evaluation_bars_per_second': None,
               'relative_to_limen_interpretation': 'Candidate duration divided by Limen duration; only complete same-contract full-engine cases qualify'}
        if complete:
            warm = [[sample for sample in worker['timing_samples'] if sample['phase'].startswith('warm-')] for worker in workers]
            first = [worker['timing_samples'][0]['full_common_ms'] for worker in workers]
            process_medians = [statistics.median(sample['full_common_ms'] for sample in block) for block in warm]
            row.update(first_full_common_ms_median=statistics.median(first),
                       first_full_common_ms_samples=first, warm_process_medians_ms=process_medians,
                       first_full_common_ms_min=min(first), first_full_common_ms_max=max(first),
                       warm_full_common_ms_median=statistics.median(process_medians),
                       warm_process_median_ms_min=min(process_medians), warm_process_median_ms_max=max(process_medians),
                       warm_full_common_call_ms_min=min(sample['full_common_ms'] for block in warm for sample in block),
                       warm_full_common_call_ms_max=max(sample['full_common_ms'] for block in warm for sample in block),
                       warm_full_common_ms_samples=[[sample['full_common_ms'] for sample in block] for block in warm],
                       peak_rss_bytes_median=statistics.median(worker['peak_rss_bytes_after_full_calls'] for worker in workers))
            if row['equity_samples'] is not None:
                row['warm_evaluation_bars_per_second'] = row['equity_samples'] * 1000 / row['warm_full_common_ms_median']
            for key in ('engine_ms', 'extraction_common_ms', 'full_common_cpu_ms'):
                row['warm_' + key + '_median'] = statistics.median(statistics.median(sample[key] for sample in block) for block in warm)
            for key in ('launch_to_ready_ms', 'launch_to_first_valid_ms'):
                values = [item['process'][key] for item in case['measurements']]
                row[key + '_median'] = statistics.median(values) if all(value is not None for value in values) else None
        rows.append(row)
    baseline = {row['strategy']: row for row in rows if row['engine'] == 'limen'
                and row['status'] == 'verified' and row['warm_full_common_ms_median'] is not None}
    for row in rows:
        if (row['status'] == 'verified' and row['rank_against_full_engine']
                and row['warm_full_common_ms_median'] is not None and row['strategy'] in baseline):
            row['relative_to_limen_warm_full_common'] = row['warm_full_common_ms_median'] / baseline[row['strategy']]['warm_full_common_ms_median']
    return rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='Frozen-source, real-data, correctness-gated backtest comparisons')
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('verify', 'run'):
        command = commands.add_parser(name, help='Untimed isolated parity checks' if name == 'verify' else 'Preflight followed by fresh independently timed process blocks')
        command.add_argument('--input', type=Path, required=True)
        command.add_argument('--expected-sha256', required=True, help='Mandatory expected hash of the entire recorded input file')
        command.add_argument('--output', type=Path, required=True, help='A new directory; existing evidence is never overwritten')
        command.add_argument('--engines', nargs='+', default=DEFAULT_ENGINES)
        command.add_argument('--strategies', nargs='+', choices=('buy_and_hold', 'sma_cross', 'flat'), default=['buy_and_hold', 'sma_cross'])
        command.add_argument('--rows', type=int, help='Evaluation prefix length; consumes one additional unchanged real settlement row')
        command.add_argument('--env-root', type=Path, default=ROOT / '.work/envs')
        command.add_argument('--timestamp-column', default='datetime')
        command.add_argument('--timestamp-semantics', choices=('bar_open', 'bar_close'), default='bar_open')
        command.add_argument('--interval-seconds', type=int, default=3600)
        command.add_argument('--initial-cash', type=float, default=1_000_000)
        command.add_argument('--fee-bps', type=float, default=0)
        command.add_argument('--slippage-bps', type=float, default=0)
        command.add_argument('--processes', type=int, default=5)
        command.add_argument('--warm-repeats', type=int, default=9)
        command.add_argument('--timeout-seconds', type=float, default=300)
        command.add_argument('--diagnostic-core', action='store_true')
    args = parser.parse_args(argv)
    if args.processes < 1 or args.warm_repeats < 1 or not 0 < args.timeout_seconds < float('inf'):
        parser.error('processes, warm-repeats and timeout must be finite and positive')
    from bench.contract import Contract
    from bench.data import prepare_scenario, read_recorded_bars
    from bench.provenance import THREAD_ENV

    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=False)
    catalog = {row['id']: row for row in json.loads((ROOT / 'catalog/candidates.json').read_text())}
    if len(set(args.engines)) != len(args.engines) or any(engine not in catalog for engine in args.engines):
        parser.error('Engines must be unique identifiers from catalog/candidates.json')
    if len(set(args.strategies)) != len(args.strategies):
        parser.error('Strategies must be unique')
    contract = Contract(initial_cash=args.initial_cash, fee_bps=args.fee_bps, slippage_bps=args.slippage_bps)
    contract_path = args.output / 'contract.json'
    contract_path.write_text(json.dumps(contract.to_dict(), indent=2) + '\n')
    report = {'schema_version': 1, 'command': args.command, 'started_utc': datetime.now(timezone.utc).isoformat(),
              'contract': contract.to_dict(), 'arguments': {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
              'cases': [], 'execution_order': [], 'aggregation': 'Median of within-process warm medians; fresh-process first calls separate; no outlier removal',
              'protocol': {'native_threads': 1, 'fresh_jit_cache_directory_per_worker': True,
                           'preflight_process_separate_from_measurement': True,
                           'balanced_blocks': 'Rotate engine order by block index; reverse it for odd-indexed strategies; alternate strategy order between blocks. Mirrored two-strategy cases balance mean engine position jointly; five blocks cover only five of seven positions within each strategy.',
                           'signals_outside_engine_interval': True,
                           'parity_outside_engine_interval': True,
                           'garbage_collection': 'Explicit gc.collect before each call is outside its timed interval; collections triggered during calls remain included',
                           'scope_warning': 'Full engines perform different native extra work; engine_scope and settings must accompany comparisons. Native-component and internal-core calls never receive full-engine ratios.'}}
    code = {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest() for path in sorted((ROOT / 'bench').rglob('*.py'))}
    report['benchmark_code_sha256'] = code
    code_manifest_path = args.output / 'benchmark-code.json'
    code_manifest_path.write_text(json.dumps(code, indent=2) + '\n')
    report_path = args.output / 'report.json'

    def persist():
        report['summary'] = aggregate_cases(report['cases'])
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
        if report['summary']:
            scalar_fields = [name for name, value in report['summary'][0].items() if not isinstance(value, (list, dict))]
            with (args.output / 'summary.csv').open('w', newline='') as handle:
                writer = csv.DictWriter(handle, scalar_fields, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(report['summary'])

    try:
        data, metadata = read_recorded_bars(args.input, evaluation_rows=args.rows,
                                           expected_sha256=args.expected_sha256,
                                           timestamp_column=args.timestamp_column,
                                           timestamp_semantics=args.timestamp_semantics,
                                           interval_seconds=args.interval_seconds)
        report['input'] = metadata
    except Exception as error:
        report.update(status='input_rejected', error=f'{type(error).__name__}: {error}')
        persist()
        raise
    scenarios = {}
    for strategy in args.strategies:
        scenarios[strategy] = prepare_scenario(data, strategy, args.output / f'prepared-{strategy}.npz')
    report['scenarios'] = scenarios

    def worker(case, mode, number):
        engine, strategy = case['engine'], case['strategy']
        directory = args.output / engine / strategy / ('preflight' if mode == 'preflight' else f'process-{number:03d}')
        python = args.env_root.resolve() / engine / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        manifest_candidates = [ROOT / '.work/manifests' / f'{engine}.json', ROOT / '.work/setup' / engine / 'manifest.json']
        manifest = next((path for path in manifest_candidates if path.is_file()), manifest_candidates[0])
        if not python.is_file() or not manifest.is_file():
            directory.mkdir(parents=True)
            failure = {'status': 'environment_missing', 'error': f'Need built frozen-source environment {python} and setup manifest {manifest}'}
            (directory / 'failure.json').write_text(json.dumps(failure, indent=2) + '\n')
            return {'worker': failure, 'process': {'returncode': None}, 'directory': str(directory)}
        scenario = scenarios[strategy]
        command = [str(python), '-m', 'bench.worker', '--engine', engine, '--prepared', scenario['prepared_path'],
                   '--prepared-sha256', scenario['prepared_file_sha256'], '--contract', str(contract_path),
                   '--environment-manifest', str(manifest), '--output', str(directory / 'result'),
                   '--benchmark-code-manifest', str(code_manifest_path),
                   '--mode', mode, '--warm-repeats', str(args.warm_repeats)]
        if args.diagnostic_core:
            command.append('--diagnostic-core')
        environment = {**os.environ, **{name: '1' for name in THREAD_ENV},
                       'PYTHONHASHSEED': '0', 'PYTHONDONTWRITEBYTECODE': '1',
                       'NUMBA_CACHE_DIR': str(directory / 'numba-cache')}
        environment.pop('PYTHONPATH', None)
        environment.pop('PYTHONHOME', None)
        report['execution_order'].append({'engine': engine, 'strategy': strategy, 'mode': mode, 'process_block': number})
        process = run_process(command, ROOT, environment, directory, args.timeout_seconds)
        result_path = directory / 'result/worker.json'
        observed = json.loads(result_path.read_text()) if result_path.is_file() else {'status': 'worker_failed', 'error': 'Worker ended without a result; inspect preserved stdout/process logs'}
        if process['timed_out']:
            observed['status'] = 'timed_out'
        return {'worker': observed, 'process': process, 'directory': str(directory)}

    for strategy in args.strategies:
        for engine in args.engines:
            case = {'engine': engine, 'strategy': strategy, 'measurements': [],
                    'requested_processes': args.processes if args.command == 'run' else 0}
            report['cases'].append(case)
            print(f'Preflight {engine}/{strategy}', flush=True)
            observed = worker(case, 'preflight', 0)
            case.update(preflight=observed, preflight_status=observed['worker']['status'],
                        rank_against_full_engine=observed['worker'].get('rank_against_full_engine', False))
            persist()
    if args.command == 'run':
        for number in range(args.processes):
            offset = number % len(args.engines)
            rotation = args.engines[offset:] + args.engines[:offset]
            strategies = args.strategies if number % 2 == 0 else list(reversed(args.strategies))
            for strategy in strategies:
                ordered = rotation if args.strategies.index(strategy) % 2 == 0 else list(reversed(rotation))
                for engine in ordered:
                    case = next(item for item in report['cases'] if item['engine'] == engine and item['strategy'] == strategy)
                    if case['preflight_status'] != 'verified':
                        continue
                    print(f'Measure {engine}/{strategy} process {number + 1}/{args.processes}', flush=True)
                    case['measurements'].append(worker(case, 'measure', number + 1))
                    persist()
    report['status'] = 'completed'
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    persist()
    print(str(report_path))
    return 0 if all(case['preflight_status'] in ('verified', 'unsupported_contract')
                    and all(item.get('worker', {}).get('status') == 'verified' for item in case['measurements'])
                    for case in report['cases']) else 2


if __name__ == '__main__':
    raise SystemExit(main())
