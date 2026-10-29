from __future__ import annotations

import math
import numpy as np

from bench.api import Adapter, UnsupportedContract, pandas_frame
from bench.contract import Result


def create_adapter(data, contract):
    import backtrader as bt

    if contract.costed:
        raise UnsupportedContract('The current Backtrader close-on-close adapter admits zero costs only; fill-time cost equity needs a separately validated observation route')
    frame = pandas_frame(data)
    desired = data['target']
    count = len(frame) - 1
    timestamp_to_bar = {bt.date2num(stamp.to_pydatetime()): bar for bar, stamp in enumerate(frame.index)}

    class CommonStrategy(bt.Strategy):
        def __init__(self):
            self.equity_observed = []
            self.fills_observed = []
            self.pending_order = None

        def next(self):
            self.equity_observed.append(float(self.broker.getvalue()))
            if self.pending_order is not None:
                raise AssertionError('An order remained pending at the next bar')
            target = desired[len(self.data) - 1]
            if target and not self.position:
                quantity = math.nextafter(float(self.broker.getcash()) / float(self.data.close[0]), 0.0)
                self.pending_order = self.buy(size=quantity)
            elif not target and self.position:
                self.pending_order = self.close()

        def notify_order(self, order):
            if order.status in (order.Submitted, order.Accepted):
                return
            if order.status != order.Completed:
                raise AssertionError(f'Native order failed: {order.getstatusname()}')
            self.fills_observed.append((timestamp_to_bar[order.executed.dt],
                                        1 if order.isbuy() else -1,
                                        float(order.executed.price), abs(float(order.executed.size)),
                                        float(order.executed.comm)))
            self.pending_order = None

    def run():
        engine = bt.Cerebro(stdstats=False)
        engine.adddata(bt.feeds.PandasData(dataname=frame))
        engine.addstrategy(CommonStrategy)
        engine.broker.setcash(contract.initial_cash)
        engine.broker.setcommission(commission=0)
        engine.broker.set_coc(True)
        return engine.run(runonce=True, preload=True)[0]

    def extract(strategy):
        if strategy.position or strategy.pending_order is not None:
            raise AssertionError('Native broker retained inventory or a pending terminal order')
        fills = sorted(strategy.fills_observed, key=lambda row: row[0])
        bars = np.asarray([row[0] for row in fills], dtype=np.int64)
        sides = np.asarray([row[1] for row in fills], dtype=np.int8)
        after = np.zeros(len(frame), dtype=np.int8)
        after[bars] = sides
        after = np.cumsum(after)
        return Result(timestamp_ns=data['timestamp_ns'][:count].copy(),
                      equity=np.asarray(strategy.equity_observed, dtype=float)[:count],
                      held=np.r_[0, after[:-1]].astype(np.int8)[:count],
                      fill_bars=bars, fill_sides=sides,
                      fill_prices=np.asarray([row[2] for row in fills], dtype=float),
                      fill_quantities=np.asarray([row[3] for row in fills], dtype=float),
                      fill_fees=np.asarray([row[4] for row in fills], dtype=float))

    return Adapter(run=run, extract=extract,
                   engine_scope='Cerebro construction, PandasData ingestion, preload and runonce event simulation; standard chart observers disabled',
                   settings={'close_on_close': True, 'preload': True, 'runonce': True,
                             'stdstats': False, 'processed_rows': len(frame), 'native_stats_requested': False},
                   output_observation={'equity': 'Actual broker value at each strategy callback; equivalent after a same-close zero-cost fill',
                                       'held': 'Incoming state reconstructed from actual completed order sides',
                                       'fills': 'Native completed order timestamps, prices, quantities and commissions',
                                       'cash_units': 'Not separately observed by this adapter'})
