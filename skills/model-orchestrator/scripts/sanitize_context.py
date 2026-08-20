#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
from orchestrator_core import load_json
PATTERNS=[("private_key",re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",re.S)),("credential",re.compile(r"(?im)^\s*[A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD|COOKIE|CREDENTIAL)[A-Z0-9_]*\s*[:=]\s*\S+")),("bearer",re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}")),("email",re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",re.I)),("cpf",re.compile(r"(?<!\d)\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?!\d)"))]
p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output"); p.add_argument("--report",required=True); p.add_argument("--classification",required=True); p.add_argument("--provider",required=True); a=p.parse_args()
c=load_json(a.classification); external=a.provider in {"opencode","openrouter"}
if external and not c.get("opencode_allowed" if a.provider=="opencode" else "openrouter_allowed"): raise SystemExit("blocked: sensitivity/risk classification prohibits external provider")
text=Path(a.input).read_text(encoding="utf-8"); counts={}; snippets=[]
for label,pattern in PATTERNS:
    text,count=pattern.subn(f"[REDACTED:{label}]",text); counts[label]=count
Path(a.output).write_text(text,encoding="utf-8")
report={"schema_version":2,"sanitization_status":"valid","provider":a.provider,"source_file":str(Path(a.input).resolve()),"files_released":[str(Path(a.output).resolve())],"redaction_counts":counts,"total_redactions":sum(counts.values()),"manual_review_required":external}
Path(a.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

