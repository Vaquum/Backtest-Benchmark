from __future__ import annotations

import numpy as np

from bench.api import Adapter, pandas_frame
from bench.contract import Result


def create_adapter(data, contract):
    import vectorbt as vbt
    from vectorbt._engine import resolve_engine

    if resolve_engine('numba') != 'numba':
        raise RuntimeError('The explicit Numba backend could not be selected')
    close = pandas_frame(data)['close']
    desired = data['target']
    previous = np.r_[0, desired[:-1]]
    entries, exits = (desired == 1) & (previous == 0), (desired == 0) & (previous == 1)
    count = len(close) - 1

    def run():
        return vbt.Portfolio.from_signals(
            close, entries=entries, exits=exits, init_cash=contract.initial_cash,
            size=np.inf, size_type='amount', direction='longonly',
            fees=contract.fee_bps / 10_000, fixed_fees=0,
            slippage=contract.slippage_bps / 10_000, accumulate=False,
            cash_sharing=False, group_by=False, engine='numba')

    def extract(portfolio):
        orders = portfolio.orders.records
        units = portfolio.assets().to_numpy(dtype=float)
        return Result(
            timestamp_ns=data['timestamp_ns'][:count].copy(),
            equity=portfolio.value().to_numpy(dtype=float)[:count],
            held=np.r_[0, units[:-1] > 0].astype(np.int8)[:count],
            fill_bars=orders['idx'].to_numpy(dtype=np.int64),
            fill_sides=np.where(orders['side'].to_numpy() == 0, 1, -1).astype(np.int8),
            fill_prices=orders['price'].to_numpy(dtype=float),
            cash=portfolio.cash().to_numpy(dtype=float)[:count], units=units[:count],
            fill_quantities=orders['size'].to_numpy(dtype=float),
            fill_fees=orders['fees'].to_numpy(dtype=float))

    return Adapter(run=run, extract=extract,
                   engine_scope='Portfolio.from_signals including framework broadcasting and Numba simulation; common extraction includes lazy account-array materialization',
                   settings={'backend': 'numba', 'accumulate': False, 'cash_sharing': False,
                             'size': 'infinity, all affordable continuous units',
                             'processed_rows': len(close), 'native_stats_requested': False,
                             'license_track': 'Public source; Apache 2.0 with Commons Clause at the frozen revision'},
                   output_observation={'equity_cash_units': 'Native Portfolio value/cash/assets arrays',
                                       'fills': 'Native Portfolio order records including quantities and fees'})
