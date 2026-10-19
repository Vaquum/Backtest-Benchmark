#!/usr/bin/env python3
"""Install hash-verified official Linux x86-64 toolchains inside .work only."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import tarfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=["rust", "dotnet"], nargs="+", default=["rust", "dotnet"])
    args = parser.parse_args()
    if platform.system() != "Linux" or platform.machine() != "x86_64":
        parser.error("This captured toolchain lock is Linux x86-64 only; supply a separately reviewed platform lock.")
    work = ROOT / ".work"
    downloads = work / "toolchain-downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    manifest = []
    for item in json.loads((ROOT / "catalog/toolchains.json").read_text())["artifacts"]:
        if item["toolchain"] not in args.only:
            continue
        start = time.monotonic()
        algo = "sha256" if "sha256" in item else "sha512"
        archive = downloads / (item["id"] + "." + item["archive"])
        checksum = hashlib.new(algo)
        if not archive.is_file():
            with urllib.request.urlopen(item["url"], timeout=60) as response, archive.open("wb") as target:
                total = 0
                while chunk := response.read(2**20):
                    total += len(chunk)
                    if total > 700_000_000:
                        raise ValueError("Official toolchain archive exceeded admitted size budget")
                    target.write(chunk)
        with archive.open("rb") as stream:
            for chunk in iter(lambda: stream.read(2**20), b""):
                checksum.update(chunk)
        if checksum.hexdigest() != item[algo]:
            raise ValueError(f"Toolchain hash mismatch: {item['id']}")
        prefix = work / "toolchains" / item["toolchain"]
        prefix.mkdir(parents=True, exist_ok=True)
        extraction = downloads / (item["id"] + "-extracted") if item["install_script"] else prefix
        extraction.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archive) as package:
            package.extractall(extraction, filter="data")
        command = None
        if item["install_script"]:
            scripts = list(extraction.glob("*/install.sh"))
            if len(scripts) != 1:
                raise ValueError("Expected one official component installer")
            command = ["sh", str(scripts[0]), f"--prefix={prefix}", "--disable-ldconfig"]
            with (downloads / f"{item['id']}.install.log").open("w") as log:
                subprocess.run(command, check=True, stdout=log, stderr=subprocess.STDOUT, timeout=180)
        manifest.append(dict(item, seconds=time.monotonic()-start, status="installed", install_command=command))
        print(json.dumps({"id": item["id"], "status": "installed", "seconds": manifest[-1]["seconds"]}), flush=True)
        (downloads / "installed.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
