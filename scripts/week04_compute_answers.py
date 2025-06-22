from math import sqrt
from statistics import NormalDist
from inference_utils import (
    se_proportion,
    confidence_interval_proportion,
    z_test_proportion,
    sample_size_for_moe,
    z_critical,
)


def main():
    norm = NormalDist()

    # Question 6
    p_hat6 = 66 / 120
    se6 = se_proportion(p_hat6, 120)
    print(f"Q6: p_hat={p_hat6:.2f}, SE={se6:.3f}")

    # Question 7
    ci7 = confidence_interval_proportion(p_hat6, 120, alpha=0.05)
    print(f"Q7: 95% CI=({ci7[0]:.2f}, {ci7[1]:.2f})")

    # Question 8
    p_hat8 = 220 / 400
    se8 = se_proportion(p_hat8, 400)
    ci99 = confidence_interval_proportion(p_hat8, 400, alpha=0.01)
    print(f"Q8: 99% CI=({ci99[0]:.2f}, {ci99[1]:.2f})")

    # Question 9
    z9 = z_test_proportion(0.52, 1000, 0.49)
    decision9 = "reject" if abs(z9) > z_critical(0.05) else "fail to reject"
    print(f"Q9: Z={z9:.1f}, {decision9} H0")

    # Question 10
    z10 = z_test_proportion(0.53, 1000, 0.50)
    p10 = 1 - norm.cdf(z10)
    decision10 = "reject" if p10 < 0.05 else "fail to reject"
    print(f"Q10: Z={z10:.2f}, P={p10:.2f}, {decision10} H0")

    # Question 12
    p_hat12 = 245 / 500
    se12 = se_proportion(p_hat12, 500)
    print(f"Q12: p_hat={p_hat12:.2f}, SE={se12:.3f}")

    # Question 13
    ci13 = confidence_interval_proportion(p_hat12, 500, alpha=0.10)
    print(f"Q13: 90% CI=({ci13[0]:.2f}, {ci13[1]:.2f})")

    # Question 14
    z14 = z_test_proportion(p_hat12, 500, 0.5)
    decision14 = "reject" if abs(z14) > z_critical(0.05) else "fail to reject"
    print(f"Q14: Z={z14:.2f}, {decision14} H0")

    # Question 17
    n17 = sample_size_for_moe(0.02, p=0.5, alpha=0.05)
    print(f"Q17: required n ~= {n17}")

    # Question 19
    sd19 = sqrt(500 * 0.60 * 0.40)
    print(f"Q19: SD count={sd19:.0f}")


if __name__ == "__main__":
    main()
