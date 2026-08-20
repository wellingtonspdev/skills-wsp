#!/usr/bin/env python3
#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import dump, load_json, preflight, validate_config
p=argparse.ArgumentParser(); p.add_argument("--context",required=True); p.add_argument("--config",required=True); p.add_argument("--output",required=True); a=p.parse_args()
cfg=load_json(a.config); validate_config(cfg,a.config)
result=preflight(load_json(a.context),cfg,a.config)
Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); dump(result)

