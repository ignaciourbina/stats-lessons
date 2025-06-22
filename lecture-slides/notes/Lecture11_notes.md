# Lecture 11 Notes

**File:** Lecture 11-Large-Sample Inference for Means.pdf

## Overview
This lecture applies the CLT and plug-in principle to construct confidence intervals and hypothesis tests for population means when the sample size is large. It covers both one-sample and two-sample situations, handling unknown variances, and extends to paired data.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Motivation and transition from proportions to means| | | |
|3|Central Limit Theorem recap|Approximate normality of $\bar{x}$|$\bar{x}\sim N(\mu,\sigma^2/n)$ for large $n$| |
|4|Handling unknown $\sigma$|Estimate with $s$|$Z=\frac{\bar{x}-\mu}{s/\sqrt{n}}$| |
|5|Large-sample CI structure| |$\bar{x}\pm z_{1-\alpha/2}\frac{s}{\sqrt{n}}$| |
|6|Margin of error components|Critical value and standard error| | |
|7|Interpreting a CI|Example statement of confidence| | |
|8|Example: commute time CI setup|Given $n$, $\bar{x}$, $s$| |Practical calculation|
|9|Example: commute time CI result|Shows numeric interval| | |
|10|Sampling distribution of difference $\bar{x}_1-\bar{x}_2$|Large-sample normality| | |
|11|Handling unknown variances for two means|Estimate with $s_1^2$ and $s_2^2$|$SE=\sqrt{s_1^2/n_1+s_2^2/n_2}$| |
|12|Large-sample CI for $\mu_1-\mu_2$| |$(\bar{x}_1-\bar{x}_2)\pm z_{1-\alpha/2}SE$| |
|13|Interpreting CI sign|Positive, zero, or negative interval meanings| | |
|14|Example: study methods CI setup| | |Two-group interval calculation|
|15|Example: study methods CI result|Numeric answer shown| | |
|16|Hypothesis testing intro|Steps for tests on means| | |
|17|Example: hours of sleep setup|Given $n$, $\bar{x}$, $s$| |Test against $7$ hours|
|18|Example: hours of sleep calc|Compute SE and $Z$| |Decision using $\alpha=0.05$|
|19|Example: new drug effectiveness|Two-sample test with difference| |Compare to critical value|
|20|Nonzero null values|Allow $\mu=\mu_0$ or $\mu_1-\mu_2=\Delta_0$|Adjusted $Z$ formulas| |
|21|Adjusted Z-statistic one mean| |$Z=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$| |
|22|Adjusted Z-statistic two means| |$Z=\frac{(\bar{x}_1-\bar{x}_2)-\Delta_0}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$| |
|23|Example: calories consumed setup|Test mean 2500| | |
|24|Example: calories consumed calc|Compute SE, $Z$, decision| | |
|25|Testing nonzero difference| |Null $\mu_1-\mu_2=\Delta_0$| |
|26|Adjusted Z-statistic formula again| | | |
|27|Example: manufacturing processes setup| | |Hypothesis test demonstration|
|28|Example: manufacturing processes calc|Compute SE, df, $Z$| |Decision at $\alpha=0.05$|
|29|Paired samples motivation|Why use before-after design| | |
|30|Paired samples CI & test|Use differences $d_i$|$\bar{d}\pm z_{1-\alpha/2} s_d/\sqrt{n}$|$Z=\frac{\bar{d}-\mu_{d0}}{s_d/\sqrt{n}}$|
|31|Example: sleep intervention CI|Paired-data calculation| |Resulting interval |
|32|Summary of key formulas|Table of CI and test statistics| | |
