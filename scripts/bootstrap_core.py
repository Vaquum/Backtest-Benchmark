#!/usr/bin/env python3
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {'limen': 'vaquum-limen', 'backtrader': 'backtrader', 'vectorbt': 'vectorbt',
            'backtesting_py': 'backtesting', 'bt': 'bt', 'qstrader': 'qstrader'}
BUILD_TOOLS = ['setuptools>=83', 'wheel', 'hatchling', 'hatch-cython', 'Cython>=0.29.25']


def main() -> int:
    parser = argparse.ArgumentParser(description='Install exact catalog source revisions into separate clean core-engine environments; retain every attempt.')
    parser.add_argument('--engines', nargs='+', choices=tuple(PACKAGES), default=list(PACKAGES))
    parser.add_argument('--source-root', type=Path, default=ROOT / '.work/sources')
    parser.add_argument('--env-root', type=Path, default=ROOT / '.work/envs')
    parser.add_argument('--python', default=sys.executable, help='Interpreter used to create clean environments')
    parser.add_argument('--jobs', type=int, default=3)
    parser.add_argument('--uv', default='uv')
    parser.add_argument('--cc', help='Explicit C compiler for source extension builds; recorded in manifests')
    parser.add_argument('--cxx', help='Explicit C++ compiler for source extension builds; recorded in manifests')
    args = parser.parse_args()
    if len(set(args.engines)) != len(args.engines):
        parser.error('Engine identifiers must be unique so concurrent builds cannot mutate the same environment')
    catalog = {row['id']: row for row in json.loads((ROOT / 'catalog/candidates.json').read_text())}
    work = ROOT / '.work'
    cache = work / 'uv-cache'
    environment = {**os.environ, 'UV_CACHE_DIR': str(cache)}
    if args.cc:
        environment['CC'] = shutil.which(args.cc) or args.cc
    if args.cxx:
        environment['CXX'] = shutil.which(args.cxx) or args.cxx
    (work / 'manifests').mkdir(parents=True, exist_ok=True)

    def install(engine):
        destination = args.env_root.resolve() / engine
        source = args.source_root.resolve() / engine
        attempt = work / 'bootstrap' / engine / f'attempt-{time.time_ns()}'
        attempt.mkdir(parents=True)
        report = {'engine': engine, 'status': 'starting', 'source_path': str(source),
                  'environment_path': str(destination), 'catalog': catalog[engine],
                  'compiler_overrides': {key: environment[key] for key in ('CC', 'CXX') if key in environment},
                  'created_utc': datetime.now(timezone.utc).isoformat(), 'commands': []}
        log_path = attempt / 'install.log'

        def run(command):
            entry = {'command': [str(part) for part in command]}
            report['commands'].append(entry)
            start = time.perf_counter()
            with log_path.open('a', encoding='utf-8') as log:
                log.write('\nCOMMAND ' + json.dumps(entry['command']) + '\n')
                log.flush()
                child = subprocess.run(entry['command'], cwd=ROOT, env=environment,
                                       stdout=log, stderr=subprocess.STDOUT, check=False)
            entry.update(returncode=child.returncode, wall_seconds=time.perf_counter() - start)
            (attempt / 'attempt.json').write_text(json.dumps(report, indent=2) + '\n')
            if child.returncode:
                raise RuntimeError(f'Command exited {child.returncode}; full output is preserved in {log_path}')

        try:
            commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
            if commit != catalog[engine]['commit']:
                raise ValueError(f'Source revision mismatch for {engine}: {commit}')
            if subprocess.run(['git', '-C', str(source), 'diff', '--quiet', 'HEAD']).returncode:
                raise ValueError(f'Tracked source changes found for {engine}')
            python = destination / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
            if not python.exists():
                run([args.uv, 'venv', '--python', args.python, str(destination)])
            config = (destination / 'pyvenv.cfg').read_text()
            if 'include-system-site-packages = true' in config:
                raise ValueError('Refusing a non-hermetic system-site environment')
            committed_lock = ROOT / 'locks' / f'{engine}.txt'
            if committed_lock.is_file():
                lock = committed_lock
                report['lock_origin'] = 'committed dependency hash lock'
            else:
                requirements = attempt / 'requirements.in'
                numerical = ['numpy>=2.4.6', 'pandas>=3.0.3,<4'] if engine == 'vectorbt' else [
                    'numpy==2.2.6', 'pandas==2.3.3']
                specific_build_tools = ['setuptools-git', 'setuptools-scm'] if engine == 'backtesting_py' else []
                requirements.write_text('\n'.join([str(source), *BUILD_TOOLS, *specific_build_tools, *numerical,
                                                   'pyarrow==23.0.1', 'threadpoolctl==3.6.0']) + '\n')
                lock = attempt / 'dependencies.lock'
                run([args.uv, 'pip', 'compile', str(requirements), '--python', str(python),
                     '--generate-hashes', '--no-emit-package', PACKAGES[engine], '--output-file', str(lock)])
                report['lock_origin'] = 'new dependency resolution; exact generated hash lock retained'
            run([args.uv, 'pip', 'install', '--python', str(python), '--require-hashes', '-r', str(lock)])
            run([args.uv, 'pip', 'install', '--python', str(python), '--no-deps', '--no-build-isolation',
                 '--no-cache', '--reinstall-package', PACKAGES[engine], str(source)])
            inspect_code = (
                'from importlib import metadata;import json,sys,platform;'
                'packages=sorted([{\"name\":d.metadata[\"Name\"],\"version\":d.version} '
                'for d in metadata.distributions()],key=lambda x:x[\"name\"].lower());'
                f'd=metadata.distribution({PACKAGES[engine]!r});'
                'print(json.dumps({\"python\":sys.version,\"platform\":platform.platform(),'
                '\"prefix\":sys.prefix,\"distributions\":packages,\"candidate_version\":d.version,'
                '\"candidate_direct_url\":d.read_text(\"direct_url.json\")},indent=2))'
            )
            observed = json.loads(subprocess.check_output([str(python), '-c', inspect_code], text=True))
            if subprocess.run(['git', '-C', str(source), 'diff', '--quiet', 'HEAD']).returncode:
                raise ValueError('Source build changed tracked candidate code')
            report.update(status='installed', source_commit=commit, python=str(python),
                          dependency_lock=str(lock.resolve()),
                          dependency_lock_sha256=sha256(lock.read_bytes()).hexdigest(),
                          observed=observed, system_site_packages=False)
            (attempt / 'freeze.txt').write_text(subprocess.check_output(
                [args.uv, 'pip', 'freeze', '--python', str(python)], env=environment, text=True))
            (work / 'manifests' / f'{engine}.json').write_text(json.dumps(report, indent=2) + '\n')
        except Exception as error:
            report.update(status='installation_failed', error=f'{type(error).__name__}: {error}',
                          traceback=traceback.format_exc())
        (attempt / 'attempt.json').write_text(json.dumps(report, indent=2) + '\n')
        return {'engine': engine, 'status': report['status'], 'attempt': str(attempt),
                'error': report.get('error'), 'python': report.get('python')}

    with ThreadPoolExecutor(max_workers=max(1, min(args.jobs, len(args.engines)))) as executor:
        results = list(executor.map(install, args.engines))
    print(json.dumps(results, indent=2))
    return 0 if all(row['status'] == 'installed' for row in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
