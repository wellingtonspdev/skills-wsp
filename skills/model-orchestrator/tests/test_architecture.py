import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
from orchestrator_core import classify, choose_route, choose_surface, detect_conflicts, load_json
CFG=load_json(ROOT/'config/orchestrator.json'); CAP=load_json(ROOT/'tests/fixtures/capabilities.json'); RT=ROOT/'tests/runtime'
def task(**kw):
    base={"data_classification":"sanitized","signals":[],"estimated_files":1,"estimated_commands":1,"estimated_test_iterations":1,"estimated_modules":1,"objective_validation":True}; base.update(kw); return base
def main():
    codex=choose_route(classify(task(signals=['authorization'])),CFG); assert codex['route']=='codex_only' and codex['harness']=='codex'
    mimo=choose_route(classify(task()),CFG); assert mimo['harness']=='opencode' and mimo['provider']=='opencode' and mimo['model']=='opencode/mimo-v2.5-free' and mimo['max_attempts']==1
    deep=choose_route(classify(task(estimated_files=4)),CFG); assert deep['harness']=='opencode' and deep['provider']=='openrouter' and 'deepseek-v4-flash-0731' in deep['model']
    lag=choose_route(classify(task(estimated_files=6,estimated_commands=8,estimated_test_iterations=3,estimated_modules=2,signals=['repository_navigation','tool_intensive'])),CFG); assert lag['harness']=='opencode' and lag['provider']=='openrouter' and 'laguna-s-2.1' in lag['model']
    gui=choose_surface({'requires_a2a':True},CAP); assert gui=={'surface':'gui_chat','a2a_allowed':True,'protocol':'iterative'}
    tui=choose_surface({},CAP); assert tui['surface']=='terminal_tui' and not tui['a2a_allowed']
    bad=json.loads(json.dumps(CAP)); bad['surfaces']['gui_chat']['a2a']=False
    try: choose_surface({'requires_a2a':True},bad); assert False
    except ValueError: pass
    assert not detect_conflicts([{'task_id':'a','allowed_files':['x.py']},{'task_id':'b','allowed_files':['x.py']}])['parallelization_allowed']
    assert detect_conflicts([{'task_id':'a','allowed_files':['x.py']},{'task_id':'b','allowed_files':['y.py']}])['parallelization_allowed']
    contract_task={"task_id":"t1","objective":"controlled","allowed_files":["x.py"],"denied_files":[".env"],"acceptance_criteria":["pass"],"validation_commands":["python -m compileall ."],"max_attempts":1,"cost_limit_usd":0,"escalation_conditions":["failure"]}
    for name,obj in [('task.json',contract_task),('route.json',mimo),('protocol.json',tui)]: (RT/name).write_text(json.dumps(obj),encoding='utf-8')
    r=subprocess.run([sys.executable,str(ROOT/'scripts/create_contract.py'),str(RT/'task.json'),str(RT/'route.json'),str(RT/'protocol.json'),'--output',str(RT/'CONTRACT.json')],capture_output=True,text=True); assert r.returncode==0
    contract=json.loads((RT/'CONTRACT.json').read_text()); assert contract['harness']=='opencode' and contract['handoff_format']['required']==['HANDOFF.md','STATUS.json']
    context={"traycer_status":"connected","display_name":"Model Orchestrator Configuration","harness":"codex","surface":"codex_session","traycer_object_type":"Task"}
    (RT/'context.json').write_text(json.dumps(context),encoding='utf-8'); (RT/'codex-route.json').write_text(json.dumps(codex),encoding='utf-8'); (RT/'contract.md').write_text('controlled',encoding='utf-8')
    r=subprocess.run([sys.executable,str(ROOT/'scripts/traycer_bridge.py'),'--config',str(ROOT/'config/orchestrator.json'),'--context',str(RT/'context.json'),'--route',str(RT/'codex-route.json'),'--contract',str(RT/'contract.md'),'--output',str(RT/'identity.json')],capture_output=True,text=True); assert r.returncode==0
    identity=json.loads((RT/'identity.json').read_text())['identity']; assert identity['agent_id'] is None and identity['identity_status']=='unverified' and identity['display_name']=='Model Orchestrator Configuration'
    ledger=RT/'ledger.jsonl'; ledger.write_text('',encoding='utf-8')
    r=subprocess.run([sys.executable,str(ROOT/'scripts/check_budget.py'),str(ledger),'--config',str(ROOT/'config/orchestrator.json'),'--estimated-cost','0.01','--route','external_worker','--provider','openrouter','--model',deep['model']],capture_output=True,text=True); assert r.returncode==0
    (RT/'HANDOFF.md').write_text('# Handoff\ncontrolled',encoding='utf-8'); (RT/'STATUS.json').write_text(json.dumps({'status':'working','task_id':'t1'}),encoding='utf-8'); assert (RT/'HANDOFF.md').is_file() and (RT/'STATUS.json').is_file()
    print('architecture tests: PASS')
if __name__=='__main__': main()