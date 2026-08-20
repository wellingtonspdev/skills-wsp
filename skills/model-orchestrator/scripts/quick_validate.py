import json, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['SKILL.md','config/orchestrator.json','scripts/pipeline.py','scripts/traycer_bridge.py','scripts/collect_metrics.py']
missing=[x for x in required if not (root/x).is_file()]
if missing: print('blocked: '+','.join(missing)); raise SystemExit(1)
json.load((root/'config/orchestrator.json').open(encoding='utf-8-sig'))
print('quick_validate: PASS')
