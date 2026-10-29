# Reproduce the 29 October Limen update

This update compares **Limen 29837e666604eee74a2ac94f328fb9803724342a** (the retained 19 October baseline, distribution 5.40.1) with **25e47866422d007da55cb19625344183599ba671** (28 October source, distribution 5.46.2). The original benchmark harness is retained from **Backtest-Benchmark c88b14c50ee8e8ded1745a7da0d0a43f709dd9a5**. This is not an exact fourteen-day baseline and does not rerun the other twelve projects.

The recorded one-hour fixture is `tests/fixtures/spot_1h_20240101_20241231.parquet`, SHA256 **a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72**, unchanged between pins. Academic and safety probes use recorded slices; performance uses the recorded full fixture under its stated contract. Source, fixture, interpreter and result identities remain part of admission.

## Scope and prerequisites

The executed environment was **Linux x86_64, CPython 3.12.14**. Native process facilities, including `/proc`, are required by the bounded safety probe and process/resource checks. The native test suite also retrieves public recorded data from Hugging Face; it needs that network access or an already valid cache. The earlier restricted attempt is preserved in [its separate receipt](environment/native-suite-initial-attempt.json) and is not part of the admitted pass count.

The recipes below use Git, Python 3.12.14 and `uv`. They construct isolated environments and fresh output directories. They have not been installed and tested on every platform. New-machine results must retain their own observed dependency and platform metadata; the historical timings are not promised outcomes.

The native research environment is **CPU-oriented, not identical to the upstream CUDA dependency lock**. [research-cpu-selection.json](environment/research-cpu-selection.json) records removed Torch/CUDA packages. [research-cpu.lock](environment/research-cpu.lock) preserves upstream versions and hashes for retained dependencies. **Torch 2.13.0+cpu was installed separately from the official CPU index and is not covered by that retained hash lock.** The upstream XGBoost dependency `nvidia-nccl-cu12` was retained. The CPU lock must not be described as a fully hash-locked reproduction of the entire installed research environment.

Use new result directories outside **every** Git checkout. Several native project-binding tests inspect parent directories, so placing their temporary directories under the benchmark repository changes their test environment. The scripts refuse existing result files or nonempty output where applicable; do not remove the preserved results to rerun in their place.

## 1. Fresh source and core environments

Start from the root of a checkout containing this update. These are clean-setup recipes, not a claim that the exact original installation command was retained.

```bash
LIMEN_BENCH="$(pwd -P)"
LIMEN_UPDATE="$LIMEN_BENCH/updates/2026-10-29-limen"
LIMEN_WORK="$(mktemp -d "${TMPDIR:-/tmp}/limen-oct29.XXXXXXXX")"
LIMEN_OUTPUT="$LIMEN_WORK/results"
mkdir "$LIMEN_OUTPUT"

git clone --no-checkout https://github.com/Vaquum/Limen.git "$LIMEN_WORK/Limen"
git -C "$LIMEN_WORK/Limen" checkout --detach 25e47866422d007da55cb19625344183599ba671
git -C "$LIMEN_WORK/Limen" worktree add --detach "$LIMEN_WORK/Limen-baseline" 29837e666604eee74a2ac94f328fb9803724342a

uv venv --python 3.12.14 "$LIMEN_WORK/envs-baseline/limen"
uv venv --python 3.12.14 "$LIMEN_WORK/envs-latest/limen"
LIMEN_BASE_PY="$LIMEN_WORK/envs-baseline/limen/bin/python"
LIMEN_LATEST_PY="$LIMEN_WORK/envs-latest/limen/bin/python"
uv pip install --python "$LIMEN_BASE_PY" --require-hashes -r "$LIMEN_BENCH/locks/limen.txt"
uv pip install --python "$LIMEN_LATEST_PY" --require-hashes -r "$LIMEN_BENCH/locks/limen.txt"
uv pip install --python "$LIMEN_BASE_PY" --no-deps --require-hashes -r "$LIMEN_UPDATE/performance/environment/lightgbm-extension.txt"
uv pip install --python "$LIMEN_LATEST_PY" --no-deps --require-hashes -r "$LIMEN_UPDATE/performance/environment/lightgbm-extension.txt"
uv pip install --python "$LIMEN_BASE_PY" --no-deps --no-build-isolation "$LIMEN_WORK/Limen-baseline"
uv pip install --python "$LIMEN_LATEST_PY" --no-deps --no-build-isolation "$LIMEN_WORK/Limen"
```

These are noneditable source installations. The probe scripts additionally import from the explicitly admitted checkout and verify the source location. The installed distribution name is **vaquum-limen**, while its Python import is **limen**. The historical [baseline](environment/baseline-install.json) and [latest](environment/latest-install.json) installation receipts describe the original core environments, not arbitrary future installations.

## 2. Independent academic and safety probes

The academic script accepts source/output paths. The archived safety script instead contains `/workspace/scratch/008a76ec4981` and its original output-directory constraint. **Do not edit those archived bytes.** The preparation helper below checks the archived script hashes and source pins, copies academic scripts byte-for-byte, and makes only three recorded changes to new safety copies: workspace root, output location, and the interpreter's expected copied-probe hash. It writes a relocation receipt before any probe execution. Preparing copies does not execute tests or models.

```bash
python3 "$LIMEN_UPDATE/academic/prepare_probe_replay.py" \
  --workspace-root "$LIMEN_WORK" --output "$LIMEN_OUTPUT/probes"

export PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1 BLIS_NUM_THREADS=1 POLARS_MAX_THREADS=1
export RAYON_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1

"$LIMEN_BASE_PY" "$LIMEN_OUTPUT/probes/academic/probe_causal_prefix.py" \
  --repo-root "$LIMEN_WORK/Limen-baseline" --revision baseline \
  --output "$LIMEN_OUTPUT/probes/academic/causal-prefix-baseline.json"
"$LIMEN_LATEST_PY" "$LIMEN_OUTPUT/probes/academic/probe_causal_prefix.py" \
  --repo-root "$LIMEN_WORK/Limen" --revision latest \
  --output "$LIMEN_OUTPUT/probes/academic/causal-prefix-latest.json"
python3 "$LIMEN_OUTPUT/probes/academic/compare_causality_reports.py"

"$LIMEN_BASE_PY" -B "$LIMEN_OUTPUT/probes/safety/boundary_probes.py" \
  --label baseline --output "$LIMEN_OUTPUT/probes/safety/baseline-boundary-results.json"
"$LIMEN_LATEST_PY" -B "$LIMEN_OUTPUT/probes/safety/boundary_probes.py" \
  --label latest --output "$LIMEN_OUTPUT/probes/safety/latest-boundary-results.json"
python3 "$LIMEN_OUTPUT/probes/safety/interpret_boundary_probes.py" \
  --output "$LIMEN_OUTPUT/probes/safety/probe-comparison.json"
```

The academic comparison checks the five end-event columns separately from the retrospective research-only span count. It also compares current historical values with frozen-baseline prefix-final values. The safety probe checks resolver identity/admission without invoking the escaped callable, manifest-store content identity, bounded fractional-difference failure behavior and actual compiled Sensor output admission using explicit invalid-output canaries. Those canaries are not learned forecasts or synthetic market observations. The baseline fractional-difference probe uses subprocess resource limits: inspect its method receipt and teardown outcome separately; a resource-limited child exit is not proof of application-level recovery.

Original evidence remains in [academic](academic/) and [safety](safety/). Fresh relocated safety receipts deliberately carry a different probe hash, with the permitted substitutions recorded in `relocation-receipt.json`.

## 3. Complete current native suite

Use a separate research environment. This recipe retains the hashed CPU selection and then installs the separately version-pinned CPU Torch replacement without resolving a new dependency population. The original CPU Torch wheel archive hash and exact original installation command were not retained; [installed package metadata](environment/research-package-metadata.json) records what was present without claiming binary attestation.

```bash
uv venv --python 3.12.14 "$LIMEN_WORK/envs-research/limen"
LIMEN_RESEARCH_PY="$LIMEN_WORK/envs-research/limen/bin/python"
uv pip install --python "$LIMEN_RESEARCH_PY" --require-hashes \
  -r "$LIMEN_UPDATE/environment/research-cpu.lock"
uv pip install --python "$LIMEN_RESEARCH_PY" --no-deps \
  --index-url https://download.pytorch.org/whl/cpu 'torch==2.13.0+cpu'
uv pip install --python "$LIMEN_RESEARCH_PY" --no-deps --no-build-isolation "$LIMEN_WORK/Limen"

"$LIMEN_RESEARCH_PY" "$LIMEN_UPDATE/native_runner/run_native_suite.py" \
  --repo-root "$LIMEN_WORK/Limen" --output "$LIMEN_OUTPUT/native-suite"
```

The runner validates the exact latest source pin, clean tracked files and the recorded fixture. It runs the entire `tests/` tree using `coverage run -m tests.run --assert=plain -n 4 --dist loadgroup --max-worker-restart=0 -q`, writes JUnit/profile/coverage outside Git, and records its exact command and environment. Do not use its legacy `--selection` argument to infer a restricted test selection: the executed path is all native tests.

The admitted historical run produced **7,388 passed, zero failed and three skipped**, with 7,391 collected/executed and four reconciled worker receipts. Skips are one explicit CUDA integration test and two opt-in TabPFN model tests. Leave those optional gates unchanged when reproducing this scope. Some native tests fetch floating public recorded data, so matching the source pin alone does not freeze every downloaded byte. The independent probes and performance campaigns instead bind the retained fixture hash.

The runtime profile reports 160.391127 seconds; launcher/JUnit timings cover different wrappers. This is regression-suite evidence, not a before/after speed ratio. The original 1,771-test curated baseline has a different scope, so do not interpret the pass-count ratio as suite growth. [Academic membership and raw-artifact hashes](academic/native-suite-academic-evidence.json)

## 4. Performance replay and archived path bindings

The archived performance drivers load preregistrations containing absolute source, interpreter, overlay and setup-manifest paths under `/workspace/scratch/008a76ec4981`. Those original plans are immutable records, not portable configuration templates. Do not edit their paths in place or replace the original benchmark catalog to admit the latest source.

The actual executed driver commands, from the historical benchmark repository root, were:

```text
.work/envs-baseline/limen/bin/python updates/2026-10-29-limen/performance/run_paired_replay.py --mode run --output updates/2026-10-29-limen/performance/paired-campaign
.work/envs-baseline/limen/bin/python updates/2026-10-29-limen/performance/run_native_replay.py --output updates/2026-10-29-limen/performance/native-campaign
```

They are shown as execution provenance, not commands to overwrite those directories. The earlier `--mode verify` preflight was functional evidence without admitted timings. The timed campaigns ran on native Linux after test/probe workloads had stopped. Keep fresh comparative timings isolated from test, installation and other benchmark workloads.

The paired campaign uses the 16 frozen benchmark Python files byte-for-byte in two source-specific overlays. It runs five process blocks per revision/strategy, each with one first call and nine warm calls, separate preflight, source/install identity, independent parity, and observed one-thread native pools including Polars. The native campaign invokes the original snapshot and factorized-preparation harnesses from each admitted source checkout. Their outputs and time conventions remain separate; no core-only duration receives a full-engine ratio.

For a fresh location, use the preparation helper with the paired core environments from section 1, including their identical hashed LightGBM extension. Environment basenames must remain `limen`, because the frozen CLI resolves `<env-root>/limen/bin/python`.

```bash
python3 "$LIMEN_UPDATE/performance/prepare_replay.py" \
  --benchmark-root "$LIMEN_BENCH" \
  --baseline-source "$LIMEN_WORK/Limen-baseline" \
  --latest-source "$LIMEN_WORK/Limen" \
  --baseline-env "$LIMEN_WORK/envs-baseline/limen" \
  --latest-env "$LIMEN_WORK/envs-latest/limen" \
  --output "$LIMEN_OUTPUT/performance"

"$LIMEN_BASE_PY" "$LIMEN_OUTPUT/performance/run_paired_replay.py" \
  --mode verify --output "$LIMEN_OUTPUT/performance/preflight"
"$LIMEN_BASE_PY" "$LIMEN_OUTPUT/performance/run_paired_replay.py" \
  --mode run --output "$LIMEN_OUTPUT/performance/paired-campaign"
"$LIMEN_BASE_PY" "$LIMEN_OUTPUT/performance/run_native_replay.py" \
  --output "$LIMEN_OUTPUT/performance/native-campaign"
```

Preparation admits Linux Python **3.12.14**, exact pinned clean source checkouts, noneditable source distributions, original dependency inventory, fixture/harness hashes and frozen benchmark Python. It emits new catalogs, install manifests and preregistrations with location-correct identities. It does not install packages, execute engines or modify original records. Preparation-only checks were exercised on the archived installed environments; they are not new timed campaigns. A rejected dependency inventory must be resolved explicitly, not bypassed or relabelled as the original installation.

The native inner commands are retained in `native_report.json`: `python -m tests.benchmark_factorized_preparation --output ...`, and `python -m tests.benchmark_backtest_strategies --inputs <pinned-fixture> --output ... --strategies buy_and_hold sma_cross --engines limen --repeats 7`, each with the respective pinned source checkout as working directory. Their repetition counts differ from the paired external harness.

## 5. Inspect retained results without running an engine

This standard-library check reads the recorded JSON and independently recomputes aggregate arithmetic. It checks source/fixture/runner bindings, 20 preflight and 20 measured worker completions, 200 full timed samples, 200 separate diagnostic samples, recorded thread-pool observations and both revision ratios. It does not re-execute the oracle or make unobserved native cash/quantity/fee fields observable.

```bash
python3 "$LIMEN_UPDATE/academic/verify_paired_report.py" \
  --campaign "$LIMEN_UPDATE/performance/paired-campaign" \
  --output "$LIMEN_OUTPUT/archived-paired-report-check.json"
```

Run the checker normally, without Python's `-O` optimization, because its checks use assertions. Ratios are current versus baseline aggregate median durations on the same host, not paired confidence intervals or comparisons with historical competitor timings. [Independent retained check](academic/paired-report-independent-check.json)

Binary NPZ/gzip evidence is also preserved in [binary-evidence.tar.xz](binary-evidence.tar.xz), with every member listed in [binary-evidence-manifest.json](binary-evidence-manifest.json). The archive SHA256 is **768c8d6d71204b642000a7762688770b967069c5a2ff9e8ad2040a563e84b7bb**: 230 members, 913,240 compressed bytes and 38,022,408 uncompressed bytes. Extract into a new directory, then verify every member against the manifest; archive member paths are relative to this update's root. This restores archived bytes, not new measurements.

```bash
python3 - "$LIMEN_UPDATE" "$LIMEN_OUTPUT/restored-binaries" <<'PY'
from hashlib import sha256
import json
from pathlib import Path
import sys
import tarfile
update, output = map(Path, sys.argv[1:])
manifest = json.loads((update / 'binary-evidence-manifest.json').read_text())
archive = update / manifest['archive']
expected = '768c8d6d71204b642000a7762688770b967069c5a2ff9e8ad2040a563e84b7bb'
if sha256(archive.read_bytes()).hexdigest() != expected:
    raise SystemExit('Archive identity differs')
output.mkdir(parents=True, exist_ok=False)
with tarfile.open(archive, 'r:xz') as handle:
    handle.extractall(output, filter='data')
for member in manifest['members']:
    path = output / member['path']
    if path.stat().st_size != member['bytes'] or sha256(path.read_bytes()).hexdigest() != member['sha256']:
        raise SystemExit('Member identity differs: ' + member['path'])
print('Verified', len(manifest['members']), 'archived members')
PY
```

Keep the native test pass/coverage result, independent boundary probes, source inspection, upstream CI status and timing measurements distinct. The current local test pass does not change the upstream hosted runtime-budget failure, and passing software tests does not establish independent economic generalization.
