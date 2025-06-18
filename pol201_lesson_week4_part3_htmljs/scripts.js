function loadPage(page) {
  fetch(page + '.html')
    .then(res => res.text())
    .then(html => {
      document.getElementById('content').innerHTML = html;
    });
}

document.addEventListener('DOMContentLoaded', () => loadPage('Page1'));

function checkAnswer(questionId, answer) {
  let message = '';
  switch (questionId) {
      case 'Q1':
        message = (answer === 'C') ? 'Correct!' : 'The correct answer is C. A hypothesis test allows researchers to assess statistical evidence by comparing observed data against a null hypothesis, which typically represents no effect or no difference. In the context of the clinical trial, the null hypothesis would state that the new medication has no effect on lowering blood pressure compared to a placebo. By analyzing the data, researchers calculate a p-value, which indicates the probability of observing the data if the null hypothesis were true. If this p-value is below a predetermined significance level (commonly 0.05), it suggests that the observed effect is unlikely due to chance alone, providing statistical evidence to reject the null hypothesis in favor of the alternative hypothesis, which claims that the medication does lower blood pressure. This process helps to ensure that the conclusions drawn are based on robust statistical analysis rather than random variation.';
        break;
      case 'Q2':
        message = (answer === 'C') ? 'Correct!' : 'C is the correct answer because in a two-tailed test, we are interested in determining whether there is any difference in the cure rate, either an increase or a decrease, compared to the historical cure rate of 30%. The null hypothesis (H0) states that the cure rate with the new drug is equal to 30%, meaning there is no effect. The alternative hypothesis (H1) states that the cure rate with the new drug is different from 30%, which could mean the cure rate is either higher or lower. This approach allows us to detect any significant deviation from the historical rate, regardless of the direction of the change.';
        break;
      case 'Q3':
        message = (answer === 'A') ? 'Correct!' : 'Answer A is correct because in a two-tailed test at a 95% confidence level, the critical value is 1.96. This value represents the z-score beyond which the null hypothesis can be rejected. The test statistic (Z) is calculated using the formula: Z = (p_hat - p_0) / \u221a(p_0 * (1 - p_0) / n), where p_hat is the sample proportion (0.367), p_0 is the historical proportion (0.30), and n is the sample size (150). The standard error (SE) is calculated using the null hypothesis proportion (p_0), not the sample proportion, to provide an accurate basis for the test statistic calculation. Plugging in the values, the test statistic is approximately 1.78.';
        break;
      case 'Q4':
        message = (answer === 'D') ? 'Correct!' : 'Answer D is correct because the test statistic (1.78) is less than the critical value (1.96), which means we fail to reject the null hypothesis. In layman terms, this means that the evidence from the clinical trial is not strong enough to prove that the new drug is more effective than the historical cure rate of 30%. Essentially, while the drug showed some promise, the results could have been due to random chance rather than a true effect of the drug. This is because in any study, there is always some uncertainty due to the variability in the data. We use statistical tests and the concept of statistical distributions to determine if the observed effect is likely to be real or just a result of this variability. Statistical distributions, like the standard normal distribution, help us understand the range of possible outcomes if there were no real effect (null hypothesis). The critical value is derived from this distribution and sets a threshold to determine whether the results are statistically significant.';
        break;
      case 'Q5':
        message = (answer === 'C') ? 'Correct!' : 'C is the correct answer.<br>1. State the null and alternative hypotheses: <br>Null hypothesis (H0): The true proportion of voters supporting Candidate A is 55% (p = 0.55). <br>Alternative hypothesis (H1): The true proportion of voters supporting Candidate A is greater than 55% (p > 0.55). <br><br>2. Calculate the sample proportion: <br>Sample proportion (p_hat) = 310 / 500 = 0.62. <br><br>3. Compute the standard error of the proportion assuming the null hypothesis: <br>Standard error (SE) = \u221a(0.55 * (1 - 0.55) / 500) = \u221a(0.55 * 0.45 / 500) \u2248 0.0222. <br><br>4. Calculate the test statistic (Z): <br>Z = (0.62 - 0.55) / 0.0222 \u2248 3.15. <br><br>5. Determine the critical value for a one-sided test at the 99% confidence level: <br>The critical value (z_99) for a one-sided test is 2.33. <br><br>6. Compare the test statistic to the critical value: <br>The test statistic (3.15) is greater than the critical value (2.33), so we reject the null hypothesis. <br><br>Conclusion: There is enough evidence to conclude that the true support for Candidate A is higher than 55%.';
        break;
  }
  return message;
}

function sendSelectedResponse(questionId) {
  const form = document.getElementById('form' + questionId);
  const selected = form.querySelector('input[name="selectedAns"]:checked');
  if (selected) {
    const message = checkAnswer(questionId, selected.value);
    document.getElementById('result' + questionId).innerHTML = '<i>' + message + '</i>';
  } else {
    alert('Please select an option.');
  }
}
