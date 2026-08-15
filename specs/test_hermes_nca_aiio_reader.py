import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "aiio/weekend/materials/hermes-nca-aiio-cert-pass-100-unit-reader.html"


class HermesNcaAiioReaderContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = TARGET.read_text(encoding="utf-8")

    def test_is_distinct_native_html_artifact(self):
        self.assertIn("<!doctype html>", self.html.lower())
        self.assertIn("NCA-AIIO", self.html)
        self.assertNotIn("PPTX", self.html)
        self.assertNotIn('class="slide"', self.html)

    def test_has_exactly_100_unique_reading_units(self):
        ids = re.findall(r'<article class="study-unit" id="unit-(\d+)"', self.html)
        self.assertEqual(ids, [str(i) for i in range(1, 101)])

    def test_matches_official_blueprint_weighting(self):
        self.assertEqual(self.html.count('data-domain="essential"'), 38)
        self.assertEqual(self.html.count('data-domain="infrastructure"'), 40)
        self.assertEqual(self.html.count('data-domain="operations"'), 22)

    def test_has_full_mock_exam(self):
        questions = re.findall(r'<details class="mock-question"', self.html)
        self.assertEqual(len(questions), 50)
        self.assertIn("60:00", self.html)

    def test_has_reader_features(self):
        for marker in ["id=\"search\"", "localStorage", "id=\"exam-timer\"", "@media print", "data-check"]:
            self.assertIn(marker, self.html)

    def test_has_verifiable_sources(self):
        self.assertGreaterEqual(self.html.count('class="source-link"'), 15)
        self.assertIn("ai-infrastructure-operations-associate", self.html)
        self.assertIn("docs.nvidia.com/datacenter/dcgm", self.html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
