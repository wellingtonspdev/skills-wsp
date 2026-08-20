#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import choose_surface, dump, load_json
p=argparse.ArgumentParser(); p.add_argument('task'); p.add_argument('capabilities'); p.add_argument('--output',required=True); a=p.parse_args()
r=choose_surface(load_json(a.task),load_json(a.capabilities)); Path(a.output).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8'); dump(r)