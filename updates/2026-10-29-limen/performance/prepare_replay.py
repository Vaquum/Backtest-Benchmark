from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlparse


HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def git(source, *arguments):
    return subprocess.check_output(['git', *arguments], cwd=source, text=True).strip()


def inspect_environment(environment, source, expected_dependencies):
    if environment.name != 'limen':
        raise ValueError('Each environment directory must end in /limen for the unchanged worker CLI')
    python = environment / 'bin/python'
    configuration = (environment / 'pyvenv.cfg').read_text().lower().replace(' ', '')
    if 'include-system-site-packages=false' not in configuration:
        raise ValueError('Use a clean venv without system site packages')
    probe = '''import importlib.metadata as m,json,platform,sys
d=m.distribution("vaquum-limen")
print(json.dumps({"python":sys.version,"python_version":platform.python_version(),"platform":platform.platform(),"sys_platform":sys.platform,"prefix":sys.prefix,"candidate_version":d.version,"candidate_direct_url":d.read_text("direct_url.json"),"distributions":sorted([{"name":p.metadata["Name"],"version":p.version} for p in m.distributions()],key=lambda p:p["name"].lower())}))'''
    environment_variables = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
    environment_variables.pop('PYTHONPATH', None)
    environment_variables.pop('PYTHONHOME', None)
    observed = json.loads(subprocess.check_output([str(python), '-c', probe], env=environment_variables, text=True))
    if observed['python_version'] != '3.12.14' or observed['sys_platform'] != 'linux':
        raise ValueError('This archived reproduction setup requires Python 3.12.14 on Linux')
    direct = json.loads(observed['candidate_direct_url'])
    url = urlparse(direct['url'])
    if url.scheme != 'file' or Path(unquote(url.path)).resolve() != source or direct.get('dir_info', {}).get('editable', False):
        raise ValueError('Install each exact source noneditably with --no-deps --no-build-isolation')
    dependencies = {row['name'].lower(): row['version'] for row in observed['distributions'] if row['name'].lower() != 'vaquum-limen'}
    if dependencies != expected_dependencies:
        raise ValueError('Installed dependency inventory differs from the archived core lock plus LightGBM extension')
    return observed


def main():
    parser = argparse.ArgumentParser(description='Prepare a fresh, location-bound replay plan without installing packages or running engines')
    parser.add_argument('--benchmark-root', type=Path, default=HERE.parents[2])
    parser.add_argument('--baseline-source', type=Path, required=True)
    parser.add_argument('--latest-source', type=Path, required=True)
    parser.add_argument('--baseline-env', type=Path, required=True)
    parser.add_argument('--latest-env', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    benchmark = args.benchmark_root.resolve()
    output = args.output.resolve()
    paired_template = HERE / 'paired-preregistration.json'
    native_template = HERE / 'native-preregistration.json'
    paired = json.loads(paired_template.read_text())
    native = json.loads(native_template.read_text())
    original_environment = json.loads((HERE / 'environment/baseline-install-extended.json').read_text())
    dependencies = {row['name'].lower(): row['version'] for row in original_environment['observed']['distributions'] if row['name'].lower() != 'vaquum-limen'}
    lock = benchmark / 'locks/limen.txt'
    if digest(lock) != paired['variants']['baseline']['dependency_lock_sha256']:
        raise ValueError('Original core hash lock changed')
    extension = HERE / 'environment/lightgbm-extension.txt'
    if digest(extension) != paired['environment_extension']['lock_sha256']:
        raise ValueError('LightGBM extension lock changed')
    for relative, expected in paired['benchmark_code_sha256'].items():
        if digest(benchmark / relative) != expected:
            raise ValueError(f'Frozen benchmark Python changed: {relative}')
    for name, expected in [('run_paired_replay.py', paired['paired_driver_sha256']), ('run_native_replay.py', native['native_driver_sha256'])]:
        if digest(HERE / name) != expected:
            raise ValueError(f'Archived outer driver changed: {name}')

    settings = {}
    for variant in ('baseline', 'latest'):
        source = getattr(args, variant + '_source').resolve()
        environment = getattr(args, variant + '_env').resolve()
        expected_commit = paired['variants'][variant]['source_commit']
        if git(source, 'rev-parse', 'HEAD') != expected_commit or git(source, 'status', '--porcelain', '--untracked-files=no'):
            raise ValueError(f'Use a clean checkout of the pinned {variant} source')
        if output.is_relative_to(source):
            raise ValueError('Replay output must be outside both source checkouts')
        if digest(source / native['fixture_relative_path']) != paired['input_sha256']:
            raise ValueError(f'Recorded fixture differs: {variant}')
        for relative, expected in native['variants'][variant]['harness_files_sha256'].items():
            if digest(source / relative) != expected:
                raise ValueError(f'Native harness differs: {variant}/{relative}')
        settings[variant] = {'source': source, 'environment': environment,
                             'observed': inspect_environment(environment, source, dependencies)}
    candidate = next(row for row in json.loads((benchmark / 'catalog/candidates.json').read_text()) if row['id'] == 'limen')
    output.mkdir(parents=True, exist_ok=False)
    (output / 'environment').mkdir()
    shutil.copyfile(lock, output / 'environment/core-limen.lock')
    shutil.copyfile(extension, output / 'environment/lightgbm-extension.txt')
    for name in ('run_paired_replay.py', 'run_native_replay.py'):
        shutil.copyfile(HERE / name, output / name)
    for variant, value in settings.items():
        source, environment = value['source'], value['environment']
        overlay = output / 'runner' / variant
        for relative in paired['benchmark_code_sha256']:
            destination = overlay / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(benchmark / relative, destination)
        shutil.copyfile(benchmark / 'bench/NOTICE', overlay / 'bench/NOTICE')
        (overlay / 'catalog').mkdir()
        current = copy.deepcopy(candidate)
        commit = paired['variants'][variant]['source_commit']
        current.update(commit=commit, commit_date=git(source, 'show', '-s', '--format=%cI', 'HEAD'),
                       source_url=f'https://github.com/Vaquum/Limen/tree/{commit}',
                       revision_policy='Explicit paired revision; no floating branch or release-tag substitution')
        for license_file in current['license_files']:
            license_file.update(sha256=digest(source / license_file['path']),
                                url=f"https://github.com/Vaquum/Limen/blob/{commit}/{license_file['path']}")
        catalog = overlay / 'catalog/candidates.json'
        catalog.write_text(json.dumps([current], indent=2) + '\n')
        manifest = {'engine': 'limen', 'source_commit': commit, 'source_path': str(source),
                    'environment_path': str(environment), 'python': str(environment / 'bin/python'),
                    'dependency_lock': str(output / 'environment/core-limen.lock'),
                    'dependency_lock_sha256': digest(lock), 'status': 'installed',
                    'system_site_packages': False, 'observed': value['observed'],
                    'dependency_extensions': [{'package': 'lightgbm', 'version': '4.6.0',
                                               'lock': str(output / 'environment/lightgbm-extension.txt'),
                                               'lock_sha256': digest(extension)}]}
        manifest_path = overlay / '.work/manifests/limen.json'
        manifest_path.parent.mkdir(parents=True)
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
        paired['variants'][variant].update(source_path=str(source), overlay=str(overlay),
                                          python=str(environment / 'bin/python'), env_root=str(environment.parent),
                                          catalog_sha256=digest(catalog), setup_manifest_sha256=digest(manifest_path))
        native['variants'][variant].update(source_path=str(source), python=str(environment / 'bin/python'),
                                          setup_manifest_sha256=digest(manifest_path))
    paired['input'] = str(settings['baseline']['source'] / native['fixture_relative_path'])
    paired['environment_extension'] = {'package': 'lightgbm==4.6.0', 'lock_sha256': digest(extension),
                                       'purpose': 'Matched original native preparation workload'}
    now = datetime.now(timezone.utc).isoformat()
    for name, record, template in [('paired', paired, paired_template), ('native', native, native_template)]:
        record.pop('native_launch_amendment', None)
        record.pop('environment_finalized_utc', None)
        record.update(registered_utc=now, status='prepared_not_executed',
                      prepared_from_archived_template_sha256=digest(template),
                      execution_environment='Run in native Linux with observable /proc/cgroup provenance; unchanged thread and parity admission',
                      preparation_script_sha256=digest(Path(__file__)))
        (output / f'{name}-preregistration.json').write_text(json.dumps(record, indent=2) + '\n')
    print(output)
    print('Prepared only. No engine calls, timings, package installation or source edits were performed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
