# Vaquum / Backtest Benchmark

A repeatable, **code-only** comparison of backtesting implementations against a frozen **Vaquum/Limen** baseline, across computation performance, academic rigor/robustness and safety properties.

**Start with the [comparison overview](reports/overview.md), the [546-cell systematic grid](reports/comparison-grid.md), and the [measured execution results](reports/performance-results.md).** Every grid cell identifies its native/adapter scope, enforcement status, evidence type, limitation and exact executable-source revision. The [CSV](reports/assessment-grid.csv) and [JSON](reports/assessment-grid.json) preserve the complete grid for filtering and subsequent comparisons.

**29 October 2026 — [Limen reassessment at `25e4786`](updates/2026-10-29-limen/README.md):** all 42 Limen criteria reviewed, five priority repairs independently checked, baseline/current timings repeated on the same host, and the full current native suite executed. The original cross-platform comparison remains frozen; the update includes its own evidence and repeat instructions.

This repository contains an assessment and a runnable benchmark. It does not assign an overall quality score, substitute documentation for implementation, or rank a failed/unsupported/unmeasured case as zero. A complete grid is not a claim that every source path, market regime or deployment has been tested.

## What is included

The source-assessed cohort has 13 implementations: **Limen, LEAN, Backtrader, vectorbt public-source edition, backtesting.py, Zipline-reloaded, Freqtrade, NautilusTrader, bt, QSTrader, hftbacktest, Qlib and Jesse**. Their full commits and observed licenses are in [the source catalog](catalog/candidates.json). The original Limen baseline is retained at `29837e666604eee74a2ac94f328fb9803724342a`; its earlier code assessment and evidence are preserved under [baseline/limen](baseline/limen/).

| Comparison layer | Admitted scope |
|---|---|
| Full native public API replay | Limen snapshot, Backtrader Cerebro, vectorbt Numba `from_signals`, backtesting.py `FractionalBacktest`, bt `Backtest` |
| Native components under an explicit benchmark driver | QSTrader `SimulatedBroker`/Portfolio; Qlib Exchange/Position. These receive **no full-engine Limen timing ratio**. |
| Code assessment and source setup; matching execution unmeasured | LEAN, Zipline-reloaded, Freqtrade, Jesse |
| Current native source assessed; build limit retained | Nautilus v2: two native test compilation attempts hit the declared 720/480-second limits. No runtime speed or native test pass is inferred. |
| Separate recorded-depth contract needed | hftbacktest: 22 native library tests passed; no fabricated order book or false hourly-OHLC timing. |

The original commercial list also included TradingView, TrendSpider, MetaTrader 5, NinjaTrader, TradeStation, AmiBroker, MultiCharts, Portfolio123, Portfolio Visualizer and StrategyQuant/X. No inspectable engine implementation was admitted for those products, so they remain in the [exclusion and re-entry register](catalog/exclusions.json), without a behavioral quality judgment. QuantConnect's hosted service and vectorbt PRO are separate from the admitted engine sources. Zipline-reloaded is the selected lineage, not a finding about every fork.

The five additions broaden the scientific comparison: bt/QSTrader cover portfolio workflows, Qlib covers model research, Jesse adds another crypto research/execution platform, and hftbacktest covers order-book/latency replay. This is a bounded cohort, not an exhaustive list of every public project.

**Licensing distinction:** the admitted vectorbt source has Apache 2.0 plus Commons Clause 1.0. It is labelled public-source, not unrestricted open source. Third-party source, dependencies and data retain their own terms; this repository's MIT license covers its own contributions.

## What the numbers mean

The recorded common workload uses one instrument, unchanged hourly prices, initial cash 1,000,000, continuous units, long/flat buy-and-hold and 50/200 SMA crossover decisions, at least one bar of decision-to-fill delay, zero costs and a predeclared terminal exit. It evaluates 8,783 observations and uses one additional unchanged real bar for settlement. No impact, queue priority, partial fills, funding, borrow, corporate actions or market-calendar model is implicit.

An independent cash/quantity oracle checks every timestamp, holding state, equity observation and fill bar/side/price, plus every native optional ledger field exposed by an adapter. Missing cash/quantity fields are disclosed; oracle values are not relabelled as engine output. Limen's snapshot has a return/holding trace rather than a native order cash/quantity ledger, and its fills are reconstructed from native exposure transitions.

The canonical campaign uses five independent process blocks, each with one first call and nine warm calls, after separate untimed preflight. It freezes code hashes, source revisions, dependencies, named native compute-pool limits of one and per-process JIT cache state. Loaded BLAS and Polars pools are observed before execution and after every call; missing required observation or a pool exceeding one rejects admission. This is not a claim that a process has only one operating-system thread. Order rotates/mirrors between cases. The warm summary is the median of the five process medians; every raw call and the process-median range are retained. No outliers are discarded, and no precise confidence interval or p95 guarantee is claimed from five processes on one host.

The [original campaign](results/campaigns/2026-10-19-common-zero-original/) is preserved with its exact runner and raw observations. It omitted Polars' separate pool control; a post-campaign diagnostic under the same settings observed nine Polars threads, while the original workers had not recorded that count. It is superseded for controlled comparisons. Only the separately preregistered corrective campaign, `2026-10-19-common-zero-single-thread`, feeds the headline tables.

Public APIs perform different native extra work. Native statistics, validation and lazy output materialization stay in their declared timing scopes. These results compare admitted public API workloads, not equal-instruction kernels or complete research campaigns. The common SMA is computed outside engine timing, so it is not an indicator-speed benchmark. A separate costed preflight admits vectorbt and Qlib at 5-bps fee plus 5-bps slippage; it does not invent a compatible costed Limen speed comparison.

Read the [complete protocol](protocol/README.md) for equations, tolerances, timing boundaries, memory limits, evidence definitions and how to add a solution. The [academic analysis](reports/academic-analysis.md) and [safety analysis](reports/safety-analysis.md) explain the consequential code findings and their scope.

## Run it

The captured runner is **Linux / Python 3.12.14**, using `uv 0.12.23`, separate engine environments, fixed named compute-pool settings and observed loaded-pool admission. POSIX process groups and Linux RSS semantics are used. Other platforms/versions require a separately recorded environment; Windows support is not asserted.

From a local clone, with Python 3.12, Git, `uv`, and a C/C++ compiler available:

```bash
git clone https://github.com/Vaquum/Backtest-Benchmark.git
cd Backtest-Benchmark

uv venv --python python3.12 .venv
uv pip install --python .venv/bin/python --require-hashes -r locks/runner.txt
uv pip install --python .venv/bin/python --no-deps --no-build-isolation -e .

.venv/bin/python scripts/fetch_sources.py --include-auxiliary
.venv/bin/python scripts/download_data.py
.venv/bin/python scripts/bootstrap_core.py --cc cc --cxx c++
.venv/bin/python scripts/bootstrap_extra.py --only qlib
```

Sources are fetched at the full catalog commits, not floating branches. Existing divergent or tracked-modified sources are refused. The fixture is downloaded by immutable URL and SHA-256; its bytes are not vendored here. Hash-locked dependencies install separately for each engine because their compatible numerical stacks differ. Source build attempts, selected manifests and imported-code fingerprints are retained.

Run the read-only evidence gate, harness controls and a small untimed parity pass first:

```bash
.venv/bin/python scripts/validate_assessment.py --sources .work/sources
.venv/bin/python -m pytest -q
.venv/bin/python -m bench verify \
  --input .work/data/recorded_spot_1h_2024.parquet \
  --expected-sha256 a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72 \
  --output .work/runs/my-preflight \
  --engines limen backtrader vectorbt backtesting_py bt qstrader qlib \
  --strategies buy_and_hold sma_cross flat --rows 999
```

Then stop other local builds/workloads and run the captured full contract. Every output directory must be new; prior evidence is not overwritten.

```bash
.venv/bin/python -m bench run \
  --input .work/data/recorded_spot_1h_2024.parquet \
  --expected-sha256 a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72 \
  --output .work/runs/my-full-campaign \
  --engines limen backtrader vectorbt backtesting_py bt qstrader qlib \
  --strategies buy_and_hold sma_cross --rows 8783 \
  --processes 5 --warm-repeats 9 --diagnostic-core

.venv/bin/python scripts/validate_assessment.py \
  --sources .work/sources --campaign .work/runs/my-full-campaign/report.json \
  --require-native-thread-policy
```

The runner emits raw process/worker results, input and code hashes, native provenance, all timing calls, parity outcomes, common result arrays and scalar CSV/JSON summaries. Published campaign copies omit market arrays/JIT caches with explicit hash inventories; local reruns regenerate them from the pinned input.

### Additional source checks and probes

```bash
.venv/bin/python scripts/bootstrap_extra.py --only freqtrade zipline jesse
.venv/bin/python scripts/bootstrap_native.py
.venv/bin/python scripts/run_native_checks.py \
  --output .work/native-checks/my-run --timeout 900
```

The native toolchain capture is Linux x86-64 only. Its script verifies official archive hashes before local installation. Native checks use pinned Cargo/NuGet resolution and retain build/test/timeout outcomes. A larger native build budget may complete where the captured Nautilus attempts timed out; that is a new result, not a retroactive pass for this campaign.

Bounded reproductions live in [scripts/probes](scripts/probes/) and [baseline/limen/scripts](baseline/limen/scripts/). Use each script's `--help` for its explicit source, interpreter/assembly, fixture and new output path. The new probes validate admitted source/data identity before native work and refuse overwrites. The original Limen kit validates its own frozen source/fixture. The current probe wrapper code is stronger than its original run wrapper; before/after script hashes and unchanged original result hashes are [retained](results/probes/probe_admission_revision.json).

## Read, extend and regenerate the assessment

```bash
.venv/bin/python scripts/render_report.py
.venv/bin/python scripts/compare.py --candidate qlib
```

`compare.py` prints a 42-criterion Limen-versus-candidate grid with native scope and code links. Add a candidate's fixed source identity, lawful reproducible setup, all 42 scoped assessment cells and an honest adapter; unknowns stay explicit until reviewed/measured. The [validator](scripts/validate_assessment.py) checks catalog/criterion coverage, exact pinned source references and campaign arithmetic/admission separation. Its structural/source-link checks do not replace semantic code review.

New quantitative evidence should receive a new campaign identity. Validate it, stage the reviewed evidence beneath `results/`, run `scripts/register_campaign.py --campaign results/<new-id>/report.json --id <new-id>`, and regenerate the reports. This updates only the relevant quantitative cells and preserves their historical baseline context. Publish the new source/data/environment identity together with the results.

## Repository map

| Path | Purpose |
|---|---|
| `catalog/` | Pinned candidate/dependency/toolchain/data identities, exclusions and campaign index |
| `protocol/` | 42 generic criteria and the repeatable evidence/execution/research/safety contracts |
| `assessment/` | Canonical 546 scoped cells and preserved Limen baseline |
| `bench/` | Independent oracle, recorded-data reader, native adapters, provenance and process runner |
| `scripts/` | Source/dependency setup, bounded probes, validation and report generation |
| `locks/` | Hashed Python dependency locks and native package/toolchain resolution |
| `results/` | Actual campaigns, failed/successful setup attempts, bounded probes and verification evidence |
| `reports/` | Generated overview, quantitative tables, full grid, 13 candidate dossiers and detailed axis analyses |
| `baseline/limen/` | Prior canonical Limen review and original reproduction kit, kept separate from new timings |

The assessment is finite and evidence-linked. It is not a full security audit, proof of statistical calibration, claim of future profitability, or certification of any live deployment. Its purpose is to make each comparison inspectable, falsifiable and repeatable.
