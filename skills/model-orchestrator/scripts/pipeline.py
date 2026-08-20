#!/usr/bin/env python3
import argparse, json, subprocess, sys
from pathlib import Path
REQUIRED=["validate_config.py","preflight.py","classify_task.py","choose_route.py","sanitize_context.py","validate_scope.py","check_budget.py","collect_metrics.py","validate_contract.py","traycer_bridge.py"]
p=argparse.ArgumentParser()
for name in ["skill_root","context","task","config","classification","route","preflight","contract","contract_validation","traycer_registration","release_file","sanitized_file","sanitization_report","scope_report","ledger","metrics"]:
    p.add_argument("--"+name.replace("_","-"),required=True)
p.add_argument("--provider",required=True); p.add_argument("--repo",required=True); p.add_argument("--worktree"); p.add_argument("--principal-repository"); p.add_argument("--estimated-cost",type=float,default=0); p.add_argument("--allow",action="append",required=True); p.add_argument("--deny",action="append",default=[]); a=p.parse_args()
root=Path(a.skill_root).resolve(); config_path=Path(a.config).resolve();
if not config_path.is_file(): raise SystemExit(f"blocked: active configuration not found: {config_path}")
missing=[x for x in REQUIRED if not (root/"scripts"/x).is_file()]
if missing: raise SystemExit("blocked: missing mandatory scripts: "+",".join(missing))
def run(script,args):
    r=subprocess.run([sys.executable,str(root/"scripts"/script),*args],capture_output=True,text=True)
    if r.returncode: raise SystemExit(f"blocked: {script}: {r.stderr.strip() or r.stdout.strip()}")
run("validate_config.py",["--config",str(config_path)]); run("preflight.py",["--context",a.context,"--config",a.config,"--output",a.preflight]); run("classify_task.py",[a.task,"--output",a.classification]); run("choose_route.py",[a.classification,"--config",a.config,"--output",a.route])
route=json.loads(Path(a.route).read_text(encoding="utf-8"))
run("sanitize_context.py",[a.release_file,a.sanitized_file,"--report",a.sanitization_report,"--classification",a.classification,"--provider",a.provider])
scope=[a.repo]
for item in a.allow: scope += ["--allow",item]
for item in a.deny: scope += ["--deny",item]
if a.worktree: scope += ["--worktree",a.worktree]
if a.principal_repository: scope += ["--principal-repository",a.principal_repository]
scope += ["--output",a.scope_report]
run("validate_scope.py",scope); run("validate_contract.py",[a.contract,"--output",a.contract_validation]); run("check_budget.py",[a.ledger,"--config",a.config,"--estimated-cost",str(a.estimated_cost),"--route",route["route"],"--provider",route.get("provider","openai"),"--model",route.get("model") or ""]); run("collect_metrics.py",[a.ledger,"--output",a.metrics]); run("traycer_bridge.py",["--config",str(config_path),"--context",a.context,"--route",a.route,"--contract",a.contract,"--output",a.traycer_registration])
print(json.dumps({"pipeline_status":"ready_for_worker","preflight":a.preflight,"classification":a.classification,"route":a.route,"sanitization":a.sanitization_report,"scope":a.scope_report,"contract":a.contract_validation,"metrics":a.metrics,"traycer_registration":a.traycer_registration},ensure_ascii=False,indent=2))



