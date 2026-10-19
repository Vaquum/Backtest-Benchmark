from __future__ import annotations

import os
from pathlib import Path

import pytest

from bench.contract import delayed_targets
from bench.data import read_recorded_bars, signals

FIXTURE_SHA256 = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'


@pytest.fixture(scope='session')
def recorded_path():
    root = Path(__file__).resolve().parents[1]
    supplied = os.environ.get('BENCH_TEST_FIXTURE')
    candidates = ([Path(supplied)] if supplied else []) + [
        root / '.work/sources/limen/tests/fixtures/spot_1h_20240101_20241231.parquet',
        root.parent / 'benchmark-sources/limen/tests/fixtures/spot_1h_20240101_20241231.parquet']
    path = next((candidate for candidate in candidates if candidate.is_file()), None)
    if path is None:
        pytest.skip('Supply the hash-pinned recorded fixture via BENCH_TEST_FIXTURE; market prices are never generated for tests')
    return path


@pytest.fixture
def recorded(recorded_path):
    data, _ = read_recorded_bars(recorded_path, evaluation_rows=999, expected_sha256=FIXTURE_SHA256)
    return data


@pytest.fixture
def buyhold(recorded):
    signal = signals(recorded['close'], 'buy_and_hold')
    return {**recorded, 'signal': signal, 'target': delayed_targets(signal)}
