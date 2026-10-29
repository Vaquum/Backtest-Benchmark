from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description='Paired old/new Limen replay through byte-identical frozen benchmark workers')
    parser.add_argument('--mode', choices=('verify', 'run'), default='verify')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    plan_path = ROOT / 'paired-preregistration.json'
    plan = json.loads(plan_path.read_text())
    if digest(Path(__file__)) != plan['paired_driver_sha256']:
        raise ValueError('Paired driver differs from preregistration')
    if digest(Path(plan['input'])) != plan['input_sha256']:
        raise ValueError('Recorded fixture differs from preregistration')
    dependencies = []
    for variant, settings in plan['variants'].items():
        overlay = Path(settings['overlay'])
        for relative, expected in plan['benchmark_code_sha256'].items():
            if digest(overlay / relative) != expected:
                raise ValueError(f'Frozen runner changed: {variant}/{relative}')
        if digest(overlay / 'catalog/candidates.json') != settings['catalog_sha256']:
            raise ValueError(f'Frozen catalog changed: {variant}')
        setup = overlay / '.work/manifests/limen.json'
        if digest(setup) != settings['setup_manifest_sha256']:
            raise ValueError(f'Frozen install manifest changed: {variant}')
        manifest = json.loads(setup.read_text())
        dependencies.append([row for row in manifest['observed']['distributions']
                             if row['name'] != 'vaquum-limen'])
    if dependencies[0] != dependencies[1]:
        raise ValueError('Paired native dependency versions differ')

    sys.path.insert(0, plan['variants']['baseline']['overlay'])
    from bench.cli import aggregate_cases, run_process
    from bench.provenance import THREAD_ENV

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / 'preregistration.json').write_bytes(plan_path.read_bytes())
    report = {'schema_version': 1, 'mode': args.mode,
              'started_utc': datetime.now(timezone.utc).isoformat(),
              'preregistration_sha256': digest(plan_path), 'status': 'running',
              'commands': [], 'summaries': [], 'comparisons': []}
    report_path = output / 'paired_report.json'
    source_cases = {variant: [] for variant in plan['variants']}

    def save():
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')

    schedule = []
    if args.mode == 'verify':
        schedule = [(0, variant, ['buy_and_hold', 'sma_cross', 'flat'])
                    for variant in ('baseline', 'latest')]
    else:
        for block in range(plan['process_blocks']):
            strategies = plan['strategies'] if block % 2 == 0 else list(reversed(plan['strategies']))
            for strategy in strategies:
                order = ['baseline', 'latest'] if block % 2 == 0 else ['latest', 'baseline']
                if strategy == 'sma_cross':
                    order.reverse()
                schedule.extend((block + 1, variant, [strategy]) for variant in order)
    save()
    for sequence, (block, variant, strategies) in enumerate(schedule, 1):
        settings = plan['variants'][variant]
        label = f'{sequence:03d}-block-{block:02d}-{variant}-' + '-'.join(strategies)
        destination = output / label
        command = [settings['python'], '-m', 'bench', 'verify' if args.mode == 'verify' else 'run',
                   '--input', plan['input'], '--expected-sha256', plan['input_sha256'],
                   '--output', str(destination), '--engines', 'limen',
                   '--strategies', *strategies, '--rows', str(plan['evaluation_rows']),
                   '--env-root', settings['env_root'], '--processes', '1',
                   '--warm-repeats', str(plan['warm_calls_per_process']), '--diagnostic-core']
        environment = {**os.environ, **dict.fromkeys(THREAD_ENV, '1'),
                       'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONHASHSEED': '0'}
        environment.pop('PYTHONPATH', None)
        environment.pop('PYTHONHOME', None)
        print(f'{sequence}/{len(schedule)} {label}', flush=True)
        process = run_process(command, Path(settings['overlay']), environment,
                              output / (label + '-launcher'), timeout=1200)
        log = Path(process['stdout_path']).read_text()
        print(log, end='' if log.endswith('\n') else '\n', flush=True)
        record = {'block': block, 'variant': variant, 'strategies': strategies,
                  'process': process, 'report_path': str(destination / 'report.json')}
        if (destination / 'report.json').is_file():
            raw = json.loads((destination / 'report.json').read_text())
            record['report_sha256'] = digest(destination / 'report.json')
            record['case_statuses'] = [case['preflight_status'] for case in raw['cases']]
            source_cases[variant].extend(raw['cases'])
        report['commands'].append(record)
        save()

    complete = all(record['process']['returncode'] == 0 and not record['process']['timed_out']
                   and record.get('case_statuses') and all(status == 'verified' for status in record['case_statuses'])
                   for record in report['commands'])
    if args.mode == 'run':
        for variant, cases in source_cases.items():
            for strategy in plan['strategies']:
                selected = [case for case in cases if case['strategy'] == strategy]
                if not selected:
                    complete = False
                    continue
                merged = dict(selected[0])
                merged['measurements'] = [item for case in selected for item in case['measurements']]
                merged['requested_processes'] = plan['process_blocks']
                if len(selected) != plan['process_blocks'] or any(case['preflight_status'] != 'verified' for case in selected):
                    merged['preflight_status'] = 'incomplete_preflight'
                row = aggregate_cases([merged])[0]
                row.pop('relative_to_limen_warm_full_common', None)
                row.pop('relative_to_limen_interpretation', None)
                row.update(variant=variant, source_commit=plan['variants'][variant]['source_commit'])
                report['summaries'].append(row)
                complete = complete and row['status'] == 'verified'
        for strategy in plan['strategies']:
            rows = {row['variant']: row for row in report['summaries'] if row['strategy'] == strategy}
            if set(rows) == {'baseline', 'latest'} and all(row['status'] == 'verified' for row in rows.values()):
                report['comparisons'].append({
                    'strategy': strategy,
                    'latest_over_baseline_warm_full_common_duration':
                        rows['latest']['warm_full_common_ms_median'] / rows['baseline']['warm_full_common_ms_median'],
                    'scope': 'Same-host paired revisions only; no cross-date or competitor ratio',
                })
    report.update(status='verified' if complete else 'incomplete_or_failed',
                  finished_utc=datetime.now(timezone.utc).isoformat())
    save()
    print(report_path, flush=True)
    return 0 if complete else 2


if __name__ == '__main__':
    raise SystemExit(main())
