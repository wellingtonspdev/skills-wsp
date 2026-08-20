#!/usr/bin/env python3
import fnmatch
import json
import os
import subprocess
from pathlib import Path

CRITICAL_SIGNALS = {"authentication","authorization","sensitive_data","process_deadlines","database_migration","concurrency","idempotency","architectural_change","security","secrets","multi_tenancy","production_incident","destructive_action"}
EXTERNAL_ALLOWED_DEFAULT = {"public","synthetic","sanitized"}
REQUIRED_CONFIG = ("schema_version","active","skill_name","orchestration","codex","opencode","openrouter","routing","privacy","verification")

def load_json(path):
    p = Path(path).resolve()
    with p.open(encoding="utf-8-sig") as f:
        return json.load(f)

def dump(value):
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))

def path_matches(path, patterns):
    normalized = str(path).replace("\\","/").lstrip("./")
    return any(fnmatch.fnmatch(normalized, str(p).replace("\\","/")) for p in patterns)

def git_root(cwd):
    r = subprocess.run(["git","-C",str(cwd),"rev-parse","--show-toplevel"],capture_output=True,text=True)
    return Path(r.stdout.strip()).resolve() if r.returncode == 0 and r.stdout.strip() else None

def classify(task):
    signals={str(x).lower() for x in task.get("signals",[])}
    data=str(task.get("data_classification","unknown")).lower()
    files=int(task.get("estimated_files",0) or 0); commands=int(task.get("estimated_commands",0) or 0)
    iterations=int(task.get("estimated_test_iterations",0) or 0); modules=int(task.get("estimated_modules",0) or 0)
    breadth="cross_module" if modules>=2 or files>=5 or signals & {"cross_module","public_api"} else ("multi_file" if files>1 else "local")
    complexity="high" if modules>=3 or files>=8 or signals & {"architectural_change","production_incident"} else ("medium" if files>=4 or modules>=2 or commands>=4 else "low")
    critical=bool(signals & CRITICAL_SIGNALS) or data in {"sensitive","secret"}
    risk="critical" if signals & {"production_incident","destructive_action"} else ("high" if critical or task.get("objective_validation") is False or signals & {"scope_unclear","business_rule_ambiguous"} else ("medium" if breadth!="local" or signals & {"public_api","cross_module"} else "low"))
    reversible="low" if signals & {"destructive_action","database_migration","production_incident"} else ("medium" if breadth!="local" else "high")
    terminal_score=sum((commands>=3,iterations>=2,files>=5,modules>=2,bool(signals & {"repository_navigation","worktree","tool_intensive"})))
    external_access_decision=("allowed" if data in EXTERNAL_ALLOWED_DEFAULT and risk in {"low","medium"} and bool(task.get("objective_validation",False)) else "blocked_unknown_or_sensitive")
    external_allowed=external_access_decision == "allowed"
    codex_model_decision="sol" if risk in {"high","critical"} or complexity=="high" else "standard"
    return {
      "schema_version":3,"classification_status":"valid","complexity":complexity,"risk":risk,
      "sensitivity":data,"scope_breadth":breadth,"reversibility":reversible,
      "external_model_required":not (complexity=="high" or risk in {"high","critical"}),
      "independent_review_required":risk in {"medium","high","critical"} or bool(task.get("requires_independent_review",False)),
      "opencode_allowed":external_allowed and complexity=="low",
      "openrouter_allowed":external_allowed,
      "terminal_score":terminal_score,"signals":sorted(signals),
      "objective_validation":bool(task.get("objective_validation",False)),
      "external_access_decision":external_access_decision,
      "codex_model_decision":codex_model_decision,
      "requires_exploration":any(task.get(k) in (None,"unknown") for k in ("estimated_files","estimated_commands"))
    }

def choose_route(c, config):
    if c.get("classification_status") != "valid":
        raise ValueError("invalid classification artifact")
    codex_role = "critical" if c.get("codex_model_decision") == "sol" else "router"
    result = {
      "schema_version":3, "decision_status":"valid", "route":"codex_only",
      "platform":"traycer", "harness":"codex", "provider":"openai",
      "surface":"codex_session", "agent_role":codex_role,
      "model":config["codex"]["critical_model" if codex_role == "critical" else "router_model"],
      "justification":"risk_privacy_or_validation_gate", "cost_limit_usd":0,
      "max_attempts":1, "fallback":config["routing"].get("fallback_route","codex_only"),
      "independent_review_required":c["independent_review_required"],
      "allowed_paid_models":config["openrouter"].get("allowed_labels",[])
    }
    if c["risk"] in {"high","critical"} or not c["objective_validation"] or not c["external_model_required"]:
        return result
    if c["opencode_allowed"] and c["complexity"] == "low" and c["scope_breadth"] == "local":
        result.update(route="external_worker", harness="opencode", provider="opencode", agent_role="free_worker", model=config["opencode"]["free_worker_slug"], justification="simple_sanitized_low_risk", max_attempts=1)
    elif c["openrouter_allowed"]:
        terminal=c["terminal_score"] >= int(config["routing"].get("terminal_score_threshold",3))
        role="terminal_agent" if terminal else "default"
        result.update(route="external_worker", harness="opencode", provider="openrouter", agent_role=role, model=config["openrouter"]["paid_workers"][role]["slug"], justification="tool_trajectory_threshold" if terminal else "paid_default_implementation", cost_limit_usd=config["openrouter"]["budget_usd"], max_attempts=config["openrouter"]["paid_workers"][role]["max_attempts"])
    return result

def choose_surface(task, capabilities):
    iterative=bool(task.get("requires_iterative_communication") or task.get("requires_a2a"))
    surface="gui_chat" if iterative else "terminal_tui"
    cap=capabilities.get("surfaces",{}).get(surface,{})
    if not cap.get("available",False):
        raise ValueError(f"surface unavailable: {surface}")
    if task.get("requires_a2a") and not cap.get("a2a",False):
        raise ValueError(f"A2A unsupported for surface: {surface}")
    return {"surface":surface,"a2a_allowed":bool(cap.get("a2a",False)),"protocol":"iterative" if surface=="gui_chat" else "launch_once_artifacts"}

def detect_conflicts(tasks):
    owners={}; conflicts=[]
    for task in tasks:
        tid=task.get("task_id")
        for path in task.get("allowed_files",[]):
            key=str(path).replace("\\","/").lower()
            if key in owners and owners[key] != tid: conflicts.append({"path":path,"tasks":[owners[key],tid]})
            else: owners[key]=tid
    return {"parallelization_allowed":not conflicts,"conflicts":conflicts}
def validate_config(config, path):
    missing=[k for k in REQUIRED_CONFIG if k not in config]
    if missing: raise ValueError("missing config keys: "+",".join(missing))
    if not Path(path).is_absolute(): raise ValueError("active config path must be absolute")
    if str(path).lower().endswith(".example.json"): raise ValueError("example config cannot be active")
    if not config.get("active"): raise ValueError("active config is disabled")
    if int(config.get("schema_version",0)) < 3: raise ValueError("schema version 3 or newer is required")
    if config.get("orchestration",{}).get("external_worker_harness") != "opencode": raise ValueError("external workers must use OpenCode harness")
    if not config.get("orchestration",{}).get("provider_is_not_harness"): raise ValueError("provider/harness separation is required")
    if config["openrouter"]["budget_usd"]<0 or config["openrouter"].get("reserve_usd",0)<0: raise ValueError("invalid budget")
    return {"config_status":"valid","config_path":str(Path(path).resolve()),"schema_version":config["schema_version"],"skill_version":config.get("skill_version")}

def preflight(ctx, config, config_path):
    cwd=Path(ctx.get("cwd",os.getcwd())).resolve(); root=git_root(cwd)
    designated=ctx.get("traycer_worktree") or ctx.get("designated_worktree")
    designated_path=Path(designated).resolve() if designated else None
    reported_current=Path(ctx.get("current_worktree",cwd)).resolve()
    if designated_path and reported_current != designated_path: raise ValueError("worktree divergence: current_worktree != traycer_worktree")
    if designated_path and cwd != designated_path and not str(cwd).startswith(str(designated_path)+os.sep): raise ValueError("worktree divergence: cwd outside designated worktree")
    if designated_path and ctx.get("principal_repository") and root and root == Path(ctx["principal_repository"]).resolve(): raise ValueError("principal repository is forbidden when a worktree is designated")
    if ctx.get("skill_name")!="model-orchestrator": raise ValueError("wrong or unloaded skill")
    if not ctx.get("harness") or not ctx.get("agent") or not ctx.get("model"): raise ValueError("harness, agent and model are required")
    return {"preflight_status":"valid","skill_name":ctx["skill_name"],"config_path":str(Path(config_path).resolve()),"cwd":str(cwd),"git_root":str(root) if root else None,"traycer_worktree":str(designated_path) if designated_path else None,"harness":ctx["harness"],"agent":ctx["agent"],"model":ctx["model"],"principal_write_forbidden":bool(designated_path)}




