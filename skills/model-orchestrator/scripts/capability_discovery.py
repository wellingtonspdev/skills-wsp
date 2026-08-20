#!/usr/bin/env python3
import argparse, json, shutil, subprocess
from pathlib import Path
from orchestrator_core import dump, load_json

def run(exe,args):
    r=subprocess.run([exe,*args],capture_output=True,text=True,shell=False,timeout=60)
    return {"args":args,"returncode":r.returncode,"stdout":r.stdout[:12000],"stderr":r.stderr[:1000]}
p=argparse.ArgumentParser(); p.add_argument('--config',required=True); p.add_argument('--output',required=True); p.add_argument('--mock'); a=p.parse_args()
if a.mock:
    matrix=load_json(a.mock)
else:
    cfg=load_json(a.config); exe=cfg['orchestration'].get('executable_path') or shutil.which(cfg['orchestration'].get('adapter_command','traycer'))
    if not exe or not Path(exe).exists(): raise SystemExit('blocked: Traycer CLI unavailable')
    probes=[['--version'],['--help'],['agent','--help'],['agent','list-harnesses','--no-progress'],['agent','list-harness-models','opencode','--no-progress'],['agent','create','--help'],['agent','transcript','--help'],['worktree','create','--help']]
    evidence=[run(exe,x) for x in probes]
    all_text='\n'.join(x['stdout']+x['stderr'] for x in evidence).lower()
    matrix={"schema_version":1,"source":"runtime_cli","traycer_version":evidence[0]['stdout'].strip(),"harnesses":{"codex":{"available":"codex" in all_text},"opencode":{"available":"opencode" in all_text}},"surfaces":{"gui_chat":{"available":True,"a2a":"send" in all_text},"terminal_tui":{"available":True,"a2a":False}},"features":{"agent_create":"agent create" in all_text,"agent_transcript":"transcript" in all_text,"worktree_create":"worktree create" in all_text},"identity":{"agent_env_supported":True,"epic_env_supported":True},"evidence":[{"args":x['args'],"returncode":x['returncode']} for x in evidence]}
if matrix.get('surfaces',{}).get('terminal_tui',{}).get('a2a') is True: raise SystemExit('blocked: terminal_tui A2A must remain disabled unless protocol is redesigned')
Path(a.output).write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); dump(matrix)