#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import classify, choose_route
p=argparse.ArgumentParser(); p.add_argument("tasks"); p.add_argument("expected"); p.add_argument("--config",required=True); a=p.parse_args()
tasks={x["id"]:x for x in (json.loads(s) for s in Path(a.tasks).read_text(encoding="utf-8-sig").splitlines() if s.strip())}
expected={x["id"]:x for x in (json.loads(s) for s in Path(a.expected).read_text(encoding="utf-8-sig").splitlines() if s.strip())}
config=json.loads(Path(a.config).read_text(encoding="utf-8-sig")); failures=[]
for task_id,task in tasks.items():
    c=classify(task); r=choose_route(c,config); e=expected[task_id]
    if c["risk"]!=e["risk"] or r["agent_role"]!=e["model_role"]: failures.append({"id":task_id,"risk":c["risk"],"agent_role":r["agent_role"],"expected":e})
print(json.dumps({"passed":len(tasks)-len(failures),"total":len(tasks),"failures":failures},ensure_ascii=False,indent=2)); raise SystemExit(0 if not failures else 1)


