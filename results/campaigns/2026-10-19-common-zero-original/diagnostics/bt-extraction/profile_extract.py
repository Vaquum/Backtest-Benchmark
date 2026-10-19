"""One post-campaign attribution profile; not a comparative timing sample."""
import argparse
import cProfile
from hashlib import sha256
import io
import json
from pathlib import Path
import pstats
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root', type=Path, required=True)
parser.add_argument('--campaign', type=Path, required=True)
parser.add_argument('--manifest', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(args.root.resolve()))
import numpy as np
from bench.adapters import create_adapter
from bench.contract import Contract, assert_parity, reference_result
from bench.data import array_digest
from bench.provenance import verify_source_install, verify_import_location, runtime_environment

campaign = json.loads((args.campaign / 'report.json').read_text())
for name, value in campaign['benchmark_code_sha256'].items():
    assert sha256((args.root / name).read_bytes()).hexdigest() == value, name
provenance = verify_source_install('bt', args.root.resolve(), args.manifest.resolve())
prepared = args.campaign / 'prepared-buy_and_hold.npz'
assert sha256(prepared.read_bytes()).hexdigest() == campaign['scenarios']['buy_and_hold']['prepared_file_sha256']
with np.load(prepared, allow_pickle=False) as loaded:
    data = {key: loaded[key] for key in loaded.files}
contract = Contract.from_dict(campaign['contract'])
expected = reference_result(data, contract)
adapter = create_adapter('bt', data, contract)
provenance['observed_candidate_imports'] = verify_import_location('bt')
native = adapter.run()
profile = cProfile.Profile()
actual = profile.runcall(adapter.extract, native)
parity = assert_parity(actual, expected, contract)
output = io.StringIO()
statistics = pstats.Stats(profile, stream=output).sort_stats('cumulative')
statistics.print_stats(60)
(args.output / 'profile.txt').write_text(output.getvalue())
rows = []
for (file, line, function), (primitive, calls, self_seconds, cumulative_seconds, callers) in statistics.stats.items():
    rows.append(dict(file=file, line=line, function=function, primitive_calls=primitive,
                     total_calls=calls, self_seconds=self_seconds, cumulative_seconds=cumulative_seconds))
rows.sort(key=lambda row: row['cumulative_seconds'], reverse=True)
result = {'status': 'verified', 'scope': 'One cProfile attribution of frozen bt adapter extraction after one native run; profiler overhead applies; not a campaign sample or speed ranking',
          'campaign_report_sha256': sha256((args.campaign / 'report.json').read_bytes()).hexdigest(),
          'prepared_arrays_sha256': array_digest(data), 'provenance': provenance,
          'runtime': runtime_environment(), 'parity': parity, 'functions': rows}
(args.output / 'profile.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
print(json.dumps({'status': result['status'], 'profile_functions': len(rows), 'top_functions': rows[:8]}, indent=2))
