# Lecture 12 Notes

**File:** Lecture 12-Small-Sample Inference for Means Student-t.pdf

## Overview
This lecture focuses on inference for means when sample sizes are small. It introduces the Student-t distribution, diagnostics for normality, one-sample and paired-sample t procedures, and compares pooled versus Welch approaches for two independent small samples.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Motivating example: tiny exit poll|Why $n<30$ and unknown $\sigma$ require new tools| | |
|3|Student t vs normal|Heavier tails due to using $s$|$T=\frac{\bar{x}-\mu}{s/\sqrt{n}}$ with $df=n-1$|Comparison plot|
|4|Checklist for small-sample methods|Sampling design and shape checks| |Decision tree|
|5|Histogram and QQ-plot diagnostics|Assess skew/outliers| | |
|6|Intuition behind QQ-plots| | |Explains 45-degree line|
|7|Sampling distribution of standardized $\bar{x}$|Behavior when $n<30$| | |
|8|CI formula for small samples| |$\bar{x}\pm t^*_{df} \frac{s}{\sqrt{n}}$| |
|9|Question comparing $t^*$ vs $z^*$|Which is larger when $df$ small| |Multiple choice concept|
|10|Worked example: local campaign donors|90% CI calculation| |Shows steps|
|11|Hypothesis testing roadmap|Five-step procedure| | |
|12|Worked example: time in booth|Two-sided t test for $\mu=6$| |Decision rule|
|13|Inference for paired samples|Why pairing helps| |Examples of before-after|
|14|Sampling distribution of mean difference|Definition of $d_i$ and $\bar{d}$|$T=\frac{\bar{d}-\mu_{d0}}{s_d/\sqrt{n}}$| |
|15|CI and test for mean difference| |$\bar{d}\pm t^*_{df} s_d/\sqrt{n}$| |
|16|Example: voter-ID law turnout|Compute 95% CI for differences| |Interval interpretation|
|17|Practice problem: paired data|Short example with $n=9$|$T$ compared to $t_{df}$|Yes/No reject|
|18|Inference for paired differences (large $n$)|Use $Z$ when $n\ge30$|$Z=\frac{\bar{d}-\mu_{d0}}{s_d/\sqrt{n}}$| |
|19|Comparing two small samples|Introduce problem of two groups| | |
|20|Why variance matters more|Plug-in noise for $s_1,s_2$| | |
|21|When & how to pool variances|Conditions for pooled $t$|$s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$|Decision rules|
|22|Welch $t$ statistic|Default approach|Formula for $df_{Welch}$ and $T$| |
|23|Pooled vs Welch decision tree|Flow chart| | |
|24|Example: civics quiz scores|Compute two-sample Welch $t$|Decision at $\alpha=0.05$|
|25|Common traps|Heteroskedasticity and imbalance| | |
|26|Key formulas and takeaways|Summary table| | |
|27|Welch degrees of freedom formula|Defines $df_{Welch}$|Formula with $s_1^2$, $s_2^2$|When variances unequal|
|28|Pooled vs Welch decision tree|Flow chart for choosing method| | |
|29|Example: civics quiz setup|Data for two small classes| |Stated hypotheses|
|30|Example: civics quiz calculation|Compute Welch $t$ and decision| |Reject or not|
|31|Common traps with two-sample t|Issues like heteroskedasticity| | |
|32|Cheat-sheet summary|Table of CI and test formulas| | |
