import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "aiio/weekend/materials/hermes-nca-aiio-100-english-question-blueprint-mock.html"
DATA = ROOT / "aiio/weekend/materials/data/hermes-nca-aiio-100-original-english-questions.json"
INDEX = ROOT / "aiio/weekend/index.html"
README = ROOT / "aiio/weekend/materials/README.md"


class NcaAiioEnglishQuestionBankContract(unittest.TestCase):
    def test_new_artifacts_exist_at_independent_paths(self):
        self.assertTrue(TARGET.exists())
        self.assertTrue(DATA.exists())
        self.assertNotEqual(TARGET.name, "hermes-nca-aiio-100-question-blueprint-mock.html")
        self.assertNotEqual(DATA.name, "hermes-nca-aiio-100-original-questions.json")
        self.assertIn(TARGET.name, INDEX.read_text(encoding="utf-8"))
        self.assertIn(TARGET.name, README.read_text(encoding="utf-8"))

    def test_json_has_100_valid_english_questions(self):
        questions = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(len(questions), 100)
        self.assertEqual([q["id"] for q in questions], list(range(1, 101)))
        self.assertEqual(len({q["question"].casefold() for q in questions}), 100)
        self.assertEqual([sum(q["answer"] == i for q in questions) for i in range(4)], [25, 25, 25, 25])
        allowed = {f"S{i}" for i in range(1, 30)}
        for q in questions:
            self.assertEqual(len(q["choices"]), 4)
            self.assertEqual(len({c.casefold() for c in q["choices"]}), 4)
            self.assertIn(q["answer"], range(4))
            self.assertTrue(q["explanation"].strip())
            self.assertTrue(q["source_keys"])
            self.assertTrue(set(q["source_keys"]) <= allowed)
            combined = q["question"] + " " + " ".join(q["choices"]) + " " + q["explanation"]
            self.assertIsNone(re.search(r"[\u3400-\u9fff]", combined))

    def test_blueprint_distribution_and_objective_coverage(self):
        questions = json.loads(DATA.read_text(encoding="utf-8"))
        counts = {d: sum(q["domain"] == d for q in questions) for d in ("essential", "infrastructure", "operations")}
        self.assertEqual(counts, {"essential": 38, "infrastructure": 40, "operations": 22})
        self.assertEqual({q["objective"] for q in questions if q["domain"] == "essential"}, {f"1.{i}" for i in range(1, 9)})
        self.assertEqual({q["objective"] for q in questions if q["domain"] == "infrastructure"}, {f"2.{i}" for i in range(1, 11)})
        self.assertEqual({q["objective"] for q in questions if q["domain"] == "operations"}, {f"3.{i}" for i in range(1, 5)})

    def test_html_is_fully_english_and_has_exam_features(self):
        html = TARGET.read_text(encoding="utf-8")
        self.assertIn('<html lang="en">', html)
        self.assertEqual(len(re.findall(r'<article class="question-card" id="q-(\d+)"', html)), 100)
        for marker in ["Start 60-Minute Timer", "Random 50-Question Mock", "Score Visible Questions", "localStorage", "@media print", "Original practice questions", "$125"]:
            self.assertIn(marker, html)
        self.assertNotIn("隨機抽", html)
        self.assertNotIn("計算成績", html)

    def test_does_not_claim_real_or_guaranteed_exam_content(self):
        html = TARGET.read_text(encoding="utf-8")
        self.assertIn("not actual or recalled exam questions", html)
        self.assertIn("does not guarantee a passing result", html)
        for forbidden in ["actual exam dump", "100% pass guarantee", "leaked questions"]:
            self.assertNotIn(forbidden, html.casefold())


if __name__ == "__main__":
    unittest.main(verbosity=2)
