#!/usr/bin/env python3
"""Exercise the built pinned LEAN Unzip helper inside one temporary root only.

The ZIP contains an innocuous ../sibling marker. Its target stays within the
probe's temporary root, while testing containment within the intended extraction
subdirectory. No financial data or live/network operation is involved. The source
project must already have been built; this script builds only a tiny local caller.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from xml.sax.saxutils import escape
from common import admit_probe, verify_unchanged, write_json_exclusive

PROGRAM = r'''
using System;
using System.IO;
using System.IO.Compression;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
internal static class Program {
    static int Main(string[] args) {
        string root = Path.GetFullPath(args[0]);
        string extraction = Path.Combine(root, "extracted");
        string marker = Path.GetFullPath(Path.Combine(extraction, "../sibling/probe_marker.txt"));
        if (!marker.StartsWith(root + Path.DirectorySeparatorChar, StringComparison.Ordinal))
            throw new InvalidOperationException("Probe destination must stay inside its temporary root");
        Directory.CreateDirectory(extraction);
        string zipPath = Path.Combine(root, "probe.zip");
        byte[] payload = Encoding.UTF8.GetBytes("bounded archive containment probe\n");
        using (var archive = new ZipArchive(File.Create(zipPath), ZipArchiveMode.Create)) {
            using var entry = archive.CreateEntry("../sibling/probe_marker.txt").Open();
            entry.Write(payload);
        }
        bool returned = QuantConnect.Compression.Unzip(zipPath, extraction, overwrite: true);
        bool exists = File.Exists(marker);
        bool outsideIntended = !marker.StartsWith(extraction + Path.DirectorySeparatorChar, StringComparison.Ordinal);
        string? hash = exists ? Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(marker))).ToLowerInvariant() : null;
        Console.WriteLine(JsonSerializer.Serialize(new {
            unzip_returned = returned, marker_exists = exists,
            marker_outside_intended_extraction_subdirectory = outsideIntended,
            marker_inside_probe_temporary_root = true, marker_sha256 = hash,
            loaded_assembly = typeof(QuantConnect.Compression).Assembly.Location
        }));
        return returned && exists && outsideIntended ? 0 : 1;
    }
}
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--dotnet", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source, dotnet, work = args.source.resolve(), args.dotnet.resolve(), args.work.resolve()
    admission = admit_probe("lean", source, output=args.output)
    assembly = source / "Compression/bin/Release/QuantConnect.Compression.dll"
    if not assembly.is_file():
        parser.error("The pinned source Compression project must already be built.")
    work.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, DOTNET_ROOT=str(dotnet.parent), DOTNET_CLI_TELEMETRY_OPTOUT="1",
               DOTNET_SKIP_FIRST_TIME_EXPERIENCE="1", DOTNET_GCHeapHardLimit="40000000",
               DOTNET_gcServer="0", MSBUILDDISABLENODEREUSE="1")
    with tempfile.TemporaryDirectory(prefix="lean-unzip-", dir=work) as temporary:
        temp = Path(temporary)
        env["DOTNET_CLI_HOME"] = str(temp / "dotnet-state")
        refs = "".join(f'<Reference Include="{escape(p.stem)}"><HintPath>{escape(str(p))}</HintPath></Reference>'
                       for p in sorted(assembly.parent.glob("*.dll")))
        project = temp / "Probe.csproj"
        project.write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
                           '<TargetFramework>net10.0</TargetFramework><Nullable>enable</Nullable>'
                           '<NuGetAudit>false</NuGetAudit></PropertyGroup><ItemGroup>' + refs + '</ItemGroup></Project>')
        (temp / "Program.cs").write_text(PROGRAM)
        (temp / "NuGet.Config").write_text('<configuration><packageSources><clear /></packageSources></configuration>')
        build = subprocess.run([str(dotnet), "build", str(project), "--configuration", "Release", "--nologo",
                                "--maxcpucount:1", "--configfile", str(temp / "NuGet.Config")],
                               env=env, text=True, capture_output=True, timeout=60, check=True)
        run = subprocess.run([str(dotnet), str(temp / "bin/Release/net10.0/Probe.dll"), str(temp / "containment")],
                             env=env, text=True, capture_output=True, timeout=15, check=True)
        observation = json.loads(run.stdout.strip().splitlines()[-1])
        loaded = Path(observation["loaded_assembly"])
        observation["loaded_assembly_sha256"] = hashlib.sha256(loaded.read_bytes()).hexdigest()
        assert observation["loaded_assembly_sha256"] == hashlib.sha256(assembly.read_bytes()).hexdigest()
        assert observation["marker_sha256"] == hashlib.sha256(b"bounded archive containment probe\n").hexdigest()
    commit = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    result = {
        "admission": admission,
        "candidate_id": "lean", "commit": commit, "evidence_type": ["Inspected", "Reproduced"],
        "scope": "Public Compression.Unzip overwrite=true helper; no automatic remote-data ingestion reachability is claimed.",
        "protocol": "Call the built pinned source helper with an innocuous parent-relative archive entry targeting a sibling of the extraction subdirectory, entirely inside one new temporary root; verify marker bytes and cleanup the root.",
        "observed": observation,
        "compiled_source_assembly": str(assembly),
        "build_output": build.stdout, "runtime_stderr": run.stderr,
        "limits": {"caller_build_timeout_seconds": 60, "probe_timeout_seconds": 15},
        "source_refs": [{"path": "Compression/Compression.cs", "start_line": 539, "end_line": 564,
                         "url": f"https://github.com/QuantConnect/Lean/blob/{commit}/Compression/Compression.cs#L539-L564"}],
        "limitation": "No existing user files were accessed or overwritten. The non-overwrite branch and ordinary market-data readers are separate routes. No claim of a remotely reachable service exploit or live trading effect.",
    }
    verify_unchanged(admission)
    write_json_exclusive(args.output, result)
    print(json.dumps({"output": str(args.output), "observed": observation}))


if __name__ == "__main__":
    main()
