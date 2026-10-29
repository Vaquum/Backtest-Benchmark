#!/usr/bin/env python3
"""Interpret retained paired probe JSON without importing or running Limen."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED_SOURCE = {
    "baseline": "29837e666604eee74a2ac94f328fb9803724342a",
    "latest": "25e47866422d007da55cb19625344183599ba671",
}
EXPECTED_PROBE = "bca9fdff1f306bacca48b4ed8d0bdf4344cf7741aecb0b6e2845e4e5f41aa9e6"
EXPECTED_FIXTURE = "a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72"


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def method_result(case: dict) -> dict:
    if "stdout_after_ready" in case:
        lines = [line for line in case["stdout_after_ready"].splitlines() if line.strip()]
        require(len(lines) == 1, "Expected exactly one completed method receipt")
        result = json.loads(lines[0])
    else:
        result = {key: case[key] for key in ("outcome", "exception", "message", "result") if key in case}
    require(result["outcome"] in ("returned", "raised"), "No completed method receipt")
    require(case["child_reaped"] is True, "Unreaped child in retained receipt")
    return result


def build() -> dict:
    paths = {label: HERE / f"{label}-boundary-results.json" for label in EXPECTED_SOURCE}
    data = {label: json.loads(path.read_text()) for label, path in paths.items()}
    require(file_hash(HERE / "boundary_probes.py") == EXPECTED_PROBE, "Probe source changed")
    for label, result in data.items():
        require(result["label"] == label, "Label mismatch")
        require(result["source_sha"] == EXPECTED_SOURCE[label], "Source admission mismatch")
        require(result["probe_sha256"] == EXPECTED_PROBE, "Recorded probe hash mismatch")
        require(result["fixture_sha256"] == EXPECTED_FIXTURE, "Recorded fixture hash mismatch")
        require(result["source_and_fixture_rechecked_after"] is True, "Missing final admission check")
        require(result["resolver"]["escaped_callable_invoked"] is False, "Unexpected callable invocation")
        require(result["resolver"]["allowed_lookup"]["result"]["callable"] is True, "Valid lookup regressed")
    old, new = data["baseline"], data["latest"]
    require(old["dependencies"] == new["dependencies"], "Reported dependency set differs")
    require(old["resolver"]["lookup"]["result"]["is_os_system"] is True, "Baseline escape identity differs")
    require(old["resolver"]["binding"]["result"]["bound_is_os_system"] is True, "Baseline bound identity differs")
    require(old["resolver"]["modified_manifest_valid"] is True, "Baseline validator result differs")
    for key in ("lookup", "binding"):
        require(new["resolver"][key].get("exception") == "ResolutionError", "Latest resolver did not reject")
    require(new["resolver"]["modified_manifest_valid"] is False, "Latest validator accepted escape")

    store_results = {}
    for label, result in data.items():
        store = result["manifest_store"]
        for key in ("valid_idempotent_control", "retained_filename_and_lineage_id", "canonical_content_changed",
                    "stored_bytes_unchanged_after_checks", "stored_mtime_unchanged_after_checks"):
            require(store[key] is True, f"Store invariant differs: {label}/{key}")
        checks = {}
        for key in ("full_uri", "short_uri", "commit_reuse"):
            outcome = store[key]
            require(outcome["outcome"] == ("returned" if label == "baseline" else "raised"), "Store outcome differs")
            if label == "latest":
                require(outcome["exception"] == "ValueError" and "content does not match" in outcome["message"],
                        "Latest store rejection has a different cause")
            checks[key] = outcome["outcome"]
        require(store["index_bytes_unchanged_after_checks"] is (label == "latest"), "Index-byte result differs")
        require(store["index_mtime_unchanged_after_checks"] is (label == "latest"), "Index-mtime result differs")
        store_results[label] = {"checks": checks, "valid_idempotent_control": True,
                                "index_unchanged": store["index_bytes_unchanged_after_checks"]}

    ffd_cases = {}
    expected_cases = {"public_nan_d", "public_nan_threshold", "public_zero_nan_threshold",
                      "private_nan_d", "private_finite_overflow"}
    for label, result in data.items():
        controls = result["fractional_difference"]["finite_recorded_controls"]
        require(len(controls) == 3 and all(c["matches_independent_short_formula"] for c in controls),
                "Finite formula control differs")
        cases = result["fractional_difference"]["cases"]
        require({case["case"] for case in cases} == expected_cases, "FFD case set differs")
        for case in cases:
            method = method_result(case)
            if label == "latest":
                require(method.get("exception") == "ValueError", "Latest FFD admission did not reject")
            elif case["case"] == "public_zero_nan_threshold":
                require(method == {"outcome": "returned", "result": 8}, "Baseline identity path differs")
            else:
                require(method.get("exception") == "MemoryError", "Baseline memory-cap outcome differs")
            require(case["controls"]["additional_virtual_bytes"] == 32 * 1024 * 1024, "Memory cap differs")
            ffd_cases.setdefault(case["case"], {})[label] = {
                "method_result": method,
                "outer_process_outcome": case["outcome"],
                "child_reaped": case["child_reaped"],
            }

    sensor_cases = {}
    for label, result in data.items():
        sensor = result["compiled_sensor"]
        require(sensor["fixture_rows"] == 8, "Recorded fixture slice differs")
        require(len(sensor["cases"]) == 8, "Sensor case count differs")
        for case in sensor["cases"]:
            require(case["model_call_row_counts"] == [8, 1], "Unexpected native Sensor call sizes")
            require(case["batch_rows"] == 8 and case["recorded_datetime_alignment_preserved"] is True,
                    "Sensor output alignment differs")
            valid = case["case"] in ("valid", "valid_missing_probability")
            expected_reason = None if valid or label == "baseline" else "sensor-error"
            require(case["single"]["reason"] == expected_reason, "Single-row reason differs")
            require(case["batch_reasons"] == [expected_reason] * 8, "Batch reasons differ")
            if not valid and label == "latest":
                for key in ("single", "last_batch"):
                    require(case[key]["prediction"] is None and case[key]["probability"] is None,
                            "Invalid Sensor output retained numeric success values")
            sensor_cases.setdefault(case["case"], {})[label] = {
                "single_reason": case["single"]["reason"],
                "batch_reason_counts": {"success" if expected_reason is None else expected_reason: 8},
                "datetime_alignment_preserved": True,
            }

    return {
        "schema": "limen-safety-boundary-comparison/v1",
        "checks_passed": True,
        "execution": "Read-only interpretation of retained JSON; no Limen imports, engine runs, or native tests.",
        "sources": EXPECTED_SOURCE,
        "files": {str(path.name): file_hash(path) for path in [*paths.values(), HERE / "boundary_probes.py", Path(__file__)]},
        "fixture": {"path": old["fixture_path"], "sha256": EXPECTED_FIXTURE, "used_rows": 8},
        "reported_dependency_versions_equal": True,
        "templates": {label: result["resolver"]["template_sha256"] for label, result in data.items()},
        "template_scope": "Each version's unmodified native rule_based.yaml passed validation first; config bytes differ between releases.",
        "resolver": {
            "baseline": "External re-export resolves, validates, and binds to the exact os.system object.",
            "latest": "Lookup and binding raise ResolutionError; validator rejects the modified manifest.",
            "positive_lookup_passed_both": True,
            "escaped_callable_invoked": False,
            "scope": "Callable identity and manifest admission only; no command executed, no Python sandbox claim.",
        },
        "manifest_store": {
            "results": store_results,
            "scope": "Existing committed body changed while filename and lineage.id remain fixed; full URI, short URI, and idempotent reuse. Fork inspected separately, not exercised here.",
        },
        "fractional_difference": {
            "cases": ffd_cases,
            "finite_formula_controls_passed_both": [0.0, 1.0, 0.5],
            "finite_formula_control_threshold": 0.2,
            "interpretation": "The child flushed a complete method receipt before outer termination in every case. Baseline hit the external address-space cap in four cases and accepted an invalid threshold on its identity path. Latest raised its explicit ValueError in all five cases.",
            "harness_limitation": "The 0.35-second communicate deadline includes interpreter shutdown. Every raw case has outer outcome external_deadline and was killed/reaped after printing its method result. These outer labels and elapsed values are not method-latency measurements and do not demonstrate a latest-method hang. Shutdown was not separately timed.",
            "scope": "Specific nonfinite admission and recurrence-overflow guards; no universal bound on legitimate finite workloads, no performance comparison.",
        },
        "compiled_sensor": {
            "cases": sensor_cases,
            "invalid_cases": 6,
            "invalid_batch_rows_per_case": 8,
            "positive_cases": 2,
            "scope": "Public Sensor.predict and Sensor.predict_all with native MLManifest preparation and explicit invalid-output canaries. No model fit, learned forecasts, or economic outcome claim. Raw results retain all single outputs, all batch reasons, and the last full batch output.",
        },
        "execution_notes": [
            "Initial default-sandbox invocations failed during child setup because /proc/self/statm was unavailable, before the FFD call/ready handshake and before any result file was committed. This is a harness environment limitation, not a Limen source failure.",
            "Retained native-runtime invocations completed with exit 0; exact source and fixture admission were rechecked afterward.",
            "Root-owned full native-suite results are separate evidence and are not inferred from these focused probes.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(HERE):
        parser.error("Output must be inside this safety update directory")
    if output.exists():
        raise FileExistsError(output)
    receipt = build()
    with output.open("x") as stream:
        json.dump(receipt, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"saved": str(output), "checks_passed": True}))


if __name__ == "__main__":
    main()
