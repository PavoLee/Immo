import re,sys
sys.path.insert(0,'.')
from scenes import S,LIKOVI
base='/home/user/Immo/knjiga-govori/kako-iscijeliti-duh-i-tijelo/'
t=open(base+'Kako iscijeliti duh i tijelo - Scenarij.md').read()
START="Ilustracija u stilu Hanne Lee Tidd, crno-bijeli ručno crtani olovčani crtež u kojem su glavne boje crna i zlatna, format 16:9, potpuno bijela pozadina, bez ikakvog teksta, slova, brojeva, logotipa i vodenog žiga, bez olovke kao predmeta u slici: glavni motiv je "
END=" Crtež je visokokvalitetan, elegantan i profesionalan, ručno crtan, s finim sjenčanjem i detaljnim linijama, zlato se koristi isključivo kao svjetleći naglasak, prirodno svjetlo sa zlatnim svjetlom kao glavnim izvorom, realistične ljudske proporcije, jasna, filmska i skladna kompozicija sa snažnom dubinom, motivirajuća, nadahnjujuća i emocionalna atmosfera koja priča emocionalnu priču."
ANIM=" Calm cinematic motion, keep the black and white hand-drawn pencil style with gold accents, no text."
# sentences per line
def position(p):
    for line in t.split('\n'):
        if p in line:
            if line.startswith('#'):
                return 'Nakon naslova „'+line.lstrip('# ').strip()+'“'
            sents=re.split(r'(?:(?<=[.!?])|(?<=[.!?]“))\s+(?=[A-ZČĆŠŽĐ„])',line)
            # rejoin sentences broken inside quotes
            for s in sents:
                if p in s: return 'Nakon rečenice „'+s.strip()+'“'
            return 'Nakon rečenice „'+line.strip()+'“'
out=['# Bildszenarien: „Kako iscijeliti duh i tijelo“ („You Can Heal Your Life“)','','Louise Hay · Kanal: Knjiga Govori · 100 scena','',
'## Likovi koji se ponavljaju (identični u svim scenama)','']
for n,d in LIKOVI: out.append(f'- **{n}:** {d}')
out+=['','Napomena: Kad prvi put nastane uspješna slika nekog lika, u svim daljnjim scenama s tim likom priložite je u Flowu kao referentnu sliku.','']
for i,(p,m,a) in enumerate(S,1):
    out+=[f'## Szene {i:02d}','',f'**Position im Skript:** {position(p)}','',f'**Bildprompt:** {START}{m}{END}','',f'**Animacija (Flow):** {a}{ANIM}','']
open(base+'Bildszenarien_Kako_iscijeliti_duh_i_tijelo.md','w').write('\n'.join(out))
# --- Audio parts
blocks=[];cur=None
for line in t.split('\n'):
    if not line.strip(): continue
    if line.startswith('#'):
        h=line.lstrip('# ').strip()
        if line.startswith('### '): h=h[0]+h[1:].lower()
        cur={'title':h,'paras':[h]};blocks.append(cur)
    else: cur['paras'].append(line.strip())
wc=lambda b:sum(len(x.split()) for x in b['paras'])
parts=[];p=[]
for b in blocks:
    if p and sum(map(wc,p))+wc(b)>560 and sum(map(wc,p))>=300:
        parts.append(p);p=[]
    p.append(b)
parts.append(p)
a=['# Audio Teile: Kako iscijeliti duh i tijelo','','Für Google AI Studio (Gemini 2.5 Flash Preview TTS, The Patient Teacher, Enceladus, Sample Context „read in croatian“, Temperature 1.1). Überschriften der Prinzipien sind schon in normale Schreibweise umgewandelt.','','| Nr. | Dateiname | Inhalt | Wörter |','|---|---|---|---|']
for i,p in enumerate(parts,1):
    a.append(f'| {i:02d} | {i:02d}_Kako_iscijeliti_duh_i_tijelo_Audio.wav | {p[0]["title"]} bis {p[-1]["title"]} | {sum(map(wc,p))} |')
a.append('')
for i,p in enumerate(parts,1):
    a+=[f'## Teil {i:02d}','','```']+['\n\n'.join(x for b in p for x in b['paras'])]+['```','']
open(base+'Audio_Teile_Kako_iscijeliti_duh_i_tijelo.md','w').write('\n'.join(a))
for i,p in enumerate(parts,1): print(i,sum(map(wc,p)),p[0]['title'][:40],'->',p[-1]['title'][:40])
