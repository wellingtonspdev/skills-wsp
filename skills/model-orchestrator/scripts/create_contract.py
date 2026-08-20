#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import load_json
p=argparse.ArgumentParser(); p.add_argument('task'); p.add_argument('route'); p.add_argument('protocol'); p.add_argument('--output',required=True); a=p.parse_args()
t=load_json(a.task); r=load_json(a.route); proto=load_json(a.protocol)
required=['task_id','objective','allowed_files','denied_files','acceptance_criteria','validation_commands','max_attempts','cost_limit_usd','escalation_conditions']
missing=[x for x in required if x not in t]
if missing: raise SystemExit('blocked: contract inputs missing: '+','.join(missing))
contract={"schema_version":1,"task_id":t['task_id'],"function":t.get('function','development_worker'),"objective":t['objective'],"context_minimum":t.get('context_minimum',''),"allowed_files":t['allowed_files'],"denied_files":t['denied_files'],"acceptance_criteria":t['acceptance_criteria'],"validation_commands":t['validation_commands'],"max_attempts":min(t['max_attempts'],r['max_attempts']),"cost_limit_usd":min(t['cost_limit_usd'],r['cost_limit_usd']) if r['cost_limit_usd'] else 0,"escalation_conditions":t['escalation_conditions'],"handoff_format":{"required":["HANDOFF.md","STATUS.json"]},"harness":r['harness'],"provider":r['provider'],"model":r['model'],"surface":proto['surface'],"a2a_allowed":proto['a2a_allowed'],"worktree":t.get('worktree')}
Path(a.output).write_text(json.dumps(contract,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(contract,ensure_ascii=False,indent=2))