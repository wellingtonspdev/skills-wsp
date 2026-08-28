# Input e output do classificador

O agente faz a análise semântica e fornece as notas; `scripts/classify_issue.py` valida intervalos, calcula C, aplica a política e gera a ficha.

## Input mínimo

```json
{
  "id": "#184",
  "title": "Adicionar novo provider",
  "task_type": "FEATURE-X",
  "factors": {
    "scope": 3,
    "navigation": 3,
    "integrations": 4,
    "logic": 2,
    "execution_horizon": 3,
    "validation_difficulty": 2
  },
  "risk": "R2",
  "quality": 82,
  "validation": "V4"
}
```

`quality` também pode conter os seis critérios, cada um de 0 a 5:

```json
{
  "problem": 5,
  "expected_behavior": 4,
  "acceptance_criteria": 5,
  "evidence": 3,
  "context": 4,
  "definition_of_done": 4
}
```

## Campos opcionais

```json
{
  "body": "...",
  "secondary_types": ["INTEGRATION"],
  "factor_evidence": {"scope": "três arquivos do provider"},
  "hard_gates": [],
  "possible_hard_gates": ["auth mencionado, toque direto não confirmado"],
  "decomposable": true,
  "root_cause_known": true,
  "exceptional_logic": false,
  "classification_status": "confirmed",
  "assumptions": [],
  "gaps": [],
  "expected_validation": ["unit", "integration", "build", "e2e"]
}
```

Para várias tarefas, use uma lista ou `{ "items": [...] }`. Cada item é classificado isoladamente.

## Output principal

```json
{
  "issue_id": "#184",
  "classification_status": "confirmed",
  "task_type": "FEATURE-X",
  "complexity": {
    "score": 57,
    "class": "C3",
    "factors": {}
  },
  "risk": "R2",
  "issue_quality": 82,
  "validation": "V4",
  "hard_gates": [],
  "workflow": "W3",
  "models": {
    "planner": {},
    "implementer": {},
    "reviewer": {},
    "escalation": {}
  },
  "review_required": true,
  "human_review_required": false,
  "expected_validation": [],
  "escalation_triggers": [],
  "labels": [],
  "rationale": []
}
```

Cada papel de modelo contém `harness`, `requested_model`, `effective_model`, `reasoning_effort` e `availability_status`. O script deixa `effective_model=null` até verificação real do runtime.

## CLI

```text
python scripts/classify_issue.py INPUT.json --format json
python scripts/classify_issue.py INPUT.json --format markdown
python scripts/classify_issue.py INPUT.json --format both
python scripts/classify_issue.py --template
```

Use `-` como input para stdin. A CLI não chama GitHub, não executa modelos e não grava arquivos por padrão.
