from __future__ import annotations

from dataclasses import replace

import numpy as np
import pytest

from bench.contract import Contract, assert_parity, delayed_targets, reference_result
from bench.data import signals


@pytest.mark.parametrize('fee,slip', [(0, 0), (5, 5), (25, 10)])
def test_buyhold_closed_form_and_cash_conservation(buyhold, fee, slip):
    contract = Contract(fee_bps=fee, slippage_bps=slip)
    result = reference_result(buyhold, contract)
    last = len(buyhold['close']) - 2
    expected = contract.initial_cash * (
        buyhold['close'][last] * (1 - slip / 10_000) * (1 - fee / 10_000)
        / (buyhold['close'][1] * (1 + slip / 10_000) * (1 + fee / 10_000)))
    np.testing.assert_allclose(result.equity[-1], expected, rtol=1e-13)
    np.testing.assert_array_equal(result.fill_bars, [1, last])
    np.testing.assert_array_equal(result.fill_sides, [1, -1])
    np.testing.assert_array_equal(result.held[:2], [0, 0])
    assert result.held[2:].all()
    np.testing.assert_allclose(result.equity, result.cash + result.units * buyhold['close'][:-1], rtol=1e-14)
    assert result.units[-1] == 0
    assert result.equity[0] == contract.initial_cash


def test_flat_no_fills_or_returns(recorded):
    decision = signals(recorded['close'], 'flat')
    result = reference_result({**recorded, 'target': delayed_targets(decision)}, Contract(fee_bps=50, slippage_bps=50))
    assert len(result.fill_bars) == 0
    assert not result.held.any()
    np.testing.assert_array_equal(result.equity, np.full(len(recorded['close']) - 1, 1_000_000.0))


@pytest.mark.parametrize('strategy', ['buy_and_hold', 'sma_cross', 'flat'])
def test_signals_are_prefix_causal_on_recorded_prices(recorded, strategy):
    full = signals(recorded['close'], strategy)
    for stop in (384, 640, 900):
        np.testing.assert_array_equal(signals(recorded['close'][:stop], strategy), full[:stop])


def test_parity_rejects_shifted_fill_wrong_path_and_wrong_ledger(buyhold):
    contract = Contract()
    result = reference_result(buyhold, contract)
    changed = result.equity.copy()
    changed[300] += 1.0
    for mutation in (replace(result, fill_bars=result.fill_bars + 1),
                     replace(result, equity=changed),
                     replace(result, equity=result.equity[:1]),
                     replace(result, cash=result.cash + 1.0),
                     replace(result, held=1 - result.held),
                     replace(result, fill_quantities=result.fill_quantities * 1.01)):
        with pytest.raises(AssertionError):
            assert_parity(mutation, result, contract)


def test_unobserved_optional_ledger_is_visible(buyhold):
    contract = Contract()
    expected = reference_result(buyhold, contract)
    actual = replace(expected, cash=None, units=None, fill_quantities=None, fill_fees=None)
    checked = assert_parity(actual, expected, contract)
    assert checked['optional_unobserved_fields'] == ['cash', 'units', 'fill_quantities', 'fill_fees']
    assert checked['equity_samples_checked'] == 999


@pytest.mark.parametrize('arguments', [
    {'initial_cash': 0}, {'initial_cash': float('nan')}, {'fee_bps': -1},
    {'fee_bps': 10_000}, {'slippage_bps': float('inf')}, {'slippage_bps': True},
    {'equity_atol': -1}, {'signal_delay_bars': 0}, {'signal_delay_bars': True},
])
def test_invalid_contract_rejected(arguments):
    with pytest.raises(ValueError):
        Contract(**arguments)
