from __future__ import annotations

import pandas as pd
import pytest
import os
import sys
from types import SimpleNamespace
from threadpoolctl import threadpool_limits

from bench.cli import aggregate_cases, run_process
from bench.data import read_recorded_bars
from bench.provenance import THREAD_ENV, observe_native_thread_pools, verify_import_location


def test_wrong_fixture_hash_rejected(recorded_path):
    with pytest.raises(ValueError, match='hash mismatch'):
        read_recorded_bars(recorded_path, expected_sha256='0' * 64)


def test_reordered_real_rows_rejected(recorded_path, tmp_path):
    frame = pd.read_parquet(recorded_path).iloc[:384]
    order = [1, 0, *range(2, len(frame))]
    path = tmp_path / 'reordered-real-bars.parquet'
    frame.iloc[order].to_parquet(path)
    with pytest.raises(ValueError, match='strictly increasing'):
        read_recorded_bars(path)


def test_missing_timestamp_rejected(recorded_path, tmp_path):
    path = tmp_path / 'missing-timestamp.parquet'
    pd.read_parquet(recorded_path).iloc[:384].drop(columns='datetime').to_parquet(path)
    with pytest.raises(ValueError, match='nonnull columns'):
        read_recorded_bars(path)


def case(engine, *, measured=True, rank=True, second_fails=False):
    worker = {'status': 'verified', 'peak_rss_bytes_after_full_calls': 100_000,
              'timing_samples': [{'phase': 'first', 'full_common_ms': 10.0},
                                 {'phase': 'warm-1', 'full_common_ms': 2.0, 'engine_ms': 1.5,
                                  'extraction_common_ms': 0.5, 'full_common_cpu_ms': 2.0},
                                 {'phase': 'warm-2', 'full_common_ms': 6.0, 'engine_ms': 5.5,
                                  'extraction_common_ms': 0.5, 'full_common_cpu_ms': 6.0}]}
    process = {'returncode': 0, 'launch_to_ready_ms': 1, 'launch_to_first_valid_ms': 100}
    measurements = [{'worker': worker, 'process': process},
                    {'worker': {**worker, 'status': 'parity_failed'} if second_fails else worker,
                     'process': process}] if measured else []
    return {'engine': engine, 'strategy': 'buy_and_hold', 'preflight_status': 'verified',
            'rank_against_full_engine': rank, 'requested_processes': 2 if measured else 0,
            'measurements': measurements}


def test_preflight_has_no_speed_ratios():
    row = aggregate_cases([case('limen', measured=False)])[0]
    assert row['status'] == 'verified'
    assert row['relative_to_limen_warm_full_common'] is None


def test_native_components_never_receive_full_engine_ratio():
    rows = aggregate_cases([case('limen'), case('qlib', rank=False)])
    assert rows[0]['relative_to_limen_warm_full_common'] == 1
    assert rows[1]['warm_full_common_ms_median'] == 4
    assert rows[1]['relative_to_limen_warm_full_common'] is None


def test_one_failed_process_invalidates_case_and_retains_samples():
    original = case('limen', second_fails=True)
    row = aggregate_cases([original])[0]
    assert row['status'] == 'incomplete_measurements'
    assert row['warm_full_common_ms_median'] is None
    assert row['relative_to_limen_warm_full_common'] is None
    assert len(original['measurements']) == 2


@pytest.mark.skipif(os.name != 'posix', reason='Process-group termination protocol currently targets POSIX hosts')
def test_timeout_cleans_descendant_even_if_direct_worker_has_exited(tmp_path):
    child_code = 'import subprocess,sys; subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"]); print("parent exited",flush=True)'
    observed = run_process([sys.executable, '-c', child_code], tmp_path, os.environ.copy(), tmp_path / 'process', timeout=0.2)
    assert observed['timed_out'] is True
    assert observed['process_wall_ms'] < 2500
    assert (tmp_path / 'process/stdout.log').read_text().strip() == 'parent exited'


def test_source_package_shadowing_cannot_pass_import_provenance(monkeypatch, tmp_path):
    monkeypatch.setitem(sys.modules, 'limen', SimpleNamespace(__file__=str(tmp_path / 'limen/__init__.py')))
    with pytest.raises(ValueError, match='outside its verified built environment'):
        verify_import_location('limen')


def test_polars_pool_must_obey_its_separate_thread_control(monkeypatch):
    for name in THREAD_ENV:
        monkeypatch.setenv(name, '1')
    monkeypatch.setitem(sys.modules, 'polars', SimpleNamespace(thread_pool_size=lambda: 9, __version__='admission-test'))
    with threadpool_limits(limits=1):
        with pytest.raises(ValueError, match='Polars native thread pool has 9 threads'):
            observe_native_thread_pools()


def test_thread_environment_cannot_change_during_a_call(monkeypatch):
    for name in THREAD_ENV:
        monkeypatch.setenv(name, '1')
    monkeypatch.setenv('POLARS_MAX_THREADS', '9')
    with pytest.raises(ValueError, match='must remain fixed to one'):
        observe_native_thread_pools()


def test_polars_absence_is_explicit_in_thread_observations(monkeypatch):
    for name in THREAD_ENV:
        monkeypatch.setenv(name, '1')
    monkeypatch.delitem(sys.modules, 'polars', raising=False)
    with threadpool_limits(limits=1):
        assert observe_native_thread_pools()['native_thread_observations']['polars'] == {'loaded': False}
