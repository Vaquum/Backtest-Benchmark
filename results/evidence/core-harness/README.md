# Core harness evidence

`campaign-preregistration.json` was written before the comparative timing campaign. It fixes the recorded input hash, 8,783 evaluated closes, seven adapters, two strategies, five independent processes per case, nine warm calls per process, cost assumptions, and execution order. It is a plan, not a claim that the measurements finished. Completed results are identified by their separate reports and successful parity gates.

The retained full-fixture preflight is `preflight/full-preflight-001/report.json`. All seven adapters passed its two strategy cases. Earlier attempts are retained with their original failures. QSTrader and Qlib execute native components through benchmark-owned replay drivers and cannot receive ratios against full frameworks. Limen emits native return/held arrays; its fills are inferred from segment boundaries, and it does not emit an independent native cash/quantity/order ledger. Available optional account fields are checked rather than manufactured.

The full engine intervals also contain different native extra work. Backtesting.py and bt calculate their native performance statistics inside their public run calls. Backtrader standard chart observers are disabled. Vectorbt account arrays are materialized during common extraction. Each report's engine scope and settings accompany its numbers. Limen's internal return kernel is a separate diagnostic.

## Preserved setup and harness corrections

| Earlier observed failure | Resolution before comparative timing |
|---|---|
| bt source extension build selected an unavailable `clang` executable. | Rebuilt the same frozen source using explicitly recorded GCC/G++ compiler overrides. |
| The first nonisolated backtesting.py wheel omitted the `autoscale_cb.js` resource loaded at import. | Installed the `setuptools_git` and `setuptools_scm` tools declared in its executable `setup.py`, then rebuilt the same source. The generated distribution version reflects the shallow checkout; the catalog commit identifies the code. |
| Untimed verify aggregation attempted to divide two null timing medians. | Required actual complete measured medians before computing any ratio; added a regression test. The first passed Limen worker and subsequent orchestration failure remain retained. |
| bt's native transaction helper indexed an empty security history in the flat control. | Explicitly registered the one native Security for every strategy case, including the flat case. No candidate code was edited. |

Current core source installation manifests and every build attempt are under `setup/`. The dependency files in the repository's `locks/` directory contain package hashes. The candidate itself is built separately from its catalog-pinned source. Workers verify the source revision, absence of tracked source changes, the built distribution's local source URL, installed code hashes, and actual imported module locations in a clean virtual environment.

`tests/` retains successive observed unit-test logs and JUnit XML. The final suite before the original campaign includes 26 tests: independent analytic cash/quantity checks on the recorded prices, prefix-causality checks, admission and parity mutations, incomplete-case and component-ratio guards, descendant-process timeout handling, and import-shadowing rejection. The unit-test runner's development interpreter is distinct from the isolated environments used for candidate measurements.

## Corrective native-pool campaign

After the original campaign, a fresh process using its same eight declared thread controls reported a nine-thread Polars pool. The original protocol omitted `POLARS_MAX_THREADS` and did not observe Polars' separate pool, so its blanket single-thread claim was not supported. The [original campaign and exact source snapshot](../../campaigns/2026-10-19-common-zero-original/) are retained as superseded-control exploratory evidence. Its numerical samples are not pooled with the replacement.

`corrective-campaign-preregistration.json` and `corrective-timing-clear.json` precede the separately executed [canonical corrective campaign](../../campaigns/2026-10-19-common-zero-single-thread/). Its worker fixes all nine environment controls, observes loaded BLAS and Polars pools before execution and after every call, and fails admission when observation is missing or a pool differs from one. `preflight/polars-corrective-preflight/` retains the observed full-data buy-and-hold, SMA, and flat checks with Polars pool size one. Its intermediate source snapshot is matched to the original preflight hashes and distinguished from the stricter final campaign snapshot.

The final corrective suite has 29 passing tests. Its first run exposed two test-context failures: the development runner had already initialized a multithreaded BLAS pool, so the new admission gate rejected that pool before the tests could exercise their intended Polars branch. Those test contexts now temporarily limit the actual loaded BLAS pool; the initial failures, successful retest, and final 29-test receipt are all retained. No candidate source was changed.

## Reproduction and retained files

Use the repository's bootstrap instructions to generate fresh local installation manifests, then the portable command in the preregistration. Absolute paths in historical logs and manifests record this observed run; they are not portable setup instructions. Every exported log, report and setup attempt is copied unchanged. Historical catalog descriptions inside an original setup manifest do not replace the current canonical catalog and its license records.

The real price arrays, full result-array files, and compiled Numba cache are not bundled in this public evidence directory. They remain in local working evidence; `retained-local-array-inventory.json` records the size and SHA-256 of each omitted array file. Recreate them from the separately supplied hash-pinned recorded fixture. New measured worker reports additionally fingerprint their actual result arrays. Market prices are never generated for the benchmark or its unit tests.
