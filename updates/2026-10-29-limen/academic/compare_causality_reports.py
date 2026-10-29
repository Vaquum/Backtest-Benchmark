"""Compare immutable per-revision receipts without importing either implementation."""
from hashlib import sha256
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASELINE = '29837e666604eee74a2ac94f328fb9803724342a'
LATEST = '25e47866422d007da55cb19625344183599ba671'
FIXTURE = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'


def main() -> None:
    paths = [ROOT / f'causal-prefix-{name}.json' for name in ('baseline', 'latest')]
    old, new = [json.loads(path.read_text()) for path in paths]
    if [old['repository_commit'], new['repository_commit']] != [BASELINE, LATEST]:
        raise SystemExit('Unexpected source revision')
    if any(report['fixture_sha256'] != FIXTURE for report in (old, new)):
        raise SystemExit('Unexpected recorded fixture')
    compared, failures, maximum = 0, [], 0.0
    for before, after in zip(old['asof_rows'], new['asof_rows'], strict=True):
        if (before['quantile'], before['cutoff']) != (after['quantile'], after['cutoff']):
            raise SystemExit('Oracle rows do not align')
        if before['prefix_last'].keys() != after['full_historical'].keys():
            raise SystemExit('Oracle columns do not align')
        for name, expected in before['prefix_last'].items():
            actual = after['full_historical'][name]
            compared += 1
            maximum = max(maximum, abs(actual - expected))
            if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12):
                failures.append({'quantile': before['quantile'], 'cutoff': before['cutoff'],
                                 'column': name, 'expected': expected, 'actual': actual})
    records = []
    for before, after in zip(old['expanded_cases'], new['expanded_cases'], strict=True):
        if before['params'] != after['params']:
            raise SystemExit('Prefix comparison parameters do not align')
        records.append({'params': before['params'], 'prefix_rows': 192, 'extended_rows': 384,
                        'baseline_changed_rows': before['rows_with_any_feature_change'],
                        'latest_changed_rows': after['rows_with_any_feature_change'],
                        'research_only_span_changes_baseline': before['research_only_column'],
                        'research_only_span_changes_latest': after['research_only_column']})
    result = {'baseline_commit': BASELINE, 'latest_commit': LATEST, 'fixture_sha256': FIXTURE,
              'receipt_sha256': {path.name: sha256(path.read_bytes()).hexdigest() for path in paths},
              'comparison_script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'original_case_changed_rows': {r['revision']: [x['rows_with_any_feature_change'] for x in r['original_probe_cases']] for r in (old, new)},
              'expanded_cases': records,
              'frozen_baseline_prefix_last_vs_latest_historical': {'rows': len(old['asof_rows']),
                  'scalar_values': compared, 'mismatches': failures, 'maximum_absolute_difference': maximum,
                  'relative_tolerance': 1e-12, 'absolute_tolerance': 1e-12},
              'both_flag_modes_have_identical_five_columns': all(x['five_common_columns_exactly_equal_across_flags'] for x in new['expanded_cases']),
              'scope': 'Bounded recorded-fixture causality and semantics regression; no general feature-causality or economic-validity claim.'}
    destination = ROOT / 'causal-prefix-comparison.json'
    with destination.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(result, indent=2))
    if failures or any(x['latest_changed_rows'] for x in records):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
