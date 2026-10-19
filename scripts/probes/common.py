"""Admission and output rules shared by the retained local boundary probes.

These are reproducibility checks, not a sandbox for supplied Python/native code.
Tracked source files must match the candidate catalog; generated build files may
be present. Native binary provenance is reported separately by each probe.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess


REPOSITORY = Path(__file__).resolve().parents[2]


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git(source, *arguments):
    completed = subprocess.run(
        ["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(source), *arguments],
        text=True, capture_output=True, timeout=15,
    )
    if completed.returncode:
        raise RuntimeError(f"Cannot verify source checkout with git {arguments[0]}")
    return completed.stdout.strip()


def verify_source(candidate_id, source):
    catalog_path = REPOSITORY / "catalog/candidates.json"
    candidates = {item["id"]: item for item in json.loads(catalog_path.read_text())}
    if candidate_id not in candidates:
        raise ValueError(f"Candidate is absent from the frozen catalog: {candidate_id}")
    expected = candidates[candidate_id]
    source = Path(source).resolve(strict=True)
    if not source.is_dir():
        raise ValueError("Source must be a candidate checkout directory")
    top = Path(_git(source, "rev-parse", "--show-toplevel")).resolve()
    if top != source:
        raise ValueError("Source must identify the checkout root, not a nested directory")
    actual = _git(source, "rev-parse", "HEAD")
    if actual != expected["commit"]:
        raise ValueError(f"Source commit does not match the frozen catalog for {candidate_id}")
    dirty = _git(source, "status", "--porcelain", "--untracked-files=no", "--ignore-submodules=none")
    if dirty:
        raise ValueError(f"Tracked source files are modified for {candidate_id}")
    return {
        "candidate_id": candidate_id, "path": str(source), "repository": expected["repository"],
        "commit": actual, "tree": _git(source, "rev-parse", "HEAD^{tree}"),
        "tracked_source_clean": True, "catalog_sha256": sha256_file(catalog_path),
    }


def verify_fixture(fixture):
    catalog_path = REPOSITORY / "catalog/data.json"
    expected = json.loads(catalog_path.read_text())
    fixture = Path(fixture).resolve(strict=True)
    if not fixture.is_file():
        raise ValueError("Fixture must be a regular recorded-data file")
    actual = sha256_file(fixture)
    if actual != expected["sha256"]:
        raise ValueError("Fixture SHA-256 does not match the frozen recorded-data catalog")
    return {"id": expected["id"], "path": str(fixture), "sha256": actual,
            "catalog_sha256": sha256_file(catalog_path)}


def assert_output_available(output):
    output = Path(output).absolute()
    if os.path.lexists(output):
        raise FileExistsError(f"Refusing to overwrite existing probe output: {output}")
    return output


def admit_probe(candidate_id, source, *, output=None, fixture=None):
    # Reject existing results before importing or executing any candidate code.
    if output is not None:
        assert_output_available(output)
    admission = {"source": verify_source(candidate_id, source)}
    if fixture is not None:
        admission["fixture"] = verify_fixture(fixture)
    return admission


def verify_imported_module(module, source):
    location = getattr(module, "__file__", None)
    if location is None:
        raise ValueError("Imported candidate module has no source-file identity")
    source = Path(source).resolve(strict=True)
    path = Path(location).resolve(strict=True)
    if not path.is_relative_to(source):
        raise ValueError("Imported candidate module is outside the admitted source checkout")
    _git(source, "ls-files", "--error-unmatch", "--", str(path.relative_to(source)))


def verify_unchanged(admission):
    prior_source = admission["source"]
    current = verify_source(prior_source["candidate_id"], prior_source["path"])
    if current != prior_source:
        raise ValueError("Source or source catalog changed while the probe was running")
    if "fixture" in admission:
        if verify_fixture(admission["fixture"]["path"]) != admission["fixture"]:
            raise ValueError("Fixture or fixture catalog changed while the probe was running")


def write_json_exclusive(output, result):
    # Exclusive creation also closes the race after the pre-execution check.
    serialized = json.dumps(result, indent=2, default=str) + "\n"
    output = assert_output_available(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        handle.write(serialized)
