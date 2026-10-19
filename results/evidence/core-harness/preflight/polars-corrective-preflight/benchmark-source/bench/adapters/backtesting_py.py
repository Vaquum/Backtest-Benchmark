from __future__ import annotations

import math
import numpy as np

from bench.api import Adapter, UnsupportedContract, pandas_frame
from bench.contract import Result


def create_adapter(data, contract):
    from backtesting import Strategy
    from backtesting.lib import FractionalBacktest

    if contract.costed:
        raise UnsupportedContract('The current FractionalBacktest adapter admits only zero costs; cost-time observations and spread semantics require a separate validated adapter')
    frame = pandas_frame(data, title_case=True)
    desired = data['target']
    count = len(frame) - 1

    class CommonStrategy(Strategy):
        def init(self):
            self.initial_observed_equity = self.equity

        def next(self):
            target = desired[len(self.data) - 1]
            if target and not self.position:
                self.buy(size=math.nextafter(1.0, 0.0))
            elif not target and self.position:
                self.position.close()

    def run():
        return FractionalBacktest(
            frame, CommonStrategy, cash=contract.initial_cash, commission=0,
            spread=0, margin=1, trade_on_close=True, hedging=False,
            exclusive_orders=False, finalize_trades=False,
            fractional_unit=1e-12).run()

    def extract(stats):
        if stats['_strategy'].position:
            raise AssertionError('Native strategy retained inventory after the settlement row')
        trades = stats['_trades']
        held = np.zeros(count, dtype=np.int8)
        bars, sides, prices, quantities = [], [], [], []
        for trade in trades.itertuples(index=False):
            held[int(trade.EntryBar) + 1:int(trade.ExitBar) + 1] = 1
            bars.extend([int(trade.EntryBar), int(trade.ExitBar)])
            sides.extend([1, -1])
            prices.extend([float(trade.EntryPrice), float(trade.ExitPrice)])
            quantities.extend([abs(float(trade.Size))] * 2)
        order = np.argsort(bars, kind='stable')
        equity = stats['_equity_curve']['Equity'].to_numpy(dtype=float)[:count].copy()
        # The engine backfills the unrecorded first slot. Preserve the strategy's
        # actual initial broker observation, before the first possible trade.
        equity[0] = stats['_strategy'].initial_observed_equity
        return Result(timestamp_ns=data['timestamp_ns'][:count].copy(), equity=equity,
                      held=held, fill_bars=np.asarray(bars, dtype=np.int64)[order],
                      fill_sides=np.asarray(sides, dtype=np.int8)[order],
                      fill_prices=np.asarray(prices, dtype=float)[order],
                      fill_quantities=np.asarray(quantities, dtype=float)[order])

    return Adapter(run=run, extract=extract,
                   engine_scope='Public FractionalBacktest.run including broker event loop, fractional conversion, equity and native performance statistics',
                   settings={'trade_on_close': True, 'fractional_unit': 1e-12,
                             'buy_fraction': math.nextafter(1.0, 0.0), 'finalize_trades': False,
                             'processed_rows': len(frame), 'native_stats_requested': True},
                   output_observation={'equity': 'Native equity curve; its first backfilled slot replaced with the actual initial strategy equity observation',
                                       'held_and_fills': 'Native completed trade entry/exit bars, prices and fractional quantities',
                                       'cash_units_fees': 'Not separately observed by this adapter'})
