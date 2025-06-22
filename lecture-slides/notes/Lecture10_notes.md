# Lecture 10 Notes

**File:** Lecture 10-Sampling Distributions for Estimators of.pdf

## Overview
This lecture explains sampling distributions for the sample mean and the difference between two means. It reviews the Central Limit Theorem, the plug-in principle for estimating variance, and introduces normal and t-based methods used when comparing means.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Sampling distribution of the sample mean|Defines sample mean and sampling distribution|$E(\bar{x})=\mu$, $\operatorname{Var}(\bar{x})=\sigma^2/n$| |
|3|Case 1: normal population, known $\sigma^2$| |$Z=\frac{\bar{x}-\mu}{\sigma/\sqrt{n}}$| |
|4|Case 2: large sample CLT|CLT approximates distribution of $\bar{x}$|$\bar{x}\approx N(\mu,\sigma^2/n)$|Use CLT for inference|
|5|Plug-in principle|Estimate $\sigma^2$ with sample variance|$\widehat{SE}(\bar{x})=s/\sqrt{n}$|$Z\approx(\bar{x}-\mu)/(s/\sqrt{n})$|
|6|Case 3: small sample, unknown variance|Introduce t-distribution|$t=\frac{\bar{x}-\mu}{s/\sqrt{n}}$| |
|7|Why compare two means|Motivating examples from business and health| | |Scenarios such as job satisfaction or exercise studies|
|8|Setup for comparing two means|Two independent samples| | |Define $\bar{x}_1$, $\bar{x}_2$|
|9|Review of properties of $E$ and $\operatorname{Var}$|Linearity and independence rules|$E(aX+bY)=aE(X)+bE(Y)$; $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)$| |
|10|Expectation of the difference|Unbiasedness of $\bar{x}_1-\bar{x}_2$|$E(\bar{x}_1-\bar{x}_2)=\mu_1-\mu_2$| |
|11|Variance and SE of the difference| |$\operatorname{Var}(\bar{x}_1-\bar{x}_2)=\sigma_1^2/n_1+\sigma_2^2/n_2$|$SE=\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}$|
|12|Sampling distribution of difference (large samples)|Difference approx normal|$\bar{x}_1-\bar{x}_2\approx N(\mu_1-\mu_2,SE^2)$| |
|13|Plug-in principle for two means|Estimate SE using $s_1^2$ and $s_2^2$|$Z=\frac{(\bar{x}_1-\bar{x}_2)-\Delta_0}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$| |
|14|Small samples and t distribution|Need t when $n_1$ or $n_2$ small|$t=\frac{(\bar{x}_1-\bar{x}_2)-(\mu_1-\mu_2)}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$|Welch-Satterthwaite df|
|15|Summary and key assumptions|Importance of CLT, plug-in, and independence| |List main bullet points on Z vs t procedures|
