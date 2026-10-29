"""Verify the published update and every archived binary without executing Limen."""
from hashlib import sha256
import json
from pathlib import Path
import tarfile


def main():
    here = Path(__file__).resolve().parent
    repository = here.parents[1]
    manifest = json.loads((here / "publication_manifest.json").read_text())
    for item in manifest["files"]:
        path = repository / item["path"]
        if not path.resolve().is_relative_to(repository):
            raise ValueError("Published path leaves the repository")
        content = path.read_bytes()
        if len(content) != item["bytes"] or sha256(content).hexdigest() != item["sha256"]:
            raise ValueError(f"Published content differs: {item['path']}")
    binaries = json.loads((here / "binary-evidence-manifest.json").read_text())
    archive = here / binaries["archive"]
    if sha256(archive.read_bytes()).hexdigest() != binaries["archive_sha256"]:
        raise ValueError("Binary archive differs")
    with tarfile.open(archive, "r:xz") as handle:
        members = handle.getmembers()
        if len(members) != binaries["member_count"]:
            raise ValueError("Binary member count differs")
        for item in binaries["members"]:
            member = handle.getmember(item["path"])
            if not member.isfile() or not (here / member.name).resolve().is_relative_to(here):
                raise ValueError("Invalid binary archive path/type")
            content = handle.extractfile(member).read()
            if len(content) != item["bytes"] or sha256(content).hexdigest() != item["sha256"]:
                raise ValueError(f"Binary content differs: {item['path']}")
    print(json.dumps({"published_files_verified": len(manifest["files"]),
                      "binary_members_verified": binaries["member_count"],
                      "scope": "Byte integrity only; no engine execution or scientific revalidation"}))


if __name__ == "__main__":
    main()
