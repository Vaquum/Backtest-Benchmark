#!/usr/bin/env python3
"""Build isolated source environments for the extended Python cohort.

Run after fetch_sources.py. Successful environments emit exact third-party locks.
Install/build failures are captured and remain explicit campaign outcomes.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
SPECS = {
    "freqtrade": {"subdir": ".", "import": "freqtrade", "extra": []},
    "zipline": {"subdir": ".", "import": "zipline", "extra": ["Cython<3.2", "setuptools-scm"]},
    "qlib": {"subdir": ".", "import": "qlib", "extra": ["Cython<3.2", "setuptools-scm"]},
    "jesse": {"subdir": ".", "import": "jesse", "extra": []},
}


def setup(candidate: str, args: argparse.Namespace) -> dict:
    spec = SPECS[candidate]
    out = args.work / "setup_locked" / candidate / str(time.time_ns())
    out.mkdir(parents=True, exist_ok=False)
    envdir = args.work / "envs" / candidate
    source = (args.sources / candidate / spec["subdir"]).resolve()
    entry = next(c for c in json.loads((ROOT / "catalog/candidates.json").read_text()) if c["id"] == candidate)
    actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
    if actual != entry["commit"] or subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=source, text=True).strip():
        raise ValueError(f"Refusing changed or divergent source: {candidate}")
    python = envdir / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    manifest = {"candidate_id": candidate, "source_path": str(source), "source_commit": actual, "started_unix": time.time(), "commands": [], "status": "started", "build_isolation": False}
    child_env = dict(os.environ, UV_CACHE_DIR=str(args.work / "uv-cache"), PIP_DISABLE_PIP_VERSION_CHECK="1")
    if os.name != "nt":
        child_env.setdefault("CC", "cc")
        child_env.setdefault("CXX", "c++")
    commands = []
    if not python.exists():
        commands.append([args.uv, "venv", "--seed", "--python", sys.executable, str(envdir)])
    lock = ROOT / "locks" / f"{candidate}.txt"
    if lock.is_file():
        manifest["dependency_lock_sha256"] = hashlib.sha256(lock.read_bytes()).hexdigest()
        commands.append([args.uv, "pip", "sync", "--python", str(python), "--require-hashes", str(lock)])
        commands.append([args.uv, "pip", "install", "--python", str(python), "--no-deps", "--no-build-isolation", "--reinstall", str(source)])
    else:
        raise ValueError(f"Missing reviewed dependency hash lock: {lock}; create a new explicit campaign lock before bootstrapping")
    commands += [
        [str(python), "-c", f"import {spec['import']}; print({spec['import']}.__file__)"],
        [args.uv, "pip", "check", "--python", str(python)],
    ]
    try:
        with (out / "build.log").open("w") as log:
            for command in commands:
                log.write("COMMAND " + json.dumps(command) + "\n")
                log.flush()
                start = time.perf_counter()
                proc = subprocess.run(command, env=child_env, stdout=log, stderr=subprocess.STDOUT, timeout=args.timeout)
                manifest["commands"].append({"argv": command, "returncode": proc.returncode, "seconds": time.perf_counter() - start})
                if proc.returncode:
                    raise RuntimeError(f"Command exited {proc.returncode}")
        freeze = subprocess.check_output([args.uv, "pip", "freeze", "--python", str(python)], text=True, env=child_env)
        (out / "freeze.txt").write_text(freeze)
        manifest["status"] = "ready"
        manifest["tracked_source_clean_after"] = not bool(subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=source, text=True).strip())
    except Exception as exc:
        manifest.update(status="blocked", error=f"{type(exc).__name__}: {exc}")
    manifest["elapsed_seconds"] = time.time() - manifest["started_unix"]
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    stable = args.work / "manifests" / f"{candidate}.json"
    stable.parent.mkdir(parents=True, exist_ok=True)
    stable.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({k: manifest[k] for k in ["candidate_id", "status", "elapsed_seconds"]}), flush=True)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", choices=list(SPECS), default=list(SPECS))
    parser.add_argument("--sources", type=Path, default=ROOT / ".work" / "sources")
    parser.add_argument("--work", type=Path, default=ROOT / ".work")
    parser.add_argument("--uv", default="uv")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--jobs", type=int, default=2)
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(lambda candidate: setup(candidate, args), args.only))
    if any(result["status"] != "ready" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
