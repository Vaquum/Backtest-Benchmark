from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import numpy as np

from bench.contract import delayed_targets

STRATEGY_PARAMETERS = {'buy_and_hold': {}, 'sma_cross': {'fast_period': 50, 'slow_period': 200},
                       'flat': {}}


def signals(close: np.ndarray, strategy: str) -> np.ndarray:
    if strategy == 'buy_and_hold':
        return np.ones(len(close), dtype=np.int8)
    if strategy == 'flat':
        return np.zeros(len(close), dtype=np.int8)
    if strategy != 'sma_cross':
        raise ValueError(f'Unknown strategy {strategy!r}')
    cumulative = np.r_[0.0, np.cumsum(close, dtype=np.float64)]
    means = []
    for period in (50, 200):
        mean = np.full(len(close), np.nan)
        if len(close) >= period:
            mean[period - 1:] = (cumulative[period:] - cumulative[:-period]) / period
        means.append(mean)
    return (means[0] > means[1]).astype(np.int8)


def array_digest(data: dict[str, np.ndarray]) -> str:
    checksum = sha256()
    for name, values in sorted(data.items()):
        value = np.asarray(values)
        checksum.update(name.encode())
        checksum.update(str(value.dtype).encode())
        checksum.update(str(value.shape).encode())
        checksum.update(value.tobytes(order='C'))
    return checksum.hexdigest()


def read_recorded_bars(path: Path, *, evaluation_rows: int | None = None,
                       expected_sha256: str | None = None, timestamp_column: str = 'datetime',
                       timestamp_semantics: str = 'bar_open', interval_seconds: int = 3600) -> tuple[dict, dict]:
    import pandas as pd

    file_hash = sha256(path.read_bytes()).hexdigest()
    if expected_sha256 and file_hash != expected_sha256:
        raise ValueError(f'Recorded input hash mismatch: {file_hash}')
    frame = pd.read_parquet(path, engine='pyarrow')
    source_row_count = len(frame)
    if evaluation_rows is not None:
        if evaluation_rows < 3 or evaluation_rows + 1 > len(frame):
            raise ValueError('Requested prefix requires at least three evaluation rows and one real settlement row')
        frame = frame.iloc[:evaluation_rows + 1]
    if len(frame) < 4:
        raise ValueError('At least four real bars are required')
    required = [timestamp_column, 'open', 'high', 'low', 'close', 'volume']
    if any(name not in frame for name in required) or frame[required].isna().any().any():
        raise ValueError(f'Recorded bars require nonnull columns {required}')
    timestamps = pd.DatetimeIndex(pd.to_datetime(frame[timestamp_column], utc=True)).as_unit('ns').asi8
    if not np.all(timestamps[1:] > timestamps[:-1]):
        raise ValueError('Recorded timestamps must be strictly increasing without duplicates')
    if timestamp_semantics not in ('bar_open', 'bar_close'):
        raise ValueError('Declare timestamp semantics as bar_open or bar_close')
    if isinstance(interval_seconds, bool) or interval_seconds <= 0:
        raise ValueError('The declared bar interval must be positive')
    close_timestamps = timestamps + (interval_seconds * 1_000_000_000 if timestamp_semantics == 'bar_open' else 0)
    values = {name: frame[name].to_numpy(dtype=np.float64) for name in ('open', 'high', 'low', 'close', 'volume')}
    if any(not np.isfinite(value).all() for value in values.values()):
        raise ValueError('Recorded OHLCV must be finite')
    if any((values[name] <= 0).any() for name in ('open', 'high', 'low', 'close')) or (values['volume'] < 0).any():
        raise ValueError('Prices must be positive and volume nonnegative')
    if ((values['low'] > np.minimum(values['open'], values['close'])).any()
            or (values['high'] < np.maximum(values['open'], values['close'])).any()
            or (values['low'] > values['high']).any()):
        raise ValueError('Recorded OHLC bounds are inconsistent')
    data = {**values, 'timestamp_ns': close_timestamps, 'source_timestamp_ns': timestamps}
    metadata = {'input_path': str(path.resolve()), 'input_sha256': file_hash,
                'source_file_rows': source_row_count, 'source_rows_used': len(frame),
                'evaluation_rows': len(frame) - 1, 'timestamp_column': timestamp_column,
                'source_timestamp_semantics': timestamp_semantics, 'bar_interval_seconds': interval_seconds,
                'normalization': 'Original prices unchanged; close event timestamp derived from declared source interval semantics',
                'first_close_timestamp_ns': int(close_timestamps[0]),
                'last_evaluated_close_timestamp_ns': int(close_timestamps[-2]),
                'settlement_close_timestamp_ns': int(close_timestamps[-1]),
                'venue_provenance': 'Byte identity only unless an external data manifest establishes more'}
    return data, metadata


def prepare_scenario(data: dict, strategy: str, destination: Path) -> dict:
    signal = signals(data['close'], strategy)
    prepared = {**data, 'signal': signal, 'target': delayed_targets(signal)}
    np.savez(destination, **prepared)
    return {'strategy': strategy, 'strategy_parameters': STRATEGY_PARAMETERS[strategy],
            'prepared_arrays_sha256': array_digest(prepared),
            'signal_sha256': sha256(signal.tobytes()).hexdigest(),
            'prepared_file_sha256': sha256(destination.read_bytes()).hexdigest(),
            'prepared_path': str(destination.resolve())}
