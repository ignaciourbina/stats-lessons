from pathlib import Path
from math import sqrt
from statistics import NormalDist

from quiz_validator import LatexQuizValidator
from inference_utils import (
    se_proportion,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
    z_critical,
)


class Week04Validator(LatexQuizValidator):
    def compute_answers(self) -> dict[int, str]:
        norm = NormalDist()
        calc: dict[int, str] = {}
        p_hat6 = 66 / 120
        se6 = se_proportion(p_hat6, 120)
        if abs(p_hat6 - 0.55) < 0.01 and abs(se6 - 0.045) < 0.005:
            calc[6] = "a"
        ci7 = confidence_interval_proportion(p_hat6, 120, alpha=0.05)
        if abs(ci7[0] - 0.46) < 0.01 and abs(ci7[1] - 0.64) < 0.01:
            calc[7] = "a"
        p_hat8 = 220 / 400
        ci99 = confidence_interval_proportion(p_hat8, 400, alpha=0.01)
        if abs(ci99[0] - 0.49) < 0.01 and abs(ci99[1] - 0.61) < 0.01:
            calc[8] = "a"
        z9 = z_test_proportion(0.52, 1000, 0.49)
        if abs(z9 - 1.9) < 0.1 and abs(z9) < z_critical(0.05):
            calc[9] = "a"
        z10 = z_test_proportion(0.53, 1000, 0.50)
        p10 = 1 - norm.cdf(z10)
        if abs(p10 - 0.03) < 0.02 and p10 < 0.05:
            calc[10] = "a"
        p_hat12 = 245 / 500
        se12 = se_proportion(p_hat12, 500)
        if abs(p_hat12 - 0.49) < 0.01 and abs(se12 - 0.022) < 0.005:
            calc[12] = "a"
        ci13 = confidence_interval_proportion(p_hat12, 500, alpha=0.10)
        if abs(ci13[0] - 0.45) < 0.01 and abs(ci13[1] - 0.53) < 0.01:
            calc[13] = "a"
        z14 = z_test_proportion(p_hat12, 500, 0.5)
        if abs(z14 + 0.45) < 0.1 and abs(z14) < z_critical(0.05):
            calc[14] = "a"
        n17 = sample_size_for_moe(0.02, p=0.5, alpha=0.05)
        if abs(n17 - 2400) <= 1:
            calc[17] = "c"
        sd19 = sqrt(500 * 0.60 * 0.40)
        if abs(sd19 - 11) < 1:
            calc[19] = "a"
        return calc


QUIZ_TEX = Path("weekly-quizzes/week04_quiz.tex")
ANSWERS_TEX = Path("weekly-quizzes/week04_answers.tex")
OUTPUT_CSV = Path("week04_validation.csv")

if __name__ == "__main__":
    Week04Validator(QUIZ_TEX, ANSWERS_TEX, OUTPUT_CSV).validate()
