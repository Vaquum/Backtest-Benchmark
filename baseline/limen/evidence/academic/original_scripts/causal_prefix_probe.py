from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np
import polars as pl

ROOT = Path('/workspace/scratch/008a76ec4981/limen-review-source')
sys.path.insert(0, str(ROOT))

from limen.features.price_lines import price_lines
from limen.features.quantile_price_lines import quantile_price_lines

FIXTURE = ROOT / 'tests/fixtures/spot_1h_20240101_20241231.parquet'


def compare(function, raw: pl.DataFrame, prefix_rows: int, params: dict) -> dict:
    prefix = function(raw.head(prefix_rows), **params)
    extended = function(raw, **params).head(prefix_rows)
    names = [name for name in prefix.columns if name not in raw.columns]
    result = {}
    row_mask = np.zeros(prefix_rows, dtype=bool)
    for name in names:
        before = prefix[name].to_numpy()
        after = extended[name].to_numpy()
        mismatches = ~np.isclose(before, after, rtol=1e-12, atol=1e-12, equal_nan=True)
        row_mask |= mismatches
        indices = np.flatnonzero(mismatches)
        result[name] = {
            'changed_rows': len(indices),
            'max_abs_difference': float(np.max(np.abs(before - after))),
            'first_change': None if not len(indices) else {
                'row': int(indices[0]),
                'datetime': str(raw['datetime'][int(indices[0])]),
                'prefix_value': float(before[indices[0]]),
                'extended_value': float(after[indices[0]]),
            },
        }
    return {
        'function': function.__module__ + '.' + function.__name__,
        'params': params,
        'prefix_rows': prefix_rows,
        'extended_rows': raw.height,
        'rows_with_any_feature_change': int(row_mask.sum()),
        'per_column': result,
    }


def main() -> None:
    raw = pl.read_parquet(FIXTURE).select('datetime', 'close').head(384)
    common = {'max_duration_hours': 48, 'min_height_pct': 0.002, 'include_research_only': False}
    records = [
        compare(price_lines, raw, 192, common),
        compare(quantile_price_lines, raw, 192, {**common, 'quantile_threshold': 0.70}),
        compare(quantile_price_lines, raw, 192, {**common, 'quantile_threshold': 0.0}),
    ]
    report = {
        'repository_commit': '29837e666604eee74a2ac94f328fb9803724342a',
        'fixture': str(FIXTURE),
        'fixture_sha256': sha256(FIXTURE.read_bytes()).hexdigest(),
        'source_period': [str(raw['datetime'][0]), str(raw['datetime'][-1])],
        'data_policy': 'Unmodified recorded observations; only prefix selection and extension.',
        'numeric_tolerance': {'relative': 1e-12, 'absolute': 1e-12},
        'probes': records,
    }
    output = json.dumps(report, indent=2, allow_nan=False)
    Path(__file__).with_suffix('.json').write_text(output + '\n')
    print(output)


if __name__ == '__main__':
    main()
