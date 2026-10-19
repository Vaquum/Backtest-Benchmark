#!/usr/bin/env python3
"""Write a SHA-256 inventory of shipped files, excluding the inventory itself and ignored workspace state."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = "ARTIFACTS.sha256.json"


def main():
    paths = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0")
    records = []
    for relative in sorted(set(paths) - {"", INVENTORY}):
        file = ROOT / relative
        if not file.is_file():
            continue
        if file.is_symlink():
            raise ValueError(f"Shipped artifacts may not escape through a symlink: {relative}")
        data = file.read_bytes()
        records.append({"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    (ROOT / INVENTORY).write_text(json.dumps({"schema_version": 1, "scope": "Exact files shipped in this repository snapshot; not a signature or upstream code-identity proof", "files": records}, indent=2) + "\n")
    print(json.dumps({"files": len(records), "bytes": sum(x["bytes"] for x in records), "inventory": INVENTORY}))


if __name__ == "__main__":
    main()
