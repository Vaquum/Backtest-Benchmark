#!/usr/bin/env python3
"""Download the one admitted recorded fixture and verify bytes before publishing it locally."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".work/data/recorded_spot_1h_2024.parquet")
    args = parser.parse_args()
    specification = json.loads((ROOT / "catalog/data.json").read_text())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        if hashlib.sha256(args.output.read_bytes()).hexdigest() != specification["sha256"]:
            raise ValueError("Existing input differs; refusing to overwrite it")
    else:
        with tempfile.NamedTemporaryFile(dir=args.output.parent, delete=False) as staged:
            temporary = Path(staged.name)
            try:
                total = 0
                digest = hashlib.sha256()
                with urllib.request.urlopen(specification["url"], timeout=45) as response:
                    while chunk := response.read(1024 * 1024):
                        total += len(chunk)
                        if total > 20_000_000:
                            raise ValueError("Input exceeds the admitted download size budget")
                        digest.update(chunk)
                        staged.write(chunk)
                staged.flush()
                if digest.hexdigest() != specification["sha256"]:
                    raise ValueError("Downloaded bytes differ from the pinned fixture hash")
                staged.close()
                temporary.replace(args.output)
            finally:
                temporary.unlink(missing_ok=True)
    print(json.dumps({"path": str(args.output.resolve()), "sha256": specification["sha256"], "source_url": specification["url"]}))


if __name__ == "__main__":
    main()
