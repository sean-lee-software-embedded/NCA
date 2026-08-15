import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "aiio/weekend/materials/hermes-nca-aiio-100-question-blueprint-mock.html"
DATA = ROOT / "aiio/weekend/materials/data/hermes-nca-aiio-100-original-questions.json"

class NcaAiioQuestionBankContract(unittest.TestCase):
    def test_artifacts_exist_and_are_distinct(self):
        self.assertTrue(TARGET.exists())
        self.assertTrue(DATA.exists())
        self.assertNotEqual(TARGET.name, "hermes-nca-aiio-cert-pass-100-unit-reader.html")

    def test_json_has_exactly_100_original_questions(self):
        questions=json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(len(questions),100)
        self.assertEqual([q["id"] for q in questions],list(range(1,101)))
        self.assertEqual(len({q["question"] for q in questions}),100)
        self.assertEqual([sum(q["answer"]==i for q in questions) for i in range(4)],[25,25,25,25])
        self.assertEqual(set(q["objective"] for q in questions if q["domain"]=="essential"),{f"1.{i}" for i in range(1,9)})
        self.assertEqual(set(q["objective"] for q in questions if q["domain"]=="infrastructure"),{f"2.{i}" for i in range(1,11)})
        self.assertEqual(set(q["objective"] for q in questions if q["domain"]=="operations"),{f"3.{i}" for i in range(1,5)})
        allowed={f"S{i}" for i in range(1,19)}
        for q in questions:
            self.assertEqual(len(q["choices"]),4)
            self.assertEqual(len(set(q["choices"])),4)
            self.assertIn(q["answer"],range(4))
            self.assertTrue(q["explanation"].strip())
            self.assertTrue(q["source_keys"])
            self.assertTrue(set(q["source_keys"]) <= allowed)

    def test_blueprint_distribution(self):
        questions=json.loads(DATA.read_text(encoding="utf-8"))
        counts={d:sum(q["domain"]==d for q in questions) for d in ["essential","infrastructure","operations"]}
        self.assertEqual(counts,{"essential":38,"infrastructure":40,"operations":22})

    def test_html_embeds_full_bank_and_exam_features(self):
        html=TARGET.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r'<article class="question-card" id="q-(\d+)"',html)),100)
        for marker in ["60:00","隨機抽 50 題","計算成績","localStorage","@media print","非真實考題"]:
            self.assertIn(marker,html)
        self.assertIn("$125",html)

    def test_no_claim_of_guaranteed_pass_or_verified_past_questions(self):
        html=TARGET.read_text(encoding="utf-8")
        for forbidden in ["保證通過","真實考古題","actual exam questions","100% Pass Guarantee"]:
            self.assertNotIn(forbidden,html)

if __name__=="__main__": unittest.main(verbosity=2)
