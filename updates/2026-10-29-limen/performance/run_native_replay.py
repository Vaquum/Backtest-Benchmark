from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def git(source, *arguments):
    return subprocess.check_output(['git', *arguments], cwd=source, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description='Run both unchanged native Limen harnesses at explicitly pinned old/new sources')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    plan_path = ROOT / 'native-preregistration.json'
    plan = json.loads(plan_path.read_text())
    if digest(Path(__file__)) != plan['native_driver_sha256']:
        raise ValueError('Native driver differs from preregistration')
    paired = json.loads((ROOT / 'paired-preregistration.json').read_text())
    for variant, settings in plan['variants'].items():
        source = Path(settings['source_path'])
        if git(source, 'rev-parse', 'HEAD') != settings['source_commit']:
            raise ValueError(f'Pinned source changed: {variant}')
        if git(source, 'status', '--porcelain', '--untracked-files=no'):
            raise ValueError(f'Tracked source is modified: {variant}')
        if digest(source / plan['fixture_relative_path']) != plan['fixture_sha256']:
            raise ValueError(f'Recorded fixture changed: {variant}')
        for relative, expected in settings['harness_files_sha256'].items():
            if digest(source / relative) != expected:
                raise ValueError(f'Native harness changed: {variant}/{relative}')
        overlay = Path(paired['variants'][variant]['overlay'])
        if digest(overlay / '.work/manifests/limen.json') != settings['setup_manifest_sha256']:
            raise ValueError(f'Install manifest changed: {variant}')
        for relative, expected in paired['benchmark_code_sha256'].items():
            if digest(overlay / relative) != expected:
                raise ValueError(f'Frozen process runner changed: {variant}/{relative}')

    sys.path.insert(0, paired['variants']['baseline']['overlay'])
    from bench.cli import run_process
    from bench.provenance import THREAD_ENV

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / 'preregistration.json').write_bytes(plan_path.read_bytes())
    report = {'schema_version': 1, 'status': 'running',
              'started_utc': datetime.now(timezone.utc).isoformat(),
              'preregistration_sha256': digest(plan_path),
              'source_execution': plan['source_execution'], 'runs': []}
    report_path = output / 'native_report.json'

    def save():
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')

    save()
    for sequence, item in enumerate(plan['run_order'], 1):
        variant, harness = item['variant'], item['harness']
        settings = plan['variants'][variant]
        source = Path(settings['source_path'])
        label = f'{sequence:02d}-{variant}-{harness}'
        destination = output / label
        command = [settings['python'], '-m',
                   'tests.benchmark_factorized_preparation' if harness == 'factorized' else 'tests.benchmark_backtest_strategies',
                   '--output', str(destination)]
        if harness == 'snapshot':
            command += ['--inputs', str(source / plan['fixture_relative_path']),
                        '--strategies', *plan['snapshot']['strategies'],
                        '--engines', 'limen', '--repeats', str(plan['snapshot']['warm_repeats'])]
        environment = {**os.environ, **dict.fromkeys(THREAD_ENV, '1'),
                       'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONHASHSEED': '0'}
        environment.pop('PYTHONPATH', None)
        environment.pop('PYTHONHOME', None)
        probe = 'import limen,json,sys; print(json.dumps({"limen_file":limen.__file__,"version":limen.__version__,"python":sys.executable}))'
        observed = json.loads(subprocess.check_output([settings['python'], '-c', probe], cwd=source, env=environment, text=True))
        if not Path(observed['limen_file']).resolve().is_relative_to(source):
            raise ValueError(f'Native source import is outside the pinned checkout: {variant}')
        print(f'{sequence}/{len(plan["run_order"])} {label}', flush=True)
        process = run_process(command, source, environment, output / (label + '-launcher'), timeout=600)
        result_path = destination / ('benchmark.json' if harness == 'factorized' else 'report.json')
        record = {**item, 'process': process, 'observed_import': observed,
                  'thread_environment': dict.fromkeys(THREAD_ENV, '1'),
                  'result_path': str(result_path)}
        verified = process['returncode'] == 0 and not process['timed_out']
        if result_path.exists():
            result = json.loads(result_path.read_text())
            record['result_sha256'] = digest(result_path)
            if harness == 'factorized':
                verified = verified and result.get('scientific_outputs_equal_at_12dp') is True
                record['scientific_outputs_equal_at_12dp'] = result.get('scientific_outputs_equal_at_12dp')
            else:
                verified = verified and result.get('status') == 'completed'
                record['native_status'] = result.get('status')
        else:
            verified = False
        record['tracked_source_clean_after'] = not git(source, 'status', '--porcelain', '--untracked-files=no')
        verified = verified and record['tracked_source_clean_after']
        record['status'] = 'verified' if verified else 'incomplete_or_failed'
        report['runs'].append(record)
        save()
        print(f'{label}: {record["status"]}; returncode={process["returncode"]}', flush=True)
    report.update(status='verified' if all(row['status'] == 'verified' for row in report['runs']) else 'incomplete_or_failed',
                  finished_utc=datetime.now(timezone.utc).isoformat())
    save()
    print(report_path, flush=True)
    return 0 if report['status'] == 'verified' else 2


if __name__ == '__main__':
    raise SystemExit(main())
