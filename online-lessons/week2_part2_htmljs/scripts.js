function loadPage(page){fetch(page+'.html').then(r=>r.text()).then(h=>{document.getElementById('content').innerHTML=h;});}
document.addEventListener('DOMContentLoaded',()=>loadPage('Page1'));
const answers={'Q1': [], 'Q2': [], 'Q3': [], 'Q4': [], 'Q5': [], 'Q6': []}
function sendSelectedResponse(qid,card){const form=document.getElementById('form'+qid);let selected=[];form.querySelectorAll('input[name=selectedAns]:checked').forEach(i=>selected.push(i.value));let corr=answers[qid];let ok=(card=='Multiple'?selected.sort().toString()==corr.sort().toString():selected[0]==corr[0]);document.getElementById('result'+qid).innerHTML=ok?'Correct!':'That is incorrect.';}
