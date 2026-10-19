#!/usr/bin/env python3
"""Render one candidate against Limen across all criteria; never collapse scopes into a score."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    catalog = {c["id"]: c for c in json.loads((ROOT / "catalog/candidates.json").read_text())}
    p.add_argument("--candidate", choices=sorted(catalog), required=True)
    p.add_argument("--baseline", choices=sorted(catalog), default="limen")
    p.add_argument("--output", type=Path, help="New Markdown file; default stdout")
    args = p.parse_args()
    rows = sum([json.loads((ROOT / f"assessment/{axis}.json").read_text()) for axis in ["performance", "academic", "safety"]], [])
    lookup = {(r["candidate_id"], r["criterion_id"]): r for r in rows}
    criteria = json.loads((ROOT / "protocol/criteria.json").read_text())
    a, b = catalog[args.baseline], catalog[args.candidate]
    lines = [f"# {b['name']} against {a['name']}", "", f"Source revisions: [{a['commit']}]({a['source_url']}); [{b['commit']}]({b['source_url']}).", "", "Statuses are scoped observations, not scores. Native research, execution and benchmark adapter layers may differ. Unknown and N/A are not passes or zero values. Quantitative comparisons require the same admitted contract and output scope.", ""]
    for criterion in criteria:
        lines += [f"## {criterion['id']} — {criterion['criterion']}", ""]
        for candidate in [a, b]:
            row = lookup[candidate["id"], criterion["id"]]
            lines += [f"### {candidate['name']}: {row['status']}", "", f"**Evidence:** {', '.join(row['evidence_type'])}. **Applicability:** {row['applicability']}. **Capability:** {row['capability']}.", "", f"**Scope:** {row['scope']}", "", row["finding"], "", f"**Limit:** {row['limitation']}", ""]
            for m in row.get("measurements", []):
                lines += ["```json", json.dumps(m, indent=2), "```", ""]
            lines += ["**Code:** " + "; ".join(f"[{r['path']}:{r['start_line']}–{r['end_line']}]({r['url']})" for r in row["source_refs"]), ""]
        lines += [f"**Repeatable check:** {criterion['protocol']}", ""]
    content = "\n".join(lines) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as output:
            output.write(content)
        print(args.output.resolve())
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
