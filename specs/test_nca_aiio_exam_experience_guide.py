from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "aiio/weekend/materials/nca-aiio-exam-experiences-prep-guide-2026.html"
INDEX = ROOT / "aiio/weekend/index.html"
README = ROOT / "aiio/weekend/materials/README.md"


class ExamExperienceGuideContract(unittest.TestCase):
    def test_published_artifact_and_entry_links_exist(self):
        self.assertTrue(GUIDE.exists())
        self.assertIn(GUIDE.name, INDEX.read_text(encoding="utf-8"))
        self.assertIn(GUIDE.name, README.read_text(encoding="utf-8"))

    def test_guide_is_native_traditional_chinese_html(self):
        html = GUIDE.read_text(encoding="utf-8")
        self.assertIn('<html lang="zh-Hant">', html)
        self.assertIn("NCA-AIIO 考試心得", html)
        self.assertNotIn("pptx", html.lower())
        self.assertGreater(len(html), 18000)

    def test_research_sections_and_action_plan_are_complete(self):
        html = GUIDE.read_text(encoding="utf-8")
        required = [
            "查核日期：2026-08-15",
            "來源與可信度",
            "網路心得共識",
            "高優先主題",
            "7 天衝刺計畫",
            "線上監考注意事項",
            "高風險資訊",
            "官方可驗證事實",
            "個人經驗",
            "商業性內容",
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, html)
        for day in range(1, 8):
            self.assertRegex(html, rf"第\s*{day}\s*天")

    def test_verified_sources_are_linked(self):
        html = GUIDE.read_text(encoding="utf-8")
        urls = [
            "https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/",
            "https://easontechtalk.com/nvidia-nca-aiio-exam/",
            "https://www.youtube.com/watch?v=lkdAejSj0KU",
            "https://www.youtube.com/watch?v=0WjfKQdfeMU",
            "https://github.com/mgonzalezo/nvidia-ai-infra-certs",
            "https://success.certiverse.com/hc/en-us/articles/49368408109211-System-Requirements-Live-and-Unproctored-Exams",
            "https://success.certiverse.com/hc/en-us/articles/50836785366811-Certiverse-Exam-Room-Preparation-and-Compliance-Requirements",
            "https://success.certiverse.com/hc/en-us/articles/49988952153115-What-to-Expect-During-a-Live-Proctored-Exam-Session",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertIn(f'href="{url}"', html)
        self.assertGreaterEqual(len(re.findall(r'target="_blank"', html)), len(urls))

    def test_no_guaranteed_pass_or_actual_question_claims(self):
        html = GUIDE.read_text(encoding="utf-8")
        self.assertIn("不保證通過", html)
        self.assertIn("不收錄未授權實際考題", html)
        self.assertNotIn("100% 必過", html)
        self.assertNotIn("保證必過", html)


if __name__ == "__main__":
    unittest.main()
