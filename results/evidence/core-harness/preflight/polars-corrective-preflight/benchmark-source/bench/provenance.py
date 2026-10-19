from __future__ import annotations

import base64
from hashlib import sha256
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from urllib.parse import unquote, urlparse

PACKAGES = {'limen': 'vaquum-limen', 'backtrader': 'backtrader', 'vectorbt': 'vectorbt',
            'backtesting_py': 'backtesting', 'bt': 'bt', 'qstrader': 'qstrader',
            'qlib': 'pyqlib', 'freqtrade': 'freqtrade', 'zipline': 'zipline-reloaded',
            'jesse': 'jesse', 'nautilus': 'nautilus_trader', 'hftbacktest': 'hftbacktest'}
MODULES = {**{key: key for key in PACKAGES}, 'backtesting_py': 'backtesting',
           'nautilus': 'nautilus_trader'}
THREAD_ENV = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
              'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'NUMBA_NUM_THREADS',
              'RAYON_NUM_THREADS', 'BLIS_NUM_THREADS', 'POLARS_MAX_THREADS')


def observe_native_thread_pools() -> dict:
    if any(os.environ.get(name) != '1' for name in THREAD_ENV):
        raise ValueError('Every declared native thread limit must remain fixed to one')
    from threadpoolctl import threadpool_info
    pools = threadpool_info()
    if any(row.get('num_threads', 1) != 1 for row in pools):
        raise ValueError('A loaded native threadpool differs from the fixed one-thread protocol')
    polars = sys.modules.get('polars')
    observations = {'polars': {'loaded': False}}
    if polars is not None:
        count = polars.thread_pool_size()
        observations['polars'] = {'loaded': True, 'pool_size': count,
                                  'version': polars.__version__}
        if count != 1:
            raise ValueError(f'The loaded Polars native thread pool has {count} threads, expected one')
    return {'threadpools': pools, 'native_thread_observations': observations}


def verify_source_install(engine: str, root: Path, manifest_path: Path) -> dict:
    catalog = {row['id']: row for row in json.loads((root / 'catalog/candidates.json').read_text())}
    candidate = catalog[engine]
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('status') not in ('installed', 'ready'):
        raise ValueError('Candidate setup manifest does not report a successful source installation')
    source = Path(manifest['source_path']).resolve()
    commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    if commit != candidate['commit']:
        raise ValueError(f'Catalog/source revision mismatch: {commit}')
    if subprocess.run(['git', '-C', str(source), 'diff', '--quiet', 'HEAD']).returncode:
        raise ValueError('Candidate tracked source was modified after the revision was frozen')
    config = Path(sys.prefix) / 'pyvenv.cfg'
    if not config.is_file() or 'include-system-site-packages = true' in config.read_text().lower():
        raise ValueError('Ranked workers require a clean virtual environment without inherited system packages')
    distribution = metadata.distribution(PACKAGES[engine])
    direct_url = json.loads(distribution.read_text('direct_url.json') or '{}')
    url = urlparse(direct_url.get('url', ''))
    if url.scheme != 'file' or Path(unquote(url.path)).resolve() != source:
        raise ValueError('Installed candidate does not identify the exact frozen local source path')
    if direct_url.get('dir_info', {}).get('editable'):
        raise ValueError('Performance workers require a built source installation, not an editable checkout')
    code_hash = sha256()
    code_count = 0
    for relative in sorted(distribution.files or [], key=str):
        if relative.suffix not in ('.py', '.so', '.pyd', '.dll', '.dylib'):
            continue
        path = Path(distribution.locate_file(relative))
        payload = path.read_bytes()
        if relative.hash and relative.hash.mode == 'sha256':
            observed = base64.urlsafe_b64encode(sha256(payload).digest()).rstrip(b'=').decode()
            if observed != relative.hash.value:
                raise ValueError(f'Installed candidate file differs from its build RECORD: {relative}')
        code_hash.update(str(relative).encode())
        code_hash.update(sha256(payload).digest())
        code_count += 1
    if not code_count:
        raise ValueError('No installed candidate code could be fingerprinted')
    return {'catalog': candidate, 'source_commit_verified': commit, 'source_path': str(source),
            'tracked_source_clean': True, 'distribution': distribution.metadata['Name'],
            'distribution_version': distribution.version, 'direct_url': direct_url,
            'installed_code_files': code_count, 'installed_code_sha256': code_hash.hexdigest(),
            'setup_manifest_sha256': sha256(manifest_path.read_bytes()).hexdigest(),
            'system_site_packages': False}


def runtime_environment() -> dict:
    constraints = {}
    for path in ('/sys/fs/cgroup/cpu.max', '/sys/fs/cgroup/memory.max'):
        file = Path(path)
        if file.is_file():
            constraints[path] = file.read_text().strip()
    try:
        affinity = sorted(os.sched_getaffinity(0))
    except AttributeError:
        affinity = None
    cpu_model = None
    cpuinfo = Path('/proc/cpuinfo')
    if cpuinfo.is_file():
        cpu_model = next((line.split(':', 1)[1].strip() for line in cpuinfo.read_text().splitlines()
                          if line.startswith('model name')), None)
    return {'python': sys.version, 'executable': sys.executable, 'prefix': sys.prefix,
            'platform': platform.platform(), 'machine': platform.machine(),
            'cpu_model': cpu_model, 'logical_cpus_visible': os.cpu_count(),
            'cpu_affinity': affinity, 'container_constraints': constraints,
            'thread_environment': {key: os.environ.get(key) for key in THREAD_ENV},
            'packages': sorted([{'name': item.metadata['Name'], 'version': item.version}
                                for item in metadata.distributions()], key=lambda row: row['name'].lower())}


def verify_import_location(engine: str) -> dict:
    namespace = MODULES[engine]
    prefix = Path(sys.prefix).resolve()
    observed = {}
    for name, module in list(sys.modules.items()):
        if name == namespace or name.startswith(namespace + '.'):
            filename = getattr(module, '__file__', None)
            if filename is None:
                continue
            path = Path(filename).resolve()
            if not path.is_relative_to(prefix):
                raise ValueError(f'Candidate module resolved outside its verified built environment: {name}: {path}')
            observed[name] = str(path)
    if namespace not in observed:
        raise ValueError('No actual candidate package import was observed')
    return observed
