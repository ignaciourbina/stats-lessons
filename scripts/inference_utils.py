from math import sqrt, ceil
from statistics import NormalDist
from scipy.stats import t as _t_dist

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


def se_diff_means(sd1: float, n1: int, sd2: float, n2: int) -> float:
    """Standard error of the difference between two sample means."""
    return sqrt(sd1 ** 2 / n1 + sd2 ** 2 / n2)


def confidence_interval_mean(x_bar: float, sample_sd: float, n: int, alpha: float = 0.05):
    """Large-sample confidence interval for a population mean."""
    z = z_critical(alpha)
    se = se_mean(sample_sd, n)
    moe = z * se
    return x_bar - moe, x_bar + moe


def z_test_mean(x_bar: float, sample_sd: float, n: int, mu0: float) -> float:
    """Z test statistic for a population mean."""
    se = se_mean(sample_sd, n)
    return (x_bar - mu0) / se


def confidence_interval_diff_means(
    x_bar1: float,
    sample_sd1: float,
    n1: int,
    x_bar2: float,
    sample_sd2: float,
    n2: int,
    alpha: float = 0.05,
):
    """Large-sample confidence interval for the difference of two means."""
    diff = x_bar1 - x_bar2
    z = z_critical(alpha)
    se = se_diff_means(sample_sd1, n1, sample_sd2, n2)
    moe = z * se
    return diff - moe, diff + moe


def z_test_diff_means(
    x_bar1: float,
    sample_sd1: float,
    n1: int,
    x_bar2: float,
    sample_sd2: float,
    n2: int,
    diff0: float = 0.0,
) -> float:
    """Z test statistic for comparing two means."""
    diff = x_bar1 - x_bar2
    se = se_diff_means(sample_sd1, n1, sample_sd2, n2)
    return (diff - diff0) / se


def t_critical(alpha: float, df: int) -> float:
    """Two-sided t critical value with given degrees of freedom."""
    return _t_dist.ppf(1 - alpha / 2, df)


def t_confidence_interval_mean(x_bar: float, sample_sd: float, n: int, alpha: float = 0.05):
    """Small-sample confidence interval for a population mean (t-distribution)."""
    t = t_critical(alpha, n - 1)
    se = se_mean(sample_sd, n)
    moe = t * se
    return x_bar - moe, x_bar + moe


def t_test_mean(x_bar: float, sample_sd: float, n: int, mu0: float) -> float:
    """t statistic for testing a population mean."""
    se = se_mean(sample_sd, n)
    return (x_bar - mu0) / se


def _welch_df(sd1: float, n1: int, sd2: float, n2: int) -> float:
    var1 = sd1 ** 2 / n1
    var2 = sd2 ** 2 / n2
    return (var1 + var2) ** 2 / (var1 ** 2 / (n1 - 1) + var2 ** 2 / (n2 - 1))


def t_confidence_interval_diff_means(
    x_bar1: float,
    sample_sd1: float,
    n1: int,
    x_bar2: float,
    sample_sd2: float,
    n2: int,
    alpha: float = 0.05,
):
    """Welch confidence interval for difference of two means."""
    diff = x_bar1 - x_bar2
    se = se_diff_means(sample_sd1, n1, sample_sd2, n2)
    df = _welch_df(sample_sd1, n1, sample_sd2, n2)
    t = t_critical(alpha, df)
    moe = t * se
    return diff - moe, diff + moe


def t_test_diff_means(
    x_bar1: float,
    sample_sd1: float,
    n1: int,
    x_bar2: float,
    sample_sd2: float,
    n2: int,
    diff0: float = 0.0,
):
    """Welch t statistic for testing difference of two means."""
    diff = x_bar1 - x_bar2
    se = se_diff_means(sample_sd1, n1, sample_sd2, n2)
    df = _welch_df(sample_sd1, n1, sample_sd2, n2)
    return (diff - diff0) / se, df


def t_confidence_interval_paired(diff_mean: float, sd_diff: float, n: int, alpha: float = 0.05):
    """Confidence interval for mean paired difference."""
    t = t_critical(alpha, n - 1)
    se = se_mean(sd_diff, n)
    moe = t * se
    return diff_mean - moe, diff_mean + moe


def t_test_paired(diff_mean: float, sd_diff: float, n: int, diff0: float = 0.0) -> float:
    """t statistic for mean paired difference."""
    se = se_mean(sd_diff, n)
    return (diff_mean - diff0) / se
