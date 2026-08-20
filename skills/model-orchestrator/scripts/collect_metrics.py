#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import dump
REQUIRED={"model","provider","agent","attempts","changed_files","commands","input_tokens","output_tokens","total_cost","duration_seconds","failures","fallback","objective_verdict","executor","reviewer"}
p=argparse.ArgumentParser(); p.add_argument("runs"); p.add_argument("--output"); a=p.parse_args()
rows=[json.loads(x) for x in Path(a.runs).read_text(encoding="utf-8-sig").splitlines() if x.strip()]
missing=[]
for r in rows:
    absent=sorted(REQUIRED-set(r))
    if not isinstance(absent,list) or any(not isinstance(x,str) for x in absent): raise SystemExit("blocked: missing_fields must be a flat string list")
    missing.extend(absent)
missing=sorted(set(missing))
accepted=[r for r in rows if r.get("objective_verdict")=="accepted"]; cost=sum(float(r.get("total_cost",0) or 0) for r in rows)
result={"schema_version":2,"metrics_status":"valid" if not missing else "blocked","runs":len(rows),"accepted_tasks":len(accepted),"total_cost":cost,"cost_per_accepted_task":cost/len(accepted) if accepted else None,"missing_fields":missing}
if a.output: Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
dump(result); raise SystemExit(0 if not missing else 4)
