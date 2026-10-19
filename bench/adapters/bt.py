from __future__ import annotations

import numpy as np

from bench.api import Adapter, UnsupportedContract, pandas_frame
from bench.contract import Result


def create_adapter(data, contract):
    import bt
    import bt.core

    if contract.slippage_bps:
        raise UnsupportedContract('This bt adapter does not yet admit a side-dependent slippage quote contract')
    symbol = 'RECORDED'
    frame = pandas_frame(data)[['close']].rename(columns={'close': symbol})
    targets = dict(zip(frame.index, data['target']))
    bars_by_date = {stamp: bar for bar, stamp in enumerate(frame.index)}
    count = len(frame) - 1

    class OnTransition(bt.Algo):
        def __init__(self):
            self.previous = 0

        def __call__(self, target):
            desired = int(targets[target.now])
            if desired != self.previous:
                target.rebalance(float(desired), symbol)
                self.previous = desired
            return True

    def commissions(quantity, price):
        return abs(quantity) * price * contract.fee_bps / 10_000

    def run():
        strategy = bt.Strategy('common', [OnTransition()], children=[bt.Security(symbol)])
        backtest = bt.Backtest(strategy, frame, initial_capital=contract.initial_cash,
                              commissions=commissions, integer_positions=False,
                              progress_bar=False)
        backtest.run()
        return backtest

    def extract(backtest):
        strategy = backtest.strategy
        positions = strategy.positions
        units = (positions[symbol].reindex(frame.index).fillna(0).to_numpy(dtype=float)
                 if symbol in positions else np.zeros(len(frame)))
        transactions = strategy.get_transactions()
        bars = np.asarray([bars_by_date[stamp] for stamp in transactions.index.get_level_values('Date')], dtype=np.int64)
        quantity = transactions['quantity'].to_numpy(dtype=float)
        return Result(timestamp_ns=data['timestamp_ns'][:count].copy(),
                      equity=strategy.values.reindex(frame.index).to_numpy(dtype=float)[:count],
                      held=np.r_[0, units[:-1] > 0].astype(np.int8)[:count],
                      fill_bars=bars, fill_sides=np.sign(quantity).astype(np.int8),
                      fill_prices=transactions['price'].to_numpy(dtype=float),
                      cash=strategy.cash.reindex(frame.index).to_numpy(dtype=float)[:count],
                      units=units[:count], fill_quantities=np.abs(quantity),
                      fill_fees=strategy.fees.reindex(frame.index).to_numpy(dtype=float)[bars])

    return Adapter(run=run, extract=extract,
                   engine_scope='Public Backtest construction and run including strategy deepcopy, event loop, allocation/accounting and native ffn performance statistics',
                   settings={'integer_positions': False, 'rebalance': 'Only on desired long/flat transitions',
                             'universe': 'One explicitly registered native Security, including flat scenarios',
                             'progress_bar': False, 'processed_rows': len(frame),
                             'native_stats_requested': True, 'bt_core_import_path': bt.core.__file__,
                             'native_reference_row': 'Engine adds a nontrading NaN bootstrap row; no fabricated market price'},
                   output_observation={'equity_cash_units': 'Native strategy values, cash and position histories',
                                       'fills': 'Native get_transactions; per-bar native fee history on fill bars'})
