#!/usr/bin/env python3
"""Read-only assessment and recorded-campaign validation using only the stdlib.

This checks structure, identities, references and recorded admission arithmetic.
It does not interpret source claims, rerun engines, or recompute array parity.
Without --sources, local source existence and line bounds are not checked.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path, PurePosixPath
import re
import statistics
import sys


ROOT = Path(__file__).resolve().parents[1]
ASSESSMENTS = {"performance": ("P", 12), "academic": ("A", 15), "safety": ("S", 15)}
STATUSES = {"Enforced", "Optional", "Partial", "Fails", "Unknown", "N/A"}
EVIDENCE = {"Inspected", "Tested", "Reproduced", "Measured"}
APPLICABILITY = {"native", "adapter_required", "out_of_scope", "unknown"}
CAPABILITIES = {"implemented", "not_implemented", "not_located", "unknown"}
WORKER_STATUSES = {
    "verified", "unsupported_contract", "adapter_unavailable", "unavailable",
    "error", "parity_failed", "environment_missing", "worker_failed", "timed_out",
}
OPTIONAL_LEDGER_FIELDS = {"cash", "units", "fill_quantities", "fill_fees"}
NATIVE_THREAD_ENVIRONMENT_V1 = {
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "NUMBA_NUM_THREADS",
    "RAYON_NUM_THREADS", "BLIS_NUM_THREADS", "POLARS_MAX_THREADS",
}
IDENTIFIER = re.compile(r"[a-z][a-z0-9_]*\Z")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
SHA1 = re.compile(r"[0-9a-f]{40}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
DOC_SUFFIXES = {".md", ".markdown", ".rst", ".rstx", ".adoc", ".asciidoc", ".pdf", ".doc", ".docx", ".html", ".htm"}
SUMMARY_TIMES = (
    "first_full_common_ms_median", "warm_full_common_ms_median",
    "warm_engine_ms_median", "warm_extraction_common_ms_median",
    "warm_full_common_cpu_ms_median", "peak_rss_bytes_median",
    "launch_to_ready_ms_median", "launch_to_first_valid_ms_median",
)
SUMMARY_EXTENSIONS = (
    "warm_process_median_ms_min", "warm_process_median_ms_max",
    "warm_full_common_call_ms_min", "warm_full_common_call_ms_max",
    "first_full_common_ms_min", "first_full_common_ms_max",
    "warm_evaluation_bars_per_second",
)


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def mapping(value, name):
    require(isinstance(value, dict), f"{name} must be an object")
    return value


def sequence(value, name, *, nonempty=False):
    require(isinstance(value, list), f"{name} must be an array")
    require(not nonempty or bool(value), f"{name} must not be empty")
    return value


def string(value, name):
    require(isinstance(value, str) and bool(value.strip()), f"{name} must be a nonempty string")
    return value


def integer(value, name, minimum=0):
    require(type(value) is int and value >= minimum, f"{name} must be an integer >= {minimum}")
    return value


def number(value, name, *, positive=False):
    require(type(value) in (int, float), f"{name} must be a finite number")
    try:
        finite = math.isfinite(value)
    except OverflowError:
        finite = False
    require(finite and (value > 0 if positive else value >= 0),
            f"{name} must be finite and {'positive' if positive else 'nonnegative'}")
    return value


def boolean(value, name):
    require(type(value) is bool, f"{name} must be a boolean")
    return value


def enum_value(value, choices, name):
    require(isinstance(value, str) and value in choices, f"invalid {name}: {value!r}")
    return value


def digest(value, name, pattern=SHA256):
    require(isinstance(value, str) and pattern.fullmatch(value) is not None, f"{name} has an invalid digest")
    return value


def unique_strings(value, name, *, nonempty=False):
    values = sequence(value, name, nonempty=nonempty)
    for item in values:
        string(item, name)
    require(len(set(values)) == len(values), f"{name} contains duplicates")
    return values


def close(actual, expected, name):
    number(actual, name)
    require(math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-9),
            f"{name} differs from recorded-sample arithmetic: {actual!r} != {expected!r}")


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON object key {key!r}")
        result[key] = value
    return result


def reject_constant(value):
    raise Invalid(f"nonfinite JSON constant {value}")


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys,
                          parse_constant=reject_constant)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise Invalid(f"cannot read {path}: {error}") from error


class AssessmentValidator:
    def __init__(self, root, sources=None):
        self.root = root
        self.sources = sources
        self.errors = []
        self.catalog = {}
        self.auxiliary = {}
        self.criteria = {}
        self.line_counts = {}
        self.reference_count = 0
        self.row_count = 0

    def attempt(self, context, function, *args):
        try:
            return function(*args)
        except Invalid as error:
            self.errors.append(f"{context}: {error}")
            return None

    def read_catalog(self, relative):
        values = sequence(read_json(self.root / relative), relative,
                          nonempty=relative == "catalog/candidates.json")
        result = {}
        for index, value in enumerate(values):
            item = mapping(value, f"{relative}[{index}]")
            identifier = string(item.get("id"), "catalog id")
            require(IDENTIFIER.fullmatch(identifier) is not None, f"invalid catalog id {identifier!r}")
            require(identifier not in result, f"duplicate catalog id {identifier}")
            repository = string(item.get("repository"), "repository")
            require(REPOSITORY.fullmatch(repository) is not None, f"invalid repository {repository!r}")
            digest(item.get("commit"), "commit", SHA1)
            require(item.get("url") == f"https://github.com/{repository}", f"noncanonical catalog URL for {identifier}")
            result[identifier] = item
        return result

    def read_criteria(self):
        values = sequence(read_json(self.root / "protocol/criteria.json"), "criteria", nonempty=True)
        expected = {f"{prefix}{i:02d}" for prefix, count in ASSESSMENTS.values() for i in range(1, count + 1)}
        result = {}
        for value in values:
            item = mapping(value, "criterion")
            identifier = string(item.get("id"), "criterion id")
            require(identifier not in result, f"duplicate criterion {identifier}")
            for field in ("aspect", "criterion", "scope", "protocol"):
                string(item.get(field), f"{identifier}.{field}")
            result[identifier] = item
        require(set(result) == expected, f"canonical criteria differ: missing={sorted(expected - set(result))}, extra={sorted(set(result) - expected)}")
        return result

    def validate_ref(self, cid, value):
        ref = mapping(value, "source reference")
        path = string(ref.get("path"), "reference path")
        parts = path.split("/")
        require(not path.startswith("/") and not any(char in path for char in "\\?#")
                and all(ord(char) >= 32 for char in path)
                and all(p not in ("", ".", "..") for p in parts),
                f"reference must use a contained relative POSIX path: {path!r}")
        lowered = [part.lower() for part in parts]
        name = lowered[-1]
        require(not any(part in {"doc", "docs", "documentation"} for part in lowered[:-1])
                and not name.startswith("readme") and PurePosixPath(path).suffix.lower() not in DOC_SUFFIXES,
                f"documentation/README is not an admissible behavioral source: {path}")
        start = integer(ref.get("start_line"), "start_line", 1)
        end = integer(ref.get("end_line"), "end_line", start)
        url = string(ref.get("url"), "source URL")
        candidates = {cid: self.catalog[cid], **self.auxiliary}
        matched = [source_id for source_id, source in candidates.items()
                   if url == f"https://github.com/{source['repository']}/blob/{source['commit']}/{path}#L{start}-L{end}"]
        require(len(matched) == 1, f"URL must exactly identify this candidate or an admitted auxiliary SHA/path/anchor: {url}")
        self.reference_count += 1
        if self.sources is not None:
            source_id = matched[0]
            key = (source_id, path)
            if key not in self.line_counts:
                base = (self.sources / source_id).resolve()
                require(base.is_dir(), f"supplied source checkout is missing: {base}")
                local = (base / path).resolve()
                require(local.is_relative_to(base), f"source file escapes its checkout: {local}")
                require(local.is_file(), f"referenced source file is missing: {local}")
                try:
                    self.line_counts[key] = len(local.read_text(encoding="utf-8").splitlines())
                except (OSError, UnicodeError) as error:
                    raise Invalid(f"cannot read referenced source {local}: {error}") from error
            require(end <= self.line_counts[key], f"{source_id}/{path}:{start}-{end} exceeds {self.line_counts[key]} source lines")

    def validate_row(self, value, prefix):
        row = mapping(value, "assessment row")
        cid = string(row.get("candidate_id"), "candidate_id")
        criterion = string(row.get("criterion_id"), "criterion_id")
        require(cid in self.catalog, f"candidate is not in catalog: {cid}")
        require(criterion in self.criteria and criterion.startswith(prefix), f"criterion is unknown or in the wrong assessment file: {criterion}")
        enum_value(row.get("status"), STATUSES, "status")
        enum_value(row.get("applicability"), APPLICABILITY, "applicability")
        enum_value(row.get("capability"), CAPABILITIES, "capability")
        evidence = unique_strings(row.get("evidence_type"), "evidence_type", nonempty=True)
        require(set(evidence) <= EVIDENCE, f"invalid evidence types: {evidence}")
        for field in ("scope", "finding", "limitation"):
            string(row.get(field), field)
        if "criterion" in row:
            require(row["criterion"] == self.criteria[criterion]["criterion"], "criterion label differs from canonical definition")
        for ref in sequence(row.get("source_refs"), "source_refs", nonempty=True):
            self.validate_ref(cid, ref)
        return cid, criterion

    def validate(self):
        self.catalog = self.attempt("catalog", self.read_catalog, "catalog/candidates.json") or {}
        self.auxiliary = self.attempt("auxiliary catalog", self.read_catalog, "catalog/auxiliary_sources.json") or {}
        self.criteria = self.attempt("criteria", self.read_criteria) or {}
        if set(self.catalog) & set(self.auxiliary):
            self.errors.append("candidate and auxiliary source IDs must be disjoint")
        if not self.catalog or not self.criteria:
            return
        seen = Counter()
        for filename, (prefix, _) in ASSESSMENTS.items():
            relative = f"assessment/{filename}.json"
            values = self.attempt(relative, read_json, self.root / relative)
            if not isinstance(values, list):
                if values is not None:
                    self.errors.append(f"{relative}: expected an array")
                continue
            self.row_count += len(values)
            for index, value in enumerate(values):
                if isinstance(value, dict) and isinstance(value.get("candidate_id"), str) and isinstance(value.get("criterion_id"), str):
                    seen[(value["candidate_id"], value["criterion_id"])] += 1
                self.attempt(f"{relative}[{index}]", self.validate_row, value, prefix)
        expected = {(cid, criterion) for cid in self.catalog for criterion in self.criteria}
        missing, extra = expected - set(seen), set(seen) - expected
        if missing:
            self.errors.append(f"missing candidate/criterion rows: {sorted(missing)}")
        if extra:
            self.errors.append(f"unrecognized candidate/criterion rows: {sorted(extra)}")
        duplicates = {f"{cid}/{criterion}": count for (cid, criterion), count in seen.items() if count != 1}
        if duplicates:
            self.errors.append(f"duplicate candidate/criterion rows: {duplicates}")
        if self.row_count != len(expected):
            self.errors.append(f"expected {len(expected)} assessment rows, found {self.row_count}")


def validate_parity(value, evaluation_rows, expected_fills=None):
    parity = mapping(value, "parity")
    require(integer(parity.get("equity_samples_checked"), "equity_samples_checked", 1) == evaluation_rows,
            "parity does not cover the declared evaluation observations")
    fills = integer(parity.get("fills_checked"), "fills_checked")
    if expected_fills is not None:
        require(fills == expected_fills, "fill count differs from the same-contract preflight")
    number(parity.get("max_abs_equity_error"), "max_abs_equity_error")
    number(parity.get("max_relative_equity_error"), "max_relative_equity_error")
    observed = set(unique_strings(parity.get("optional_observed_fields_checked"), "observed ledger fields"))
    unobserved = set(unique_strings(parity.get("optional_unobserved_fields"), "unobserved ledger fields"))
    require(not observed & unobserved and observed | unobserved == OPTIONAL_LEDGER_FIELDS,
            "optional ledger observation accounting is incomplete or overlapping")
    if "actual_result_arrays_sha256" in parity:
        digest(parity["actual_result_arrays_sha256"], "actual_result_arrays_sha256")
    return fills


def validate_native_thread_policy(report, required=False):
    protocol = mapping(report.get("protocol", {}), "campaign protocol")
    policy = protocol.get("native_thread_observation_policy")
    controls = protocol.get("native_thread_environment")
    if policy is None and controls is None:
        require(not required, "a declared native-thread observation policy is required")
        return None
    require(policy == "loaded-pools-v1", "unsupported native-thread observation policy")
    limit = integer(protocol.get("native_threads"), "native_threads", 1)
    controls = mapping(controls, "declared native-thread environment")
    require(NATIVE_THREAD_ENVIRONMENT_V1 <= set(controls),
            "declared loaded-pools-v1 controls omit a required native-thread environment variable")
    for name, value in controls.items():
        string(name, "native-thread environment name")
        require(value == str(limit), f"declared native-thread environment {name} differs from native_threads")
    return {"limit": limit, "environment": controls}


def validate_native_thread_runtime(worker, policy):
    runtime = mapping(worker.get("runtime"), "worker runtime")
    environment = mapping(runtime.get("thread_environment"), "observed native-thread environment")
    for name, value in policy["environment"].items():
        require(environment.get(name) == value, f"worker native-thread environment differs for {name}")
    pools = sequence(runtime.get("threadpools"), "observed native threadpools")
    for pool in pools:
        mapping(pool, "observed native threadpool")
        count = integer(pool.get("num_threads"), "observed threadpool num_threads", 1)
        require(count <= policy["limit"], "observed native threadpool exceeds the declared thread limit")
    observations = mapping(runtime.get("native_thread_observations"), "native thread observations")
    polars = mapping(observations.get("polars"), "Polars thread observation")
    loaded = boolean(polars.get("loaded"), "Polars loaded disposition")
    if loaded:
        count = integer(polars.get("pool_size"), "observed Polars pool_size", 1)
        require(count <= policy["limit"], "observed Polars pool exceeds the declared thread limit")
        string(polars.get("version"), "observed Polars version")
    else:
        require(polars.get("pool_size") is None and polars.get("version") is None,
                "unloaded Polars disposition has contradictory pool/version observations")


def validate_timing_samples(samples, warm_repeats, evaluation_rows, fills, thread_policy=None):
    samples = sequence(samples, "timing samples")
    require(len(samples) == warm_repeats + 1, f"expected first call plus {warm_repeats} warm calls, found {len(samples)} samples")
    for index, value in enumerate(samples):
        sample = mapping(value, "timing sample")
        expected_phase = "first" if index == 0 else f"warm-{index}"
        require(sample.get("phase") == expected_phase, f"missing, duplicate, or unordered timing phase; expected {expected_phase}")
        require(sample.get("admitted") is True, f"{expected_phase} has no successful admission")
        if thread_policy is not None:
            require(sample.get("native_thread_limits_verified") is True,
                    f"{expected_phase} lacks a successful post-call native-thread admission")
        for field in ("engine_ms", "extraction_common_ms", "engine_cpu_ms", "full_common_cpu_ms"):
            number(sample.get(field), field)
        number(sample.get("full_common_ms"), "full_common_ms", positive=True)
        close(sample["full_common_ms"], sample["engine_ms"] + sample["extraction_common_ms"], "full_common_ms")
        validate_parity(sample.get("parity"), evaluation_rows, fills)
    return samples


def validate_worker(item, engine, mode, report, catalog, scenario, expected_rank, expected_fills=None, thread_policy=None):
    item = mapping(item, "worker/process record")
    worker = mapping(item.get("worker"), "worker")
    process = mapping(item.get("process"), "process")
    require(worker.get("status") == "verified", "an admitted worker must have verified status")
    require(type(process.get("returncode")) is int and process["returncode"] == 0, "verified worker lacks a successful process exit")
    require(process.get("timed_out") is False, "verified worker timed out or lacks a timeout disposition")
    require(worker.get("engine") == engine and worker.get("mode") == mode, "worker engine/mode differs from the case")
    require(worker.get("contract") == report["contract"], "worker contract differs from the campaign contract")
    require(worker.get("prepared_arrays_sha256") == scenario["prepared_arrays_sha256"], "worker input digest differs from the prepared scenario")
    provenance = mapping(worker.get("provenance"), "worker provenance")
    require(provenance.get("source_commit_verified") == catalog[engine]["commit"], "worker source revision differs from the catalog")
    require(provenance.get("tracked_source_clean") is True, "worker did not record clean tracked source")
    if thread_policy is not None:
        validate_native_thread_runtime(worker, thread_policy)
    require(boolean(worker.get("rank_against_full_engine"), "worker rank flag") == expected_rank, "worker/case ranking flags disagree")
    settings = mapping(worker.get("settings"), "worker settings")
    require(boolean(settings.get("rank_against_full_engine", True), "settings rank flag") == expected_rank, "settings/worker ranking flags disagree")
    if settings.get("benchmark_layer") in ("native-components", "internal-core", "diagnostic"):
        require(not expected_rank, "component/core diagnostics must not qualify for full-engine ratios")
    string(worker.get("engine_scope"), "engine_scope")
    mapping(worker.get("output_observation"), "output_observation")
    require(worker.get("timings_admitted") is not False, "verified worker has timings_admitted=false")
    fills = validate_parity(worker.get("parity"), report["input"]["evaluation_rows"], expected_fills)
    summary = mapping(worker.get("summary"), "worker summary")
    entries = integer(summary.get("entries"), "entries")
    exits = integer(summary.get("exits"), "exits")
    require(entries + exits == fills, "worker summary entry/exit counts differ from its fill parity")
    if mode == "preflight":
        require(worker.get("timing_samples") == [], "preflight must not contribute timing samples")
        require(worker.get("core_diagnostic_samples") == [], "preflight must not contribute core timing samples")
    else:
        validate_timing_samples(worker.get("timing_samples"), report["arguments"]["warm_repeats"], report["input"]["evaluation_rows"], fills, thread_policy)
        number(worker.get("peak_rss_bytes_after_full_calls"), "peak_rss_bytes_after_full_calls", positive=True)
        wall = number(process.get("process_wall_ms"), "process_wall_ms", positive=True)
        ready = number(process.get("launch_to_ready_ms"), "launch_to_ready_ms")
        first = number(process.get("launch_to_first_valid_ms"), "launch_to_first_valid_ms")
        require(ready <= first <= wall, "parent process event times are inconsistent")
        core = sequence(worker.get("core_diagnostic_samples"), "core_diagnostic_samples")
        if core or "core_diagnostic_scope" in worker:
            require(report["arguments"].get("diagnostic_core") is True, "undeclared core diagnostics were timed")
            string(worker.get("core_diagnostic_scope"), "core_diagnostic_scope")
            validate_timing_samples(core, report["arguments"]["warm_repeats"], report["input"]["evaluation_rows"], fills, thread_policy)
            for sample in core:
                require(sample.get("rank_against_full_engine") is not True
                        and all(value is None for key, value in sample.items() if key.startswith("relative_to_limen")),
                        "internal-core samples must not carry full-engine ranking or ratios")
    return worker, fills


def validate_aggregate(row, workers, measurements, complete, fills, evaluation_rows):
    list_fields = ("warm_full_common_ms_samples", "first_full_common_ms_samples", "warm_process_medians_ms")
    require(all(field in row for field in SUMMARY_TIMES + list_fields + ("relative_to_limen_warm_full_common",)),
            "campaign summary omits a required aggregation field")
    require(integer(row.get("independent_processes"), "independent_processes") == len(workers), "summary process count differs from admitted workers")
    if fills is not None:
        require(row.get("equity_samples") == evaluation_rows and row.get("fills_checked") == fills,
                "summary parity counts differ from preflight")
    if not complete:
        for field in SUMMARY_TIMES + SUMMARY_EXTENSIONS:
            require(row.get(field) is None, f"incomplete/preflight case has a speed or resource aggregate: {field}")
        for field in list_fields:
            require(row.get(field) == [], f"incomplete/preflight case has admitted aggregate samples: {field}")
        require(row.get("relative_to_limen_warm_full_common") is None, "incomplete/preflight case has a speed ratio")
        return None
    first = [worker["timing_samples"][0]["full_common_ms"] for worker in workers]
    warm = [[sample for sample in worker["timing_samples"][1:]] for worker in workers]
    blocks = [[sample["full_common_ms"] for sample in block] for block in warm]
    medians = [statistics.median(block) for block in blocks]
    expected = {
        "first_full_common_ms_median": statistics.median(first),
        "warm_full_common_ms_median": statistics.median(medians),
        "peak_rss_bytes_median": statistics.median(w["peak_rss_bytes_after_full_calls"] for w in workers),
        "first_full_common_ms_min": min(first), "first_full_common_ms_max": max(first),
        "warm_process_median_ms_min": min(medians), "warm_process_median_ms_max": max(medians),
        "warm_full_common_call_ms_min": min(min(block) for block in blocks),
        "warm_full_common_call_ms_max": max(max(block) for block in blocks),
        "warm_evaluation_bars_per_second": evaluation_rows * 1000 / statistics.median(medians),
    }
    for field in ("engine_ms", "extraction_common_ms", "full_common_cpu_ms"):
        expected[f"warm_{field}_median"] = statistics.median(statistics.median(sample[field] for sample in block) for block in warm)
    for field in ("launch_to_ready_ms", "launch_to_first_valid_ms"):
        expected[f"{field}_median"] = statistics.median(item["process"][field] for item in measurements)
    for field in SUMMARY_TIMES:
        close(row.get(field), expected[field], field)
    for field in SUMMARY_EXTENSIONS:
        if field in row:
            close(row[field], expected[field], field)
    for field, expected_values in zip(list_fields, (blocks, first, medians)):
        require(row.get(field) == expected_values, f"{field} differs from the complete recorded samples")
    return expected["warm_full_common_ms_median"]


def validate_campaign(path, catalog, require_native_thread_policy=False):
    path = path / "report.json" if path.is_dir() else path
    report = mapping(read_json(path), "campaign report")
    require(report.get("schema_version") == 1, "unsupported campaign schema_version")
    require(report.get("status") == "completed", "campaign is not a completed report")
    command = enum_value(report.get("command"), {"verify", "run"}, "campaign command")
    args = mapping(report.get("arguments"), "campaign arguments")
    require(args.get("command") == command, "campaign/argument commands disagree")
    engines = unique_strings(args.get("engines"), "engines", nonempty=True)
    require(set(engines) <= set(catalog), "campaign contains a noncatalog engine")
    strategies = unique_strings(args.get("strategies"), "strategies", nonempty=True)
    processes = integer(args.get("processes"), "processes", 1)
    integer(args.get("warm_repeats"), "warm_repeats", 1)
    boolean(args.get("diagnostic_core"), "diagnostic_core")
    thread_policy = validate_native_thread_policy(report, require_native_thread_policy)
    mapping(report.get("contract"), "campaign contract")
    source = mapping(report.get("input"), "campaign input")
    evaluation_rows = integer(source.get("evaluation_rows"), "evaluation_rows", 1)
    require(digest(source.get("input_sha256"), "input_sha256") == digest(args.get("expected_sha256"), "expected_sha256"), "input digest differs from the declared expected digest")
    scenarios = mapping(report.get("scenarios"), "scenarios")
    require(set(scenarios) == set(strategies), "scenario identities differ from recorded strategies")
    for strategy, scenario in scenarios.items():
        mapping(scenario, "scenario")
        require(scenario.get("strategy") == strategy, "scenario strategy differs from its key")
        for field in ("prepared_arrays_sha256", "signal_sha256", "prepared_file_sha256"):
            digest(scenario.get(field), field)
    cases = sequence(report.get("cases"), "cases", nonempty=True)
    summaries = sequence(report.get("summary"), "summary", nonempty=True)
    expected_pairs = {(engine, strategy) for engine in engines for strategy in strategies}
    summary_by_pair = {}
    for summary in summaries:
        mapping(summary, "summary row")
        pair = (string(summary.get("engine"), "summary engine"), string(summary.get("strategy"), "summary strategy"))
        require(pair not in summary_by_pair, f"duplicate campaign summary {pair}")
        summary_by_pair[pair] = summary
    require(set(summary_by_pair) == expected_pairs, "summary does not cover exactly the recorded engine/strategy grid")
    seen, medians, fills_by_strategy = set(), {}, {}
    verified_processes = 0
    thread_workers_checked = 0
    thread_samples_checked = 0
    for case in cases:
        mapping(case, "case")
        engine, strategy = string(case.get("engine"), "case engine"), string(case.get("strategy"), "case strategy")
        pair = (engine, strategy)
        require(pair in expected_pairs and pair not in seen, f"unexpected or duplicate case {pair}")
        seen.add(pair)
        row = summary_by_pair[pair]
        requested = integer(case.get("requested_processes"), "requested_processes")
        require(requested == (processes if command == "run" else 0), f"{pair}: requested process count differs from command arguments")
        rank = boolean(case.get("rank_against_full_engine"), "case rank flag")
        require(boolean(row.get("rank_against_full_engine"), "summary rank flag") == rank, f"{pair}: summary/case ranking flags disagree")
        preflight = mapping(case.get("preflight"), "preflight")
        pre_worker = mapping(preflight.get("worker"), "preflight worker")
        status = enum_value(case.get("preflight_status"), WORKER_STATUSES, "preflight_status")
        require(pre_worker.get("status") == status, f"{pair}: inconsistent preflight disposition")
        measurements = sequence(case.get("measurements"), "measurements")
        fills = None
        workers = []
        if status == "verified":
            directories = {string(preflight.get("directory"), "preflight directory")}
            _, fills = validate_worker(preflight, engine, "preflight", report, catalog, scenarios[strategy], rank, fills_by_strategy.get(strategy), thread_policy)
            if thread_policy is not None:
                thread_workers_checked += 1
            fills_by_strategy[strategy] = fills
            require(len(measurements) == requested, f"{pair}: missing or extra recorded process attempts ({len(measurements)} != {requested})")
            for item in measurements:
                mapping(item, "measurement")
                directory = string(item.get("directory"), "measurement directory")
                require(directory not in directories, f"{pair}: repeated process evidence directory {directory}")
                directories.add(directory)
                worker = mapping(item.get("worker"), "measurement worker")
                process = mapping(item.get("process"), "measurement process")
                enum_value(worker.get("status"), WORKER_STATUSES, "terminal worker status")
                if worker.get("status") == "verified":
                    checked, _ = validate_worker(item, engine, "measure", report, catalog, scenarios[strategy], rank, fills, thread_policy)
                    workers.append(checked)
                    if thread_policy is not None:
                        thread_workers_checked += 1
                        thread_samples_checked += len(checked["timing_samples"]) + len(checked["core_diagnostic_samples"])
                else:
                    require(worker.get("timings_admitted") is not True, "failed worker claims admitted timings")
                    require(process.get("returncode") != 0 or worker.get("status") in {"environment_missing", "timed_out", "worker_failed"},
                            "failed worker has an inconsistent successful process exit")
        else:
            require(not measurements, f"{pair}: measurements exist despite rejected preflight")
        complete = bool(workers) and len(workers) == requested and status == "verified"
        expected_status = "verified" if complete else (status if not measurements else "incomplete_measurements")
        require(row.get("status") == expected_status, f"{pair}: summary misstates case completion")
        median = validate_aggregate(row, workers, measurements, complete, fills, evaluation_rows)
        medians[pair] = (median, complete, rank)
        verified_processes += len(workers)
    require(seen == expected_pairs, f"campaign cases are missing: {sorted(expected_pairs - seen)}")
    for pair, (median, complete, rank) in medians.items():
        baseline = medians.get(("limen", pair[1]))
        ratio = summary_by_pair[pair].get("relative_to_limen_warm_full_common")
        eligible = complete and rank and baseline is not None and baseline[1] and baseline[2]
        if eligible:
            close(ratio, median / baseline[0], f"{pair} relative_to_limen_warm_full_common")
        else:
            require(ratio is None, f"{pair}: unmeasured/component/incomplete case must not receive a full-engine ratio")
    thread_scope = (f"Declared environment values and observed loaded native/Polars pool limits checked for {thread_workers_checked} verified workers; {thread_samples_checked} recorded post-call admission flags checked. No physical thread/CPU isolation verification."
                    if thread_policy is not None else
                    "No native-thread observation policy declared; this validation does not establish observed native-thread control.")
    return {"path": str(path), "command": command, "cases": len(cases), "verified_timed_processes": verified_processes,
            "native_thread_observation_policy": report.get("protocol", {}).get("native_thread_observation_policy"),
            "native_thread_observed_workers_checked": thread_workers_checked,
            "native_thread_timed_samples_checked": thread_samples_checked,
            "native_thread_control_scope": thread_scope,
            "scope": "Recorded settings, completeness, parity admission metadata, aggregate arithmetic and ranking separation; no engine execution or array-parity recomputation."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Benchmark repository root (default: this script's repository)")
    parser.add_argument("--sources", type=Path, help="Local source parent containing candidate/auxiliary ID directories; missing referenced files fail")
    parser.add_argument("--campaign", type=Path, action="append", default=[], help="Completed report.json or its directory; may be repeated")
    parser.add_argument("--require-native-thread-policy", action="store_true", help="Require every supplied campaign to declare and satisfy the observed native-thread metadata policy")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable validation results to stdout")
    args = parser.parse_args(argv)
    if args.require_native_thread_policy and not args.campaign:
        parser.error("--require-native-thread-policy requires at least one --campaign")
    validator = AssessmentValidator(args.root.resolve(), args.sources.resolve() if args.sources is not None else None)
    validator.validate()
    campaigns = []
    if validator.catalog:
        for path in args.campaign:
            outcome = validator.attempt(f"campaign {path}", validate_campaign, path.resolve(), validator.catalog, args.require_native_thread_policy)
            if outcome is not None:
                campaigns.append(outcome)
    scope = ("Assessment structure and pinned source-link syntax only; local source files and line bounds were not checked."
             if args.sources is None else
             "Assessment structure, pinned source-link syntax, and referenced local file containment/existence/line bounds.")
    result = {"ok": not validator.errors, "assessment_rows": validator.row_count,
              "expected_rows": len(validator.catalog) * len(validator.criteria),
              "candidates": len(validator.catalog), "criteria": len(validator.criteria),
              "source_references": validator.reference_count, "local_source_files_checked": len(validator.line_counts),
              "scope": scope, "campaigns": campaigns,
              "limitations": "This read-only gate does not verify local git/build byte identity, interpret whether source lines support a claim, exclude comments within code, replay numerical/statistical results, or enforce CPU/thread-pool isolation.",
              "errors": validator.errors}
    if args.json:
        print(json.dumps(result, indent=2, allow_nan=False))
    else:
        print(f"{'PASS' if result['ok'] else 'FAIL'}: {result['assessment_rows']}/{result['expected_rows']} assessment rows; "
              f"{result['candidates']} candidates × {result['criteria']} criteria; {result['source_references']} source references.")
        print(scope)
        print(result["limitations"])
        for campaign in campaigns:
            print(f"Campaign checked: {campaign['path']} ({campaign['cases']} cases, {campaign['verified_timed_processes']} admitted timed processes).")
        for error in validator.errors:
            print(f"ERROR: {error}", file=sys.stderr)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
