import csv
import re
from pathlib import Path

from inference_utils import (
    se_mean,
    prob_mean_exceeds,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
    z_critical,
)

HTML_FILE = Path('interactive-problem-sets/introduction-to-inference/index.html')
OUTPUT_CSV = Path('intro_inference_validation.csv')


def parse_correct_answers(html_text: str):
    pattern = re.compile(r'{\s*id:\s*(\d+).*?correctAnswer:\s*"([a-d])"', re.S)
    return {int(qid): ans for qid, ans in re.findall(pattern, html_text)}


def main():
    html_text = HTML_FILE.read_text()
    answers = parse_correct_answers(html_text)

    # Hard-coded calculations for numeric questions
    calculated = {}

    # Q4: SE of mean
    se = se_mean(10, 100)
    calculated[4] = 'c' if abs(se - 1) < 1e-6 else None

    # Q5: Probability mean exceeds 52
    prob = prob_mean_exceeds(52, 50, 10, 100)
    calculated[5] = 'b' if abs(prob - 0.023) < 0.005 else None

    # Q6: 95% CI for proportion
    p_hat = 120 / 400
    ci = confidence_interval_proportion(p_hat, 400)
    if abs(ci[0] - 0.255) < 0.005 and abs(ci[1] - 0.345) < 0.005:
        calculated[6] = 'b'
    else:
        calculated[6] = None

    # Q7: Z test statistic for proportion
    z = z_test_proportion(0.48, 1000, 0.5)
    calculated[7] = 'a' if abs(z + 1.27) < 0.05 else None

    # Q9: required sample size for MOE 0.05
    n_required = sample_size_for_moe(0.05, p=0.5)
    calculated[9] = 'c' if n_required == 385 else None

    # Q19: Z critical value for 99% CI
    zcrit = z_critical(0.01)
    calculated[19] = 'c' if abs(zcrit - 2.576) < 0.01 else None

    with OUTPUT_CSV.open('w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['question_id', 'html_answer', 'calculated_answer', 'match'])
        for qid in sorted(calculated):
            html_ans = answers.get(qid)
            calc_ans = calculated[qid]
            writer.writerow([qid, html_ans, calc_ans, html_ans == calc_ans])


if __name__ == '__main__':
    main()
