import re,docx
from docx.shared import Pt
base='/home/user/Immo/knjiga-govori/kako-iscijeliti-duh-i-tijelo/'
md=open(base+'Bildszenarien_Kako_iscijeliti_duh_i_tijelo.md').read()
d=docx.Document()
d.styles['Normal'].font.name='Calibri';d.styles['Normal'].font.size=Pt(11)
def para(line):
    p=d.add_paragraph()
    for part in re.split(r'(\*\*[^*]+\*\*)',line):
        if part.startswith('**'): p.add_run(part[2:-2]).bold=True
        elif part: p.add_run(part)
for line in md.split('\n'):
    if not line.strip(): continue
    if line.startswith('# '): d.add_heading(line[2:],0)
    elif line.startswith('## Szene'): d.add_heading(line[3:],1)
    elif line.startswith('## '): d.add_heading(line[3:],2)
    elif line.startswith('- '): para(line[2:]); d.paragraphs[-1].style='List Bullet'
    else: para(line)
d.save(base+'Bildszenarien_Kako_iscijeliti_duh_i_tijelo.docx')
