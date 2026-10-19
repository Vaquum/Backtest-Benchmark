from __future__ import annotations

import importlib
import re

from bench.api import Adapter, AdapterUnavailable


def create_adapter(engine: str, data, contract) -> Adapter:
    if not re.fullmatch(r'[a-z][a-z0-9_]*', engine):
        raise ValueError('Engine IDs contain lowercase letters, digits and underscores')
    try:
        module = importlib.import_module(f'bench.adapters.{engine}')
    except ModuleNotFoundError as error:
        if error.name == f'bench.adapters.{engine}':
            raise AdapterUnavailable(f'No common-contract adapter implemented for {engine}; this is an unimplemented benchmark route, not a native engine capability failure') from error
        raise
    adapter = module.create_adapter(data, contract)
    if not isinstance(adapter, Adapter):
        raise TypeError('Adapter factory must return bench.api.Adapter')
    return adapter
