from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
import csv
import re
from math import sqrt
from statistics import NormalDist

from inference_utils import (
    se_mean,
    prob_mean_exceeds,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
    z_critical,
    se_proportion,
)


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

    def compute_answers(self) -> dict[int, str]:
        calc: dict[int, str] = {}
        # Q4: SE of mean
        se = se_mean(10, 100)
        if abs(se - 1) < 1e-6:
            calc[4] = "c"
        # Q5: Probability mean exceeds 52
        prob = prob_mean_exceeds(52, 50, 10, 100)
        if abs(prob - 0.023) < 0.005:
            calc[5] = "b"
        # Q6: 95% CI for proportion
        p_hat = 120 / 400
        ci = confidence_interval_proportion(p_hat, 400)
        if abs(ci[0] - 0.255) < 0.005 and abs(ci[1] - 0.345) < 0.005:
            calc[6] = "b"
        # Q7: Z test statistic for proportion
        z = z_test_proportion(0.48, 1000, 0.5)
        if abs(z + 1.27) < 0.05:
            calc[7] = "a"
        # Q9: required sample size for MOE 0.05
        n_required = sample_size_for_moe(0.05, p=0.5)
        if n_required == 385:
            calc[9] = "c"
        # Q19: Z critical value for 99% CI
        zcrit = z_critical(0.01)
        if abs(zcrit - 2.576) < 0.01:
            calc[19] = "c"
        return calc


class LatexQuizValidator(QuizValidator):
    def __init__(self, quiz_tex: Path, answers_tex: Path, output_csv: Path):
        super().__init__(output_csv)
        self.quiz_tex = Path(quiz_tex)
        self.answers_tex = Path(answers_tex)

    def parse_answers(self) -> dict[int, str]:
        text = self.answers_tex.read_text()
        letters = re.findall(r"\\item\s*([A-D])", text)
        return {i + 1: letter.lower() for i, letter in enumerate(letters)}

    def compute_answers(self) -> dict[int, str]:
        norm = NormalDist()
        calc: dict[int, str] = {}
        # Q6
        p_hat6 = 66 / 120
        se6 = se_proportion(p_hat6, 120)
        if abs(p_hat6 - 0.55) < 0.01 and abs(se6 - 0.045) < 0.005:
            calc[6] = "a"
        # Q7
        ci7 = confidence_interval_proportion(p_hat6, 120, alpha=0.05)
        if abs(ci7[0] - 0.46) < 0.01 and abs(ci7[1] - 0.64) < 0.01:
            calc[7] = "a"
        # Q8
        p_hat8 = 220 / 400
        ci99 = confidence_interval_proportion(p_hat8, 400, alpha=0.01)
        if abs(ci99[0] - 0.49) < 0.01 and abs(ci99[1] - 0.61) < 0.01:
            calc[8] = "a"
        # Q9
        z9 = z_test_proportion(0.52, 1000, 0.49)
        if abs(z9 - 1.9) < 0.1 and abs(z9) < z_critical(0.05):
            calc[9] = "a"
        # Q10
        z10 = z_test_proportion(0.53, 1000, 0.50)
        p10 = 1 - norm.cdf(z10)
        if abs(p10 - 0.03) < 0.02 and p10 < 0.05:
            calc[10] = "a"
        # Q12
        p_hat12 = 245 / 500
        se12 = se_proportion(p_hat12, 500)
        if abs(p_hat12 - 0.49) < 0.01 and abs(se12 - 0.022) < 0.005:
            calc[12] = "a"
        # Q13
        ci13 = confidence_interval_proportion(p_hat12, 500, alpha=0.10)
        if abs(ci13[0] - 0.45) < 0.01 and abs(ci13[1] - 0.53) < 0.01:
            calc[13] = "a"
        # Q14
        z14 = z_test_proportion(p_hat12, 500, 0.5)
        if abs(z14 + 0.45) < 0.1 and abs(z14) < z_critical(0.05):
            calc[14] = "a"
        # Q17
        n17 = sample_size_for_moe(0.02, p=0.5, alpha=0.05)
        if abs(n17 - 2400) <= 1:
            calc[17] = "c"
        # Q19
        sd19 = sqrt(500 * 0.60 * 0.40)
        if abs(sd19 - 11) < 1:
            calc[19] = "a"
        return calc
