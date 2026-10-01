# -*- coding: utf-8 -*-
import re, html, json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad')
import laae_src as L
from laae_src import E, PV, DESC, FAQ, FAQD, CATALOG, CATD, DIMS, DIM_TIP, WA
P = '/home/user/soluintel/artefatos/parceiros/laae-laboratorio/index.html'
DOC = '/home/user/soluintel/docs/solusite-padrao.md'
s = open(P, encoding='utf-8').read()
SPEC = re.search(r'## 7\..*?```text\n(.*?)```', open(DOC, encoding='utf-8').read(), re.S).group(1).rstrip('\n')
def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, f'anchor x{n}: {old[:90]!r}'
    s = s.replace(old, new)

# ------------------------------------------------------------------ marcação
def pvmark(t, pv, tip=''):
    lab, base, _ = PV[pv]
    full = (lab.upper() + ' · ' + (tip or base))
    return f'<mark class="pv {pv}" data-tip="{E(full)}">{E(t)}</mark>'
def goodmark(t, pv, tip=''):
    tip = tip or PV[pv][1]
    cls = 'm-fill' if pv in ('site', 'pend') else 'm-good'
    if pv == 'site' and 'Conferir' not in tip: tip += ' Conferir na fonte antes de publicar.'
    if pv == 'pend' and 'Confirmar' not in tip: tip += ' Confirmar com o laboratório.'
    return f'<mark class="{cls}" data-tip="{E(tip)}">{E(t)}</mark>'

def render_desc(mk, site):
    hx = 'h2' if site else 'h5'
    o = ['<p>' + ' '.join(mk(*x) for x in DESC['abertura']) + '</p>']
    for head, intro, items, as_list in DESC['blocos']:
        o.append(f'<{hx}>{E(head)}</{hx}>')
        if intro: o.append(f'<p>{mk(*intro)}</p>')
        if as_list: o.append('<ul>' + ''.join(f'<li>{mk(*x)}</li>' for x in items) + '</ul>')
        else: o.append('<p>' + ' '.join(mk(*x) for x in items) + '</p>')
    if site:
        o.append(f'<p class="pg-cta">{mk(*DESC["cta"])}</p><span class="pg-btn" aria-hidden="true">Pedir análise no WhatsApp</span>')
    else:
        o.append(f'<p class="cta">{mk(*DESC["cta"])}</p>')
    return '\n            '.join(o)

def render_item(c, mk, site):
    o = []
    if not site:
        o.append(f'<p><mark class="m-good" data-tip="{E("O título é o H1 da página do site e o nome do item na Solutudo: o termo que a pessoa busca, sem rótulo genérico.")}">{E(c["h1"])}</mark></p>')
    o.append('<p style="margin-top:8px">' + ' '.join(mk(t, pv) for t, pv in c['intro']) + '</p>')
    o.append('<ul style="margin-top:8px">' + ''.join(f'<li>{mk(t, pv)}</li>' for t, pv in c['bullets']) + '</ul>')
    o.append(f'<p class="{"pg-cta" if site else "cta"}">{mk(*c["cta"])}</p>')
    fq = L.item_faq(c)
    if fq:
        o.append('<div class="ifaq"><span class="ifaq-h">Perguntas desta página</span>' +
                 ''.join(f'<p class="ifaq-q">{E(q)}</p><p class="ifaq-a">{mk(a, pv) if a else "<i>Sem resposta publicável hoje.</i>"}</p>' for q, a, pv in fq) + '</div>')
    if c.get('pend'):
        o.append(f'<p style="margin-top:8px" class="sub"><b>Pendente:</b> {E(c["pend"])}.</p>')
    if c.get('cond'):
        o.append(f'<p style="margin-top:8px" class="sub"><b>Sobe quando chegar:</b> {E(c["cond"])}.</p>')
    return '\n'.join(o)

def bars(total, dims, label):
    rows = []
    for name, mx, got, crit in dims:
        pct = round(100 * got / mx)
        tip = ' · '.join(f"{'✓' if ok else '✗'} {lab}" for lab, ok, p in crit)
        rows.append(f'<div class="scrow"><span class="sl">{E(name)}<span class="hint" data-tip="{E(DIM_TIP[name])}">?</span></span>'
                    f'<span class="st"><span class="sf" style="width:{pct}%"></span></span><span class="sv" data-tip="{E(tip)}">{got}<i>/{mx}</i></span></div>')
    return f'<div class="sc"><div class="scnum"><b>{total}</b><span>/100 · {label}</span></div>' + ''.join(rows) + '</div>'

def crit_table(dims):
    r = []
    for name, mx, got, crit in dims:
        cs = ''.join(f'<li class="{"ok" if ok else "no"}">{E(lab)}</li>' for lab, ok, p in crit)
        r.append(f'<tr><td><b>{E(name)}</b></td><td class="num"><b>{got}</b>/{mx}</td><td><ul class="crit">{cs}</ul></td></tr>')
    return '<div class="scroller"><table class="crt"><tr><th>Dimensão</th><th>Pontos</th><th>Critérios</th></tr>' + ''.join(r) + '</table></div>'

DT, DD = L.score_desc()
IS = {c['key']: L.score_item(c) for c in CATALOG}

# ================================================================== ABA DESTAQUE
# 1. descrição 3.0 (coluna "next") + placar recalculado
a = s.index('<div class="col next"><div class="colh">● Descrição 3.0</div><div class="colb">')
a2 = s.index('<div class="colb">', a) + len('<div class="colb">')
b = s.index('</div><div class="sc"><div class="scnum">', a2)
c_end = s.index('<span class="delta">Ganho de 47 pontos · 47 → ', b)
s = s[:a2] + '\n        ' + render_desc(goodmark, site=False) + '\n        </div>' + bars(DT, DD, 'Descrição 3.0') + '\n      </div>\n      </div>\n      ' + s[c_end:]
s = re.sub(r'<span class="delta">Ganho de 47 pontos · 47 → \d+</span>', f'<span class="delta">Ganho de {DT-47} pontos · 47 → {DT}</span>', s, count=1)
old_note = re.search(r'<div class="note" style="background:var\(--tint-lav\);color:#4A1080"><b>Este é o mesmo texto da página Sobre do site</b>.*?</div>', s, re.S)
assert old_note
s = s.replace(old_note.group(0), '''<div class="note" style="background:var(--tint-lav);color:#4A1080"><b>Este é o mesmo texto da página do laboratório no site</b> — um conteúdo, duas vitrines (<a href="#s-conteudo" onclick="return goSec('s-conteudo')">aba Solusite, seção 2</a>, com todas as métricas da Descrição 3.0). Revisado em 29/09/2026: títulos que respondem a uma busca no lugar de rótulos genéricos, a lista inteira das nove cidades, o prazo de 24 horas com a ressalva de ensaio e o nome LabLAAE ligado ao LAAE na primeira frase. <b>A nota foi recalculada</b> com os critérios explícitos da rubrica: passe o mouse sobre cada número para ver quais critérios foram cumpridos. As marcações em roxo pedem confirmação antes de publicar.</div>''')

# 2. FAQ da página Solutudo = FAQ do site
fa = s.index('<span class="badge">FAQ — respondendo o que as pessoas realmente buscam</span>')
h3a = s.index('<h3>', fa); h3b = s.index('</h3>', h3a) + 5
s = s[:h3a] + '<h3>8 perguntas: 7 respondidas, 1 que depende do escopo de acreditação — as mesmas do site</h3>' + s[h3b:]
tx = s.index('<div class="txt">', fa); tx_end = s.index('</div>', tx) + 6
faq_html = ['<div class="txt">']
for f in FAQ:
    if f['a']:
        faq_html.append(f'        <h4>{E(f["q"])}</h4>\n        <p>{goodmark(f["a"], f["pv"], f["why"])}</p>')
    else:
        faq_html.append(f'        <h4 style="color:#A3200F">{E(f["q"])}</h4>\n        <p><b>Sem resposta hoje — e é a pendência mais cara do dossiê.</b> A reunião registra <b>130 tipos de exame</b>, e o cadastro não nomeia um. Sem o escopo de acreditação, nenhum parâmetro pode ser publicado: dizer que se analisa um ensaio fora do escopo é problema técnico e regulatório, não erro de texto.</p>')
faq_html.append('      </div>')
s = s[:tx] + '\n'.join(faq_html) + s[tx_end:]

# 3. catálogo: cabeçalho, cartões e fichas
rep('<h3>9 itens: 4 cadastrados e 5 que a empresa entrega e não descreve</h3>',
    '<h3>10 itens: 4 cadastrados, 3 prontos para subir e 3 que esperam confirmação — cada um é também uma página do site</h3>')
rep('Os cinco <b>sugeridos</b> saem da norma citada na própria lista de palavras-chave (Portaria 888), do público declarado na reunião (poço artesiano, agronegócio), da categoria Engenharia Ambiental cadastrada sem produto, e da operação real — a coleta própria nas nove cidades.</p>',
    'Os <b>sugeridos</b> saem da norma citada na própria lista de palavras-chave (Portaria 888), do público declarado na reunião (poço artesiano, agronegócio), da categoria Engenharia Ambiental cadastrada sem produto, da operação real — a coleta própria nas nove cidades — e do site oficial, de onde veio a <b>água de hemodiálise</b>. <b>Um item, uma página:</b> o texto de cada ficha é o mesmo da página do item no Solusite, e as notas usam a rubrica com critérios explícitos.</p>')
for c in CATALOG:
    k = c['key']; tot = IS[k][0]
    m = re.search(r"(<button class=\"catcard\" onclick=\"openItem\('" + re.escape(k) + r"',this\)\".*?<span class=\"catsc next\">)(\d+)(</span>)", s, re.S)
    if m:
        s = s[:m.start(2)] + str(tot) + s[m.end(2):]
# novo cartão: hemodiálise
HC = CATD['s-hemodialise']
card_h = f'''        <button class="catcard" onclick="openItem('s-hemodialise',this)" aria-haspopup="dialog">
          <span class="cattop"><span class="cattag sug">Sugerido</span><span class="cattag st">depende do escopo</span></span>
          <span class="catname">{E(HC["card"])}</span>
          <span class="catprev"><em>Veio do site oficial, que não foi aberto. Serviço regulado, público hospitalar e depoimento do Hospital do Câncer já publicado.</em></span>
          <span class="catfoot"><span class="catsc now zero">—</span><span class="catarrow">→</span><span class="catsc next">{IS["s-hemodialise"][0]}</span><span class="catopen">ver ficha</span></span>
        </button>
'''
agro_btn = s.index("openItem('s-agro',this)")
agro_end = s.index('</button>', agro_btn) + len('</button>\n')
s = s[:agro_end] + card_h + s[agro_end:]
# fichas: coluna "proposta" e delta
for c in CATALOG:
    k = c['key']
    if k == 's-hemodialise': continue
    i = s.index(f'<div class="itemfull" id="if-{k}"')
    j = s.index('<div class="col next">', i)
    now_score = re.search(r'<div class="scnum"><b>(\d+|—)</b>', s[i:j]).group(1)
    jend = s.index('<span class="delta">', j)
    dend = s.index('</span>', jend) + 7
    tot, dims = IS[k]
    new_next = f'<div class="col next"><div class="colh">● Proposta · página {E(c["url"])}</div><div class="colb">{render_item(c, goodmark, False)}</div>{bars(tot, dims, "proposta")}</div></div>'
    if now_score.isdigit():
        delta = f'<span class="delta">Ganho de {tot-int(now_score)} pontos · {now_score} → {tot}</span>'
    else:
        delta = f'<span class="delta">De zero a {tot} — item que hoje não disputa busca nenhuma</span>'
    s = s[:j] + new_next + delta + s[dend:]
# nova ficha: hemodiálise
tot, dims = IS['s-hemodialise']
ficha_h = (f'<div class="itemfull" id="if-s-hemodialise" data-title="Água para hemodiálise · sugerido, depende do escopo"><div class="cmp">'
  f'<div class="col now"><div class="colh">● Hoje</div><div class="colb"><p><b>Não existe no cadastro.</b> A aplicação aparece no site oficial, que não foi aberto, e o laboratório já tem depoimento publicado do Hospital do Câncer do Norte de Minas.</p>'
  f'<p style="margin-top:8px">É o serviço de maior valor e menor concorrência do portfólio: água para hemodiálise tem exigência própria e é auditada.</p></div>'
  f'<div class="sc"><div class="scnum"><b>—</b><span>/100 · sem conteúdo</span></div></div></div>'
  f'<div class="col next"><div class="colh">● Proposta · página {E(HC["url"])}</div><div class="colb">{render_item(HC, goodmark, False)}</div>{bars(tot, dims, "proposta")}</div></div>'
  f'<span class="delta">De zero a {tot} — condicionado ao escopo de acreditação</span></div>\n')
agro_f = s.index('<div class="itemfull" id="if-s-agro"')
agro_f_end = s.index('</div>\n', s.index('<span class="delta">', agro_f)) + 7
s = s[:agro_f_end] + ficha_h + s[agro_f_end:]

# ================================================================== ABA GOOGLE e REDES (mesma enumeração)
g = re.search(r'(<span class="badge">Descrição do perfil<span class="cnt">)(\d+)/750(</span></span>\s*<div class="txt"><p>)(.*?)(</p></div>)', s, re.S)
if not g:
    g = re.search(r'(Descrição do perfil<span class="cnt">)(\d+)/750(</span>.*?<p>)(O LAAE é um laboratório.*?)(</p>)', s, re.S)
assert g, 'google'
s = s[:g.start(2)] + str(len(L.GOOGLE)) + '/750' + s[g.end(2)+4:g.start(4)] + E(L.GOOGLE) + s[g.end(4):]
bio_old = re.search(r'(<span class="badge">Bio do Instagram<span class="cnt">)(\d+)/150(</span></span>\s*<div class="txt"><p>)(.*?)(</p></div>)', s, re.S)
assert bio_old, 'bio'
s = s[:bio_old.start(2)] + str(len(L.BIO)) + '/150' + s[bio_old.end(2)+4:bio_old.start(4)] + E(L.BIO) + s[bio_old.end(4):]
s = re.sub(r'<li>Contado em UTF-16, como o Instagram conta \(\d+ de 150\)\.</li>', f'<li>Contado em UTF-16, como o Instagram conta ({len(L.BIO)} de 150). "Serviços acreditados", e não "acreditado": a bio também respeita a ressalva do escopo.</li>', s, count=1)

open(P, 'w', encoding='utf-8').write(s)
print('destaque, google e redes ok · desc', DT, '· itens', {k: v[0] for k, v in IS.items()})
