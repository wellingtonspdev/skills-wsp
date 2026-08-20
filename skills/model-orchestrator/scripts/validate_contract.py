#!/usr/bin/env python3
import argparse, json
from pathlib import Path
REQUIRED=["## Objetivo","## Contexto mínimo sanitizado","## Escopo permitido","## Escopo proibido","## Critérios de aceite objetivos","## Comandos de validação","## Riscos e rollback","## Limites de tentativas, tempo, custo, tokens e chamadas","## Condições de escalonamento","## Formato e destino do handoff"]
p=argparse.ArgumentParser(); p.add_argument("contract"); p.add_argument("--output",required=True); a=p.parse_args()
text=Path(a.contract).read_text(encoding="utf-8"); missing=[x for x in REQUIRED if x not in text]
result={"schema_version":2,"contract_status":"valid" if not missing else "blocked","contract_path":str(Path(a.contract).resolve()),"missing_sections":missing}
Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,ensure_ascii=False,indent=2)); raise SystemExit(0 if not missing else 2)

