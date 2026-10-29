#!/usr/bin/env python3
"""Pinned, local-only old/new safety boundary probes; never invokes escaped callables."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from hashlib import sha256
import importlib.metadata
import json
import math
import os
from pathlib import Path
import resource
import selectors
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path('/workspace/scratch/008a76ec4981')
SAFE = ROOT / 'Backtest-Benchmark/updates/2026-10-29-limen/safety'
SOURCES = {
    'baseline': ('Limen-baseline', '29837e666604eee74a2ac94f328fb9803724342a'),
    'latest': ('Limen', '25e47866422d007da55cb19625344183599ba671'),
}
FIXTURE = 'tests/fixtures/spot_1h_20240101_20241231.parquet'
FIXTURE_SHA256 = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'
THREAD_ENV = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
              'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS',
              'RAYON_NUM_THREADS', 'POLARS_MAX_THREADS')
for name in THREAD_ENV:
    os.environ[name] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True


def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()


def admit(label):
    directory, expected = SOURCES[label]
    source = ROOT / directory
    head = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    dirty = subprocess.check_output(['git', '-C', str(source), 'status', '--porcelain', '--untracked-files=no'], text=True)
    if head != expected or dirty:
        raise RuntimeError('Source SHA or tracked-file identity differs from the admitted snapshot')
    if file_hash(source / FIXTURE) != FIXTURE_SHA256:
        raise RuntimeError('Recorded market fixture identity differs')
    sys.path.insert(0, str(source))
    import limen
    if not Path(limen.__file__).resolve().is_relative_to(source.resolve()):
        raise RuntimeError('Imported Limen is not the admitted source')
    return source


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return 'NaN' if math.isnan(value) else ('+Infinity' if value > 0 else '-Infinity')
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if hasattr(value, 'isoformat'):
        return value.isoformat()
    if hasattr(value, 'item'):
        return clean(value.item())
    return value


def observation(call):
    try:
        result = call()
        return {'outcome': 'returned', 'result': clean(result)}
    except Exception as exc:
        return {'outcome': 'raised', 'exception': type(exc).__name__, 'message': str(exc)}


def resolver_probe(source):
    import os as operating_system
    from limen.yaml.compiler import build_manifest
    from limen.yaml.parser import parse
    from limen.yaml.resolver import resolve
    from limen.yaml.validator import validate
    template = source / 'limen/yaml/templates/rule_based.yaml'
    document, errors = parse(template.read_text())
    if errors or not validate(document).valid:
        raise AssertionError('Unmodified native template failed the positive control')
    path = 'limen.data.historical_data.os.system'
    lookup = observation(lambda: {'is_os_system': resolve(path) is operating_system.system})
    positive = observation(lambda: {'callable': callable(resolve('limen.data.HistoricalData.get_any_file'))})
    document['sfd']['manifest']['data_source']['method'] = path
    validation = validate(document)
    binding = observation(lambda: {'bound_is_os_system': build_manifest(document).data_source_config.method is operating_system.system})
    return {'template_sha256': file_hash(template), 'lookup': lookup, 'allowed_lookup': positive,
            'modified_manifest_valid': validation.valid, 'binding': binding,
            'escaped_callable_invoked': False}


def store_probe(source):
    from limen.yaml.config import round_trip_yaml
    from limen.yaml.store import canonical_manifest_id, commit_manifest, resolve_manifest_uri
    template = source / 'limen/yaml/templates/rule_based.yaml'
    with tempfile.TemporaryDirectory(prefix='store-probe-', dir=SAFE) as directory:
        root = Path(directory)
        (root / 'limen.toml').write_text('[store]\nbackup_remote = ""\n')
        working = root / 'source.yaml'
        working.write_bytes(template.read_bytes())
        identity, existed = commit_manifest(working, root)
        assert existed is False
        assert commit_manifest(working, root) == (identity, True)
        target = root / 'manifests/committed' / (identity.removeprefix('sha256:') + '.yaml')
        index = target.parent / 'index.json'
        parser = round_trip_yaml()
        document = parser.load(target.read_text())
        original_id = document['lineage']['id']
        document['metadata']['name'] += '_content_mutation_probe'
        with target.open('w') as stream:
            parser.dump(document, stream)
        assert document['lineage']['id'] == original_id == identity
        assert canonical_manifest_id(document) != identity
        target_before, index_before = target.read_bytes(), index.read_bytes()
        target_mtime, index_mtime = target.stat().st_mtime_ns, index.stat().st_mtime_ns
        full = observation(lambda: str(resolve_manifest_uri('manifest://' + identity, root)[0].relative_to(root)))
        short = observation(lambda: str(resolve_manifest_uri('manifest://' + identity[:15], root)[0].relative_to(root)))
        reuse = observation(lambda: commit_manifest(working, root))
        return {'template_sha256': file_hash(template), 'valid_idempotent_control': True,
                'retained_filename_and_lineage_id': True, 'canonical_content_changed': True,
                'full_uri': full, 'short_uri': short, 'commit_reuse': reuse,
                'stored_bytes_unchanged_after_checks': target.read_bytes() == target_before,
                'index_bytes_unchanged_after_checks': index.read_bytes() == index_before,
                'stored_mtime_unchanged_after_checks': target.stat().st_mtime_ns == target_mtime,
                'index_mtime_unchanged_after_checks': index.stat().st_mtime_ns == index_mtime}


def ffd_child(label, case):
    source = admit(label)
    import polars as pl
    from limen.features.fractional_diff import _get_weights_ffd, fractional_diff
    data = pl.read_parquet(source / FIXTURE).head(8)
    vm_bytes = int(Path('/proc/self/statm').read_text().split()[0]) * os.sysconf('SC_PAGE_SIZE')
    limit = vm_bytes + 32 * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    used_cpu = math.ceil(time.process_time())
    resource.setrlimit(resource.RLIMIT_CPU, (used_cpu + 1, used_cpu + 2))
    print(json.dumps({'phase': 'ready', 'address_space_limit_bytes': limit,
                      'additional_virtual_bytes': 32 * 1024 * 1024}), flush=True)
    if sys.stdin.readline().strip() != 'go':
        raise RuntimeError('Missing parent execution handshake')
    calls = {
        'public_nan_d': lambda: fractional_diff(data, d=float('nan'), threshold=.1, cols=['close']).height,
        'public_nan_threshold': lambda: fractional_diff(data, d=.5, threshold=float('nan'), cols=['close']).height,
        'public_zero_nan_threshold': lambda: fractional_diff(data, d=0., threshold=float('nan'), cols=['close']).height,
        'private_nan_d': lambda: _get_weights_ffd(float('nan'), .1).tolist(),
        'private_finite_overflow': lambda: _get_weights_ffd(1e308, .1).tolist(),
    }
    print(json.dumps(observation(calls[case]), allow_nan=False), flush=True)


def bounded_ffd(label, case):
    command = [sys.executable, '-B', str(Path(__file__).resolve()), '--label', label, '--ffd-child', case]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, start_new_session=True,
                               cwd=ROOT / SOURCES[label][0], env=os.environ.copy())
    try:
        with selectors.DefaultSelector() as ready:
            ready.register(process.stdout, selectors.EVENT_READ)
            if not ready.select(timeout=45):
                raise RuntimeError('FFD child did not finish imports before startup deadline')
        line = process.stdout.readline()
        if not line:
            raise RuntimeError('FFD child exited before ready: ' + process.stderr.read())
        controls = json.loads(line)
        if controls.get('phase') != 'ready':
            raise RuntimeError('Invalid FFD startup receipt')
        start = time.monotonic()
        try:
            stdout, stderr = process.communicate('go\n', timeout=.35)
            result = json.loads(stdout) if stdout.strip() else {'outcome': 'child_exit', 'returncode': process.returncode}
            result['stderr'] = stderr
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate(timeout=5)
            result = {'outcome': 'external_deadline', 'returncode': process.returncode,
                      'stdout_after_ready': stdout, 'stderr': stderr}
        result.update(case=case, controls=controls, execution_deadline_seconds=.35,
                      elapsed_after_ready_seconds=time.monotonic() - start,
                      child_reaped=process.poll() is not None)
        return result
    finally:
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate(timeout=5)


def ffd_probe(source, label):
    import polars as pl
    import numpy as np
    from limen.features.fractional_diff import fractional_diff
    raw = pl.read_parquet(source / FIXTURE).head(8)
    close = raw['close'].to_numpy()
    controls = []
    for d in (0., 1., .5):
        result = fractional_diff(raw, d=d, threshold=.2, cols=['close'])['close_fracdiff'].to_list()
        expected = close.tolist() if d == 0. else [None] + (close[1:] - (.5 if d == .5 else 1.) * close[:-1]).tolist()
        assert [v is None for v in result] == [v is None for v in expected]
        np.testing.assert_allclose([v for v in result if v is not None], [v for v in expected if v is not None])
        controls.append({'d': d, 'threshold': .2, 'matches_independent_short_formula': True})
    cases = ['public_nan_d', 'public_nan_threshold', 'public_zero_nan_threshold',
             'private_nan_d', 'private_finite_overflow']
    return {'finite_recorded_controls': controls, 'cases': [bounded_ffd(label, case) for case in cases],
            'scope': 'Nonfinite admission and overflow termination only; no bound claimed for all finite workloads.'}


def sensor_probe(source):
    import numpy as np
    import polars as pl
    from limen.experiment.manifest_core import MLManifest
    from limen.inference.sensor import Sensor
    raw = pl.read_parquet(source / FIXTURE).head(8)

    class OutputCanary:
        prediction_mode = 'binary'
        def __init__(self, prediction, probability):
            self.prediction, self.probability = prediction, probability
            self.calls = []
        def predict(self, data):
            n = len(data['x_test'])
            self.calls.append(n)
            result = {'_preds': np.array([self.prediction] * n)}
            if self.probability is not None:
                result['_probs'] = np.array([self.probability] * n)
            return result

    cases = [('valid', 1., .5), ('valid_missing_probability', 1., None),
             ('nan_prediction', float('nan'), .5), ('infinite_prediction', float('inf'), .5),
             ('nan_probability', 1., float('nan')), ('high_probability', 1., 1.1),
             ('boolean_prediction', True, .5), ('boolean_probability', 1., True)]
    results = []
    for name, prediction, probability in cases:
        model = OutputCanary(prediction, probability)
        sensor = Sensor(yaml_reference={}, model=model, fitted_params={}, round_params={'bar_type': 'base'})
        sensor._manifest = MLManifest().set_split_config(3, 1, 1)
        batch = sensor.predict_all(raw)
        single = sensor.predict(raw)
        assert model.calls == [raw.height, 1], (name, model.calls)
        assert len(batch) == raw.height
        assert [row.datetime for row in batch] == raw['datetime'].to_list()
        assert single.datetime == raw['datetime'][-1]
        if name.startswith('valid'):
            assert all(row.reason is None and row.prediction == 1. for row in batch)
            assert single.reason is None and single.prediction == 1.
        results.append({'case': name, 'model_call_row_counts': model.calls,
                        'batch_rows': len(batch), 'batch_reasons': [row.reason for row in batch],
                        'single': clean(asdict(single)), 'last_batch': clean(asdict(batch[-1])),
                        'recorded_datetime_alignment_preserved': True})
    return {'fixture_rows': raw.height, 'cases': results,
            'scope': 'Actual compiled Sensor predict/predict_all with native MLManifest preparation; explicitly synthetic invalid-output canaries, not learned forecasts or evaluation outcomes. No model fitting or quality claim.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', choices=tuple(SOURCES), required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--ffd-child')
    args = parser.parse_args()
    if args.ffd_child:
        ffd_child(args.label, args.ffd_child)
        return
    if args.output is None or not args.output.resolve().is_relative_to(SAFE.resolve()):
        parser.error('Output must be inside the dedicated safety update directory')
    if args.output.exists():
        raise FileExistsError(args.output)
    source = admit(args.label)
    result = {'label': args.label, 'source_sha': SOURCES[args.label][1], 'source_root': str(source),
              'probe_sha256': file_hash(Path(__file__)), 'fixture_path': FIXTURE,
              'fixture_sha256': FIXTURE_SHA256, 'python': sys.version, 'executable': sys.executable,
              'dependencies': {n: importlib.metadata.version(n) for n in ['numpy', 'polars', 'scikit-learn', 'ruamel.yaml']},
              'thread_environment': {n: os.environ[n] for n in THREAD_ENV}}
    for name, callback in [('resolver', lambda: resolver_probe(source)), ('manifest_store', lambda: store_probe(source)),
                           ('fractional_difference', lambda: ffd_probe(source, args.label)), ('compiled_sensor', lambda: sensor_probe(source))]:
        result[name] = callback()
        print(json.dumps({'label': args.label, 'completed_boundary': name}), flush=True)
    _ = admit(args.label)
    result['source_and_fixture_rechecked_after'] = True
    with args.output.open('x') as stream:
        json.dump(clean(result), stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'saved': str(args.output)}), flush=True)


if __name__ == '__main__':
    main()
