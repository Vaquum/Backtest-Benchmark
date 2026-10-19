# Limen code assessment: reproducibility kit

This kit preserves the evidence for the code assessment of **Vaquum/Limen 5.40.1**, commit **`29837e666604eee74a2ac94f328fb9803724342a`**, assessed on 19 October 2026. It contains the comparison baseline, original local reports and logs, every benchmark sample, and portable scripts for repeating the bounded probes and selected test campaign. Candidate fields remain empty because no competitor was assessed.

## Contents and evidence scope

| Location | Contents |
| --- | --- |
| `baseline/limen_baseline.json` | Unified 42-criterion grid, 28 measurement rows, pinned code references, comparison protocol and blank candidate fields |
| `baseline/criteria.csv`, `baseline/measurements.csv`, `baseline/evidence.csv` | Portable exports derived from the unified baseline |
| `baseline/protocol.json` | Comparison protocol extracted from the unified baseline |
| `report/Limen_Code_Assessment_complete.md` | Complete assessment text, criterion inventory and source index |
| `evidence/performance/` | Original benchmark logs, complete JSON/CSV reports, both factorization arms, and all snapshot timing samples |
| `evidence/academic/` | Original prefix-probe JSON and the original source script |
| `evidence/safety/` | Original bounded boundary-probe JSON and the original source script |
| `evidence/tests/` | Initial command manifest, stdout log, JUnit, runtime profiles, original coverage reports, three-case retest evidence and setup history |
| `environment/` | Exact committed research requirement lock/configuration, fixture and source hashes, supplemental observed runtime inventory |
| `scripts/` | Portable runners accepting `--repo-root` and `--output` |

`baseline/limen_baseline.json` is the sole canonical criteria/status record. CSV and protocol files are derived exports. Unreconciled reviewer drafts and earlier criterion versions are excluded. Original observed evidence files retain their original absolute paths and timestamps. Portable scripts are separate derivatives; they add path arguments, source/fixture checks and fresh output directories without changing the probe calculations. They were syntax-checked and their help interfaces inspected during packaging; the scientific probes, benchmarks and expensive tests were **not rerun** for packaging. The repository benchmark code is supplied by the pinned clone, and the portable benchmark runner invokes those exact modules.

The kit excludes the repository, virtual environment, fixture copies, generated prepared-market arrays, large round-data blobs and temporary test projects. Obtain the recorded input from the pinned clone and verify its hash. Matching committed bytes does not independently authenticate upstream market provenance.

`CHECKSUMS.sha256` inventories every other packaged file. After extracting the archive, run `sha256sum -c CHECKSUMS.sha256` from the extracted kit directory to check its contents. These checksums detect accidental alteration; they are not an independent publisher signature.

## Reconstruct the dependency setup

Use a new workspace **outside every existing Git checkout** so test temporary projects cannot inherit another repository. The following is a reproducible setup reconstruction, not a retained transcript of the original installation. Git, Bash and `uv` are prerequisites; the observed `uv` version was 0.12.23. The measured interpreter was CPython 3.12.14 on Linux x86_64.

```bash
LIMEN_KIT="/absolute/path/to/repro-kit"
LIMEN_WORK="/absolute/path/to/new-limen-review"
mkdir -p "$LIMEN_WORK"
LIMEN_REPO="$LIMEN_WORK/source"
LIMEN_ENV="$LIMEN_WORK/venv"

git clone --no-checkout https://github.com/Vaquum/Limen.git "$LIMEN_REPO"
git -C "$LIMEN_REPO" checkout --detach 29837e666604eee74a2ac94f328fb9803724342a

uv python install 3.12.14
uv venv --python 3.12.14 --seed "$LIMEN_ENV"
"$LIMEN_ENV/bin/python" -m pip install \
  'pip==26.2.1' 'setuptools==84.0.0' 'wheel==0.48.0'
cmp "$LIMEN_REPO/requirements/ci/research-env.txt" "$LIMEN_KIT/environment/research-env.txt"
"$LIMEN_ENV/bin/python" -m pip install --require-hashes \
  -r "$LIMEN_REPO/requirements/ci/research-env.txt"
"$LIMEN_ENV/bin/python" -m pip install --no-deps --no-build-isolation -e "$LIMEN_REPO"

cd "$LIMEN_REPO"
sha256sum -c "$LIMEN_KIT/environment/fixture.sha256"
```

The research dependencies are version- and hash-pinned by the committed lock. The explicitly listed bootstrap/build-tool versions reproduce the observed tool versions; their installer artifacts are not vendored here. The original virtual environment enabled system site packages, so it was **not hermetic**. Relevant NumPy, pandas, Polars, scikit-learn, SciPy, LightGBM, pytest and coverage imports were verified inside the measured venv; build tools resolved from its parent runtime. `environment/observed_runtime.json` preserves that configuration, import paths and duplicate visible distribution metadata. The clean-venv recipe makes that dependency boundary explicit; it is not a claim to reproduce the entire original host image or identical timings.

The primary recorded fixture has 8,784 rows and SHA-256:

```text
a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72
```

## Repeat the two benchmark harnesses

Run timing work sequentially with other tests and probes idle. The portable runner sets the recorded explicit thread environment, runs fitted preparation first, and then runs only Limen on the two fixed-signal scenarios with **seven warm repetitions**:

```bash
"$LIMEN_ENV/bin/python" "$LIMEN_KIT/scripts/run_benchmarks.py" \
  --repo-root "$LIMEN_REPO" --output "$LIMEN_WORK/new-benchmarks"
```

For direct invocation, the corresponding existing harness commands are:

```bash
cd "$LIMEN_REPO"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1 BLIS_NUM_THREADS=1 POLARS_MAX_THREADS=1
export NUMEXPR_NUM_THREADS=1 PYTHONHASHSEED=0

"$LIMEN_ENV/bin/python" -m tests.benchmark_factorized_preparation \
  --output "$LIMEN_WORK/direct-factorized"

"$LIMEN_ENV/bin/python" -m tests.benchmark_backtest_strategies \
  --inputs "$LIMEN_REPO/tests/fixtures/spot_1h_20240101_20241231.parquet" \
  --output "$LIMEN_WORK/direct-backtest" \
  --strategies buy_and_hold sma_cross --engines limen --repeats 7
```

The wrapper is preferable when retaining new logs because it saves complete stdout/stderr, exact command arrays and exit codes. Direct and wrapper examples are alternatives; do not run both unless deliberately collecting another repetition.

The preserved snapshot results cover 8,783 evaluated bars plus a final real settlement bar: zero fees/slippage, all-in long/flat, close timing and one-bar lag. The cash-and-quantity replay checks every equity sample, held state and fill. Warm full-snapshot medians were **2.150025 ms** for buy and hold and **1.699665 ms** for SMA crossover. The SMA **7.946189 ms** observation is retained. These seven within-process observations do not establish a tail-latency guarantee.

The fitted-preparation experiment was **one fixed-order pair**, 48 terminal rounds per arm. Both arms enabled factorization; only fitted-target/scaler reuse differed. Target and scaler fits fell from 24 to 1 while model fits stayed at 24. Complete-process times were **10.552470680 s** and **10.597700401 s**, giving fresh/reuse **0.995732119**. The outputs matched at 12 decimals. This establishes the narrow reuse mechanism and parity, with no demonstrated end-to-end speed gain. Do not add nested preparation and target/scaler stage spans or treat 24-to-1 fewer fits as a system speed ratio.

## Repeat bounded academic and safety probes

```bash
"$LIMEN_ENV/bin/python" "$LIMEN_KIT/scripts/causal_prefix_probe.py" \
  --repo-root "$LIMEN_REPO" --output "$LIMEN_WORK/new-prefix-probe"

"$LIMEN_ENV/bin/python" "$LIMEN_KIT/scripts/reproduce_safety_boundaries.py" \
  --repo-root "$LIMEN_REPO" --output "$LIMEN_WORK/new-safety-probes"
```

The prefix probe compares an unchanged 192-row recorded prefix with the same prefix calculated inside 384 rows at `rtol=atol=1e-12`. The preserved nonzero-quantile case changed **173/192 earlier rows**; ordinary price lines and zero-quantile controls changed zero. This is a counterexample for the specified configuration, not a population failure-rate estimate or a measure of backtest inflation.

The safety script checks a resolver's callable identity without invoking that callable, direct snapshot admission versus event-policy admission, and manifest URI integrity after a metadata mutation in a disposable local store. It disables remote store backup. Repository files are untouched. The original results show prefixed `os.system` resolution/compilation, acceptance of negative direct snapshot costs, and stale URI resolution. The unbounded fractional-difference finding is supported by code inspection; this script does not invoke that loop.

## Repeat the selected test campaign

```bash
"$LIMEN_ENV/bin/python" "$LIMEN_KIT/scripts/run_selected_tests.py" \
  --repo-root "$LIMEN_REPO" --output "$LIMEN_WORK/new-selected-tests"

# Optional independent execution of only the three historical setup-failure cases:
"$LIMEN_ENV/bin/python" "$LIMEN_KIT/scripts/run_selected_tests.py" \
  --repo-root "$LIMEN_REPO" --output "$LIMEN_WORK/new-three-cases" \
  --selection retest3
```

These are new executions with fresh coverage databases. The original run contained 1,771 distinct tests across 82 selected modules: 1,768 passed initially, then all three setup failures passed after editable installation and external temporary-directory correction. Only those three were rerun: **1,771 distinct tests have passing executions across two runs**, totaling 1,774 executions. This is not a full-suite, clean single-campaign or hosted-CI claim. See `evidence/tests/setup_and_retest.md` for the failures, evidence boundaries and the unavailable original retest command transcript. Original JUnit/runtime files and both coverage JSON files are preserved verbatim.

## Use the comparison baseline

Freeze the candidate commit, configuration, outputs, economics, data and resource limits before comparing. Require temporal validity and numerical/ledger parity before ranking speed. Record unsupported required capabilities explicitly, preserve unknowns, separate startup/core/full-pipeline/persistence scopes, and collect fresh paired runs of **both** solutions on the same host. The proposed repeated-comparison protocol in the unified JSON has not already been executed. This kit provides no competitor score, broad speed ranking or aggregate safety/quality grade.
