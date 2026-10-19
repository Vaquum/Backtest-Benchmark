from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess

PINNED_SHA = '29837e666604eee74a2ac94f328fb9803724342a'
FIXTURE = 'tests/fixtures/spot_1h_20240101_20241231.parquet'
FIXTURE_SHA256 = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'
BENCHMARK_ENV = {
    'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
    'VECLIB_MAXIMUM_THREADS': '1', 'BLIS_NUM_THREADS': '1', 'POLARS_MAX_THREADS': '1',
    'NUMEXPR_NUM_THREADS': '1', 'PYTHONHASHSEED': '0',
}


def validate_repository(repo_root: Path) -> Path:
    root = repo_root.expanduser().resolve(strict=True)
    actual_root = Path(subprocess.check_output(
        ['git', '-C', str(root), 'rev-parse', '--show-toplevel'], text=True).strip()).resolve()
    if actual_root != root:
        raise SystemExit('--repo-root must be the top-level pinned Limen checkout')
    actual_sha = subprocess.check_output(
        ['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
    if actual_sha != PINNED_SHA:
        raise SystemExit(f'Expected commit {PINNED_SHA}; found {actual_sha}')
    changed = subprocess.check_output(
        ['git', '-C', str(root), 'diff', '--name-only', 'HEAD'], text=True).strip()
    if changed:
        raise SystemExit(f'Tracked source changes prevent a pinned baseline run: {changed}')
    digest = sha256((root / FIXTURE).read_bytes()).hexdigest()
    if digest != FIXTURE_SHA256:
        raise SystemExit(f'Fixture SHA256 mismatch: {digest}')
    return root


def prepare_output(output: Path, repo_root: Path, *, outside_git: bool = False) -> Path:
    target = output.expanduser().resolve()
    if target == repo_root or repo_root in target.parents:
        raise SystemExit('--output must be outside the Limen repository')
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        raise SystemExit('--output must be a new or empty directory; prior evidence will not be overwritten')
    target.mkdir(parents=True, exist_ok=True)
    if outside_git:
        git_context = subprocess.run(['git', '-C', str(target), 'rev-parse', '--show-toplevel'],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if git_context.returncode == 0:
            raise SystemExit('Test temporary output must be outside every Git checkout, because project-binding tests inspect ancestors')
    return target
