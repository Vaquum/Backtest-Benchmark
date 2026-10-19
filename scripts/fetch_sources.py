#!/usr/bin/env python3
"""Fetch exactly the reviewed revisions. Existing divergent checkouts are refused."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.check_output(["git", *args], cwd=cwd, text=True).strip()


def fetch(candidate: dict, destination: Path) -> dict:
    target = destination / candidate["id"]
    expected = candidate["commit"]
    if target.exists():
        if git("rev-parse", "HEAD", cwd=target) != expected:
            raise RuntimeError(f"Refusing divergent source checkout: {target}")
        if git("status", "--porcelain", "--untracked-files=no", cwd=target):
            raise RuntimeError(f"Refusing modified tracked source: {target}")
    else:
        target.mkdir(parents=True)
        git("init", "--quiet", cwd=target)
        git("remote", "add", "origin", candidate["url"] + ".git", cwd=target)
        git("fetch", "--depth", "1", "origin", expected, cwd=target)
        git("checkout", "--detach", "FETCH_HEAD", cwd=target)
    actual = git("rev-parse", "HEAD", cwd=target)
    if actual != expected:
        raise RuntimeError(f"Source revision mismatch for {candidate['id']}")
    return {"id": candidate["id"], "commit": actual, "path": str(target)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", help="Candidate IDs; default all reviewed sources")
    parser.add_argument("--include-auxiliary", action="store_true", help="Also admit pinned native dependency sources listed separately in the catalog")
    parser.add_argument("--destination", type=Path, default=ROOT / ".work" / "sources")
    args = parser.parse_args()
    candidates = json.loads((ROOT / "catalog" / "candidates.json").read_text())
    if args.include_auxiliary:
        candidates += json.loads((ROOT / "catalog" / "auxiliary_sources.json").read_text())
    if args.only:
        unknown = set(args.only) - {c["id"] for c in candidates}
        if unknown:
            parser.error(f"Unknown candidate IDs: {sorted(unknown)}")
        candidates = [c for c in candidates if c["id"] in args.only]
    args.destination.mkdir(parents=True, exist_ok=True)
    for candidate in candidates:
        print(json.dumps(fetch(candidate, args.destination)), flush=True)


if __name__ == "__main__":
    main()
