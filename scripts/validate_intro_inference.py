from pathlib import Path

from quiz_validator import HtmlQuizValidator
from inference_utils import (
    se_mean,
    prob_mean_exceeds,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
    z_critical,
)


class IntroInferenceValidator(HtmlQuizValidator):
    def compute_answers(self) -> dict[int, str]:
        calc: dict[int, str] = {}
        se = se_mean(10, 100)
        if abs(se - 1) < 1e-6:
            calc[4] = "c"
        prob = prob_mean_exceeds(52, 50, 10, 100)
        if abs(prob - 0.023) < 0.005:
            calc[5] = "b"
        p_hat = 120 / 400
        ci = confidence_interval_proportion(p_hat, 400)
        if abs(ci[0] - 0.255) < 0.005 and abs(ci[1] - 0.345) < 0.005:
            calc[6] = "b"
        z = z_test_proportion(0.48, 1000, 0.5)
        if abs(z + 1.27) < 0.05:
            calc[7] = "a"
        n_required = sample_size_for_moe(0.05, p=0.5)
        if n_required == 385:
            calc[9] = "c"
        zcrit = z_critical(0.01)
        if abs(zcrit - 2.576) < 0.01:
            calc[19] = "c"
        return calc

HTML_FILE = Path('interactive-problem-sets/introduction-to-inference/index.html')
OUTPUT_CSV = Path('intro_inference_validation.csv')

if __name__ == '__main__':
    IntroInferenceValidator(HTML_FILE, OUTPUT_CSV).validate()
