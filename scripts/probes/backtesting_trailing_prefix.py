#!/usr/bin/env python3
"""Inspect native TrailingStrategy prefix dependence on unchanged recorded OHLC.

The public Backtest.run -> TrailingStrategy.init/set_atr_periods/set_trailing_pct
path constructs each helper. This probe reads the native helper's stored ATR and
ATR multiplier for observation; it does not implement an alternative indicator or
place trades. It reports historical stop-distance coefficients, not P&L.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from common import admit_probe, verify_imported_module, verify_unchanged, write_json_exclusive


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--fixture', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--prefix-rows', type=int, default=192)
    parser.add_argument('--full-rows', type=int, default=384)
    parser.add_argument('--atr-period', type=int, default=40)
    parser.add_argument('--trailing-pct', type=float, default=0.10)
    args = parser.parse_args()
    source, fixture = args.source.resolve(), args.fixture.resolve()
    admission = admit_probe('backtesting_py', source, output=args.output, fixture=fixture)
    sys.path.insert(0, str(source))
    import numpy as np
    import pandas as pd
    import pyarrow.parquet as pq
    import backtesting
    from backtesting import Backtest
    from backtesting.lib import TrailingStrategy

    verify_imported_module(backtesting, source)
    original = pq.read_table(fixture)
    selected = original.slice(0, args.full_rows)
    frame = selected.to_pandas().rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}).set_index('datetime')[['Open', 'High', 'Low', 'Close', 'Volume']]
    assert args.atr_period < args.prefix_rows < args.full_rows == len(frame)

    class PercentTrailingProbe(TrailingStrategy):
        def init(self):
            super().init()
            self.set_atr_periods(args.atr_period)
            self.set_trailing_pct(args.trailing_pct)
        def next(self):
            super().next()

    class FixedAtrProbe(TrailingStrategy):
        def init(self):
            super().init()
            self.set_atr_periods(args.atr_period)
            self.set_trailing_sl(6)
        def next(self):
            super().next()

    def observe(data, strategy_cls):
        strategy = Backtest(data, strategy_cls, cash=1_000_000).run()['_strategy']
        return (np.asarray(getattr(strategy, '_TrailingStrategy__atr'), dtype=float),
                float(getattr(strategy, '_TrailingStrategy__n_atr')))

    prefix = frame.iloc[:args.prefix_rows]
    short_atr, short_coef = observe(prefix, PercentTrailingProbe)
    full_atr, full_coef = observe(frame, PercentTrailingProbe)
    control_short_atr, control_short_coef = observe(prefix, FixedAtrProbe)
    control_full_atr, control_full_coef = observe(frame, FixedAtrProbe)
    n = args.prefix_rows
    fully_observable = np.arange(n) >= args.atr_period - 1
    short_dist, full_dist = short_atr * short_coef, full_atr[:n] * full_coef
    changed = ~np.isclose(short_dist, full_dist, rtol=1e-12, atol=1e-12, equal_nan=True)
    valid_changed = np.flatnonzero(changed & fully_observable)
    control_changed = ~np.isclose(
        control_short_atr * control_short_coef,
        control_full_atr[:n] * control_full_coef,
        rtol=1e-12, atol=1e-12, equal_nan=True,
    )
    assert np.allclose(short_atr, full_atr[:n], rtol=1e-12, atol=1e-12)
    assert short_coef != full_coef
    assert len(valid_changed) == int(fully_observable.sum())
    assert not control_changed.any()
    first = int(valid_changed[0])
    known_warmup = args.atr_period - 1
    assert np.all(short_atr[:known_warmup] == short_atr[known_warmup])
    commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    result = {
        'admission': admission,
        'candidate_id': 'backtesting_py', 'commit': commit,
        'imported_module': str(Path(backtesting.__file__).resolve()),
        'fixture': {'path': str(fixture), 'sha256': hashlib.sha256(fixture.read_bytes()).hexdigest(), 'rows': original.num_rows},
        'selection': {'prefix_rows': n, 'full_rows': len(frame), 'source_row_range': [0, len(frame)-1], 'transformation': 'Columns renamed and datetime used as index; original OHLCV values unchanged.'},
        'configuration': {'atr_period': args.atr_period, 'trailing_pct': args.trailing_pct, 'rtol': 1e-12, 'atol': 1e-12},
        'public_path': 'Backtest.run -> subclass.init -> TrailingStrategy.set_atr_periods -> TrailingStrategy.set_trailing_pct',
        'percent_trailing': {
            'prefix_atr_multiplier': short_coef, 'full_atr_multiplier': full_coef,
            'native_atr_changed_prefix_rows': int(np.sum(~np.isclose(short_atr, full_atr[:n], rtol=1e-12, atol=1e-12, equal_nan=True))),
            'historical_stop_distance_changed_rows': int(changed.sum()),
            'fully_observable_rows': int(fully_observable.sum()),
            'fully_observable_stop_distance_changed_rows': len(valid_changed),
            'first_fully_observable_changed_source_row': first,
            'first_fully_observable_changed_timestamp': str(frame.index[first]),
            'rows_after_first_divergence_until_prefix_end': n - 1 - first,
            'prefix_stop_distance_at_first_divergence': float(short_dist[first]),
            'full_stop_distance_at_first_divergence': float(full_dist[first]),
            'max_abs_stop_distance_difference_fully_observable': float(np.max(np.abs(short_dist[fully_observable] - full_dist[fully_observable]))),
        },
        'controls': {
            'fixed_six_atr_stop_distance_changed_rows': int(control_changed.sum()),
            'fixed_six_atr_prefix_multiplier': control_short_coef,
            'fixed_six_atr_full_multiplier': control_full_coef,
            'native_atr_arrays_identical_on_common_prefix': True,
        },
        'warmup_observation': {
            'first_complete_atr_source_row': known_warmup,
            'earlier_rows_backfilled_with_first_complete_atr': known_warmup,
            'borrowed_atr_value': float(short_atr[known_warmup]),
            'borrowed_atr_source_timestamp': str(frame.index[known_warmup]),
        },
        'limitations': [
            'This is the public TrailingStrategy percentage helper used from init; no claim applies to every Backtest strategy.',
            'No orders were placed. The measured quantity is the native stored ATR multiplier and implied stop distance that next uses, not a realized trade, return or performance impact.',
            'Fully observable comparison excludes the first atr_period-1 warmup rows. Hence the percentage-helper divergence is not explained by an incomplete ATR window at the prefix boundary.',
            'The core engine slices registered indicators and visible data per callback; that does not make an already full-sample-fit init coefficient causal.',
            'The separate early ATR backfill observation is an inspected warmup lookahead mechanism, not a second population failure rate.',
        ],
        'versions': {'python': sys.version.split()[0], 'numpy': np.__version__, 'pandas': pd.__version__, 'backtesting': backtesting.__version__},
        'criteria': ['A01'],
    }
    verify_unchanged(admission)
    write_json_exclusive(args.output, result)
    print(json.dumps({'candidate': 'backtesting_py', 'commit': commit, 'fully_observable_changed_rows': len(valid_changed), 'fully_observable_rows': int(fully_observable.sum()), 'prefix_multiplier': short_coef, 'full_multiplier': full_coef, 'control_changed_rows': int(control_changed.sum()), 'output': str(args.output)}))

if __name__ == '__main__':
    main()
