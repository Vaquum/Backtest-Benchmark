#!/usr/bin/env python3
"""Bounded local reproduction of AsyncCaller error propagation at a pinned source.

No market data, model, recorder, network operation or external service is used.
The subprocess deadline contains the library's unbounded thread join.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
from common import admit_probe, verify_imported_module, verify_unchanged, write_json_exclusive


def child(source):
    import threading

    sys.path.insert(0, str(source))
    import qlib
    from qlib.utils.paral import AsyncCaller

    verify_imported_module(qlib, source)
    observed = {"callback_did_run": False, "tail_callback_did_run": False}
    released = threading.Event()
    exceptions = []
    previous_hook = threading.excepthook

    def capture_error(args):
        exceptions.append({"type": args.exc_type.__name__, "message": str(args.exc_value)})

    def fail():
        observed["callback_did_run"] = True
        assert released.wait(3), "probe coordination deadline expired"
        raise ValueError("bounded local callback failure")

    def tail():
        observed["tail_callback_did_run"] = True

    threading.excepthook = capture_error
    try:
        caller = AsyncCaller()
        caller(fail)
        caller(tail)
        released.set()
        try:
            caller.wait()
            observed["wait_returned_normally"] = True
            observed["wait_exception"] = None
        except Exception as error:
            observed["wait_returned_normally"] = False
            observed["wait_exception"] = type(error).__name__
        observed["worker_alive_after_wait"] = caller._t.is_alive()
        observed["queued_items_after_wait"] = caller._q.qsize()
        observed["thread_exceptions"] = exceptions
    finally:
        threading.excepthook = previous_hook
    assert observed["callback_did_run"]
    assert not observed["tail_callback_did_run"]
    assert observed["wait_returned_normally"]
    assert not observed["worker_alive_after_wait"]
    assert observed["queued_items_after_wait"] == 2
    assert exceptions == [{"type": "ValueError", "message": "bounded local callback failure"}]
    print(json.dumps(observed, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--child", action="store_true")
    args = parser.parse_args()
    source = args.source.resolve()
    if args.child:
        admission = admit_probe("qlib", source)
        child(source)
        verify_unchanged(admission)
        return
    if args.output is None:
        parser.error("--output is required")
    admission = admit_probe("qlib", source, output=args.output)
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--source", str(source), "--child"],
        text=True, capture_output=True, timeout=20, check=True,
    )
    observed = json.loads(completed.stdout.strip().splitlines()[-1])
    commit = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    result = {
        "admission": admission,
        "candidate_id": "qlib", "commit": commit,
        "scope": "Native AsyncCaller only; MLflowRecorder call-site implications are inspected, not executed.",
        "evidence_type": ["Inspected", "Reproduced"],
        "protocol": "Queue one bounded ValueError callback followed by an observable tail callback; capture threading.excepthook; call native wait under a 20-second subprocess deadline.",
        "source_path": str(source), "python": sys.version,
        "observed": observed,
        "interpretation": "The worker exception is reported to the thread hook, while wait returns normally and the following callback and stop marker remain queued.",
        "limitations": "No actual MLflow write, recorder end_run, process kill, live trading or network operation was executed.",
        "source_refs": [
            {"path": "qlib/utils/paral.py", "start_line": 84, "end_line": 116},
            {"path": "qlib/workflow/recorder.py", "start_line": 390, "end_line": 405},
            {"path": "qlib/workflow/recorder.py", "start_line": 490, "end_line": 506},
        ],
    }
    for ref in result["source_refs"]:
        ref["url"] = f"https://github.com/microsoft/qlib/blob/{commit}/{ref['path']}#L{ref['start_line']}-L{ref['end_line']}"
    verify_unchanged(admission)
    write_json_exclusive(args.output, result)
    print(json.dumps({"output": str(args.output), "observed": observed}))


if __name__ == "__main__":
    main()
