from pathlib import Path
from statistics import NormalDist

from quiz_validator import HtmlQuizValidator
from inference_utils import (
    se_proportion,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
)


class OneProportionValidator(HtmlQuizValidator):
    def compute_answers(self) -> dict[int, str]:
        norm = NormalDist()
        calc: dict[int, str] = {}

        p_hat = 45 / 120
        if abs(p_hat - 0.375) < 1e-3:
            calc[1] = "a"

        se = se_proportion(p_hat, 120)
        if abs(se - 0.044) < 0.001:
            calc[2] = "a"

        ci = confidence_interval_proportion(p_hat, 120)
        if abs(ci[0] - 0.29) < 0.01 and abs(ci[1] - 0.46) < 0.01:
            calc[3] = "a"

        z = z_test_proportion(p_hat, 120, 0.5)
        if abs(z + 2.74) < 0.01:
            calc[4] = "c"

        p_val = norm.cdf(z)
        if abs(p_val - 0.003) < 0.001:
            calc[5] = "a"

        n_req = sample_size_for_moe(0.04, p=0.4)
        if abs(n_req - 577) <= 1:
            calc[6] = "c"

        calc[7] = "b"
        calc[8] = "b"

        return calc


HTML_FILE = Path("interactive-problem-sets/inference-one-proportion/index.html")
OUTPUT_CSV = Path("inference_one_proportion_validation.csv")

if __name__ == "__main__":
    OneProportionValidator(HTML_FILE, OUTPUT_CSV).validate()
