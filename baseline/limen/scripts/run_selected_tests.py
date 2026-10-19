from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

from kit_common import PINNED_SHA, prepare_output, validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description='Run the original 82 selected test modules, or the three setup-failure cases, in a correctly installed checkout.')
    parser.add_argument('--repo-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='New or empty directory outside every Git repository')
    parser.add_argument('--selection', choices=['selected', 'retest3'], default='selected')
    args = parser.parse_args()
    root = validate_repository(args.repo_root)
    out = prepare_output(args.output, root, outside_git=True)
    selection_file = Path(__file__).resolve().parents[1] / 'evidence/tests/selected_tests.json'
    selections = json.loads(selection_file.read_text())
    paths = selections['selected_modules' if args.selection == 'selected' else 'retest_case_ids']
    variables = {
        'POLARS_MAX_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
        'VECLIB_MAXIMUM_THREADS': '1', 'BLIS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1',
        'OMP_THREAD_LIMIT': '1', 'PYTEST_DISABLE_PLUGIN_AUTOLOAD': '1', 'COVERAGE_CORE': 'sysmon',
        'COVERAGE_FILE': str(out / 'coverage.db'),
        'LIMEN_RUNTIME_PROFILE_PATH': str(out / 'test_runtime_profile.json'),
    }
    command = [sys.executable, '-m', 'coverage', 'run', '-m', 'tests.run', '-q',
               '--basetemp', str(out / 'pytest-temp'), '--junitxml', str(out / 'junit.xml'), *paths]
    manifest = {'commit': PINNED_SHA, 'command': command, 'environment_overrides': variables,
                'selected_arguments': len(paths), 'selection': args.selection,
                'scope': 'New targeted reproduction campaign; fresh coverage database; not the full repository suite',
                'platform': platform.platform(), 'python': sys.version,
                'logical_cpu_count': os.cpu_count(),
                'cpu_affinity_count': len(os.sched_getaffinity(0)) if hasattr(os, 'sched_getaffinity') else None}
    (out / 'run_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    start = time.perf_counter()
    with (out / 'pytest.log').open('w', encoding='utf-8') as log:
        with subprocess.Popen(command, cwd=root, env={**os.environ, **variables},
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1) as child:
            assert child.stdout is not None
            for line in child.stdout:
                log.write(line)
                log.flush()
                sys.stdout.write(line)
                sys.stdout.flush()
            code = child.wait()
    manifest.update(exit_code=code, wall_seconds=time.perf_counter() - start)
    report = subprocess.run([sys.executable, '-m', 'coverage', 'json', '-o', str(out / 'coverage.json')],
                            cwd=root, env={**os.environ, **variables}, check=False)
    manifest['coverage_json_returncode'] = report.returncode
    (out / 'run_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return code


if __name__ == '__main__':
    raise SystemExit(main())
