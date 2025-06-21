# Week 4 - Lecture 8 Notes

**File:** Week 4 - Lecture 8-Statistical Inference for One Proportion.pdf

## Overview
This lecture introduces statistical inference for a single proportion. Topics include the sampling distribution of the sample proportion, constructing confidence intervals, and performing hypothesis tests for proportions.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Learning objectives| | | |
|3|Sample proportion sampling distribution| | | |
|4|Inference with proportions|Defines population proportion (p) and sample proportion (p̂)|p̂ = S/n| |
|5|Intuition behind inference|Explains sampling variability concept| | |
|6|Visualizing sample variability in vaccination rates| | |Figure showing p̂ across samples|
|7|Sample proportion notation|Defines sample as {Xi} and p̂ = (1/n)∑Xi| | |
|8|Expectation and variance of p̂|E[p̂]=p ; Var(p̂)=p(1−p)/n|p̂ formula| |
|9|Sampling distribution of p̂|Uses CLT approximation|p̂≈N(p, p(1−p)/n)| |
|10|Confidence intervals overview| | | |
|11|Definition of a confidence interval| | | |
|12|Confidence interval formula| |p̂±1.96√(p(1−p)/n)| |
|13|Calculating the confidence interval range| | |Shows probability step to derive CI|
|14|Logic behind the CI derivation|Explains standardization with Z-scores| | |
|15|Anatomy of a confidence interval| | |Discusses role of confidence level|
|16|Intuition behind confidence intervals|Long-run capture rate explanation| | |
|17|Estimating the standard error| |SE≈√(p̂(1−p̂)/n)| |
|18|Margin of error|MOE = z_{1−α/2} × SE| | |
|19|Constructing the confidence interval| | |CI = [p̂ − MOE, p̂ + MOE]|
|20|General CI formula for p| |p̂ ± z_{1−α/2} √(p̂(1−p̂)/n)| |
|21|Steps for a 99% confidence interval| | |List critical value, SE, MOE, CI|
|22|Applied example of CI|Sample of 400 with 120 successes| | |
|23|Step 1: calculate SE| |SE = √(p̂(1−p̂)/n)|Computation example|
|24|Step 2: 95% CI| | |MOE=1.96×SE; compute interval|
|25|Step 3: 99% CI| | |MOE=2.576×SE; compute interval|
|26|Interpretation of intervals|Compare widths| | |
|27|Future sample proportions vs. CI|Discusses why CI coverage is about p, not future p̂| | |
|28|Hypothesis testing introduction| | | |
|29|Why test hypotheses?| | |Examples of baseline vs alternative|
|30|How hypothesis testing works|Explains null vs alternative, decision rule| | |
|31|Introducing the test statistic|Defines test statistic| | |
|32|Understanding the test statistic|Discusses scale (standardized)| | |
|33|Formal hypothesis test setup|Shows H₀: p=p₀ and Hₐ alternatives| | |
|34|Significance level intuition|Defines α as tolerance for error| | |
|35|Example: voting preference test setup| | | |
|36|Solution: test statistic and conclusion|Compute Z and compare to critical value| | |
|37|Rejection region and critical values|Provides formulas for two-sided and one-sided tests| | |
|38|Understanding the P-value|Defines P-value and formulas| | |
|39|P-value and significance levels| | |Interpretation example|
|40|Example: computing one-sided P-value|Sample with p̂=0.52, n=1000|Z = 1.265; P-value=0.103| |
