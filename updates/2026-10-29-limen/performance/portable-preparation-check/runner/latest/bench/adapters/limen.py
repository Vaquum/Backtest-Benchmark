from __future__ import annotations

import numpy as np

from bench.api import Adapter, Diagnostic, UnsupportedContract
from bench.contract import Result


def create_adapter(data, contract):
    from limen.backtest._snapshot_execution import snapshot_with_execution
    from limen.backtest.long_flat_strategy import long_flat_strategy

    if contract.costed:
        raise UnsupportedContract(
            'Limen snapshot uses entry-notional fee subtraction and charges entry costs on the first held return bar; '
            'this differs from the common cash-affordable fill-time fee contract. No costed speed score is emitted.')
    count = len(data['close']) - 1
    close, opened, desired = (data[name][:count] for name in ('close', 'open', 'target'))
    change = close - opened
    columns = {'open': opened, 'close': close, 'price_change': change, 'predictions': desired}

    def run():
        return snapshot_with_execution(columns, execution_lag_bars=1, fee_bps=0, slip_bps=0)

    def extract_execution(execution):
        held = np.asarray(execution.pos, dtype=np.int8)
        entries = np.flatnonzero((held == 1) & (np.r_[0, held[:-1]] == 0)) - 1
        exits = np.flatnonzero((held == 1) & (np.r_[held[1:], 0] == 0))
        bars = np.r_[entries, exits]
        sides = np.r_[np.ones(len(entries), dtype=np.int8), -np.ones(len(exits), dtype=np.int8)]
        order = np.argsort(bars, kind='stable')
        bars, sides = bars[order], sides[order]
        return Result(timestamp_ns=data['timestamp_ns'][:count].copy(),
                      equity=contract.initial_cash * np.cumprod(1 + execution.net), held=held,
                      fill_bars=bars, fill_sides=sides, fill_prices=close[bars].copy())

    def core():
        return long_flat_strategy(desired, opened, close, change,
                                  execution_lag_bars=1, fee_bps=0, slip_bps=0)

    return Adapter(
        run=run, extract=lambda result: extract_execution(result[1]),
        engine_scope='snapshot_with_execution: snapshot validation, return execution and all native bar metrics; internal implementation called to retain trace',
        settings={'execution_lag_bars': 1, 'input_target_already_delayed': True,
                  'lag_mapping': 'target[t] fills at close[t]; native pos[t+1] earns close[t] to close[t+1]',
                  'public_entrypoint_equivalent': 'backtest_snapshot discards execution from the same implementation',
                  'processed_rows': count},
        output_observation={'equity': 'Compounded native net returns',
                            'held': 'Native ExecutionResult.pos',
                            'fills': 'Derived from native held-segment boundaries and source close prices; no native order ledger',
                            'cash_units_quantities_fees': 'Not emitted by this return-based engine'},
        core=Diagnostic(run=core, extract=extract_execution,
                        scope='Internal long_flat_strategy return kernel only; diagnostic, not a cross-framework full-engine ranking'),
    )
