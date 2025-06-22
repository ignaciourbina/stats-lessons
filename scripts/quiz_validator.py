from __future__ import annotations

"""Utility classes for validating quiz answer files."""

from abc import ABC, abstractmethod
from pathlib import Path
import csv
import re


class QuizValidator(ABC):
    """Abstract base class for quiz validation."""

    def __init__(self, output_csv: Path):
        self.output_csv = Path(output_csv)

    @abstractmethod
    def parse_answers(self) -> dict[int, str]:
        """Return mapping of question id to recorded answer letter."""

    @abstractmethod
    def compute_answers(self) -> dict[int, str]:
        """Return mapping of question id to calculated answer letter."""

    def write_report(self, parsed: dict[int, str], computed: dict[int, str]) -> None:
        with self.output_csv.open("w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["question_id", "file_answer", "calculated_answer", "match"])
            for qid in sorted(computed):
                file_ans = parsed.get(qid)
                calc_ans = computed[qid]
                writer.writerow([qid, file_ans, calc_ans, file_ans == calc_ans])

    def validate(self) -> None:
        parsed = self.parse_answers()
        computed = self.compute_answers()
        self.write_report(parsed, computed)


class HtmlQuizValidator(QuizValidator):
    def __init__(self, html_file: Path, output_csv: Path):
        super().__init__(output_csv)
        self.html_file = Path(html_file)

    def parse_answers(self) -> dict[int, str]:
        text = self.html_file.read_text()
        pattern = re.compile(r"{\s*id:\s*(\d+).*?correctAnswer:\s*\"([a-d])\"", re.S)
        return {int(qid): ans for qid, ans in re.findall(pattern, text)}

    @abstractmethod
    def compute_answers(self) -> dict[int, str]:
        """Return mapping of question id to calculated answer letter."""


class LatexQuizValidator(QuizValidator):
    def __init__(self, quiz_tex: Path, answers_tex: Path, output_csv: Path):
        super().__init__(output_csv)
        self.quiz_tex = Path(quiz_tex)
        self.answers_tex = Path(answers_tex)

    def parse_answers(self) -> dict[int, str]:
        text = self.answers_tex.read_text()
        letters = re.findall(r"\\item\s*([A-D])", text)
        return {i + 1: letter.lower() for i, letter in enumerate(letters)}

    @abstractmethod
    def compute_answers(self) -> dict[int, str]:
        """Return mapping of question id to calculated answer letter."""
