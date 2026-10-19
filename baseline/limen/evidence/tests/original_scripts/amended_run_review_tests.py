from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'limen-review-source'
OUT = ROOT / 'review-work/test-run'
PYTHON = ROOT / 'review-venv/bin/python'
MODULES = '''splits walk_forward_contracts walk_forward_uel calibration convergence_report target_source_columns holdout_research holdout_assessment family_acceptance_report feature_causality acceptance_gates yaml yaml_store yaml_config round_storage round_signals checkpoint_manager parallel_rounds python_sensor sensor sensor_from_model property_contracts funding_adapter elapsed_trade_exits backtest_tp_sl nullable_trade_controls direction_sizing target_exposure objective_funding objective_resume experiment_objective objective_yaml factorized_preparation factorize_equivalence factorized_cache_bounds factorized_traversal factorized_traversal_yaml grid_permutation large_param_space msq param_space param_domain search_strategies sobol_search standard_search_enumeration feedback_controller budget_reducer correlation_reducer focus_reducer saturation_reducer sanity_reducer pruning_strategy backtest_numerical_equivalence backtest_reuse_comparator backtest_benchmark event_execution_reuse trade_outcome_target trade_outcome_reuse fixed_trade_sources record_execution record_model_outputs recording_policy transform_reuse source_interval temporal_parameters positive_training_overrides sklearn_input_boundaries feature_library_regimes feature_library_primitives feature_library_context feature_library_liquidity feature_library_realized_risk feature_library_range_volatility feature_library_candle_structure feature_library_cross_timescale feature_library_seasonality feature_library_composites column_shims ablation_result_metadata rule_based_metrics targets target_exposure metrics_and_log_helpers'''.split()
MODULES = list(dict.fromkeys(MODULES))


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    paths = [f'tests/test_{name}.py' for name in MODULES]
    missing = [p for p in paths if not (SOURCE / p).is_file()]
    if missing:
        raise FileNotFoundError(missing)
    variables = {
        'POLARS_MAX_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1',
        'MKL_NUM_THREADS': '1', 'VECLIB_MAXIMUM_THREADS': '1',
        'BLIS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1',
        'OMP_THREAD_LIMIT': '1', 'PYTEST_DISABLE_PLUGIN_AUTOLOAD': '1',
        'COVERAGE_CORE': 'sysmon', 'COVERAGE_FILE': str(OUT / 'coverage.db'),
        'LIMEN_RUNTIME_PROFILE_PATH': str(OUT / 'test_runtime_profile.json'),
    }
    command = [str(PYTHON), '-m', 'coverage', 'run', '-m', 'tests.run', '-q',
               '--basetemp', str(OUT / 'pytest-temp'),
               '--junitxml', str(OUT / 'junit.xml'), *paths]
    manifest = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=SOURCE, text=True).strip(),
        'command': command, 'environment_overrides': variables,
        'module_count': len(paths), 'scope': 'Targeted code review campaign, not full repository suite',
        'platform': platform.platform(), 'python': sys.version,
        'logical_cpu_count': os.cpu_count(),
        'cpu_affinity_count': len(os.sched_getaffinity(0)) if hasattr(os, 'sched_getaffinity') else None,
    }
    (OUT / 'run_manifest.json').write_text(json.dumps(manifest, indent=2))
    started = time.perf_counter()
    with (OUT / 'pytest.log').open('w') as log:
        with subprocess.Popen(command, cwd=SOURCE, env={**os.environ, **variables},
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1) as child:
            for line in child.stdout:
                log.write(line)
                log.flush()
                sys.stdout.write(line)
                sys.stdout.flush()
            code = child.wait()
    manifest.update(exit_code=code, wall_seconds=time.perf_counter() - started)
    (OUT / 'run_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(json.dumps({'review_test_campaign': manifest}, indent=2), flush=True)
    report = subprocess.run([str(PYTHON), '-m', 'coverage', 'json', '-o', str(OUT / 'coverage.json')],
                            cwd=SOURCE, env={**os.environ, **variables}, check=False)
    if report.returncode:
        print(f'Coverage JSON generation failed: {report.returncode}', flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
