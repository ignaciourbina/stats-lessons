# Week 4 - Lecture 7 Notes

**File:** Week 4 - Lecture 7-Estimators and Sampling Distributions.pdf

## Overview
This lecture introduces key ideas about estimators, their properties, and how sampling distributions allow us to make inferences about population parameters. The presentation covers bias, efficiency, the Central Limit Theorem, and simulated examples illustrating sampling variability.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Introduction & motivation for studying estimators and sampling distributions| | | |
|3|Population parameters vs. sample estimators|Defines *population parameter* and *sample estimator*| | |
|4|Basic properties of estimators|Defines *unbiasedness*, *consistency*, *efficiency*| | |
|5|Bias and efficiency comparison|Defines bias as E[θ̂]−θ; efficiency via variance comparison|Bias = E[θ̂]−θ; V(θ̂₁)<V(θ̂₂)| |
|6|Bias vs. variance illustration| | |Graphical example|
|7|Using estimators for inference|Questions about inference on population mean| | |
|8|Sample variability simulation setup| | |R code to simulate Uniform(0,100)|
|9|Plot of simulated population data| | |Histogram|
|10|Random sampling from uniform population| | |R code generating three samples and means|
|11|Computing true mean and sample means| | |Shows calculated means|
|12|Visualizing the sampling process| | |Plots comparing samples to population|
|13|Understanding sampling variability|Explains uncertainty from repeated sampling| | |
|14|Definition of sampling distribution|Defines sampling distribution of an estimator| | |
|15|Example sampling distribution for normal population| |E[X̄]=µ; SE(X̄)=σ/√n| |
|16|Standard error vs. standard deviation|Defines standard error|SE(X̄)=σ/√n| |
|17|Review of normal distribution| |PDF formula|Empirical rule description|
|18|Standard normal PDF and CDF plot| | |Graph|
|19|CDF table of standard normal| | |Table of probabilities|
|20|Computing probabilities using standard normal| |Uses pnorm()|R example calculations|
|21|Z-scores & probability computations|Defines Z-score formula|Z=(X̄−µ)/(σ/√n)|Example calculation|
|22|Using standard normal CDF with Z-score| | | |
|23|Wrapping up normal CDFs → sampling distributions| | | |
|24|Distribution of sum of normal random variables| | | |
|25|Sampling distribution of X̄ when Xi∼N(µ,σ²)| | | |
|26|Sampling distribution of sample mean example|Assume X∼N(µ=50,σ²=25)| | |
|27|Recap of sampling distributions|Summarizes key points| | |
|28|Central Limit Theorem (CLT) statement|Defines CLT| | |
|29|Assumptions of the CLT|Lists independence, identical distribution, finite variance, large n| | |
|30|CLT simulated example: Uniform(20,80)| | |Density plots for different n|
|31|CLT example 2: Binomial(n=20,p=0.15)| | |Density plots for different n|
|32|Z-scores, CLT, and probability computations| |Z computation for sample mean| |
|33|Plug-in principle & CLT in practice|Approximate distribution using sample statistics|Ȳ≈N(Ȳ,s²/n)| |
|34|Law of Large Numbers (LLN)|States LLN|X̄ₙ→µ| |
|35|Using the CLT – practical example|Probability that sample mean>25 with n=400| |R code using pnorm|
|36|Conclusion slide with key takeaways|Summarizes estimators, sampling distributions, CLT, and Z-scores| | |
