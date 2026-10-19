#!/usr/bin/env python3
"""Bind a completed, validated campaign to the quantitative cells without replacing raw evidence."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--campaign", type=Path, required=True)
    p.add_argument("--id", required=True)
    args = p.parse_args()
    path = args.campaign.resolve()
    relative = path.relative_to(ROOT).as_posix()
    subprocess.run([sys.executable, str(ROOT / "scripts/validate_assessment.py"), "--campaign", str(path), "--require-native-thread-policy"], check=True)
    campaign = json.loads(path.read_text())
    if campaign.get("status") != "completed" or campaign.get("command") != "run":
        raise ValueError("Only a complete measurement campaign can be registered")
    catalog_path = ROOT / "catalog/campaigns.json"
    catalog = json.loads(catalog_path.read_text()) if catalog_path.exists() else []
    entry = {"id": args.id, "report": relative, "report_sha256": sha256(path.read_bytes()).hexdigest(), "scope": "Recorded hourly zero-cost full-engine and separately labelled native-component replay", "contract": campaign["contract"], "input_sha256": campaign["input"]["sha256"] if "sha256" in campaign["input"] else campaign["input"].get("input_sha256"), "started_utc": campaign["started_utc"], "finished_utc": campaign["finished_utc"]}
    existing = [x for x in catalog if x["id"] == args.id]
    if existing and existing != [entry]:
        raise ValueError("Campaign ID already belongs to different evidence")
    rows = json.loads((ROOT / "assessment/performance.json").read_text())
    by_id = {(r["candidate_id"], r["criterion_id"]): r for r in rows}
    fields = {
        "P03": ["first_full_common_ms_median", "first_full_common_ms_min", "first_full_common_ms_max", "launch_to_ready_ms_median", "launch_to_first_valid_ms_median"],
        "P07": ["warm_full_common_ms_median", "warm_engine_ms_median", "warm_extraction_common_ms_median", "warm_full_common_cpu_ms_median", "warm_process_medians_ms", "warm_process_median_ms_min", "warm_process_median_ms_max", "warm_evaluation_bars_per_second", "relative_to_limen_warm_full_common"],
        "P09": ["peak_rss_bytes_median"],
    }
    touched = set()
    for result in campaign["summary"]:
        if result["status"] != "verified" or result.get("warm_full_common_ms_median") is None:
            continue
        for cid, keys in fields.items():
            row = by_id[result["engine"], cid]
            identity = result["engine"], cid
            if identity not in touched:
                row.setdefault("pre_campaign_status", row["status"])
                row.setdefault("pre_campaign_limitation", row["limitation"])
                row["status"] = "Partial"
                row["evidence_type"] = list(dict.fromkeys([*row["evidence_type"], "Tested", "Measured"]))
                row["measurement_state"] = "Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured"
                row["measurements"] = [x for x in row.get("measurements", []) if x.get("campaign_id") != args.id]
                row["limitation"] = {
                    "P03": "First-call figures belong to the declared public API/component scope. Process-launch-to-first-valid includes identity, imports, data, oracle and validation, not just engine startup. No full trained research campaign or fleet-level latency guarantee.",
                    "P07": "One recorded single-instrument zero-cost contract and two fixed signals. Native APIs perform different extra work. Components and internal kernels cannot receive full-engine ratios; costs, data-size scaling, native indicators and other markets require separate campaigns.",
                    "P09": "Process high-water RSS includes imported dependencies, compilation and earlier calls; it is not incremental engine memory, process-tree PSS or a hard resource bound. Multi-asset/grid/parallel memory scaling remains unmeasured.",
                }[cid]
                touched.add(identity)
            row["measurements"].append({"campaign_id": args.id, "report": relative, "strategy": result["strategy"],
                                        "rank_against_full_engine": result["rank_against_full_engine"], "independent_processes": result["independent_processes"],
                                        **{key: result.get(key) for key in keys}})
    (ROOT / "assessment/performance.json").write_text(json.dumps(rows, indent=2, allow_nan=False) + "\n")
    if not existing:
        catalog.append(entry)
    catalog_path.write_text(json.dumps(catalog, indent=2) + "\n")
    print(json.dumps({"campaign": args.id, "quantitative_cells_updated": len(touched)}))


if __name__ == "__main__":
    main()
