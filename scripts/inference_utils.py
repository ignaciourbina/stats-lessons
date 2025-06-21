from math import sqrt, ceil
from statistics import NormalDist

_norm = NormalDist()


def se_mean(sample_sd: float, n: int) -> float:
    """Return standard error of the sample mean."""
    return sample_sd / sqrt(n)


def prob_mean_exceeds(threshold: float, mu: float, sigma: float, n: int) -> float:
    """Probability sample mean exceeds threshold using CLT."""
    se = sigma / sqrt(n)
    z = (threshold - mu) / se
    return 1 - _norm.cdf(z)


def se_proportion(p_hat: float, n: int) -> float:
    """Standard error of a sample proportion."""
    return sqrt(p_hat * (1 - p_hat) / n)


def confidence_interval_proportion(p_hat: float, n: int, alpha: float = 0.05):
    """Return lower and upper bounds of CI for proportion."""
    z = _norm.inv_cdf(1 - alpha / 2)
    se = se_proportion(p_hat, n)
    moe = z * se
    return p_hat - moe, p_hat + moe


def z_test_proportion(p_hat: float, n: int, p0: float) -> float:
    """Z test statistic for single proportion."""
    se = sqrt(p0 * (1 - p0) / n)
    return (p_hat - p0) / se


def sample_size_for_moe(moe: float, p: float = 0.5, alpha: float = 0.05) -> int:
    """Sample size needed for given margin of error for proportion."""
    z = _norm.inv_cdf(1 - alpha / 2)
    return ceil(z**2 * p * (1 - p) / moe**2)


def z_critical(alpha: float) -> float:
    """Two-sided z critical value for significance level alpha."""
    return _norm.inv_cdf(1 - alpha / 2)
