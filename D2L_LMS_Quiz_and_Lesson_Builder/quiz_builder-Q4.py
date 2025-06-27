"""
Quiz 4 – Brightspace bulk-upload builder
---------------------------------------
Put this script in the same directory as `module_quiz_builder_to_csv.py`
(or leave the original .txt name and import via importlib) and run it.
It will write `quiz4.csv`, encoded UTF-8-BOM, ready for the Brightspace
“Bulk question upload” tool.
"""

from module_quiz_builder_to_csv import (
    QuestionBank,
    MultipleChoice,
    MCOption,
)

# ---------------------------------------------------------------------
# Build the question bank
# ---------------------------------------------------------------------
bank = QuestionBank()

# 1. Central Limit Theorem
bank.add(
    MultipleChoice(
        title="CLT – sampling distribution of x̄",html_used=True,
        question_text=r"""
<p>According to the <strong>Central Limit Theorem</strong>, what is the approximate sampling distribution of the sample mean for large <em>n</em> when sampling from a population with mean&nbsp;μ and standard deviation&nbsp;σ?</p>
""",
        options=[
            MCOption("N(μ, σ / √n)", 100, html_used=True),          # correct
            MCOption("N(0, 1)", 0, html_used=True),
            MCOption("N(μ, σ)", 0, html_used=True),
            MCOption("Binomial(μ, σ)", 0, html_used=True),
            MCOption("Same as the original distribution", 0, html_used=True),
        ],
    )
)

# 2. 95 % CI for a proportion
bank.add(
    MultipleChoice(
        title="Tutoring-program support – 95 % CI",html_used=True,
        question_text=r"""
<p>A <strong>school board</strong> is deliberating a new <strong>after-school tutoring program</strong> and surveys <strong>500 randomly selected parents</strong>; <strong>165</strong> support the program.  
Based on this sample, what is the <strong>95 % confidence interval</strong> for the true proportion of parents who support the program?</p>
""",
        options=[
            MCOption("0.33 ± 0.05", 0, html_used=True),
            MCOption("[0.289,&nbsp;0.371]", 100, html_used=True),   # correct
            MCOption("Between 0.30 and 0.36", 0, html_used=True),
            MCOption("[0.295,&nbsp;0.365]", 0, html_used=True),
            MCOption("0.29 ≤ p ≤ 0.37", 0, html_used=True),
        ],
    )
)

# 3. Z statistic for p ≠ 0.52 test
bank.add(
    MultipleChoice(
        title="Campus-shuttle support – Z statistic",html_used=True,
        question_text=r"""
<p>A <strong>university administration</strong> surveys <strong>1 200</strong> students; <strong>660&nbsp;(55 %)</strong> favor expanding the shuttle system.  
To test H<sub>0</sub>: p = 0.52 vs. H<sub>a</sub>: p ≠ 0.52, what is the value of the <strong>Z</strong> test statistic?</p>
""",
        options=[
            MCOption("−2.08", 0, html_used=True),
            MCOption("2.08", 100, html_used=True),                  # correct
            MCOption("−1.37", 0, html_used=True),
            MCOption("1.37", 0, html_used=True),
            MCOption("1.96", 0, html_used=True),
            MCOption("0", 0, html_used=True),
        ],
    )
)

# 4. Interpreting a 95 % CI for the mean
bank.add(
    MultipleChoice(
        title="PM₂.₅ CI interpretation",html_used=True,
        question_text=r"""
<p>An <strong>environmental agency</strong> samples <strong>50</strong> air-quality sites (mean 12.0 µg/m<sup>3</sup>, SD 3.2 µg/m<sup>3</sup>)  
and constructs a <strong>95 % confidence interval</strong>: <strong>[10.5 µg/m<sup>3</sup>, 13.5 µg/m<sup>3</sup>]</strong>.  
Which statement correctly interprets this interval?</p>
""",
        options=[
            MCOption("There is a 95 % probability that the <em>sample</em> mean lies between 10.5 µg/m³ and 13.5 µg/m³.", 0, html_used=True),
            MCOption("We are 95 % confident that the <strong>true</strong> mean PM₂.₅ concentration for all monitoring sites lies between 10.5 µg/m³ and 13.5 µg/m³.", 100, html_used=True),  # correct
            MCOption("95 % of all monitoring sites have concentrations between those limits.", 0, html_used=True),
            MCOption("If we repeated the study, there is a 95 % chance the <em>next</em> sample mean would fall inside the interval.", 0, html_used=True),
            MCOption("There is a 5 % probability that the true mean equals exactly 12.0 µg/m³.", 0, html_used=True),
        ],
    )
)

# 5. Definition of a population parameter
bank.add(
    MultipleChoice(
        title="Population parameter definition",html_used=True,
        question_text=r"""
<p>Which of the following best describes a <strong>population parameter</strong>?</p>
""",
        options=[
            MCOption("A theoretical value describing an entire population", 100, html_used=True),  # correct
            MCOption("A statistic computed from a sample", 0, html_used=True),
            MCOption("A random variable obtained from repeated sampling", 0, html_used=True),
            MCOption("The standard error of an estimator", 0, html_used=True),
        ],
    )
)

# 6. Meaning of “reject H₀ at α = 0.05”
bank.add(
    MultipleChoice(
        title="Interpreting rejection at 5 % level",html_used=True,
        question_text=r"""
<p>In hypothesis testing, what does it mean to <strong>reject the null hypothesis at the 5 % significance level</strong>?</p>
""",
        options=[
            MCOption("There is strong evidence that the null hypothesis is true.", 0, html_used=True),
            MCOption("There is sufficient statistical evidence to reject the null hypothesis in favour of the alternative hypothesis.", 100, html_used=True),  # correct
            MCOption("The probability that the null hypothesis is true is exactly 5 %.", 0, html_used=True),
            MCOption("The data were collected with a 5 % probability of measurement error.", 0, html_used=True),
        ],
    )
)

# 7. Z statistic for p < 0.25 one-sided test
bank.add(
    MultipleChoice(
        title="Cable-subscription rate – Z statistic",html_used=True,
        question_text=r"""
<p>A <strong>consumer advocacy group</strong> believes that <strong>fewer than 25 %</strong> of households still subscribe to cable TV.  
They survey <strong>600</strong> households and find <strong>126</strong> subscriptions.  
For H<sub>0</sub>: p = 0.25 vs. H<sub>a</sub>: p &lt; 0.25 at α = 0.05, what is the <strong>Z</strong> test statistic?</p>
""",
        options=[
            MCOption("−2.26", 100, html_used=True),                 # correct
            MCOption("2.26", 0, html_used=True),
            MCOption("−1.15", 0, html_used=True),
            MCOption("1.15", 0, html_used=True),
            MCOption("0", 0, html_used=True),
        ],
    )
)

# 8. Decision for the one-sided test
bank.add(
    MultipleChoice(
        title="Cable-subscription rate – test decision",html_used=True,
        question_text=r"""
<p>Using the Z statistic from Question 7 and α = 0.05 (one-sided), what is the correct <strong>test decision</strong>?</p>
""",
        options=[
            MCOption("Reject H₀; there is statistically significant evidence that <strong>fewer than 25 %</strong> of households still subscribe to cable TV.", 100, html_used=True),  # correct
            MCOption("Fail to reject H₀; the data do not provide sufficient evidence that the subscription rate is below 25 %.", 0, html_used=True),
            MCOption("Reject H₀; there is statistically significant evidence that <strong>more than 25 %</strong> of households still subscribe to cable TV.", 0, html_used=True),
            MCOption("Accept H₀; exactly 25 % of households subscribe to cable TV.", 0, html_used=True),
            MCOption("No decision can be made because the sample size is too small.", 0, html_used=True),
        ],
    )
)

# ---------------------------------------------------------------------
# Export to CSV
# ---------------------------------------------------------------------
bank.export_csv("quiz4.csv")
print("✅  quiz4.csv created – ready to import into Brightspace.")
