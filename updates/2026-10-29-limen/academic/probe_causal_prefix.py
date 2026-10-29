"""Repeat the original recorded-prefix test at either explicitly pinned revision."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
PINS = {
    'baseline': '29837e666604eee74a2ac94f328fb9803724342a',
    'latest': '25e47866422d007da55cb19625344183599ba671',
}
FIXTURE = 'tests/fixtures/spot_1h_20240101_20241231.parquet'
FIXTURE_SHA256 = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'
TOLERANCE = {'relative': 1e-12, 'absolute': 1e-12}


def admit(root: Path, pin: str) -> None:
    def git(*args: str) -> str:
        return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()
    if Path(git('rev-parse', '--show-toplevel')).resolve() != root:
        raise SystemExit('Source must be the exact repository root')
    if git('rev-parse', 'HEAD') != pin:
        raise SystemExit('Source HEAD differs from the declared assessment pin')
    if git('diff', '--name-only', 'HEAD'):
        raise SystemExit('Tracked source modifications prevent pin admission')
    if sha256((root / FIXTURE).read_bytes()).hexdigest() != FIXTURE_SHA256:
        raise SystemExit('Recorded fixture digest differs from the original assessment')


def compare(function, raw, prefix_rows, params, *, research_column=False):
    import numpy as np
    prefix = function(raw.head(prefix_rows), **params)
    extended = function(raw, **params).head(prefix_rows)
    names = [name for name in prefix.columns if name not in raw.columns
             and (research_column or name != 'active_quantile_count')]
    row_mask = np.zeros(prefix_rows, dtype=bool)
    columns = {}
    for name in names:
        before, after = prefix[name].to_numpy(), extended[name].to_numpy()
        changed = ~np.isclose(before, after, rtol=1e-12, atol=1e-12, equal_nan=True)
        row_mask |= changed
        indices = np.flatnonzero(changed)
        columns[name] = {
            'changed_rows': int(len(indices)),
            'max_abs_difference': float(np.max(np.abs(before - after))),
            'first_change': None if not len(indices) else {
                'row': int(indices[0]), 'datetime': str(raw['datetime'][int(indices[0])]),
                'prefix_value': float(before[indices[0]]), 'extended_value': float(after[indices[0]]),
            },
        }
    return {'function': function.__module__ + '.' + function.__name__, 'params': params,
            'prefix_rows': prefix_rows, 'extended_rows': raw.height,
            'rows_with_any_feature_change': int(row_mask.sum()), 'per_column': columns}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-root', type=Path, required=True)
    parser.add_argument('--revision', choices=PINS, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root, output = args.repo_root.resolve(strict=True), args.output.resolve()
    if output.exists() or output == root or root in output.parents:
        raise SystemExit('Output must be a new file outside the source checkout')
    admit(root, PINS[args.revision])
    sys.path.insert(0, str(root))
    import limen
    import numpy as np
    import polars as pl
    from limen.features.price_lines import price_lines
    from limen.features.quantile_price_lines import quantile_price_lines
    if root not in Path(limen.__file__).resolve().parents:
        raise SystemExit('Imported Limen differs from admitted source')
    fixture = root / FIXTURE
    raw = pl.read_parquet(fixture).select('datetime', 'close').head(384)
    common = {'max_duration_hours': 48, 'min_height_pct': .002, 'include_research_only': False}
    original = [compare(price_lines, raw, 192, common),
                compare(quantile_price_lines, raw, 192, {**common, 'quantile_threshold': .7}),
                compare(quantile_price_lines, raw, 192, {**common, 'quantile_threshold': 0.})]
    expanded, asof = [], []
    for quantile in (.7, .8):
        for research in (False, True):
            params = {**common, 'quantile_threshold': quantile, 'include_research_only': research}
            record = compare(quantile_price_lines, raw, 192, params)
            with_research = compare(quantile_price_lines, raw, 192, params, research_column=True)
            record['research_only_column'] = with_research['per_column'].get('active_quantile_count')
            first = quantile_price_lines(raw, **params)
            second = quantile_price_lines(raw, **{**params, 'include_research_only': not research})
            columns = list(record['per_column'])
            record['five_common_columns_exactly_equal_across_flags'] = first.select(columns).equals(second.select(columns))
            expanded.append(record)
    for quantile in (0., .7, .8, 1.):
        params = {**common, 'quantile_threshold': quantile}
        full = quantile_price_lines(raw, **params)
        columns = [name for name in full.columns if name not in raw.columns]
        for cutoff in (1, 2, 17, 19, 48, 96, 192, 384):
            prefix = quantile_price_lines(raw.head(cutoff), **params)
            asof.append({'quantile': quantile, 'cutoff': cutoff,
                         'prefix_last': {name: float(prefix[name][-1]) for name in columns},
                         'full_historical': {name: float(full[name][cutoff - 1]) for name in columns}})
    distribution = {'name': 'vaquum-limen', 'version': importlib.metadata.version('vaquum-limen')}
    report = {'revision': args.revision, 'repository_commit': PINS[args.revision],
              'source_root': str(root), 'imported_limen': str(Path(limen.__file__).resolve()),
              'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
              'fixture': FIXTURE, 'fixture_sha256': FIXTURE_SHA256,
              'source_period': [str(raw['datetime'][0]), str(raw['datetime'][-1])],
              'numeric_tolerance': TOLERANCE,
              'data_policy': 'Unchanged recorded observations; only original prefix selection/extension.',
              'runtime': {'python': sys.version, 'numpy': np.__version__, 'polars': pl.__version__,
                          'installed_distribution': distribution},
              'probe_script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_file_sha256': {path: sha256((root / path).read_bytes()).hexdigest() for path in (
                  'limen/features/quantile_price_lines.py', 'limen/features/price_lines.py',
                  'limen/utils/_line_arrays.py')},
              'original_probe_cases': original, 'expanded_cases': expanded, 'asof_rows': asof,
              'limits': ['No population defect-rate estimate.', 'Research-only active span count is reported separately.',
                         'No claim of general feature causality or split/fitting isolation.']}
    admit(root, PINS[args.revision])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'output': str(output), 'sha256': sha256(output.read_bytes()).hexdigest(),
                      'revision': args.revision,
                      'original_changed_rows': [r['rows_with_any_feature_change'] for r in original],
                      'expanded_changed_rows': [r['rows_with_any_feature_change'] for r in expanded],
                      'asof_rows': len(asof)}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
