// Simple SPA loader for the week 5 lesson
let questions = [];
let answers = {};
let current = 0;

function loadQuestions() {
  fetch('questions.json')
    .then((r) => r.json())
    .then((qs) => {
      questions = qs;
      renderQuestion();
    });
}

function renderQuestion() {
  const root = document.getElementById('question-root');
  if (current >= questions.length) {
    root.innerHTML = '<p>Thank you for completing the lesson!</p>';
    return;
  }

  const q = questions[current];
  let form = '<form id="qform">';
  if (q.choices && q.choices.length) {
    form += q.choices
      .map((c) => `<label><input type="radio" name="choice" value="${c.id}"> ${c.text}</label>`)
      .join('<br>');
    form += '<br>';
  }
  form += '<button type="submit">Submit</button>';
  form += '<div id="error" style="color:red;margin-top:10px;"></div>';
  form += '</form>';

  root.innerHTML = q.html + form;
  document.getElementById('qform').addEventListener('submit', (ev) => {
    ev.preventDefault();
    let selected = null;
    if (q.choices && q.choices.length) {
      const chk = root.querySelector('input[name="choice"]:checked');
      if (q.required && !chk) {
        root.querySelector('#error').textContent = 'Please select an option.';
        return;
      }
      selected = chk ? chk.value : null;
    }

    answers[q.id] = selected;
    current++;
    renderQuestion();
  });
}

document.addEventListener('DOMContentLoaded', loadQuestions);
