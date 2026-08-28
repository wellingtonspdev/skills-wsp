#!/usr/bin/env python3
"""Deterministic T/C/R/Q/V routing calculator for ai-issue-router.

The agent or human supplies semantic scores. This script validates the scores,
applies routing policy, and emits auditable JSON/Markdown. It performs no model
calls, GitHub mutations, delegation, or telemetry writes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


TASK_TYPES = {
    "DOC", "TEST", "UI", "BUG-L", "BUG-X", "FEATURE-L", "FEATURE-X",
    "REFACTOR-L", "REFACTOR-X", "PERF", "CI", "INFRA", "DB", "ARCH",
    "INTEGRATION", "ALGO", "SECURITY", "AUTH", "REVIEW", "RESEARCH",
}

FACTOR_SPECS = {
    "scope": ("S", 5, ("s",)),
    "navigation": ("N", 4, ("n",)),
    "integrations": ("I", 3, ("i", "dependencies")),
    "logic": ("L", 3, ("l",)),
    "execution_horizon": ("H", 3, ("h", "horizon")),
    "validation_difficulty": ("X", 2, ("x",)),
}

QUALITY_FIELDS = (
    "problem",
    "expected_behavior",
    "acceptance_criteria",
    "evidence",
    "context",
    "definition_of_done",
)

WORKFLOW_RANK = {"W1": 1, "W2": 2, "W3": 3, "W4": 4, "W5": 5}

CRITICAL_GATES = {
    "destructive_migration",
    "production_data",
    "data_isolation",
    "multi_tenant_isolation",
    "critical_concurrency",
    "irreversible_change",
    "critical_security_boundary",
}

TEMPLATE = {
    "id": "#184",
    "title": "Adicionar novo provider",
    "task_type": "FEATURE-X",
    "factors": {
        "scope": 3,
        "navigation": 3,
        "integrations": 4,
        "logic": 2,
        "execution_horizon": 3,
        "validation_difficulty": 2,
    },
    "factor_evidence": {
        "scope": "três arquivos relacionados",
        "integrations": "provider externo e API interna",
    },
    "risk": "R2",
    "quality": 82,
    "validation": "V4",
    "hard_gates": [],
    "possible_hard_gates": [],
    "decomposable": True,
    "root_cause_known": True,
    "classification_status": "confirmed",
    "expected_validation": ["unit", "integration", "build", "e2e"],
}


class InputError(ValueError):
    """Invalid classification input."""


def integer_in_range(value: Any, label: str, minimum: int, maximum: int) -> int:
    if isinstance(value, bool):
        raise InputError(f"{label} must be an integer from {minimum} to {maximum}")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise InputError(f"{label} must be an integer from {minimum} to {maximum}") from exc
    if parsed != value and not (isinstance(value, str) and str(parsed) == value.strip()):
        raise InputError(f"{label} must be an integer from {minimum} to {maximum}")
    if not minimum <= parsed <= maximum:
        raise InputError(f"{label} must be between {minimum} and {maximum}")
    return parsed


def get_factor(raw: dict[str, Any], name: str, aliases: tuple[str, ...]) -> Any:
    if name in raw:
        return raw[name]
    lowered = {str(key).lower(): value for key, value in raw.items()}
    for alias in aliases:
        if alias in lowered:
            return lowered[alias]
    raise InputError(f"missing complexity factor: {name}")


def normalize_factors(raw: Any) -> dict[str, int]:
    if not isinstance(raw, dict):
        raise InputError("factors must be an object")
    result: dict[str, int] = {}
    for name, (_, _, aliases) in FACTOR_SPECS.items():
        result[name] = integer_in_range(get_factor(raw, name, aliases), f"factors.{name}", 0, 5)
    return result


def complexity_score(factors: dict[str, int]) -> int:
    return sum(factors[name] * spec[1] for name, spec in FACTOR_SPECS.items())


def complexity_class(score: int) -> str:
    if score <= 20:
        return "C1"
    if score <= 40:
        return "C2"
    if score <= 60:
        return "C3"
    if score <= 80:
        return "C4"
    return "C5"


def normalize_quality(raw: Any) -> tuple[int, dict[str, int] | None]:
    if isinstance(raw, dict):
        missing = [field for field in QUALITY_FIELDS if field not in raw]
        if missing:
            raise InputError(f"quality is missing criteria: {', '.join(missing)}")
        criteria = {
            field: integer_in_range(raw[field], f"quality.{field}", 0, 5)
            for field in QUALITY_FIELDS
        }
        return round(sum(criteria.values()) / 30 * 100), criteria
    return integer_in_range(raw, "quality", 0, 100), None


def normalize_prefixed_level(raw: Any, prefix: str, maximum: int, label: str) -> int:
    if isinstance(raw, str):
        value = raw.strip().upper()
        if value.startswith(prefix):
            value = value[1:]
        raw = value
    return integer_in_range(raw, label, 0, maximum)


def normalize_bool(raw: Any, label: str, default: bool) -> bool:
    if raw is None:
        return default
    if not isinstance(raw, bool):
        raise InputError(f"{label} must be a JSON boolean")
    return raw


def promote(current: str, minimum: str, rationale: list[str], reason: str) -> str:
    if WORKFLOW_RANK[current] < WORKFLOW_RANK[minimum]:
        rationale.append(reason)
        return minimum
    return current


def select_base_workflow(
    c_level: int,
    risk: int,
    quality: int,
    validation: int,
    decomposable: bool,
    root_cause_known: bool,
) -> tuple[str, list[str]]:
    rationale: list[str] = []
    if risk == 4:
        return "W5", ["R4 impõe ownership crítico e revisão humana"]
    if risk == 3:
        return "W4", ["R3 impõe controle e revisão por Sol"]
    if risk == 2:
        if c_level <= 2:
            return "W2", ["C1/C2 com R2 requer microplano e revisão independente"]
        if c_level == 3:
            return "W3", ["C3 com R2 requer planejamento GPT e execução delimitada"]
        if c_level == 4:
            if quality >= 60 and validation >= 3 and decomposable:
                return "W3", ["C4/R2 é decomponível, especificado e validável"]
            return "W4", ["C4/R2 sem decomposição ou validação suficiente requer controle Sol"]
        return "W4", ["C5/R2 requer controle Sol"]

    if c_level == 1:
        return "W1", ["C1 e R0/R1 permitem execução direta quando os demais gates passarem"]
    if c_level == 2:
        if quality >= 80 and validation >= 2:
            return "W1", ["C2/R0-R1 tem Q>=80 e V>=V2"]
        return "W2", ["C2/R0-R1 precisa de microplano por Q ou V"]
    if c_level == 3:
        if quality >= 70 and validation >= 2 and decomposable and root_cause_known:
            return "W2", ["C3/R0-R1 é conhecido, decomponível, bem especificado e testável"]
        return "W3", ["C3/R0-R1 precisa de investigação/decomposição GPT"]
    if c_level == 4:
        return "W3", ["C4/R0-R1 requer planejamento GPT antes da execução"]
    if decomposable and validation >= 3:
        return "W3", ["C5/R0-R1 pode ser decomposto em subtarefas validáveis"]
    return "W4", ["C5 não decomponível ou pouco validável requer controle Sol"]


def role(harness: str | None, requested_model: str | None, effort: str | None, **extra: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "harness": harness,
        "requested_model": requested_model,
        "effective_model": None,
        "reasoning_effort": effort,
        "availability_status": "not_checked" if requested_model else "not_applicable",
    }
    result.update(extra)
    return result


def select_models(workflow: str, task_type: str, c_level: int, risk: int, exceptional_logic: bool) -> dict[str, Any]:
    if workflow == "W1":
        return {
            "planner": role(None, None, None),
            "implementer": role("antigravity", "gemini-3.7-flash", "medium"),
            "reviewer": role("codex", "gpt-5.6-terra", "medium", review_mode="batched_or_on_demand"),
            "escalation": role("codex", "gpt-5.6-terra", "medium"),
        }
    if workflow == "W2":
        implementer = "gemini-3.1-pro" if exceptional_logic else "gemini-3.7-flash"
        return {
            "planner": role("codex", "gpt-5.6-terra", "medium"),
            "implementer": role("antigravity", implementer, "high" if c_level >= 2 else "medium"),
            "reviewer": role("codex", "gpt-5.6-terra", "medium"),
            "escalation": role("codex", "gpt-5.6-sol", "high"),
        }
    if workflow == "W3":
        use_sol = task_type in {"ARCH", "BUG-X", "SECURITY", "AUTH"} or c_level >= 4
        planner = "gpt-5.6-sol" if use_sol else "gpt-5.6-terra"
        reviewer = "gpt-5.6-sol" if use_sol or (risk >= 2 and c_level >= 4) else "gpt-5.6-terra"
        implementer = "gemini-3.1-pro" if exceptional_logic else "gemini-3.7-flash"
        return {
            "planner": role("codex", planner, "high"),
            "implementer": role("antigravity", implementer, "high"),
            "reviewer": role("codex", reviewer, "high", review_mode="independent"),
            "escalation": role("codex", "gpt-5.6-sol", "high"),
        }
    if workflow == "W4":
        effort = "xhigh" if task_type in {"SECURITY", "AUTH", "ARCH"} or risk >= 3 else "high"
        return {
            "planner": role("codex", "gpt-5.6-sol", effort),
            "implementer": role("antigravity", "gemini-3.7-flash", "high", execution_mode="under_gpt_contract"),
            "reviewer": role("codex", "gpt-5.6-sol", effort, review_mode="independent_session"),
            "escalation": role("codex", "gpt-5.6-sol", "xhigh", human_on_material_decision=True),
        }
    return {
        "planner": role("codex", "gpt-5.6-sol", "xhigh", ownership="critical_core"),
        "implementer": role(
            "codex",
            "gpt-5.6-sol",
            "high",
            ownership="critical_core",
            supporting_harness="antigravity",
            supporting_model="gemini-3.7-flash",
            supporting_scope="isolated_peripheral_work_only",
        ),
        "reviewer": role("codex", "gpt-5.6-sol", "xhigh", review_mode="independent_session"),
        "escalation": role("human", "technical_owner", None),
    }


def default_validation(task_type: str, validation: int, risk: int) -> list[str]:
    if task_type == "DOC":
        checks = ["docs-check", "link-check"]
    else:
        checks = ["targeted-tests", "build"]
    if validation >= 2 and "unit" not in checks:
        checks.append("unit")
    if validation >= 3 or task_type in {"INTEGRATION", "DB", "INFRA"}:
        checks.append("integration")
    if validation >= 4 or task_type == "UI":
        checks.append("e2e")
    if task_type in {"SECURITY", "AUTH"} or risk >= 3:
        checks.append("security-review")
    if task_type == "DB":
        checks.extend(["migration-dry-run", "rollback-or-recovery-check"])
    return list(dict.fromkeys(checks))


def normalize_string_list(raw: Any, label: str) -> list[str]:
    if raw is None:
        return []
    if not isinstance(raw, list) or not all(isinstance(item, str) for item in raw):
        raise InputError(f"{label} must be a list of strings")
    return [item.strip() for item in raw if item.strip()]


def classify_item(item: Any) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise InputError("each item must be an object")

    task_type = str(item.get("task_type", "")).strip().upper()
    if task_type not in TASK_TYPES:
        raise InputError(f"task_type must be one of: {', '.join(sorted(TASK_TYPES))}")

    factors = normalize_factors(item.get("factors"))
    score = complexity_score(factors)
    c_class = complexity_class(score)
    c_level = int(c_class[1:])
    risk = normalize_prefixed_level(item.get("risk"), "R", 4, "risk")
    quality, quality_factors = normalize_quality(item.get("quality"))
    validation = normalize_prefixed_level(item.get("validation"), "V", 5, "validation")

    hard_gates = normalize_string_list(item.get("hard_gates"), "hard_gates")
    possible_hard_gates = normalize_string_list(item.get("possible_hard_gates"), "possible_hard_gates")
    decomposable = normalize_bool(item.get("decomposable"), "decomposable", True)
    root_cause_known = normalize_bool(
        item.get("root_cause_known"), "root_cause_known", task_type != "BUG-X"
    )
    exceptional_logic = normalize_bool(item.get("exceptional_logic"), "exceptional_logic", False)
    critical_core = normalize_bool(item.get("critical_core"), "critical_core", False)

    workflow, rationale = select_base_workflow(
        c_level, risk, quality, validation, decomposable, root_cause_known
    )

    if quality < 60:
        workflow = promote(workflow, "W3", rationale, "Q<60 exige exploração/planejamento antes de implementar")
    if validation <= 1:
        minimum = "W4" if risk >= 2 or c_level >= 4 or not root_cause_known else "W3"
        workflow = promote(workflow, minimum, rationale, f"V{validation} aumenta controle e revisão independente")

    normalized_gates = {gate.strip().lower().replace("-", "_").replace(" ", "_") for gate in hard_gates}
    if hard_gates:
        minimum = "W5" if risk == 4 or critical_core or normalized_gates & CRITICAL_GATES else "W4"
        workflow = promote(workflow, minimum, rationale, f"hard gate confirmado impõe no mínimo {minimum}")

    if task_type in {"SECURITY", "AUTH"}:
        minimum = "W5" if risk == 4 or critical_core else "W4"
        workflow = promote(workflow, minimum, rationale, f"{task_type} impõe controle especializado")
    if task_type == "ARCH" and (critical_core or c_level == 5):
        workflow = promote(workflow, "W5", rationale, "arquitetura central/C5 requer ownership Sol")

    status = str(item.get("classification_status", "confirmed")).strip().lower()
    if status not in {"confirmed", "preliminary", "blocked"}:
        raise InputError("classification_status must be confirmed, preliminary, or blocked")
    if possible_hard_gates and status == "confirmed":
        status = "preliminary"
        rationale.append("possible_hard_gates pendentes impedem classificação confirmada")

    expected_validation = normalize_string_list(item.get("expected_validation"), "expected_validation")
    if not expected_validation:
        expected_validation = default_validation(task_type, validation, risk)

    models = select_models(workflow, task_type, c_level, risk, exceptional_logic)
    review_required = workflow != "W1" or risk >= 2 or task_type in {"SECURITY", "AUTH", "ARCH"}
    human_review_required = risk == 4 or workflow == "W5" or critical_core

    issue_id = str(item.get("id") or item.get("issue_number") or "unidentified")
    title = str(item.get("title") or "Untitled task")
    labels = [
        f"ai:type/{task_type.lower()}",
        f"ai:complexity/{c_class}",
        f"ai:risk/R{risk}",
        f"ai:readiness/Q{quality}",
        f"ai:validation/V{validation}",
        f"ai:workflow/{workflow}",
    ]
    if human_review_required:
        labels.append("ai:human-review/required")

    result: dict[str, Any] = {
        "issue_id": issue_id,
        "title": title,
        "classification_status": status,
        "task_type": task_type,
        "secondary_types": normalize_string_list(item.get("secondary_types"), "secondary_types"),
        "complexity": {
            "score": score,
            "class": c_class,
            "factors": factors,
            "factor_evidence": item.get("factor_evidence", {}),
        },
        "risk": f"R{risk}",
        "issue_quality": quality,
        "quality_factors": quality_factors,
        "validation": f"V{validation}",
        "hard_gates": hard_gates,
        "possible_hard_gates": possible_hard_gates,
        "workflow": workflow,
        "models": models,
        "review_required": review_required,
        "human_review_required": human_review_required,
        "expected_validation": expected_validation,
        "escalation_triggers": [
            "same_failure_twice",
            "root_cause_unknown",
            "scope_gt_2x_estimate",
            "unexpected_module_or_dependency",
            "unexpected_auth_security_or_migration",
            "plan_deviation",
            "validation_unavailable",
        ],
        "labels": labels,
        "assumptions": normalize_string_list(item.get("assumptions"), "assumptions"),
        "gaps": normalize_string_list(item.get("gaps"), "gaps"),
        "rationale": rationale,
    }
    return result


def normalize_items(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and "items" in payload:
        if not isinstance(payload["items"], list):
            raise InputError("items must be a list")
        return payload["items"]
    if isinstance(payload, dict):
        return [payload]
    raise InputError("input must be an object, a list, or an object with items")


def classify_payload(payload: Any) -> dict[str, Any]:
    results = [classify_item(item) for item in normalize_items(payload)]
    counts: dict[str, int] = {}
    for result in results:
        counts[result["workflow"]] = counts.get(result["workflow"], 0) + 1
    return {
        "schema_version": "1.0",
        "classification_count": len(results),
        "workflow_counts": dict(sorted(counts.items())),
        "items": results,
    }


def model_label(model: dict[str, Any]) -> str:
    requested = model.get("requested_model") or "none"
    effort = model.get("reasoning_effort")
    return f"{requested} ({effort})" if effort else requested


def markdown_for_item(result: dict[str, Any]) -> str:
    factors = result["complexity"]["factors"]
    short_factors = ", ".join(
        f"{FACTOR_SPECS[name][0]}={value}" for name, value in factors.items()
    )
    gates = ", ".join(result["hard_gates"]) or "None"
    rationale = "\n".join(f"- {reason}" for reason in result["rationale"])
    validations = "\n".join(f"- {check}" for check in result["expected_validation"])
    return f"""## AI ROUTING CARD — {result['issue_id']}

**Title:** {result['title']}<br>
**Status:** {result['classification_status']}<br>
**Type:** {result['task_type']}<br>
**Complexity:** {result['complexity']['class']} — {result['complexity']['score']}/100 ({short_factors})<br>
**Risk:** {result['risk']}<br>
**Issue Quality:** Q{result['issue_quality']}<br>
**Validation:** {result['validation']}<br>
**Hard gates:** {gates}<br>
**Workflow:** {result['workflow']}<br>
**Planner:** {model_label(result['models']['planner'])}<br>
**Implementer:** {model_label(result['models']['implementer'])}<br>
**Reviewer:** {model_label(result['models']['reviewer'])}<br>
**Escalation:** {model_label(result['models']['escalation'])}<br>
**Human review:** {'required' if result['human_review_required'] else 'not required by router'}

### Rationale

{rationale}

### Expected validation

{validations}
"""


def render_markdown(report: dict[str, Any]) -> str:
    items = report["items"]
    if len(items) == 1:
        return markdown_for_item(items[0]).rstrip()
    rows = ["| Item | Type | C | R | Q | V | Workflow |", "|---|---|---:|---:|---:|---:|---|"]
    for item in items:
        rows.append(
            f"| {item['issue_id']} | {item['task_type']} | {item['complexity']['class']} "
            f"({item['complexity']['score']}) | {item['risk']} | Q{item['issue_quality']} | "
            f"{item['validation']} | {item['workflow']} |"
        )
    cards = "\n\n".join(markdown_for_item(item).rstrip() for item in items)
    return "# AI ROUTING BATCH\n\n" + "\n".join(rows) + "\n\n" + cards


def load_payload(path: str) -> Any:
    if path == "-":
        return json.load(sys.stdin)
    with Path(path).open("r", encoding="utf-8-sig") as stream:
        return json.load(stream)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate T/C/R/Q/V scores and route engineering work")
    parser.add_argument("input", nargs="?", help="JSON file or - for stdin")
    parser.add_argument("--format", choices=("json", "markdown", "both"), default="json")
    parser.add_argument("--template", action="store_true", help="print a valid input template")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.template:
        print(json.dumps(TEMPLATE, ensure_ascii=False, indent=2))
        return 0
    if not args.input:
        print("error: input is required unless --template is used", file=sys.stderr)
        return 2
    try:
        report = classify_payload(load_payload(args.input))
    except (OSError, json.JSONDecodeError, InputError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format in {"markdown", "both"}:
        print(render_markdown(report))
    if args.format == "both":
        print("\n--- JSON ---\n")
    if args.format in {"json", "both"}:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
