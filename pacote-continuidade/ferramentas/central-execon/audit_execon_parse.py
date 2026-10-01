# -*- coding: utf-8 -*-
"""Extrai textos do dossiê Execon (30, 31, HUB) e o envelope (20) para a auditoria.
Só lê; grava um JSON intermediário no scratchpad."""
import re, ast, json, unicodedata, pathlib

BASE = pathlib.Path('/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad')
D = BASE / 'dossie-grupo-execon'
ENV = (D / '20-envelope.md').read_text(encoding='utf-8')
TXT = (D / '30-textos.md').read_text(encoding='utf-8')
CAT = (D / '31-catalogo.md').read_text(encoding='utf-8')
SRC = (BASE / 'execon_src.py').read_text(encoding='utf-8')

out = {}

# ---------- normalização
def nfc_report(name, s):
    comb = sum(1 for ch in s if unicodedata.combining(ch))
    return {'file': name, 'is_NFC': unicodedata.is_normalized('NFC', s), 'combining_marks': comb}
out['nfc'] = [nfc_report(n, s) for n, s in [('20', ENV), ('30', TXT), ('31', CAT), ('src', SRC)]]

# ---------- envelope
facts = {}
for m in re.finditer(r'^- \[(fact\.[a-z_]+\.\d{3})\] (.*)$', ENV, re.M):
    fid, rest = m.group(1), m.group(2)
    parts = [p.strip() for p in rest.split(' | ')]
    status = parts[3] if len(parts) > 3 else ''
    facts[fid] = {'status': status, 'pub': status.startswith('PUB'), 'line': rest[:160]}
ints = re.findall(r'^- \[(int\.[a-z_]+\.\d{3})\]', ENV, re.M)
bars = re.findall(r'^- \[(B\d{2})\]', ENV, re.M)
confs = re.findall(r'^- \[(C\d{2})\]', ENV, re.M)
pcs = re.findall(r'^- \[(PC\d)\]', ENV, re.M)
out['envelope'] = {'facts': facts, 'n_fact': len(facts), 'n_pub': sum(f['pub'] for f in facts.values()),
                   'n_int': len(ints), 'ints': ints, 'n_B': len(bars), 'n_C': len(confs), 'n_PC': len(pcs)}

# ---------- 30-textos: linhas "frase | [ids]" dentro de blocos de código, por seção
def code_blocks_with_section(md):
    res, sec, in_code = [], None, False
    for line in md.splitlines():
        if not in_code and line.startswith('#'):
            sec = line.strip('# ').strip()
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            res.append((sec, line))
    return res

rows30 = []
for sec, line in code_blocks_with_section(TXT):
    m = re.match(r'^(.*?) \| \[(.*)\]\s*$', line)
    if m:
        rows30.append({'sec': sec, 'text': m.group(1).strip(), 'ids': m.group(2)})
out['t30_rows'] = rows30

# canais (tabela do §3)
chan = []
for m in re.finditer(r'^\| (seo\.title|seo\.meta|title|meta) · ([^|]+?) \| (.+?) \| \*\*(\d+)\*\* \|', TXT, re.M):
    chan.append({'field': m.group(1), 'where': m.group(2).strip(), 'text': m.group(3).strip(), 'declared': int(m.group(4))})
out['t30_channels'] = chan

# perguntas do FAQ geral (títulos ### P#)
out['t30_faq_q'] = re.findall(r'^### (P\d) · (.+?)(?: — Sem resposta publicável hoje)?$', TXT, re.M)

# selo canônico citado no §2
m = re.search(r'\*\*Alternativa canônica\*\* \(sem adaptação, (\d+) caracteres\): "(.+?)"\s*$', TXT, re.M)
out['t30_selo_canon'] = {'declared': int(m.group(1)), 'text': m.group(2)} if m else None

# ---------- 31-catalogo: fichas
fichas = []
for sec in re.split(r'^## ', CAT, flags=re.M)[1:]:
    head = sec.splitlines()[0]
    key = head.split(' · ')[0].strip()
    if not re.match(r'^(p\d+|s-[a-z-]+)$', key):
        continue
    f = {'key': key, 'head': head}
    kind = re.search(r'^- \*\*kind:\*\* (\S+)', sec, re.M)
    f['kind'] = kind.group(1) if kind else None
    for fld in ['card', 'url', 'serve', 'links internos', 'frases']:
        mm = re.search(r'^- \*\*' + re.escape(fld) + r':\*\* (.+)$', sec, re.M)
        f[fld] = mm.group(1).strip() if mm else None
    mm = re.search(r'^- \*\*h1(?: \(reservado\))?:\*\* (.+)$', sec, re.M)
    f['h1'] = mm.group(1).strip() if mm else None
    mm = re.search(r'^- \*\*title \((\d+)/60(?:, reservado)?\):\*\* (.+)$', sec, re.M)
    f['title'], f['title_decl'] = (mm.group(2).strip(), int(mm.group(1))) if mm else (None, None)
    mm = re.search(r'^- \*\*meta \((\d+)/155(?:, reservado)?\):\*\* (.+)$', sec, re.M)
    if mm:
        raw = mm.group(2).strip()
        t = re.split(r' \| \[| — rascunho', raw)[0].strip()
        ids = re.search(r'\| \[(.*?)\]', raw)
        f['meta'], f['meta_decl'], f['meta_ids'] = t, int(mm.group(1)), ids.group(1) if ids else ''
    else:
        f['meta'], f['meta_decl'], f['meta_ids'] = None, None, ''
    def sent(line):
        m2 = re.match(r'^(.*?) \| \[(.*)\]\s*$', line.strip())
        return {'text': m2.group(1).strip(), 'ids': m2.group(2)} if m2 else None
    mm = re.search(r'^- \*\*intro:\*\* (.+)$', sec, re.M)
    f['intro'] = sent(mm.group(1)) if mm else None
    mm = re.search(r'^- \*\*cta:\*\* (.+)$', sec, re.M)
    f['cta'] = sent(mm.group(1)) if mm else None
    bl = re.search(r'^- \*\*bullets:\*\*\n((?:  - .+\n)+)', sec, re.M)
    f['bullets'] = [sent(x[4:]) for x in bl.group(1).splitlines()] if bl else []
    fq = re.search(r'^- \*\*faq:\*\*\n((?:  - .+\n)+)', sec, re.M)
    faq = []
    if fq:
        for x in fq.group(1).splitlines():
            p = x[4:].split(' | ')
            faq.append({'q': p[0].strip(), 'a': p[1].strip(), 'ids': p[2].strip('[] ') if len(p) > 2 else ''})
    f['faq'] = faq
    fichas.append(f)
out['cat'] = fichas

# enumeração declarada no catálogo
mm = re.search(r'\*\*Enumeração de serviços \(a mesma em todos os canais\):\*\* (.+?)\. A descrição', CAT)
out['cat_enum'] = [x.strip() for x in mm.group(1).split('·')] if mm else None

# ---------- HUB (só a lista HUB e o ENUM_NOTE, via ast, sem executar o arquivo)
start = SRC.index('HUB = [')
end = SRC.index('\n]\n', start) + 2
hub_src = SRC[start:end]
tree = ast.parse(hub_src)
hub = []
desc_h1 = re.search(r"^ 'h1': '(.+?)',$", SRC, re.M).group(1)
for call in tree.body[0].value.elts:
    d = {}
    for kw in call.keywords:
        if isinstance(kw.value, ast.Constant):
            d[kw.arg] = kw.value.value
        else:
            d[kw.arg] = '<<' + ast.unparse(kw.value) + '>>'
    if d.get('h1') == "<<DESC['h1']>>":
        d['h1'] = desc_h1
        d['h1_from'] = "DESC['h1']"
    hub.append(d)
out['hub'] = hub
em = re.search(r"ENUM_NOTE = \((.+?)\)\n", SRC, re.S)
out['enum_note'] = ''.join(ast.literal_eval('(' + em.group(1) + ',)')) if em else None

(BASE / 'audit_execon_parsed.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('ok', len(rows30), 'linhas 30;', len(chan), 'canais;', len(fichas), 'fichas;', len(hub), 'HUB')
print('envelope:', out['envelope']['n_fact'], 'fact.*', out['envelope']['n_pub'], 'PUB', out['envelope']['n_int'], 'int', out['envelope']['n_B'], 'B', out['envelope']['n_C'], 'C', out['envelope']['n_PC'], 'PC')
print('nfc:', out['nfc'])
