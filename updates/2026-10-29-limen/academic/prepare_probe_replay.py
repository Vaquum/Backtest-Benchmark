"""Prepare fresh external probe copies; preserve source pins and archived evidence."""
import argparse
import ast
from hashlib import sha256
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
PINS = {'Limen-baseline': '29837e666604eee74a2ac94f328fb9803724342a', 'Limen': '25e47866422d007da55cb19625344183599ba671'}
FIXTURE = 'tests/fixtures/spot_1h_20240101_20241231.parquet'
FIXTURE_SHA = 'a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72'


def digest(data):
    return sha256(data).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Archived assignment differs')
    return text.replace(old, new)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    workspace, output = args.workspace_root.resolve(strict=True), args.output.resolve()
    if output.exists():
        raise FileExistsError(output)
    for name, pin in PINS.items():
        root = workspace / name
        actual = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
        dirty = subprocess.check_output(['git', '-C', str(root), 'status', '--porcelain', '--untracked-files=no'], text=True).strip()
        if actual != pin or dirty or digest((root / FIXTURE).read_bytes()) != FIXTURE_SHA:
            raise ValueError('Source or recorded fixture admission differs: ' + name)
    safety = HERE.parent / 'safety'
    expected = json.loads((safety / 'probe-comparison.json').read_text())['files']
    originals = {n: (safety / n).read_bytes() for n in ('boundary_probes.py', 'interpret_boundary_probes.py')}
    if any(digest(data) != expected[name] for name, data in originals.items()):
        raise ValueError('Archived safety script hash differs')
    probe = replace_once(originals['boundary_probes.py'].decode(), "ROOT = Path('/workspace/scratch/008a76ec4981')", 'ROOT = Path(' + repr(str(workspace)) + ')')
    probe = replace_once(probe, "SAFE = ROOT / 'Backtest-Benchmark/updates/2026-10-29-limen/safety'", 'SAFE = Path(__file__).resolve().parent')
    interpreter = replace_once(originals['interpret_boundary_probes.py'].decode(), 'EXPECTED_PROBE = "' + expected['boundary_probes.py'] + '"', 'EXPECTED_PROBE = "' + digest(probe.encode()) + '"')
    academic = {n: (HERE / n).read_bytes() for n in ('probe_causal_prefix.py', 'compare_causality_reports.py')}
    if digest(academic['probe_causal_prefix.py']) != json.loads((HERE / 'causal-prefix-baseline.json').read_text())['probe_script_sha256']:
        raise ValueError('Archived academic probe hash differs')
    if digest(academic['compare_causality_reports.py']) != json.loads((HERE / 'causal-prefix-comparison.json').read_text())['comparison_script_sha256']:
        raise ValueError('Archived academic interpreter hash differs')
    copies = {**{'academic/' + name: data for name, data in academic.items()}, 'safety/boundary_probes.py': probe.encode(), 'safety/interpret_boundary_probes.py': interpreter.encode()}
    for name, data in copies.items():
        ast.parse(data, filename=name)
    ancestor = output.parent
    while not ancestor.exists():
        ancestor = ancestor.parent
    if subprocess.run(['git', '-C', str(ancestor), 'rev-parse', '--show-toplevel'], capture_output=True).returncode == 0:
        raise ValueError('Replay output must be outside every Git checkout')
    output.mkdir(parents=True, exist_ok=False)
    for name, data in copies.items():
        target = output / name
        target.parent.mkdir(exist_ok=True)
        with target.open('xb') as stream:
            stream.write(data)
    receipt = {'scope': 'Preparation only; no engine, probe or native-test execution. Archived evidence is unchanged.',
               'workspace_root': str(workspace), 'output': str(output), 'source_pins': PINS, 'fixture_sha256': FIXTURE_SHA,
               'permitted_changes': ['Safety ROOT points to supplied workspace.', 'Safety SAFE is the copied script directory.', 'Safety interpreter EXPECTED_PROBE binds the copied probe hash.'],
               'academic_scripts': 'Copied byte-for-byte.', 'original_safety_sha256': {n: digest(data) for n, data in originals.items()},
               'copied_sha256': {n: digest(data) for n, data in copies.items()}, 'helper_sha256': digest(Path(__file__).read_bytes())}
    with (output / 'relocation-receipt.json').open('x') as stream:
        json.dump(receipt, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'prepared': str(output), 'executed': False}))


if __name__ == '__main__':
    main()
