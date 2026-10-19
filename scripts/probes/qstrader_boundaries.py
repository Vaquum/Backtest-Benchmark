#!/usr/bin/env python3
"""Bounded, local QSTrader boundary probes using unchanged recorded prices.

Run with a Python environment containing pandas, numpy, polars and pytz:
  python scripts/probes/qstrader_boundaries.py --source ../benchmark-sources/qstrader \
    --fixture ../benchmark-sources/limen/tests/fixtures/spot_1h_20240101_20241231.parquet \
    --output results/probes/qstrader_boundaries.json

The two CSV observations select existing midnight rows from the supplied hourly
fixture. Prices are not generated, perturbed, resampled or adjusted. This tests
lookup and affordability boundaries, not a daily strategy or an instrument model.
"""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from common import admit_probe, verify_imported_module, verify_unchanged, write_json_exclusive


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve()
    fixture = args.fixture.resolve()
    admission = admit_probe("qstrader", source, output=args.output, fixture=fixture)
    sys.path.insert(0, str(source))
    import numpy as np
    import pandas as pd
    import polars as pl
    import qstrader
    from qstrader import settings
    from qstrader.asset.universe.static import StaticUniverse
    from qstrader.broker.simulated_broker import SimulatedBroker
    from qstrader.data.backtest_data_handler import BacktestDataHandler
    from qstrader.data.daily_bar_csv import CSVDailyBarDataSource
    from qstrader.exchange.simulated_exchange import SimulatedExchange
    from qstrader.execution.order import Order

    verify_imported_module(qstrader, source)
    settings.set_print_events(False)
    original = pl.read_parquet(fixture).with_row_index("source_row")
    selected = original.filter(
        (pl.col("datetime").dt.hour() == 0)
        & (pl.col("datetime").dt.minute() == 0)
    ).head(2)
    assert selected.height == 2
    observations = selected.select("source_row", "datetime", "open", "close").to_dicts()
    csv_frame = selected.select(
        pl.col("datetime").dt.replace_time_zone(None).alias("Date"),
        pl.col("open").alias("Open"),
        pl.col("close").alias("Close"),
    ).to_pandas()
    csv_frame = csv_frame.set_index("Date")

    with tempfile.TemporaryDirectory(prefix="qstrader-boundary-") as tmp:
        csv_path = Path(tmp) / "RECORDED.csv"
        csv_frame.to_csv(csv_path, float_format="%.17g")
        ds = CSVDailyBarDataSource(tmp, "EQ", adjust_prices=False, csv_symbols=["RECORDED"])
        asset = "EQ:RECORDED"
        native_quotes = ds.asset_bid_ask_frames[asset]
        first_dt = native_quotes.index[0]
        query_dt = first_dt - pd.Timedelta(seconds=1)
        last_dt = native_quotes.index[-1]
        before_bid = float(ds.get_bid(query_dt, asset))
        before_ask = float(ds.get_ask(query_dt, asset))
        last_price = float(native_quotes.iloc[-1]["Bid"])
        first_price = float(native_quotes.iloc[0]["Bid"])
        assert before_bid == before_ask == last_price
        assert query_dt < first_dt < last_dt
        assert first_price == float(observations[0]["open"])

        starting_cash = first_price / 2
        data_handler = BacktestDataHandler(StaticUniverse([asset]), [ds])
        broker = SimulatedBroker(
            first_dt,
            SimulatedExchange(first_dt),
            data_handler,
            initial_funds=starting_cash,
        )
        broker.create_portfolio("probe")
        broker.subscribe_funds_to_portfolio("probe", starting_cash)
        broker.submit_order("probe", Order(first_dt, asset, 1, order_id="recorded-boundary-probe"))
        broker.update(first_dt)
        portfolio = broker.portfolios["probe"]
        cash_after = float(portfolio.cash)
        quantity = float(portfolio.pos_handler.positions[asset].net_quantity)
        assert quantity == 1
        assert cash_after == starting_cash - first_price
        assert cash_after < 0

    git_commit = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    result = {
        "admission": admission,
        "candidate_id": "qstrader",
        "commit": git_commit,
        "imported_module": str(Path(qstrader.__file__).resolve()),
        "fixture": {"path": str(fixture), "sha256": hashlib.sha256(fixture.read_bytes()).hexdigest(), "rows": original.height},
        "selection": {"source_rows": [int(o["source_row"]) for o in observations], "observations": observations, "price_transformation": "None; unchanged open/close values, columns renamed, UTC zone marker removed for native CSV parser."},
        "prehistory_lookup": {
            "query_time": str(query_dt), "first_available_quote_time": str(first_dt),
            "selected_future_quote_time": str(last_dt),
            "returned_bid": before_bid, "returned_ask": before_ask,
            "last_quote_price": last_price, "matches_last_quote": True,
            "native_padded_index": int(native_quotes.index.get_indexer([query_dt], method="pad")[0]),
            "criteria": ["S10", "A01"],
        },
        "cash_affordability": {
            "path": "SimulatedBroker.create_portfolio -> subscribe_funds_to_portfolio -> submit_order -> update -> _execute_order -> Portfolio.transact_asset",
            "starting_cash": starting_cash, "recorded_execution_price": first_price,
            "submitted_quantity": 1, "filled_quantity": quantity,
            "fee_model": "native default ZeroFeeModel", "cash_after": cash_after,
            "negative_cash_admitted": True, "criteria": ["S11"],
        },
        "limitations": [
            "A local simulator only; no network request or live order occurred.",
            "The source synthesizes fixed 14:30/21:00 timestamps for CSV open/close quotes. This probe tests that source's getter boundary on two unchanged price observations; it does not assert daily market-clock fidelity.",
            "Negative cash can represent borrowing in a chosen model. The demonstrated property is absence of a hard cash-only affordability constraint on the tested default simulated-broker route.",
            "The prehistory query is a reachable public getter input; no claim is made that every configured trading-session loop queries before the data begins.",
        ],
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "polars": pl.__version__},
    }
    verify_unchanged(admission)
    write_json_exclusive(args.output, result)
    print(json.dumps({"candidate": "qstrader", "commit": git_commit, "prehistory_future_quote": before_bid, "negative_cash_after": cash_after, "output": str(args.output)}))


if __name__ == "__main__":
    main()
