from __future__ import annotations

import numpy as np

from bench.api import Adapter, UnsupportedContract
from bench.contract import Result


def create_adapter(data, contract):
    import pandas as pd
    from qstrader import settings
    from qstrader.broker.fee_model.zero_fee_model import ZeroFeeModel
    from qstrader.broker.simulated_broker import SimulatedBroker
    from qstrader.execution.order import Order

    if contract.fee_bps:
        raise UnsupportedContract('QSTrader SimulatedBroker rounds consideration before calculating percentage fees; the common fee contract uses unrounded actual fill notional')
    settings.PRINT_EVENTS = False
    symbol, portfolio_id = 'RECORDED', 'COMMON'
    dates = pd.to_datetime(data['timestamp_ns'], utc=True)
    close = data['close']
    bars_by_date = {stamp: bar for bar, stamp in enumerate(dates)}
    count, slip = len(close) - 1, contract.slippage_bps / 10_000

    class RecordedExchange:
        def is_open_at_datetime(self, dt):
            return dt in bars_by_date

    class RecordedQuotes:
        def get_asset_latest_mid_price(self, dt, asset):
            if asset != symbol:
                raise KeyError(asset)
            return float(close[bars_by_date[dt]])

        def get_asset_latest_bid_ask_price(self, dt, asset):
            mid = self.get_asset_latest_mid_price(dt, asset)
            return mid * (1 - slip), mid * (1 + slip)

    def run():
        broker = SimulatedBroker(dates[0], RecordedExchange(), RecordedQuotes(),
                                 initial_funds=contract.initial_cash, fee_model=ZeroFeeModel())
        broker.create_portfolio(portfolio_id, name='Common recorded replay')
        broker.subscribe_funds_to_portfolio(portfolio_id, contract.initial_cash)
        portfolio = broker.portfolios[portfolio_id]
        fills = []
        native_transact = portfolio.transact_asset

        def observed_transact(transaction):
            native_transact(transaction)
            fills.append((bars_by_date[transaction.dt], int(np.sign(transaction.quantity)),
                          float(transaction.price), abs(float(transaction.quantity)),
                          float(transaction.commission)))

        portfolio.transact_asset = observed_transact
        equity, cash, units, held = [], [], [], []
        for bar in range(count):
            timestamp = dates[bar]
            broker.update(timestamp)
            position = portfolio.pos_handler.positions.get(symbol)
            quantity = 0.0 if position is None else float(position.net_quantity)
            held.append(int(quantity > 0))
            side = 0
            if data['target'][bar] and quantity == 0:
                side = 1
                request = float(portfolio.cash) / (float(close[bar]) * (1 + slip))
            elif not data['target'][bar] and quantity > 0:
                side = -1
                request = -quantity
            if side:
                broker.submit_order(portfolio_id, Order(timestamp, symbol, request, order_id=f'common-{bar}'))
                broker.update(timestamp)
                # Native execution marks the acquired position at its fill price;
                # mark the close after execution using the broker's own update.
                broker.update(timestamp)
            position = portfolio.pos_handler.positions.get(symbol)
            units.append(0.0 if position is None else float(position.net_quantity))
            cash.append(float(portfolio.cash))
            equity.append(float(broker.get_portfolio_total_equity(portfolio_id)))
        return Result(timestamp_ns=data['timestamp_ns'][:count].copy(),
                      equity=np.asarray(equity), held=np.asarray(held, dtype=np.int8),
                      cash=np.asarray(cash), units=np.asarray(units),
                      fill_bars=np.asarray([row[0] for row in fills], dtype=np.int64),
                      fill_sides=np.asarray([row[1] for row in fills], dtype=np.int8),
                      fill_prices=np.asarray([row[2] for row in fills], dtype=float),
                      fill_quantities=np.asarray([row[3] for row in fills], dtype=float),
                      fill_fees=np.asarray([row[4] for row in fills], dtype=float))

    return Adapter(run=run, extract=lambda result: result,
                   engine_scope='Native SimulatedBroker, order queue, portfolio and position ledger with a benchmark-owned hourly replay driver; excludes BacktestTradingSession daily calendar, alpha/risk/optimizer workflow',
                   settings={'benchmark_layer': 'native-components', 'rank_against_full_engine': False,
                             'processed_rows': count, 'PRINT_EVENTS': False,
                             'exchange_schedule': 'Exactly the recorded close timestamps',
                             'deterministic_order_ids': True},
                   output_observation={'equity_cash_units': 'Native broker/portfolio getters after fill and native close mark',
                                       'fills': 'Observed actual Transaction objects passed into native Portfolio.transact_asset'})
