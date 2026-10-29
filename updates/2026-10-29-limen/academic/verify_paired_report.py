"""Standard-library verification of retained paired results; imports no engines."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path
from statistics import median


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.campaign.resolve(strict=True)
    assert not args.output.exists()
    path = root / 'paired_report.json'
    report = json.loads(path.read_text())
    plan_path = root / 'preregistration.json'
    plan = json.loads(plan_path.read_text())
    pins = {'baseline': '29837e666604eee74a2ac94f328fb9803724342a', 'latest': '25e47866422d007da55cb19625344183599ba671'}
    assert report['status'] == 'verified' and report['mode'] == 'run'
    assert digest(plan_path) == report['preregistration_sha256']
    assert {k: v['source_commit'] for k, v in plan['variants'].items()} == pins
    assert len(report['commands']) == plan['process_blocks'] * len(plan['strategies']) * 2
    groups, child_hashes, result_hashes = defaultdict(list), {}, defaultdict(set)
    counts, combinations = Counter(), Counter()
    for command in report['commands']:
        variant, strategy = command['variant'], command['strategies'][0]
        combinations[command['block'], variant, strategy] += 1
        assert command['process']['returncode'] == 0 and not command['process']['timed_out']
        child_path = root / Path(command['report_path']).parent.name / 'report.json'
        assert digest(child_path) == command['report_sha256']
        child_hashes[str(child_path.relative_to(root))] = digest(child_path)
        raw = json.loads(child_path.read_text())
        assert raw['status'] == 'completed' and len(raw['cases']) == 1
        assert raw['benchmark_code_sha256'] == plan['benchmark_code_sha256']
        assert raw['input']['input_sha256'] == plan['input_sha256']
        assert raw['input']['evaluation_rows'] == plan['evaluation_rows']
        assert raw['arguments']['warm_repeats'] == plan['warm_calls_per_process']
        protocol = raw['protocol']
        assert protocol['native_thread_observation_policy'] == 'loaded-pools-v1'
        assert protocol['native_threads'] == 1 and all(v == '1' for v in protocol['native_thread_environment'].values())
        case = raw['cases'][0]
        assert case['engine'] == 'limen' and case['strategy'] == strategy
        assert case['preflight_status'] == 'verified' and len(case['measurements']) == case['requested_processes'] == 1
        for label, item in [('preflight', case['preflight']), ('measurement', case['measurements'][0])]:
            worker, process = item['worker'], item['process']
            assert process['returncode'] == 0 and not process['timed_out']
            assert {'ready', 'first_valid', 'complete'} <= process['parent_observed_events_ms'].keys()
            assert worker['status'] == 'verified'
            provenance = worker['provenance']
            assert provenance['source_commit_verified'] == provenance['catalog']['commit'] == pins[variant]
            assert provenance['tracked_source_clean'] and not provenance['system_site_packages']
            assert provenance['setup_manifest_sha256'] == plan['variants'][variant]['setup_manifest_sha256']
            assert worker['prepared_arrays_sha256'] == raw['scenarios'][strategy]['prepared_arrays_sha256']
            runtime = worker['runtime']
            assert runtime['thread_environment'] == protocol['native_thread_environment']
            assert runtime['native_thread_observations']['polars']['loaded'] is True
            assert runtime['native_thread_observations']['polars']['pool_size'] == 1
            assert runtime['threadpools'] and all(p['num_threads'] == 1 for p in runtime['threadpools'])
            parity = worker['parity']
            assert parity['equity_samples_checked'] == plan['evaluation_rows']
            assert parity['fills_checked'] == {'buy_and_hold': 2, 'sma_cross': 52}[strategy]
            assert parity['optional_observed_fields_checked'] == []
            assert set(parity['optional_unobserved_fields']) == {'cash', 'units', 'fill_quantities', 'fill_fees'}
            result_hashes[strategy].add(parity['actual_result_arrays_sha256'])
            if label == 'preflight':
                assert worker['timing_samples'] == worker['core_diagnostic_samples'] == []
            else:
                phases = ['first'] + [f'warm-{i}' for i in range(1, plan['warm_calls_per_process'] + 1)]
                for field, counter in [('timing_samples', 'full_timed_calls'), ('core_diagnostic_samples', 'core_diagnostic_calls')]:
                    assert [s['phase'] for s in worker[field]] == phases
                    for sample in worker[field]:
                        assert sample['admitted'] and sample['native_thread_limits_verified']
                        assert sample['parity'] == parity
                        assert all(math.isfinite(sample[k]) and sample[k] >= 0 for k in ('engine_ms', 'extraction_common_ms', 'full_common_ms', 'full_common_cpu_ms'))
                        counts[counter] += 1
                assert 'diagnostic, not a cross-framework full-engine ranking' in worker['core_diagnostic_scope']
            counts[label + '_workers'] += 1
        groups[variant, strategy].append(case['measurements'][0])
    assert combinations == Counter({(block, variant, strategy): 1 for block in range(1, plan['process_blocks'] + 1) for variant in pins for strategy in plan['strategies']})
    assert all(len(v) == 1 for v in result_hashes.values())
    recomputed = []
    assert len(report['summaries']) == len(pins) * len(plan['strategies'])
    for row in report['summaries']:
        items = groups[row['variant'], row['strategy']]
        assert len(items) == plan['process_blocks'] == row['independent_processes']
        assert row['status'] == 'verified' and row['source_commit'] == pins[row['variant']]
        assert 'relative_to_limen_warm_full_common' not in row
        warm = [[s for s in item['worker']['timing_samples'] if s['phase'].startswith('warm-')] for item in items]
        first = [item['worker']['timing_samples'][0]['full_common_ms'] for item in items]
        medians = [median(s['full_common_ms'] for s in samples) for samples in warm]
        expected = {'first_full_common_ms_samples': first, 'first_full_common_ms_median': median(first),
                    'first_full_common_ms_min': min(first), 'first_full_common_ms_max': max(first),
                    'warm_full_common_ms_samples': [[s['full_common_ms'] for s in samples] for samples in warm],
                    'warm_process_medians_ms': medians, 'warm_full_common_ms_median': median(medians),
                    'warm_process_median_ms_min': min(medians), 'warm_process_median_ms_max': max(medians),
                    'warm_full_common_call_ms_min': min(s['full_common_ms'] for samples in warm for s in samples),
                    'warm_full_common_call_ms_max': max(s['full_common_ms'] for samples in warm for s in samples),
                    'peak_rss_bytes_median': median(item['worker']['peak_rss_bytes_after_full_calls'] for item in items),
                    'warm_evaluation_bars_per_second': plan['evaluation_rows'] * 1000 / median(medians)}
        for key in ('engine_ms', 'extraction_common_ms', 'full_common_cpu_ms'):
            expected['warm_' + key + '_median'] = median(median(s[key] for s in samples) for samples in warm)
        for key in ('launch_to_ready_ms', 'launch_to_first_valid_ms'):
            expected[key + '_median'] = median(item['process'][key] for item in items)
        assert all(row[key] == value for key, value in expected.items()), (row['variant'], row['strategy'])
        recomputed.append({'variant': row['variant'], 'strategy': row['strategy'], 'warm_median_ms': median(medians), 'first_median_ms': median(first), 'checked_aggregate_fields': len(expected)})
    assert len(report['comparisons']) == len(plan['strategies'])
    for comparison in report['comparisons']:
        rows = {r['variant']: r for r in report['summaries'] if r['strategy'] == comparison['strategy']}
        assert comparison['latest_over_baseline_warm_full_common_duration'] == rows['latest']['warm_full_common_ms_median'] / rows['baseline']['warm_full_common_ms_median']
    receipt = {'status': 'passed', 'scope': 'Independent standard-library interpretation of retained JSON: source/fixture/runner identities, completion, recorded pool observations, call admission flags, aggregate arithmetic and ratio separation. No engine import, timing or re-evaluation of raw equity.',
               'report_sha256': digest(path), 'preregistration_sha256': digest(plan_path), 'checker_sha256': digest(Path(__file__)),
               'commands_checked': len(report['commands']), 'counts': dict(counts), 'aggregate_rows': recomputed,
               'comparisons': report['comparisons'], 'result_array_digests_by_strategy': {k: sorted(v) for k, v in result_hashes.items()},
               'observation_limit': 'Cash, units, fill quantities and fill fees are unobserved by this adapter. Metadata checks do not add those observations.',
               'child_report_sha256': child_hashes}
    with args.output.open('x') as stream:
        json.dump(receipt, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'status': 'passed', 'commands': len(report['commands']), **dict(counts), 'output': str(args.output)}))


if __name__ == '__main__':
    main()
