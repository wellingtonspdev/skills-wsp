#!/usr/bin/env python3
"""Operational Traycer CLI bridge. All calls use argv lists and fail closed."""
import argparse, json, os, shutil, subprocess
from pathlib import Path
from orchestrator_core import dump, load_json

def exe(config):
    configured=config.get('orchestration',{}).get('executable_path')
    return configured if configured and Path(configured).exists() else shutil.which(config.get('orchestration',{}).get('adapter_command','traycer'))

def call(config, args, timeout=60):
    command=exe(config)
    if not command: raise RuntimeError('blocked: Traycer CLI executable not found')
    r=subprocess.run([command,*args],capture_output=True,text=True,timeout=timeout,shell=False)
    if r.returncode: raise RuntimeError(f'Traycer CLI failed ({r.returncode}): {r.stderr.strip()[:500]}')
    return r.stdout

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config',required=True); p.add_argument('--context',required=True); p.add_argument('--route',required=True); p.add_argument('--contract',required=True); p.add_argument('--output',required=True); p.add_argument('--create-child',action='store_true'); a=p.parse_args()
    cfg=load_json(a.config); ctx=load_json(a.context); route=load_json(a.route)
    if route.get('decision_status')!='valid': raise SystemExit('blocked: invalid route artifact')
    if ctx.get('traycer_status')!='connected': raise SystemExit('blocked: Traycer context is not connected')
    version=call(cfg,['--version']).strip()
    agent_id=ctx.get('agent_id') or os.getenv('TRAYCER_AGENT_ID')
    identity={'agent_id':agent_id if agent_id else None,'display_name':ctx.get('display_name'),'parent_agent_id':ctx.get('parent_agent_id'),'epic_id':ctx.get('epic_id') or os.getenv('TRAYCER_EPIC_ID'),'harness':ctx.get('harness'),'requested_model':route.get('model'),'effective_model':None,'reviewer_agent_id':ctx.get('reviewer_agent_id'),'reviewer_display_name':ctx.get('reviewer_display_name'),'surface':route.get('surface') or ctx.get('surface'),'identity_status':'verified' if agent_id else 'unverified'}
    if identity['surface']=='terminal_tui' and ctx.get('send_a2a_after_launch'):
        raise SystemExit('blocked: A2A communication is unsupported for terminal_tui')
    if ctx.get('requires_verified_hierarchy') and identity['identity_status']!='verified':
        raise SystemExit('blocked: verified agent hierarchy is required')
    result={'schema_version':3,'traycer_registration_status':'valid','cli_version':version,'object_type':ctx.get('traycer_object_type','Task'),'task_id':ctx.get('traycer_task_id'),'identity':identity,'worktree':ctx.get('traycer_worktree'),'permissions':ctx.get('permissions',{}),'handoff_artifact':str(Path(a.contract).resolve()),'child_agent_required':route.get('route')!='codex_only','child_agent_created':False}
    if result['child_agent_required'] and a.create_child:
        epic=ctx.get('epic_id') or os.getenv('TRAYCER_EPIC_ID'); sender=identity['agent_id']
        if not epic or not sender: raise SystemExit('blocked: TRAYCER_EPIC_ID and TRAYCER_AGENT_ID are required for child creation')
        model=route['model'].replace('/',':',1) if route['model'].startswith('opencode/') else route['model']
        out=call(cfg,['agent','create','--json','--no-progress','--epic-id',epic,'--sender-agent-id',sender,'--harness','opencode','--surface',str(identity['surface'] or 'terminal'),'--model',model,'--cwd',str(ctx['traycer_worktree'])])
        payload=None
        for line in out.splitlines():
            try:
                obj=json.loads(line)
                if isinstance(obj,dict) and (obj.get('agent_id') or obj.get('id')): payload=obj; break
            except json.JSONDecodeError: continue
        if not payload: raise SystemExit('blocked: Traycer child creation returned no structured agent id')
        result['child_agent_created']=True; result['child_agent']={'agent_id':payload.get('agent_id') or payload.get('id'),'display_name':payload.get('name'),'harness':'opencode','requested_model':route['model'],'effective_model':payload.get('model')}
    if result['child_agent_required'] and not result['child_agent_created']: raise SystemExit('blocked: delegated route requires real Traycer child agent')
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); dump(result)
if __name__=='__main__': main()

