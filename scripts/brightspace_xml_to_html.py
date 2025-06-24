import os
import xml.etree.ElementTree as ET
from html import unescape


def parse_brightspace_xml(xml_path, output_dir):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    ns = {'d2l': 'http://desire2learn.com/xsd/d2lcp_v2p0'}

    container = root.find('.//section[@ident="CONTAINER_SECTION"]')
    if container is None:
        raise ValueError("Could not find container section")

    sections = container.findall('section')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    answers = {}
    page_files = []
    qnum = 1

    for i, sect in enumerate(sections, start=1):
        page_html = ''
        mat = sect.find('.//presentation_material/flow_mat/flow_mat/material/mattext')
        if mat is not None and mat.text:
            page_html += unescape(mat.text)

        for item in sect.findall('item'):
            qtext_elem = item.find('.//presentation/flow/material/mattext')
            qtext = unescape(qtext_elem.text or '') if qtext_elem is not None else ''
            lid = item.find('.//response_lid')
            cardinality = lid.attrib.get('rcardinality', 'Single') if lid is not None else 'Single'
            input_type = 'checkbox' if cardinality == 'Multiple' else 'radio'
            options = []
            for resp_label in item.findall('.//response_label'):
                opt_id = resp_label.attrib.get('ident')
                opt_text_elem = resp_label.find('.//material/mattext')
                opt_text = unescape(opt_text_elem.text or '') if opt_text_elem is not None else ''
                options.append((opt_id, opt_text))

            correct = []
            for resp in item.findall('.//respcondition'):
                varequal = resp.find('.//varequal')
                setvar = resp.find('setvar')
                if varequal is not None and setvar is not None and setvar.attrib.get('varname') == 'D2L_Correct':
                    correct.append(varequal.text)

            qid = f"Q{qnum}"
            answers[qid] = correct
            page_html += f"<div><p><b>{qtext}</b></p><form id='form{qid}'>"
            for opt_id, opt_text in options:
                page_html += f"<label><input type='{input_type}' name='selectedAns' value='{opt_id}'>{opt_text}</label>"
            page_html += f"</form><button onclick=\"sendSelectedResponse('{qid}','{cardinality}')\">Submit Answer</button><p id='result{qid}'></p></div>"
            qnum += 1

        nav = []
        if i > 1:
            nav.append(f"<button onclick=\"loadPage('Page{i-1}')\">Back</button>")
        if i < len(sections):
            nav.append(f"<button onclick=\"loadPage('Page{i+1}')\">Next</button>")
        if nav:
            page_html += f"<div class='nav'>{' '.join(nav)}</div>"

        page_file = os.path.join(output_dir, f"Page{i}.html")
        with open(page_file, 'w') as f:
            f.write(page_html)
        page_files.append(page_file)

    # write index.html
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Lesson</title><link rel='stylesheet' href='../styles.css'></head><body><div id='content'></div><script src='scripts.js'></script></body></html>")

    # write scripts.js
    with open(os.path.join(output_dir, 'scripts.js'), 'w') as f:
        f.write("function loadPage(page){fetch(page+'.html').then(r=>r.text()).then(h=>{document.getElementById('content').innerHTML=h;});}\n")
        f.write("document.addEventListener('DOMContentLoaded',()=>loadPage('Page1'));\n")
        f.write("const answers=" + str(answers) + "\n")
        f.write("function sendSelectedResponse(qid,card){const form=document.getElementById('form'+qid);let selected=[];form.querySelectorAll('input[name=selectedAns]:checked').forEach(i=>selected.push(i.value));let corr=answers[qid];let ok=(card=='Multiple'?selected.sort().toString()==corr.sort().toString():selected[0]==corr[0]);document.getElementById('result'+qid).innerHTML=ok?'Correct!':'That is incorrect.';}\n")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Convert Brightspace XML to simple HTML lesson')
    parser.add_argument('xml_path')
    parser.add_argument('output_dir')
    args = parser.parse_args()
    parse_brightspace_xml(args.xml_path, args.output_dir)
