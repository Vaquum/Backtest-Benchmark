"""Replay bounded metadata-only corruption checks without importing engines.

Run after timing, with --sources and --campaign pointing to retained inputs.
The optional --output writes only a new check receipt and refuses overwrite.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import runpy
import tempfile
from unittest.mock import patch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    sources = args.sources.resolve()
    if args.output is not None and args.output.exists():
        parser.error('--output already exists; evidence is never overwritten')
    namespace = runpy.run_path(str(root / 'scripts/validate_assessment.py'))
    Validator = namespace['AssessmentValidator']
    Invalid = namespace['Invalid']
    campaign_check = namespace['validate_campaign']
    receipt = []

    def check(name, function, reject=False):
        try:
            function()
        except Invalid as error:
            if not reject:
                raise
            receipt.append({'check': name, 'passed': True, 'rejected': str(error)})
        else:
            if reject:
                raise AssertionError(name + ' unexpectedly admitted')
            receipt.append({'check': name, 'passed': True})

    validator = Validator(root, sources)
    validator.validate()
    if validator.errors:
        raise AssertionError(validator.errors)
    receipt.append({'check': 'complete matrix with supplied source bounds', 'passed': True,
                    'rows': validator.row_count, 'references': validator.reference_count})
    syntax = Validator(root)
    syntax.validate()
    if syntax.errors:
        raise AssertionError(syntax.errors)
    receipt.append({'check': 'explicit source-link syntax mode', 'passed': True})
    row = json.loads((root / 'assessment/academic.json').read_text())[0]

    def malformed_row(edit):
        value = deepcopy(row)
        edit(value)
        validator.validate_row(value, 'A')

    check('nonempty finding required', lambda: malformed_row(lambda r: r.update(finding='  ')), True)
    check('invalid enum rejected without a TypeError', lambda: malformed_row(lambda r: r.update(status=[])), True)
    check('floating source revision rejected', lambda: malformed_row(
        lambda r: r['source_refs'][0].update(url=r['source_refs'][0]['url'].replace('/blob/' + validator.catalog[r['candidate_id']]['commit'] + '/', '/blob/main/'))), True)

    def use_readme(value):
        ref = value['source_refs'][0]
        ref['path'] = 'README.md'
        source = validator.catalog[value['candidate_id']]
        ref['url'] = f"https://github.com/{source['repository']}/blob/{source['commit']}/README.md#L{ref['start_line']}-L{ref['end_line']}"
    check('README behavioral reference rejected', lambda: malformed_row(use_readme), True)

    def excessive_lines(value):
        ref = value['source_refs'][0]
        ref['end_line'] += 1_000_000
        source = validator.catalog[value['candidate_id']]
        ref['url'] = f"https://github.com/{source['repository']}/blob/{source['commit']}/{ref['path']}#L{ref['start_line']}-L{ref['end_line']}"
    check('real local source line bounds enforced', lambda: malformed_row(excessive_lines), True)
    missing = Validator(root, sources / 'deliberately-absent-validation-check-source-root')
    missing.catalog, missing.auxiliary, missing.criteria = validator.catalog, validator.auxiliary, validator.criteria
    check('supplied missing source root fails', lambda: missing.validate_row(row, 'A'), True)

    with tempfile.TemporaryDirectory(prefix='assessment-validator-', dir=Path(__file__).resolve().parent) as temporary:
        target = Path(temporary)
        for relative in ('catalog/candidates.json', 'catalog/auxiliary_sources.json', 'protocol/criteria.json',
                         'assessment/performance.json', 'assessment/academic.json', 'assessment/safety.json'):
            path = target / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((root / relative).read_bytes())
        altered_path = target / 'assessment/academic.json'
        content = json.loads(altered_path.read_text())
        altered_path.write_text(json.dumps(content[:-1]))
        truncated = Validator(target)
        truncated.validate()
        if not any('missing candidate/criterion' in value for value in truncated.errors):
            raise AssertionError('truncated matrix was not identified')
        receipt.append({'check': 'missing matrix row rejected', 'passed': True})
        altered_path.write_text(json.dumps(content + [content[0]]))
        duplicated = Validator(target)
        duplicated.validate()
        if not any('duplicate candidate/criterion' in value for value in duplicated.errors):
            raise AssertionError('duplicate matrix pair was not identified')
        receipt.append({'check': 'duplicate matrix pair rejected', 'passed': True})

    campaign_path = args.campaign / 'report.json' if args.campaign.is_dir() else args.campaign
    original = json.loads(campaign_path.read_text())
    has_thread_policy = original.get('protocol', {}).get('native_thread_observation_policy') == 'loaded-pools-v1'
    check('actual complete campaign admitted', lambda: campaign_check(campaign_path, validator.catalog, has_thread_policy))

    def bad_campaign(edit):
        report = deepcopy(original)
        edit(report)
        with patch.dict(campaign_check.__globals__, {'read_json': lambda _: report}):
            campaign_check(Path('metadata-only-mutated-report.json'), validator.catalog, has_thread_policy)

    ranked = next(i for i, case in enumerate(original['cases']) if case['measurements'] and case['rank_against_full_engine'])
    component = next(i for i, row_ in enumerate(original['summary']) if not row_['rank_against_full_engine'] and row_['warm_full_common_ms_median'] is not None)
    check('missing declared warm call rejected', lambda: bad_campaign(
        lambda r: r['cases'][ranked]['measurements'][0]['worker']['timing_samples'].pop()), True)
    check('unadmitted timing sample rejected', lambda: bad_campaign(
        lambda r: r['cases'][ranked]['measurements'][0]['worker']['timing_samples'][0].update(admitted=False)), True)
    check('component full-engine ratio rejected', lambda: bad_campaign(
        lambda r: r['summary'][component].update(relative_to_limen_warm_full_common=1.0)), True)
    check('wrong median arithmetic rejected', lambda: bad_campaign(
        lambda r: r['summary'][ranked].update(warm_full_common_ms_median=r['summary'][ranked]['warm_full_common_ms_median'] + 1)), True)
    check('repeated process evidence rejected', lambda: bad_campaign(
        lambda r: r['cases'][ranked]['measurements'][1].update(directory=r['cases'][ranked]['measurements'][0]['directory'])), True)
    check('wrong parity coverage rejected', lambda: bad_campaign(
        lambda r: r['cases'][ranked]['measurements'][0]['worker']['parity'].update(equity_samples_checked=1)), True)
    if has_thread_policy:
        limit = original['protocol']['native_threads']
        loaded_polars = next(i for i, case in enumerate(original['cases']) if case['measurements']
                             and case['measurements'][0]['worker']['runtime']['native_thread_observations']['polars']['loaded'])
        check('missing declared Polars observation rejected', lambda: bad_campaign(
            lambda r: r['cases'][ranked]['preflight']['worker']['runtime']['native_thread_observations'].pop('polars')), True)
        check('observed Polars pool above declared limit rejected', lambda: bad_campaign(
            lambda r: r['cases'][loaded_polars]['measurements'][0]['worker']['runtime']['native_thread_observations']['polars'].update(pool_size=limit + 1)), True)
        check('missing post-call native-thread admission rejected', lambda: bad_campaign(
            lambda r: r['cases'][ranked]['measurements'][0]['worker']['timing_samples'][0].pop('native_thread_limits_verified')), True)
        check('worker thread environment differs from declaration rejected', lambda: bad_campaign(
            lambda r: r['cases'][ranked]['preflight']['worker']['runtime']['thread_environment'].update(POLARS_MAX_THREADS=str(limit + 1))), True)
        check('missing threadpool observations rejected', lambda: bad_campaign(
            lambda r: r['cases'][ranked]['preflight']['worker']['runtime'].update(threadpools='unavailable')), True)

        def erase_policy(report):
            report['protocol'].pop('native_thread_observation_policy')
            report['protocol'].pop('native_thread_environment')
        check('required native-thread policy cannot silently fall back to legacy', lambda: bad_campaign(erase_policy), True)
    else:
        check('legacy report cannot satisfy required native-thread observation policy',
              lambda: campaign_check(campaign_path, validator.catalog, True), True)
    output = {'checks': receipt, 'count': len(receipt), 'passed': True,
              'scope': 'Only assessment and recorded-report metadata were read or copied. No engines were imported and no price/return observations or measurements were generated. These checks do not establish CPU or thread-pool isolation.'}
    if args.output is not None:
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
