"""Read-only Limen API probes; no external calls or command invocation.

Uses repository-recorded market data. The manifest mutation changes only
metadata in a disposable scratch project; repository files are untouched.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

SOURCE = Path('/workspace/scratch/008a76ec4981/limen-review-source')
OUTPUT = Path('/workspace/scratch/008a76ec4981/review-work/safety')
sys.path.insert(0, str(SOURCE))

import numpy as np
import polars as pl

from limen.backtest import backtest_snapshot
from limen.backtest._snapshot_execution import snapshot_with_execution
from limen.backtest.trade_contract import ProductSpec, TradePolicy
from limen.sfd.rule_based.common_strategies import strategy_signals
from limen.yaml.compiler import build_manifest
from limen.yaml.errors import ResolutionError
from limen.yaml.parser import parse
from limen.yaml.resolver import resolve
from limen.yaml.store import canonical_manifest_id, commit_manifest, resolve_manifest_uri
from limen.yaml.validator import validate

results = {'source_commit': '29837e666604eee74a2ac94f328fb9803724342a'}
template = SOURCE / 'limen/yaml/templates/logreg_binary.yaml'
baseline, errors = parse(template)
assert not errors
assert validate(baseline).valid

try:
    resolve('os.system')
except ResolutionError:
    direct_outside_rejected = True
else:
    direct_outside_rejected = False
path = 'limen.data.historical_data.os.system'
resolved = resolve(path)
modified = copy.deepcopy(baseline)
modified['sfd']['manifest']['data_source'] = {'method': path, 'params': {}}
validation = validate(modified)
compiled = build_manifest(modified)
results['resolver'] = {
    'direct_os_system_rejected': direct_outside_rejected,
    'prefixed_path': path,
    'resolves_to_os_system': resolved is os.system,
    'modified_manifest_valid': validation.valid,
    'validation_errors': [str(error) for error in validation.errors],
    'compiled_data_source_is_os_system': compiled.data_source_config.method is os.system,
    'callable_invoked': False,
}

fixture = SOURCE / 'tests/fixtures/spot_1h_20240101_20241231.parquet'
bars = pl.read_parquet(fixture)
columns = {name: bars[name].to_numpy() for name in ('open', 'high', 'low', 'close')}
columns['price_change'] = columns['close'] - columns['open']
columns['predictions'] = strategy_signals(bars, 'sma_cross')
cost_runs = {}
for name, options in {
    'ordinary_costs': {'fee_bps': 5.0, 'slip_bps': 5.0},
    'negative_fee': {'fee_bps': -5.0, 'slip_bps': 5.0},
    'negative_slippage': {'fee_bps': 5.0, 'slip_bps': -5.0},
    'zero_lag': {'execution_lag_bars': 0},
}.items():
    try:
        public_metrics = backtest_snapshot(columns, **options)
        metrics, execution = snapshot_with_execution(columns, **options)
        cost_runs[name] = {
            'accepted': True,
            'all_net_returns_finite': bool(np.isfinite(execution.net).all()),
            'mean_cost_bps': public_metrics['cost_per_bar_bps'],
            'mean_pnl_bps': metrics['pnl_per_bar_bps'],
        }
    except Exception as error:
        cost_runs[name] = {'accepted': False, 'error': f'{type(error).__name__}: {error}'}
event_checks = {}
for name, options in {'negative_fee': {'fee_bps': -5.0}, 'negative_slippage': {'slip_bps': -5.0}}.items():
    try:
        TradePolicy(ProductSpec('cash_spot', 'BTCUSDT', 'BTC', 'USDT', 0.00001, 5), **options)
    except ValueError as error:
        event_checks[name] = {'rejected': True, 'error': str(error)}
    else:
        event_checks[name] = {'rejected': False}
results['snapshot_boundary'] = {
    'fixture': str(fixture.relative_to(SOURCE)),
    'fixture_sha256': hashlib.sha256(fixture.read_bytes()).hexdigest(),
    'fixture_rows': bars.height,
    'signal_rule': 'sma_cross',
    'public_snapshot_results': cost_runs,
    'event_policy_contrast': event_checks,
}

with tempfile.TemporaryDirectory(prefix='manifest-probe-', dir=OUTPUT) as directory:
    project = Path(directory)
    (project / 'limen.toml').write_text('[store]\nbackup_remote = ""\n', encoding='utf-8')
    original = project / 'original.yaml'
    original.write_bytes(template.read_bytes())
    identity, existed = commit_manifest(original, project)
    assert not existed
    path, _ = resolve_manifest_uri(f'manifest://{identity}', project)
    before = path.read_text(encoding='utf-8')
    old_name = baseline['metadata']['name']
    after = before.replace(f'name: {old_name}', f'name: {old_name}_mutated', 1)
    assert after != before
    path.write_text(after, encoding='utf-8')
    mutated, errors = parse(path)
    assert not errors
    current_identity = canonical_manifest_id(mutated)
    assert current_identity != identity
    resolved_path, _ = resolve_manifest_uri(f'manifest://{identity}', project)
    results['manifest_uri_integrity'] = {
        'requested_identity': identity,
        'actual_current_identity': current_identity,
        'content_changed': current_identity != identity,
        'stale_uri_still_resolves': resolved_path == path,
        'mutated_field': 'metadata.name',
        'repository_files_modified': False,
    }

output = json.dumps(results, indent=2, allow_nan=False)
(OUTPUT / 'safety_boundary_results.json').write_text(output + '\n', encoding='utf-8')
print(output)
