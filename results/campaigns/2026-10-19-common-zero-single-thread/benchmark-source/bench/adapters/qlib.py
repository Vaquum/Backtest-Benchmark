"""Qlib exchange/position component replay; not the full Qlib research executor.

The data-loading extension supplies unchanged recorded close quotes directly.
All order acceptance, cost, fill amount and account updates use native Qlib code.
This is a separately labeled component measurement, never an end-to-end winner.
"""
from __future__ import annotations

import numpy as np

from bench.api import Adapter
from bench.contract import Result


def create_adapter(data, contract):
    import pandas as pd
    from qlib.backtest.decision import Order, OrderDir
    from qlib.backtest.exchange import Exchange
    from qlib.backtest.position import Position
    from qlib.config import C

    # Initialize only native regional configuration; no provider, recorder,
    # server, network connection or external data source is registered.
    C.set_region("us")

    symbol = "RECORDED"
    count = len(data["close"]) - 1
    dates = pd.to_datetime(data["timestamp_ns"], utc=True)
    close = data["close"]
    fee_rate = contract.fee_bps / 10_000
    slip_rate = contract.slippage_bps / 10_000
    quote = pd.DataFrame(
        {"$close": close, "$buy": close * (1 + slip_rate),
         "$sell": close * (1 - slip_rate), "$volume": data["volume"],
         "$factor": 1.0, "$change": 0.0,
         "$limit_buy": False, "$limit_sell": False},
        index=pd.MultiIndex.from_arrays([[symbol] * len(close), dates],
                                        names=["instrument", "datetime"]),
    )

    class RecordedExchange(Exchange):
        def get_quote_from_qlib(self):
            # Supported data-loading extension only; order economics stay native.
            self.quote_df = quote.copy()
            self.trade_w_adj_price = False
            self._update_limit(self.limit_threshold)

    def run():
        exchange = RecordedExchange(
            freq="60min", codes=[symbol], start_time=dates[0], end_time=dates[-1],
            deal_price=("$buy", "$sell"),
            limit_threshold=("$limit_buy", "$limit_sell"),
            trade_unit=None, open_cost=fee_rate, close_cost=fee_rate,
            min_cost=0.0, impact_cost=0.0,
        )
        position = Position(cash=contract.initial_cash)
        equity, cash, units, held = [], [], [], []
        fill_bars, fill_sides, fill_prices, fill_qty, fill_fees = [], [], [], [], []
        for bar in range(count):
            quantity = position.get_stock_amount(symbol)
            held.append(int(quantity > 0))
            side = 0
            if data["target"][bar] and quantity == 0:
                side = 1
                requested = position.get_cash() / (close[bar] * (1 + slip_rate) * (1 + fee_rate))
            elif not data["target"][bar] and quantity > 0:
                side = -1
                requested = quantity
            if side:
                order = Order(symbol, requested, OrderDir.BUY if side == 1 else OrderDir.SELL,
                              dates[bar], dates[bar])
                _, fee, price = exchange.deal_order(order, position=position, dealt_order_amount={})
                if order.deal_amount > 0:
                    fill_bars.append(bar)
                    fill_sides.append(side)
                    fill_prices.append(price)
                    fill_qty.append(order.deal_amount)
                    fill_fees.append(fee)
            quantity = position.get_stock_amount(symbol)
            if quantity:
                position.update_stock_price(symbol, float(close[bar]))
            units.append(quantity)
            cash.append(position.get_cash())
            equity.append(position.calculate_value())
        return Result(
            timestamp_ns=data["timestamp_ns"][:count].copy(),
            equity=np.asarray(equity), held=np.asarray(held, dtype=np.int8),
            cash=np.asarray(cash), units=np.asarray(units),
            fill_bars=np.asarray(fill_bars, dtype=np.int64),
            fill_sides=np.asarray(fill_sides, dtype=np.int8),
            fill_prices=np.asarray(fill_prices), fill_quantities=np.asarray(fill_qty),
            fill_fees=np.asarray(fill_fees),
        )

    return Adapter(
        run=run, extract=lambda value: value,
        engine_scope="Qlib Exchange + Position with a benchmark-owned replay loop; excludes Qlib executor, research, and data-provider workflow",
        settings={"benchmark_layer": "native-components", "rank_against_full_engine": False,
                  "trade_unit": None, "min_cost": 0.0, "impact_cost": 0.0,
                  "market_model": "Continuous quantities, unrestricted trading, fixed contract quote adjustments"},
        output_observation={"equity": "Position.calculate_value after native fill and close mark",
                            "fills": "Order.deal_amount and Exchange.deal_order native outputs",
                            "cash_units": "Native Position getters"},
    )
