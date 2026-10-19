from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from kit_common import BENCHMARK_ENV, FIXTURE, FIXTURE_SHA256, PINNED_SHA, prepare_output, validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description='Run the two pinned repository benchmark harnesses sequentially; no competitor engine is selected.')
    parser.add_argument('--repo-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='New or empty directory outside the repository')
    parser.add_argument('--only', choices=['both', 'factorized', 'snapshot'], default='both')
    args = parser.parse_args()
    root = validate_repository(args.repo_root)
    out = prepare_output(args.output, root)
    runs = []
    if args.only in ('both', 'factorized'):
        runs.append(('factorized-current', [sys.executable, '-m', 'tests.benchmark_factorized_preparation',
                                           '--output', str(out / 'factorized-current')]))
    if args.only in ('both', 'snapshot'):
        runs.append(('backtest-current', [sys.executable, '-m', 'tests.benchmark_backtest_strategies',
                                         '--inputs', str(root / FIXTURE), '--output', str(out / 'backtest-current'),
                                         '--strategies', 'buy_and_hold', 'sma_cross', '--engines', 'limen', '--repeats', '7']))
    manifest = {'created_utc': datetime.now(timezone.utc).isoformat(), 'commit': PINNED_SHA,
                'fixture_sha256': FIXTURE_SHA256, 'environment_overrides': BENCHMARK_ENV,
                'runs': [], 'scope': 'New reproduction run; never a replacement for preserved historical evidence'}
    for name, command in runs:
        record = {'name': name, 'command': command}
        manifest['runs'].append(record)
        (out / 'command_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        start = time.perf_counter()
        with (out / f'{name}.log').open('w', encoding='utf-8') as log:
            with subprocess.Popen(command, cwd=root, env={**os.environ, **BENCHMARK_ENV},
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1) as child:
                assert child.stdout is not None
                for line in child.stdout:
                    log.write(line)
                    log.flush()
                    sys.stdout.write(line)
                    sys.stdout.flush()
                code = child.wait()
        record.update(exit_code=code, wrapper_wall_seconds=time.perf_counter() - start)
        (out / 'command_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        if code:
            return code
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
