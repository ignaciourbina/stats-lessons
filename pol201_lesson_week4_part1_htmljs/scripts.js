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
      message = (answer === 'B') ? 'Correct!' : 'That is incorrect. Here is the correct calculation: Z = (X - mean)/sd = (40 - 55)/10 = -1.5.';
      break;
    case 'Q2':
      message = (answer === 'A') ? 'Correct!' : 'That is incorrect. Here is the correct calculation: Z = (X - mean)/sd = (65 - 55)/10 = 1.0.';
      break;
    case 'Q3':
      message = (answer === 'B') ? 'Correct!' : 'That is incorrect. Here is the correct calculation: P(X<=40) is the same as P(Z<=(40 - 55)/10). Thus, if we look the correct row and column of the z-table we will find that P(Z<=-1.5)=0.0668. Note: Search the value where the row is Z=-1.5 and the column is 0.00.';
      break;
    case 'Q4':
      message = (answer === 'C') ? 'Correct!' : 'That is incorrect. Here is the correct calculation: To find P(X >= 65), we calculate 1 - P(X < 65). Transforming the score, Z = (65 - 55) / 10 = 1. Using the z-table, we find P(Z <= 1) = 0.8413. Therefore, P(Z >= 1) = 1 - P(Z <= 1) = 1 - 0.8413 = 0.1587.';
      break;
    case 'Q5':
      message = (answer === 'A') ? 'Correct!' : 'That is incorrect. The sample size is sufficiently large because np = 120 and n(1-p) = 280, both greater than 10, which are the conditions needed for the normal approximation to the binomial distribution.';
      break;
    case 'Q6':
      message = (answer === 'A') ? 'Correct!' : 'That is incorrect. The correct calculation involves normal approximation where Z = (140 - 120) / 9.13 = 2.19. Then, Pr(Z>2.19) = 1 - Pr(Z<=2.19). Since Pr(Z<=2.19)=0.9857, this leads to a probability of Pr(Z>2.19)=1.43% which falls under the option \'Less than 10%\'.';
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
