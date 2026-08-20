#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import load_json, dump
p=argparse.ArgumentParser(); p.add_argument('ledger'); p.add_argument('--config',required=True); p.add_argument('--estimated-cost',type=float,required=True); p.add_argument('--route',default='codex_only'); p.add_argument('--provider',default='openai'); p.add_argument('--model'); a=p.parse_args()
cfg=load_json(a.config); paid=a.route=='external_worker' and a.provider=='openrouter'
allowed_slugs={x['slug'] for x in cfg['openrouter']['paid_workers'].values()}
if paid and a.model not in allowed_slugs: raise SystemExit('blocked: paid model is not allowlisted')
rows=[] if not Path(a.ledger).exists() else [json.loads(x) for x in Path(a.ledger).read_text(encoding='utf-8-sig').splitlines() if x.strip()]
spent=sum(float(x.get('total_cost',0) or 0) for x in rows); budget=float(cfg['openrouter']['budget_usd']); reserve=float(cfg['openrouter'].get('reserve_usd',0)); remaining=budget-spent
allowed=not paid or (a.estimated_cost>=0 and remaining-a.estimated_cost>=reserve)
result={'schema_version':3,'budget_status':'valid' if allowed else 'blocked','route':a.route,'provider':a.provider,'model':a.model,'budget':budget,'spent':spent,'remaining':remaining,'reserve':reserve,'estimated_cost':a.estimated_cost,'paid_model_slugs':sorted(allowed_slugs)}
dump(result); raise SystemExit(0 if allowed else 3)