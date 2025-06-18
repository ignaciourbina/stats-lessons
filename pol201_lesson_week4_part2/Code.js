function doGet() {
    return HtmlService.createHtmlOutputFromFile('Index');
}

function checkAnswer(questionId, answers) {
  var response = {};
  switch (questionId) {

      case 'Q1': // Simple multiple choice
          if (answers === 'B') {
              response.message = "Correct!";
          } else {
              response.message = "The correct answer is B: A parameter is a fixed value that describes a characteristic of a population, while an estimator is a rule or formula used to calculate an estimate of the parameter based on sample data. This distinction highlights that a parameter is an actual value characterizing a population (like the mean age of all people in a city), which typically cannot be known exactly and must be estimated. An estimator, on the other hand, is the method or rule (like using the average age from a sample of people) to estimate that parameter.";
          }
          break;
      case 'Q2': // Simple multiple choice
          if (answers === 'B') {
              response.message = "Correct!";
          } else {
              response.message = "The correct answer is B: Because it allows us to use sample data to make inferences about the population mean, even if the population distribution is not normal, given a sufficiently large sample size. The Central Limit Theorem (CLT) is significant because it states that as the size of the sample increases, the sample mean will be approximately normally distributed, regardless of the shape of the population distribution. This property allows for the use of normal distribution assumptions in hypothesis testing and confidence intervals when dealing with sample means.";
          }
          break;
      case 'Q3': // Simple multiple choice
          if (answers === 'A') {
              response.message = "Correct!";
          } else {
              response.message = "Suppose you have a sample of 200 students, and you find that 60 of them prefer online learning. The sample proportion p is calculated as follows: p = Number of students preferring online learning / Total sample size = 60 / 200 = 0.3. Using the SE formula: SE = √(0.3(1-0.3) / 200) = √(0.3*0.7 / 200) = √(0.21 / 200) = √(0.00105) ≈ 0.0324. The Standard Error of the sample proportion is approximately 0.0324, which indicates the variability of the sampling distribution.";
          }
          break;
    case 'Q4': // Simple multiple choice
        if (answers === 'D') {
            response.message = "Correct!";
        } else {
            response.message = "The correct statement is D: The interval from 52% to 58% will contain the true population proportion with 95% of confidence. This interpretation properly reflects that the confidence interval is constructed so that it captures the true population proportion in a certain percentage of all possible samples, given that the sampling process is repeated under the same conditions.";
        }
        break;

        case 'Q5': // Is the sample size large enough for the normal approximation?
          if (answers === 'A') {
              response.message = "Correct!";
          } else {
              response.message = "To calculate the 95% confidence interval, follow these steps:<br> Calculate the Sample Proportion (p): Divide the number of satisfied customers by the total number of respondents.<br> Sample Proportion (p) = 175 / 250 = 0.70<br><br> Calculate the Standard Error (SE): Use the formula SE = √{p(1-p) / n}, where n is the sample size.<br> SE = √{0.70 * 0.30 / 250} ≈ 0.028<br><br> Determine the Critical Value (z): For a 95% confidence level, refer to the z-table to find the critical value, which is approximately 1.96 for a two-tailed test.<br><br> Calculate the Margin of Error: Multiply the standard error by the critical value.<br> Margin of Error = 1.96 * 0.028 ≈ 0.055<br><br> Construct the Confidence Interval: Add and subtract the margin of error from the sample proportion to find the upper and lower bounds.<br> Lower Bound = 0.70 - 0.055 ≈ 0.645<br> Upper Bound = 0.70 + 0.055 ≈ 0.755<br><br> The 95% confidence interval for the population proportion of satisfied customers is approximately from 0.645 to 0.755.";
          }
          break;
    
  }
  return response;
}

function getPage(pageName) {
    return HtmlService.createHtmlOutputFromFile(pageName).getContent();
}