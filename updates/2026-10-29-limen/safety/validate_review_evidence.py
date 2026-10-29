#!/usr/bin/env python3
"""Validate source anchors and count retained native-suite membership; no tests run."""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
BENCH = HERE.parents[2]
WORKSPACE = BENCH.parent
SOURCE = WORKSPACE / 'Limen'
OLD_SOURCE = WORKSPACE / 'Limen-baseline'
RUN = WORKSPACE / 'limen-rerun-output/native-suite-native-linux'


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def status(case: ET.Element) -> str:
    if case.find('skipped') is not None:
        return 'skipped'
    if case.find('failure') is not None or case.find('error') is not None:
        return 'failed'
    return 'passed'


def main() -> None:
    output_paths = [HERE / 'source-reference-validation.json', HERE / 'native-test-membership.json']
    require(not any(path.exists() for path in output_paths), 'Refusing to overwrite retained evidence')
    assessment = json.loads((HERE / 'safety-delta.json').read_text())
    for path, expected in ((SOURCE, assessment['latest_source_sha']), (OLD_SOURCE, assessment['baseline_source_sha'])):
        head = subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip()
        require(head == expected, 'Pinned source HEAD mismatch')
        dirty = subprocess.check_output(['git', '-C', str(path), 'status', '--porcelain', '--untracked-files=no'], text=True)
        require(not dirty, 'Tracked source differs from pinned HEAD')

    references = []
    for item in assessment['criteria']:
        for key, root, commit in (('source_refs', SOURCE, assessment['latest_source_sha']),
                                   ('baseline_source_refs', OLD_SOURCE, assessment['baseline_source_sha'])):
            for reference in item[key]:
                path = root / reference['path']
                data = path.read_bytes()
                lines = data.splitlines(keepends=True)
                first, last = reference['start_line'], reference['end_line']
                require(1 <= first <= last <= len(lines), f'Invalid source range: {reference}')
                expected = f"https://github.com/Vaquum/Limen/blob/{commit}/{reference['path']}#L{first}-L{last}"
                require(reference['url'] == expected, f'Unexpected source URL: {reference}')
                references.append({'criterion_id': item['criterion_id'], 'source_commit': commit, **reference,
                                   'file_sha256': sha256(data).hexdigest(),
                                   'range_sha256': sha256(b''.join(lines[first - 1:last])).hexdigest()})
    source_receipt = {
        'latest_source_sha': assessment['latest_source_sha'],
        'baseline_source_sha': assessment['baseline_source_sha'],
        'tracked_sources_clean': True, 'path_line_and_url_checks_passed': True,
        'assessment_sha256': digest(HERE / 'safety-delta.json'),
        'latest_reference_count': sum(r['source_commit'] == assessment['latest_source_sha'] for r in references),
        'baseline_reference_count': sum(r['source_commit'] == assessment['baseline_source_sha'] for r in references),
        'references': references,
        'method': 'Read exact pinned workspace files, validate every path/range/URL, hash files and cited byte ranges. No source mutation, imports or engines.',
    }

    profile_path, manifest_path, junit_path = (RUN / name for name in ('test_runtime_profile.json', 'run_manifest.json', 'junit.xml'))
    profile, manifest = json.loads(profile_path.read_text()), json.loads(manifest_path.read_text())
    require(manifest['commit'] == assessment['latest_source_sha'], 'Native campaign source mismatch')
    require(manifest['exit_code'] == 0, 'Native campaign did not finish successfully')
    parallel = profile['parallel']
    require(parallel['reconciled'] is True and parallel['worker_count'] == 4 and not parallel['errors'],
            'Native parallel receipt is not reconciled')
    tests = profile['tests']
    cases = list(ET.parse(junit_path).iter('testcase'))
    require(len(tests) == len(cases) == parallel['collected_count'] == parallel['execution_count'] == 7391,
            'Native test population differs')
    require(len({(test['module'], test['test_name']) for test in tests}) == len(tests), 'Duplicate native profile identities')
    profile_counts = Counter(test['status'] for test in tests)
    junit_counts = Counter(status(case) for case in cases)
    require(profile_counts == junit_counts == Counter(passed=7388, failed=0, skipped=3), 'Native statuses disagree')
    modules = sorted({module for row in assessment['criteria'] for module in row['native_test_modules']})
    module_receipts = {}
    for module in modules:
        selected = [test for test in tests if test['module'] == module]
        xml_selected = [case for case in cases if case.get('classname') == module]
        require(bool(selected), f'Absent mapped module: {module}')
        counts = Counter(test['status'] for test in selected)
        require(counts == Counter(status(case) for case in xml_selected), f'Module profile/JUnit mismatch: {module}')
        require(counts['failed'] == 0 and counts['skipped'] == 0, f'Mapped module not entirely passed: {module}')
        module_receipts[module] = {
            'passed': counts['passed'], 'failed': counts['failed'], 'skipped': counts['skipped'],
            'node_ids': sorted(test['test_name'] for test in selected),
        }
    criterion_membership = {}
    for row in assessment['criteria']:
        mapped = row['native_test_modules']
        criterion_membership[row['criterion_id']] = {
            'modules': mapped,
            'passed_module_members': sum(module_receipts[module]['passed'] for module in mapped),
            'failed_module_members': 0, 'skipped_module_members': 0,
            'scope': 'Mapped native module execution, not a claim that every finding clause is directly asserted or exhaustive.',
        }
    native_receipt = {
        'source_commit': manifest['commit'], 'admission': 'completed_native_linux_campaign',
        'campaign_directory': str(RUN), 'files': {str(path): digest(path) for path in (profile_path, manifest_path, junit_path)},
        'suite': profile['suite'], 'parallel': {'worker_count': 4, 'reconciled': True, 'collected_count': 7391, 'execution_count': 7391},
        'profile_junit_counts_match': True,
        'mapped_distinct_modules': len(modules),
        'mapped_unique_passed_tests': sum(row['passed'] for row in module_receipts.values()),
        'modules': module_receipts, 'criteria': criterion_membership,
        'skipped_tests': [test['test_name'] for test in tests if test['status'] == 'skipped'],
        'limitations': [
            'Criteria share modules: their per-criterion counts must not be added as independent test totals.',
            'Passing a module does not prove every assessed control or exhaustive adversarial coverage; inspected assertions and source anchors identify the stronger claims.',
            'The initial restricted-environment attempt remains separate and not admitted; upstream CI execution is separate evidence.',
            'The native suite duration is not a matched old/new performance result and is not used to infer code speedup.',
        ],
    }
    for path, value in zip(output_paths, (source_receipt, native_receipt), strict=True):
        with path.open('x') as stream:
            json.dump(value, stream, indent=2, allow_nan=False)
            stream.write('\n')
    print(json.dumps({'saved': [str(path) for path in output_paths],
                      'latest_refs': source_receipt['latest_reference_count'],
                      'baseline_refs': source_receipt['baseline_reference_count'],
                      'mapped_modules': len(modules),
                      'mapped_unique_passed_tests': native_receipt['mapped_unique_passed_tests']}))


if __name__ == '__main__':
    main()
