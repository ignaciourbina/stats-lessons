import json
import re
from pathlib import Path
import sys

# Ensure the quiz builder module is importable when running this script
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR / "D2L_LMS_Quiz_and_Lesson_Builder"))

from module_quiz_builder_to_csv import (
    QuestionBank,
    MultipleChoice,
    MCOption,
    SectionHeader,
)

def clean_html(text: str) -> str:
    """Remove meta, title and style tags unsupported in Brightspace."""
    text = re.sub(r"<meta[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<title[^>]*>.*?</title>", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.IGNORECASE | re.DOTALL)
    return text.strip()

def convert(json_path: Path, csv_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    bank = QuestionBank()
    slide_num = 1
    qnum = 1
    for item in data:
        html = clean_html(item.get("html", ""))
        if item.get("choices"):
            options = [MCOption(percent=0, text=c["text"], html_used=True) for c in item["choices"]]
            mc = MultipleChoice(
                title=f"Question {qnum}",
                question_text=html,
                points=0,
                options=options,
                html_used=True,
            )
            bank.add(mc)
            qnum += 1
        else:
            bank.add(SectionHeader(title=f"Slide {slide_num}", body_html=html))
            slide_num += 1
    bank.export_csv(csv_path)
    print(f"\u2713 Wrote {csv_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert lesson JSON to D2L CSV")
    parser.add_argument("json", type=Path, help="Path to questions.json")
    parser.add_argument("csv", type=Path, help="Output CSV path")
    args = parser.parse_args()
    convert(args.json, args.csv)
