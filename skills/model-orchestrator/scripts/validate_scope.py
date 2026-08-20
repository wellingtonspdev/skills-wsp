#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path
from orchestrator_core import dump, path_matches, git_root
p=argparse.ArgumentParser(); p.add_argument("repo"); p.add_argument("--allow",action="append",required=True); p.add_argument("--deny",action="append",default=[]); p.add_argument("--worktree"); p.add_argument("--principal-repository"); p.add_argument("--output"); a=p.parse_args()
repo=Path(a.repo).resolve(); root=git_root(repo)
if a.worktree and repo != Path(a.worktree).resolve(): raise SystemExit("blocked: scope check repo differs from designated worktree")
if a.worktree and a.principal_repository and root and root==Path(a.principal_repository).resolve(): raise SystemExit("blocked: principal repository write forbidden")
run=subprocess.run(["git","-C",str(repo),"status","--porcelain","-z"],capture_output=True,text=True,check=True)
files=[(e[3:] if len(e)>3 else e).split(" -> ")[-1] for e in run.stdout.split("\0") if e]
unexpected=[x for x in files if not path_matches(x,a.allow)]; denied=[x for x in files if path_matches(x,a.deny)]
result={"schema_version":2,"scope_status":"valid" if not unexpected and not denied else "blocked","worktree":str(repo),"git_root":str(root) if root else None,"changed_files":files,"unexpected_files":unexpected,"denied_files":denied}
if a.output: Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
dump(result)
raise SystemExit(0 if result["scope_status"]=="valid" else 2)

