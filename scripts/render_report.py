#!/usr/bin/env python3
"""Deterministically render code-linked comparison views from canonical assessment JSON."""
from __future__ import annotations
import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = {"Enforced": "E", "Optional": "O", "Partial": "P", "Fails": "F", "Unknown": "?", "N/A": "N/A"}


def escape(x):
    return str(x).replace("|", "\\|").replace("\n", " ")


def source_links(row):
    return "; ".join(f"[{ref['path']}:{ref['start_line']}–{ref['end_line']}]({ref['url']})" for ref in row["source_refs"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "reports")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    candidates = json.loads((ROOT / "catalog/candidates.json").read_text())
    criteria = json.loads((ROOT / "protocol/criteria.json").read_text())
    overview = json.loads((ROOT / "catalog/overview.json").read_text())
    rows = sum([json.loads((ROOT / f"assessment/{axis}.json").read_text()) for axis in ["performance", "academic", "safety"]], [])
    lookup = {(r["candidate_id"], r["criterion_id"]): r for r in rows}
    assert len(rows) == len(candidates) * len(criteria) == len(lookup)
    campaigns_path = ROOT / "catalog/campaigns.json"
    campaigns = json.loads(campaigns_path.read_text()) if campaigns_path.exists() else []
    measured = []
    for entry in campaigns:
        report_path = ROOT / entry["report"]
        if entry.get("report_sha256") != sha256(report_path.read_bytes()).hexdigest():
            raise ValueError(f"Registered campaign bytes changed: {entry['id']}")
        report = json.loads(report_path.read_text())
        measured += [dict(row, campaign_id=entry["id"], report=entry["report"]) for row in report["summary"]]

    fields = ["candidate_id", "criterion_id", "aspect", "criterion", "status", "evidence_type", "applicability", "capability", "scope", "finding", "limitation", "measurement_state", "measurements", "source_refs"]
    exported = []
    for candidate in candidates:
        for criterion in criteria:
            row = lookup[candidate["id"], criterion["id"]]
            exported.append({**row, "aspect": criterion["aspect"], "criterion": criterion["criterion"]})
    (out / "assessment-grid.json").write_text(json.dumps(exported, indent=2, allow_nan=False) + "\n")
    with (out / "assessment-grid.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in exported:
            writer.writerow({key: json.dumps(row.get(key), ensure_ascii=False) if isinstance(row.get(key), (list, dict)) else row.get(key) for key in fields})

    matrix = ["# Systematic comparison grid", "", f"{len(candidates)} implementations × {len(criteria)} criteria = {len(rows)} scoped cells. Generated from canonical JSON; the underlying code and retained runs are the evidence.", "", "**E** Enforced · **O** Optional · **P** Partial · **F** Fails · **?** Unknown · **N/A** outside the selected native layer. These labels are not scores. Click a cell for scope, applicability, evidence, limitations and pinned code.", "", "[Human overview](overview.md) · [Quantitative replay results](performance-results.md) · [Machine-readable CSV](assessment-grid.csv) · [JSON](assessment-grid.json) · [Protocol](../protocol/README.md)", ""]
    for prefix, title in [("P", "Computation performance"), ("A", "Academic rigor and robustness"), ("S", "Safety properties")]:
        matrix += [f"## {title}", "", "| Criterion | " + " | ".join(escape(c["name"]) for c in candidates) + " |", "|---|" + "---|" * len(candidates)]
        for criterion in (x for x in criteria if x["id"].startswith(prefix)):
            cells = [f"[{SHORT[lookup[c['id'], criterion['id']]['status']]}](candidates/{c['id']}.md#{criterion['id'].lower()})" for c in candidates]
            matrix.append(f"| {criterion['id']} {escape(criterion['criterion'])} | " + " | ".join(cells) + " |")
        matrix += [""]
    (out / "comparison-grid.md").write_text("\n".join(matrix) + "\n")

    pages = out / "candidates"
    pages.mkdir(exist_ok=True)
    for candidate in candidates:
        cid = candidate["id"]
        summary = overview.get(cid, {})
        lines = [f"# {candidate['name']}", "", f"**Frozen source:** [{candidate['repository']} @ {candidate['commit']}]({candidate['source_url']})", "", f"**Observed license label:** {candidate.get('license_label', 'Unreviewed')}  ", f"**Layer:** {summary.get('layer', candidate.get('track', 'Unspecified'))}", "", "[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)", ""]
        for axis in ["computation", "academic", "safety"]:
            if axis in summary:
                lines += [f"**{axis.title()}:** {summary[axis]}", ""]
        for criterion in criteria:
            row = lookup[cid, criterion["id"]]
            lines += [f"## {criterion['id']}", "", f"### {criterion['criterion']}", "", f"**{row['status']}** · {', '.join(row['evidence_type'])} · applicability `{row['applicability']}` · capability `{row['capability']}`", "", f"**Scope:** {row['scope']}", "", row["finding"], "", f"**Limit:** {row['limitation']}", ""]
            if row.get("measurement_state"):
                lines += [f"**Measurement state:** {row['measurement_state']}", ""]
            if row.get("measurements"):
                lines += ["**Recorded measurements:**", "", "```json", json.dumps(row["measurements"], indent=2), "```", ""]
            if row.get("subcapabilities"):
                lines += ["**Distinct sub-capabilities:** " + "; ".join(f"{k}: {v}" for k,v in row["subcapabilities"].items()), ""]
            lines += ["**Executable sources:** " + source_links(row), "", f"**Repeatable criterion protocol:** {criterion['protocol']}", ""]
        (pages / f"{cid}.md").write_text("\n".join(lines) + "\n")

    def number(value, decimals=3):
        return "—" if value is None else f"{value:,.{decimals}f}"

    perf = ["# Recorded execution performance", "", "Values describe the frozen source builds, exact real input and declared public API/component workload. They are not universal engine speed, native indicator throughput, a trained research campaign, or live-trading capacity.", "", "Warm latency is the median of the within-process medians; process and repetition counts belong to each campaign's raw report. First full-API calls use fresh processes/JIT caches. Full-common latency includes common-output extraction; native extra work differs. The process-median range is descriptive, not a confidence interval. Separate campaigns must not be pooled or compared without reconciling source, data, contract, machine and timing scope. See the [full protocol](../protocol/README.md).", ""]
    if measured:
        for entry in campaigns:
            campaign_rows = [r for r in measured if r["campaign_id"] == entry["id"]]
            perf += [f"## Campaign {entry['id']}", "", f"[Raw report](../{entry['report']}) · SHA-256 `{entry['report_sha256']}`", "", f"Input SHA-256 `{entry['input_sha256']}`. Started {entry['started_utc']}; finished {entry['finished_utc']}.", ""]
            for rank, title in [(True, "Full native public API results"), (False, "Native components — no full-engine ratios")]:
                perf += [f"### {title}", "", "| Engine | Strategy | Status / processes | Warm full-common ms | Process-median range ms | First full-common ms | Candidate/Limen duration | Peak process RSS MiB |", "|---|---|---|---:|---:|---:|---:|---:|"]
                for row in campaign_rows:
                    if bool(row["rank_against_full_engine"]) != rank:
                        continue
                    spread = number(row.get("warm_process_median_ms_min")) + "–" + number(row.get("warm_process_median_ms_max"))
                    ratio = row.get("relative_to_limen_warm_full_common")
                    perf += [f"| [{row['engine']}](candidates/{row['engine']}.md#p07) | {row['strategy']} | {row['status']} / {row.get('independent_processes', 0)} | {number(row.get('warm_full_common_ms_median'))} | {spread} | {number(row.get('first_full_common_ms_median'))} | {number(ratio, 2) + '×' if ratio is not None else 'Not eligible'} | {number(row['peak_rss_bytes_median']/2**20 if row.get('peak_rss_bytes_median') else None,1)} |"]
                perf += [""]
            perf += ["### Cold process and timing decomposition", "", "Launch-to-first-valid includes source verification, imports, input loading, oracle and successful parity. It is a reproducible harness journey, not pure native startup. RSS is a process high-water mark, not incremental engine allocation.", "", "| Engine | Strategy | Native warm ms | Extraction warm ms | Warm CPU ms | Launch to first valid ms | Evaluated bars/s |", "|---|---|---:|---:|---:|---:|---:|"]
            for row in campaign_rows:
                perf += [f"| {row['engine']} | {row['strategy']} | {number(row.get('warm_engine_ms_median'))} | {number(row.get('warm_extraction_common_ms_median'))} | {number(row.get('warm_full_common_cpu_ms_median'))} | {number(row.get('launch_to_first_valid_ms_median'))} | {number(row.get('warm_evaluation_bars_per_second'),0)} |"]
            perf += [""]
        perf += ["## Interpretation and retained attempts", "", "Machine-level raw results include scope/settings, native output observability, every timing call, process medians, source/build identity, code hashes, parity checks and process logs. Prepared market arrays and compiler caches are omitted from published evidence with digests; rerunning from the hashed source fixture regenerates them.", "", "The separately retained [original campaign](../results/campaigns/2026-10-19-common-zero-original/) did not limit Polars' separate pool and is excluded from these registered headline tables. The corrective campaign adds explicit Polars limits and observed loaded-pool admission. See [performance interpretation](performance-analysis.md) for native execution versus lazy output materialization, the original control deviation and the separately labelled Limen internal-core diagnostics. A core diagnostic's phase named first runs after the full snapshot calls and is not process-cold.", ""]
    else:
        perf += ["No completed quantitative campaign has been registered. Unknown values must not be converted into scores or zeros.", ""]
    perf += ["## Unmeasured comparison scopes", "", "LEAN, Zipline-reloaded, Freqtrade and Jesse are fully included in the code grid but lack an admitted matched replay adapter in this campaign. Nautilus's native source test compilation hit two explicit time limits; no execution or test-success result is inferred. hftbacktest is a recorded-depth specialist; its 22 passing native library tests are not an OHLC performance measurement. Full QSTrader/Qlib workflows, parameter/search scaling, native indicator kernels, parallel/GPU throughput, market-impact fidelity and restart costs remain unmeasured.", "", "Only vectorbt and Qlib passed the separate 5-bps fee plus 5-bps slippage component/public-API preflight; it is not a comparative costed-speed campaign. Limen's common snapshot adapter rejects that accounting convention, so a costed Limen ratio is absent by design.", ""]
    (out / "performance-results.md").write_text("\n".join(perf) + "\n")

    summary = ["# Comparison overview", "", "This is a code-evidenced baseline and extensible benchmark, not a product ranking. The complete grid retains every criterion and every unknown. Scope, implementation and evidence remain separate.", "", "[42-criterion grid](comparison-grid.md) · [Measured performance](performance-results.md) · [Academic analysis](academic-analysis.md) · [Safety analysis](safety-analysis.md) · [Protocol](../protocol/README.md)", "", "| Implementation and native layer | Computation | Academic rigor / robustness | Safety properties |", "|---|---|---|---|"]
    for c in candidates:
        o = overview.get(c["id"], {})
        summary += [f"| [{escape(c['name'])}](candidates/{c['id']}.md) — {escape(o.get('layer', c.get('track','')))} | {escape(o.get('computation','Unreviewed'))} [P01–P12](candidates/{c['id']}.md#p01) | {escape(o.get('academic','Unreviewed'))} [A01–A15](candidates/{c['id']}.md#a01) | {escape(o.get('safety','Unreviewed'))} [S01–S15](candidates/{c['id']}.md#s01) |"]
    summary += ["", "## Cohort and exclusions", "", "Ten original products are excluded from the behavioral grid because no inspectable engine implementation was admitted: TradingView, TrendSpider, MetaTrader 5, NinjaTrader, TradeStation, AmiBroker, MultiCharts, Portfolio123, Portfolio Visualizer and StrategyQuant/X. This is an evidence-eligibility result, not a capability or quality judgment. QuantConnect's hosted service and vectorbt PRO are separate from the admitted LEAN/public-source engines. Zipline-reloaded is one frozen lineage, not a result for all Zipline forks. See [exclusion/re-entry register](../catalog/exclusions.json).", "", "Added coverage: bt and QSTrader for portfolio workflows, Qlib for model research, Jesse for crypto research/execution and hftbacktest for specialized depth/latency replay. This is a deliberately bounded cohort, not an exhaustive inventory of every public backtesting project.", "", "## Source and licensing identities", "", "| Candidate | Frozen revision | Observed source license |", "|---|---|---|"]
    for c in candidates:
        summary += [f"| {escape(c['name'])} | [{c['commit'][:12]}]({c['source_url']}) | {escape(c.get('license_label','Unreviewed'))} |"]
    summary += ["", "The public vectorbt source carries Apache 2.0 plus Commons Clause 1.0. The benchmark labels it public-source and does not present it as unrestricted open source. Candidate code/data retain their own terms; the benchmark's MIT license covers its own contributions.", ""]
    (out / "overview.md").write_text("\n".join(summary) + "\n")
    print(json.dumps({"candidates": len(candidates), "criteria": len(criteria), "cells": len(rows), "quantitative_case_rows": len(measured), "output": str(out)}))


if __name__ == "__main__":
    main()
