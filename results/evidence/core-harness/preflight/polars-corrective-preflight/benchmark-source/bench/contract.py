from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = 1


@dataclass(frozen=True)
class Contract:
    initial_cash: float = 1_000_000.0
    fee_bps: float = 0.0
    slippage_bps: float = 0.0
    signal_delay_bars: int = 1
    equity_rtol: float = 1e-10
    equity_atol: float = 1e-6
    price_rtol: float = 1e-12
    price_atol: float = 1e-8
    quantity_rtol: float = 1e-10
    quantity_atol: float = 1e-10

    def __post_init__(self):
        for name in ('initial_cash', 'fee_bps', 'slippage_bps', 'equity_rtol',
                     'equity_atol', 'price_rtol', 'price_atol', 'quantity_rtol', 'quantity_atol'):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f'{name} must be a finite number')
        if self.initial_cash <= 0:
            raise ValueError('initial_cash must be positive')
        if not 0 <= self.fee_bps < 10_000 or not 0 <= self.slippage_bps < 10_000:
            raise ValueError('Fees/slippage must be nonnegative and below 10,000 bps')
        if self.signal_delay_bars != 1 or isinstance(self.signal_delay_bars, bool):
            raise ValueError('This contract requires exactly one bar between decision and close fill')
        if min(self.equity_rtol, self.equity_atol, self.price_rtol, self.price_atol,
               self.quantity_rtol, self.quantity_atol) < 0:
            raise ValueError('Numerical tolerances must be nonnegative')

    @property
    def costed(self) -> bool:
        return bool(self.fee_bps or self.slippage_bps)

    def to_dict(self) -> dict:
        return {
            **asdict(self),
            'schema_version': SCHEMA_VERSION,
            'name': 'prior-close-decision_next-close-fill_long-flat_v1',
            'sizing': 'All affordable continuous units on entry; hold units until exit; no ongoing rebalancing',
            'signal_availability': 'Decision uses only the prefix through close[t]; earliest fill is close[t+1]',
            'fill_price': 'Entry close*(1+slippage); exit close*(1-slippage)',
            'fee_basis': 'fee_bps/10000 times actual fill price times absolute executed quantity',
            'equity_observation': 'Cash plus units marked at the unadjusted close, after the close fill',
            'held_observation': 'Incoming held state over the interval ending at the current close, before its fill',
            'terminal_rule': 'Predeclared liquidation at penultimate real close; final real row settles delayed bookkeeping',
            'unmodelled': ['market impact', 'partial fills', 'funding', 'borrowing', 'corporate actions', 'exchange calendars'],
        }

    @classmethod
    def from_dict(cls, values: dict) -> 'Contract':
        return cls(**{name: values[name] for name in cls.__dataclass_fields__ if name in values})


@dataclass
class Result:
    timestamp_ns: np.ndarray
    equity: np.ndarray
    held: np.ndarray
    fill_bars: np.ndarray
    fill_sides: np.ndarray
    fill_prices: np.ndarray
    cash: np.ndarray | None = None
    units: np.ndarray | None = None
    fill_quantities: np.ndarray | None = None
    fill_fees: np.ndarray | None = None


def delayed_targets(signal: np.ndarray) -> np.ndarray:
    values = np.asarray(signal)
    if values.ndim != 1 or len(values) < 4 or not np.isin(values, (0, 1)).all():
        raise ValueError('Signals require at least four real rows and binary decisions')
    desired = np.zeros(len(values), dtype=np.int8)
    desired[1:] = values[:-1]
    desired[-2:] = 0
    return desired


def reference_result(data: dict[str, np.ndarray], contract: Contract) -> Result:
    """Independent explicit cash/quantity replay; never imports a tested engine."""
    close, desired = data['close'], data['target']
    count = len(close) - 1
    equity = np.empty(count, dtype=np.float64)
    cash_path = np.empty(count, dtype=np.float64)
    units_path = np.empty(count, dtype=np.float64)
    held = np.empty(count, dtype=np.int8)
    fill_bars, fill_sides, fill_prices, fill_quantities, fill_fees = [], [], [], [], []
    cash, quantity = float(contract.initial_cash), 0.0
    fee_rate, slip = contract.fee_bps / 10_000, contract.slippage_bps / 10_000
    for bar in range(count):
        held[bar] = quantity > 0
        mark = float(close[bar])
        side = 0
        if desired[bar] and quantity == 0:
            side = 1
            fill_price = mark * (1 + slip)
            executed = cash / (fill_price * (1 + fee_rate))
            fee = executed * fill_price * fee_rate
            cash -= executed * fill_price + fee
            quantity = executed
        elif not desired[bar] and quantity > 0:
            side = -1
            fill_price = mark * (1 - slip)
            executed = quantity
            fee = executed * fill_price * fee_rate
            cash += executed * fill_price - fee
            quantity = 0.0
        if side:
            fill_bars.append(bar)
            fill_sides.append(side)
            fill_prices.append(fill_price)
            fill_quantities.append(executed)
            fill_fees.append(fee)
        cash_path[bar], units_path[bar] = cash, quantity
        equity[bar] = cash + quantity * mark
    if quantity != 0:
        raise AssertionError('The declared terminal rule failed to close reference inventory')
    return Result(
        timestamp_ns=data['timestamp_ns'][:count].copy(), equity=equity, held=held,
        fill_bars=np.asarray(fill_bars, dtype=np.int64),
        fill_sides=np.asarray(fill_sides, dtype=np.int8),
        fill_prices=np.asarray(fill_prices, dtype=float), cash=cash_path, units=units_path,
        fill_quantities=np.asarray(fill_quantities, dtype=float), fill_fees=np.asarray(fill_fees, dtype=float),
    )


def assert_parity(actual: Result, expected: Result, contract: Contract) -> dict:
    for name in Result.__dataclass_fields__:
        value = getattr(actual, name)
        if value is None:
            if name in ('cash', 'units', 'fill_quantities', 'fill_fees'):
                continue
            raise AssertionError(f'{name} is missing')
        if np.asarray(value).ndim != 1 or not np.isfinite(value).all():
            raise AssertionError(f'{name} must be a finite one-dimensional array')
        if np.asarray(value).shape != np.asarray(getattr(expected, name)).shape:
            raise AssertionError(f'{name} shape mismatch: {np.asarray(value).shape} != {np.asarray(getattr(expected, name)).shape}')
    for name in ('timestamp_ns', 'held', 'fill_bars', 'fill_sides'):
        np.testing.assert_array_equal(getattr(actual, name), getattr(expected, name), err_msg=f'{name} mismatch')
    np.testing.assert_allclose(actual.fill_prices, expected.fill_prices,
                               rtol=contract.price_rtol, atol=contract.price_atol, err_msg='fill price mismatch')
    np.testing.assert_allclose(actual.equity, expected.equity,
                               rtol=contract.equity_rtol, atol=contract.equity_atol, err_msg='full equity path mismatch')
    checked_optional = []
    for name in ('cash', 'units', 'fill_quantities', 'fill_fees'):
        actual_value = getattr(actual, name)
        if actual_value is None:
            continue
        is_quantity = name in ('units', 'fill_quantities')
        np.testing.assert_allclose(actual_value, getattr(expected, name),
                                   rtol=contract.quantity_rtol if is_quantity else contract.equity_rtol,
                                   atol=contract.quantity_atol if is_quantity else contract.equity_atol,
                                   err_msg=f'{name} mismatch')
        checked_optional.append(name)
    error = np.abs(actual.equity - expected.equity)
    return {'equity_samples_checked': len(expected.equity), 'fills_checked': len(expected.fill_bars),
            'max_abs_equity_error': float(np.max(error)),
            'max_relative_equity_error': float(np.max(error / expected.equity)),
            'optional_observed_fields_checked': checked_optional,
            'optional_unobserved_fields': [name for name in ('cash', 'units', 'fill_quantities', 'fill_fees')
                                          if name not in checked_optional]}


def result_summary(result: Result, contract: Contract) -> dict:
    peak = np.maximum.accumulate(np.r_[contract.initial_cash, result.equity])[1:]
    returns = result.equity / np.r_[contract.initial_cash, result.equity[:-1]] - 1
    return {'final_equity': float(result.equity[-1]),
            'total_return': float(result.equity[-1] / contract.initial_cash - 1),
            'max_drawdown': float(np.min(result.equity / peak - 1)),
            'mean_bar_return': float(np.mean(returns)), 'held_fraction': float(np.mean(result.held)),
            'entries': int(np.sum(result.fill_sides == 1)), 'exits': int(np.sum(result.fill_sides == -1))}


def save_result(path: Path, result: Result) -> None:
    np.savez(path, **{name: getattr(result, name) for name in Result.__dataclass_fields__
                     if getattr(result, name) is not None})


def load_result(path: Path) -> Result:
    with np.load(path, allow_pickle=False) as saved:
        return Result(**{name: saved[name] for name in saved.files})
