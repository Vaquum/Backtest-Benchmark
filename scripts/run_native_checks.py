#!/usr/bin/env python3
"""Build pinned native sources and run bounded crate tests; never report these as economic benchmarks."""
from __future__ import annotations
import argparse
import concurrent.futures
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=ROOT / ".work/sources")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only", nargs="+", choices=["lean", "hftbacktest", "nautilus"], default=["lean", "hftbacktest", "nautilus"])
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    work = ROOT / ".work"
    rust = work / "toolchains/rust"
    dotnet = work / "toolchains/dotnet"
    env = dict(os.environ)
    env.update({
        "PATH": str(rust / "bin") + os.pathsep + env.get("PATH", ""),
        "LD_LIBRARY_PATH": str(rust / "lib") + os.pathsep + env.get("LD_LIBRARY_PATH", ""),
        "CARGO_HOME": str(work / "cargo-home"),
        "CARGO_BUILD_JOBS": "2",
        "CC": "cc", "CXX": "c++",
        "DOTNET_ROOT": str(dotnet),
        "DOTNET_CLI_HOME": str(work / "dotnet-state"),
        "DOTNET_CLI_TELEMETRY_OPTOUT": "1",
        "DOTNET_SKIP_FIRST_TIME_EXPERIENCE": "1",
        "NUGET_PACKAGES": str(work / "nuget"),
        "DOTNET_GCHeapHardLimit": "40000000",
        "DOTNET_gcServer": "0",
    })
    commands = {
        "lean": [str(dotnet / "dotnet"), "build", "Launcher/QuantConnect.Lean.Launcher.csproj", "--configuration", "Release", "--maxcpucount:2", "--nologo", "-p:RestoreLockedMode=true"],
        "hftbacktest": [str(rust / "bin/cargo"), "test", "--locked", "-p", "hftbacktest", "--lib", "--no-default-features", "--features", "backtest"],
        "nautilus": [str(rust / "bin/cargo"), "test", "--locked", "-p", "nautilus-backtest", "--lib"],
    }

    def run(candidate):
        source = args.sources.resolve() / candidate
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
        expected = next(c["commit"] for c in json.loads((ROOT / "catalog/candidates.json").read_text()) if c["id"] == candidate)
        if head != expected:
            raise ValueError(f"Source revision differs for {candidate}")
        if subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=source, text=True).strip():
            raise ValueError(f"Tracked source modified for {candidate}")
        if candidate == "hftbacktest":
            lock = ROOT / "locks/native/hftbacktest.Cargo.lock"
            if lock.is_file():
                source_lock = source / "Cargo.lock"
                if source_lock.is_file() and source_lock.read_bytes() != lock.read_bytes():
                    raise ValueError("Existing HFT dependency lock differs from this campaign")
                shutil.copyfile(lock, source_lock)
        if candidate == "lean":
            for lock in (ROOT / "locks/lean").rglob("packages.lock.json"):
                source_lock = source / lock.relative_to(ROOT / "locks/lean")
                if source_lock.is_file() and source_lock.read_bytes() != lock.read_bytes():
                    raise ValueError(f"Existing NuGet lock differs: {source_lock}")
                shutil.copyfile(lock, source_lock)
        local_env = dict(env, CARGO_TARGET_DIR=str(work / "native-target" / candidate))
        start = time.monotonic()
        command = commands[candidate]
        timed_out = False
        with (args.output / f"{candidate}.log").open("w") as log:
            proc = subprocess.Popen(command, cwd=source, env=local_env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = proc.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    code = proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    code = proc.wait(timeout=10)
        record = {"candidate_id": candidate, "commit": head, "command": command, "source": str(source), "seconds": time.monotonic()-start,
                  "returncode": code, "timed_out": timed_out, "status": "passed" if code == 0 and not timed_out else "timeout" if timed_out else "failed",
                  "scope": "Native launcher build" if candidate == "lean" else "Native backtest crate library tests; not a matched-market performance workload",
                  "timeout_seconds": args.timeout, "parallel_compile_jobs_per_process": 2,
                  "tracked_source_clean_after": not bool(subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=source, text=True).strip())}
        (args.output / f"{candidate}.json").write_text(json.dumps(record, indent=2)+"\n")
        print(json.dumps(record), flush=True)
        return record

    # Cargo uses one shared registry cache; run the two crate tests sequentially.
    def rust_checks():
        return [run(x) for x in ["hftbacktest", "nautilus"] if x in args.only]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(rust_checks)]
        if "lean" in args.only:
            futures.append(pool.submit(run, "lean"))
        for future in futures:
            future.result()


if __name__ == "__main__":
    main()
