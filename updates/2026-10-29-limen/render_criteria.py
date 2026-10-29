"""Render the existing qualitative statuses; never derive scores from symbols."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SYMBOL = {"Enforced": "●", "Partial": "◐", "Optional": "◐ (opt-in)", "Fails": "○", "Unknown": "—"}
NOTES = {
    "P01": "Canonical choice validation added; construction scaling unmeasured.",
    "P02": "Candidate identity strengthened; no new consumption-throughput measurement.",
    "P03": "First call and launch-to-admitted-output measured separately.",
    "P04": "One native 48-round pair per revision; general throughput unestablished.",
    "P05": "Both revisions reduce target/scaler fits 24→1; scientific digests agree.",
    "P06": "Feature implementation reviewed; scaling not timed.",
    "P07": "Five processes per revision/strategy; identical outputs, overlapping ranges.",
    "P08": "Event/label code reviewed; no new throughput experiment.",
    "P09": "Process peak RSS measured; allocation-only and scaling costs unmeasured.",
    "P10": "Parallel implementation reviewed; no parallel-speedup experiment.",
    "P11": "Cache identities/reuse reviewed; key/hit/eviction overhead unmeasured.",
    "P12": "Recovery integrity strengthened; recording/restart cost unmeasured.",
    "A01": "Quantile historical leakage repaired; retrospective output still exists.",
    "A02": "Split/preparation admission strengthened; custom feature causality remains a contract.",
    "A03": "Formed/linkage availability strengthened; arbitrary horizons not inferred.",
    "A04": "Chronological contracts remain scoped; no universal purge/embargo inference.",
    "A05": "Fold-local automatic FFD now joins scaler/PCA refitting and row checks.",
    "A06": "Calibration/decision receipts strengthened; shared validation selection remains.",
    "A07": "Binary confusion admission improved; fold averages remain unpooled.",
    "A08": "Independent prefix oracle and native assertions added; no universal proof.",
    "A09": "More model implementations; no common convergence-quality gate.",
    "A10": "Typed identity and local failure recording; outside search history unknown.",
    "A11": "PBO accepts supported even block counts; retained-family diagnostic only.",
    "A12": "Fold/source evidence strengthened; complete economic comparability remains scoped.",
    "A13": "Protected research broader; final admission remains deliberately narrow.",
    "A14": "No independent external predictive/live-execution validity study.",
    "A15": "Observed-cost scenarios and repeatable perturbation/surrogate diagnostics added.",
    "S01": "External callable re-export blocked; installed Python is still trusted.",
    "S02": "More numeric/parser checks; direct snapshot cost admission gap remains.",
    "S03": "Five FFD invalid/overflow cases reject; general resource limits unestablished.",
    "S04": "Optional recorded-Parquet SHA check added; broader ingestion limits remain.",
    "S05": "Body-verified read/reuse repaired; index rebuilding remains narrower.",
    "S06": "Recorded-round integrity retained and extended to exits/checkpoints.",
    "S07": "Typed/protected resume strengthened; no whole-output transaction/fsync.",
    "S08": "Bounded dispatch/failure propagation retained; protected worker authority added.",
    "S09": "Six invalid Sensor canaries become unavailable; full signal semantics remain scoped.",
    "S10": "Chronology/source admission extended to declared dynamic barriers.",
    "S11": "Supported event affordability/exposure constraints retained.",
    "S12": "Observed-cost and exit controls added; live fill fidelity unestablished.",
    "S13": "Protected composition/resume broader; final holdout still restricted.",
    "S14": "CI evidence/supply-chain controls strengthened; runtime gate currently fails.",
    "S15": "Independent repaired-boundary probes and full native assertions executed.",
}


def clean(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def main():
    perf = json.loads((ROOT / "performance/performance_update.json").read_text())["rows"]
    academic = json.loads((ROOT / "academic/academic_delta.json").read_text())["criteria"]
    safety = json.loads((ROOT / "safety/safety-delta.json").read_text())["criteria"]
    rows = perf + academic + safety
    assert len(rows) == 42 and {r["criterion_id"] for r in rows} == set(NOTES)
    lines = [
        "# All 42 criteria — baseline and current Limen", "",
        "Baseline `29837e6` → current `25e4786`. Symbols summarize the original scoped status, not a numerical rating. **●** Enforced in the declared native boundary; **◐** Partial; **○** a demonstrated failure; **—** Unknown. Unknown is never treated as absence. Optional controls are explicitly labelled. An unchanged broad status can contain substantial repaired behavior.", "",
        "Performance is reported as measurements in [PERFORMANCE_RESULTS.md](performance/PERFORMANCE_RESULTS.md). Its status words below describe the coverage of an assessment, not engine speed. The canonical JSON rows retain code references, test membership, scope and limitations. Whole-module test membership is execution evidence, not assertion-level proof.", "",
    ]
    groups = [
        ("Computation", perf, "previous_status", "current_status", "performance/performance_update.json", False),
        ("Academic robustness", academic, "baseline_status", "latest_status", "academic/academic_delta.json", True),
        ("Safety", safety, "status_before", "status_after", "safety/safety-delta.json", True),
    ]
    changes = []
    for title, group, old_key, new_key, source, symbols in groups:
        lines += [f"## {title}", "", f"[Canonical records and implementation evidence]({source}).", "", "| ID | Criterion | Baseline | Current | What changed / remaining scope |", "|---|---|:---:|:---:|---|"]
        for row in group:
            cid = row["criterion_id"]
            old, new = row[old_key], row[new_key]
            if old != new:
                changes.append(f"{cid}: {old} → {new}")
            old_display = SYMBOL[old] if symbols else old
            new_display = SYMBOL[new] if symbols else new
            lines.append("| " + " | ".join(map(clean, (cid, row["criterion"], old_display, new_display, NOTES[cid]))) + " |")
        lines += [""]
    lines += ["## Status changes", "", "; ".join(changes) + ". No numerical index is calculated.", "", "Generated from the three canonical criterion records by `python render_criteria.py`. The brief notes are editorial summaries; consult the linked records for exact evidence and boundaries.", ""]
    (ROOT / "CRITERIA.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
