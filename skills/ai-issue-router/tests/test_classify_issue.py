import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "classify_issue.py"
SPEC = importlib.util.spec_from_file_location("classify_issue", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def issue(**overrides):
    payload = {
        "id": "#1",
        "title": "Tarefa de teste",
        "task_type": "UI",
        "factors": {
            "scope": 1,
            "navigation": 1,
            "integrations": 1,
            "logic": 1,
            "execution_horizon": 1,
            "validation_difficulty": 1,
        },
        "risk": "R1",
        "quality": 90,
        "validation": "V4",
    }
    payload.update(overrides)
    return payload


class RoutingTests(unittest.TestCase):
    def test_simple_ui_matches_study(self):
        result = MODULE.classify_item(issue())
        self.assertEqual(result["complexity"]["score"], 20)
        self.assertEqual(result["complexity"]["class"], "C1")
        self.assertEqual(result["workflow"], "W1")
        self.assertEqual(result["models"]["implementer"]["requested_model"], "gemini-3.7-flash")

    def test_concurrency_bug_routes_to_w4(self):
        result = MODULE.classify_item(issue(
            task_type="BUG-X",
            factors={
                "scope": 3,
                "navigation": 4,
                "integrations": 3,
                "logic": 4,
                "execution_horizon": 4,
                "validation_difficulty": 4,
            },
            risk="R3",
            quality=75,
            validation="V3",
            root_cause_known=False,
        ))
        self.assertEqual(result["complexity"]["score"], 72)
        self.assertEqual(result["complexity"]["class"], "C4")
        self.assertEqual(result["workflow"], "W4")
        self.assertEqual(result["models"]["planner"]["requested_model"], "gpt-5.6-sol")

    def test_auth_risk_dominates_small_scope(self):
        result = MODULE.classify_item(issue(
            task_type="AUTH",
            risk="R4",
            hard_gates=["authorization"],
        ))
        self.assertEqual(result["complexity"]["class"], "C1")
        self.assertEqual(result["workflow"], "W5")
        self.assertTrue(result["human_review_required"])

    def test_low_quality_promotes_direct_task_to_w3(self):
        result = MODULE.classify_item(issue(quality=30))
        self.assertEqual(result["workflow"], "W3")
        self.assertTrue(any("Q<60" in reason for reason in result["rationale"]))

    def test_possible_gate_makes_status_preliminary(self):
        result = MODULE.classify_item(issue(possible_hard_gates=["auth mention not confirmed"]))
        self.assertEqual(result["classification_status"], "preliminary")

    def test_batch_preserves_individual_routes(self):
        report = MODULE.classify_payload([
            issue(id="#1"),
            issue(id="#2", task_type="SECURITY", risk="R3", hard_gates=["security_boundary"]),
        ])
        self.assertEqual(report["classification_count"], 2)
        self.assertEqual(report["items"][0]["workflow"], "W1")
        self.assertEqual(report["items"][1]["workflow"], "W4")

    def test_string_boolean_is_rejected(self):
        with self.assertRaises(MODULE.InputError):
            MODULE.classify_item(issue(decomposable="false"))


if __name__ == "__main__":
    unittest.main()
