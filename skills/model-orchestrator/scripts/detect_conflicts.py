#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import detect_conflicts, dump, load_json
p=argparse.ArgumentParser(); p.add_argument('plan'); p.add_argument('--output',required=True); a=p.parse_args()
r=detect_conflicts(load_json(a.plan).get('tasks',[])); Path(a.output).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); dump(r); raise SystemExit(0 if r['parallelization_allowed'] else 5)