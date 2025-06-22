from inference_utils import se_mean, confidence_interval_mean, t_confidence_interval_paired


def main():
    # Question 6
    se6 = se_mean(7, 100)
    print(f"Q6: SE={se6:.1f}")

    # Question 7
    ci7 = confidence_interval_mean(32.5, 7, 100, alpha=0.05)
    print(f"Q7: 95% CI=({ci7[0]:.1f}, {ci7[1]:.1f})")

    # Question 12
    ci12 = t_confidence_interval_paired(-1.8, 2.7, 10, alpha=0.05)
    print(f"Q12: 95% CI=({ci12[0]:.1f}, {ci12[1]:.1f})")


if __name__ == "__main__":
    main()
