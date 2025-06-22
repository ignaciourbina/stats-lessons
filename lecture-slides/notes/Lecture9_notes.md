# Lecture 9 Notes

**File:** Lecture 9-Inference for Two Proportions.pdf

## Overview
This lecture covers inference methods for comparing two independent population proportions. It introduces the sampling distribution of the difference in sample proportions, how to construct confidence intervals, and how to conduct hypothesis tests using a pooled estimator and standard error. Practical examples and common misconceptions are discussed throughout.

## Slide Summary
| Slide | Concepts Covered | Definitions | Formulas | Procedures or Examples |
|------|-----------------|-------------|----------|-----------------------|
|1|Title slide| | | |
|2|Motivation for categorical differences| | |Examples of policy and spending comparisons|
|3|Why compare proportions?| | |Applications in medicine, marketing, and social science|
|4|Example scenarios| | |Medical, marketing, and social science contexts|
|5|Public opinion example| | |Comparing support by age group|
|6|Psychological experiment example| | |CBT vs. MBSR treatment comparison|
|7|Notation for two proportions|Defines p1, p2, p̂1, p̂2, n1, n2| | |
|8|Statistic p̂1−p̂2| | |Goal to estimate p1−p2 and assess significance|
|9|Review of expectation and variance rules| |E(aX+bY)=aE(X)+bE(Y); Var(aX+bY)=a²Var(X)+b²Var(Y)| |
|10|Expectation of difference| |E(p̂1−p̂2)=p1−p2| |
|11|Variance of difference| |Var(p̂1−p̂2)=p1(1−p1)/n1 + p2(1−p2)/n2| |
|12|Standard error of difference| |SE(p̂1−p̂2)=√(p1(1−p1)/n1 + p2(1−p2)/n2)| |
|13|Sampling distribution| |p̂1−p̂2≈N(p1−p2, SE²)| |
|14|Deriving sampling distribution|Var(p̂)=p(1−p)/n|SE=√Var(p̂1−p̂2)| |
|15|Confidence interval formula| |(p̂1−p̂2)±z*SE| |
|16|Steps to build CI| | |Compute p̂1,p̂2, SE, MOE, then CI|
|17|Vaccination example setup| | |n1=400,p̂1=0.30; n2=500,p̂2=0.25|
|18|Vaccination example calculation| | |SE≈0.032; CI=[−0.013,0.113]|
|19|Interpreting CI| | |Interval includes 0 → no significant difference|
|20|Common misconceptions about CIs| | |Coverage, width, and interpretation errors|
|21|Summary of CI concepts| | |Importance of large samples and CI interpretation|
|22|Hypothesis testing intro| | |Testing significance of difference in proportions|
|23|Formulating hypotheses|Defines H0 and Ha| |One- and two-tailed alternatives|
|24|Test statistic under H0| |z=(p̂1−p̂2)/SE0| |
|25|Standard error under H0|Defines pooled proportion p̂|SE0=√(p̂(1−p̂)(1/n1+1/n2))| |
|26|Steps to compute z| | |Calculate p̂, SE0, then z|
|27|Decision rule and p-value| | |Reject H0 if |z|>critical value; p-value formula|
|28|Hypothesis test example setup| | |Vaccination data with x1=120,x2=125|
|29|Hypothesis test calculations| | |p̂≈0.272; SE0≈0.0299; z≈1.675|
|30|Example decision| | |Fail to reject H0; p-value≈0.094|
|31|Interpreting test results| | |Difference not significant; consider sample variability|
|32|Common misconceptions in tests| | |Non-significance doesn’t prove no difference, etc.|
|33|Final summary| | |Key points on hypothesis testing and interpretation|
