from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

from bench.contract import Contract, Result

PreparedData = dict[str, np.ndarray]


class UnsupportedContract(ValueError):
    """The inspected adapter cannot preserve the requested common semantics."""


class AdapterUnavailable(RuntimeError):
    """No executable adapter has yet been implemented for a catalog candidate."""


@dataclass
class Diagnostic:
    run: Callable[[], Any]
    extract: Callable[[Any], Result]
    scope: str


@dataclass
class Adapter:
    """A fresh engine invocation and extraction of that invocation's real outputs.

    Factories implement create_adapter(data: PreparedData, contract: Contract).
    data arrays are source rows including one real settlement row. `target` is
    already delayed by one bar and forced flat on the final two source rows.
    Equity covers data['close'][:-1], after any fill at each close. `held`
    describes incoming inventory during the return interval ending at that close.
    Adapters must never call the benchmark oracle to produce engine outputs.
    """

    run: Callable[[], Any]
    extract: Callable[[Any], Result]
    engine_scope: str
    settings: dict[str, Any] = field(default_factory=dict)
    output_observation: dict[str, str] = field(default_factory=dict)
    core: Diagnostic | None = None


def pandas_frame(data: PreparedData, *, title_case: bool = False):
    import pandas as pd

    return pd.DataFrame(
        {(name.title() if title_case else name): data[name]
         for name in ('open', 'high', 'low', 'close', 'volume')},
        index=pd.to_datetime(data['timestamp_ns'], utc=True),
    )
