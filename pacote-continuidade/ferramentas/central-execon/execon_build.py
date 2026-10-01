# -*- coding: utf-8 -*-
"""Monta a central da Execon a partir da fonte única (execon_src) e dos módulos de cada aba."""
import re, sys, html, importlib
SP = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad'
sys.path.insert(0, SP)
import execon_rubric as R, execon_src as S, execon_frame as F, execon_parc as PA, execon_agt as AG, execon_dest as DE, execon_site as SI, execon_cont as CO
E = html.escape
OUT = '/home/user/soluintel/artefatos/parceiros/grupo-execon/index.html'
DOC = '/home/user/soluintel/docs/solusite-padrao.md'
SPEC = re.search(r'## 7\..*?```text\n(.*?)```', open(DOC, encoding='utf-8').read(), re.S).group(1).rstrip('\n')
PROMPT = re.search(r'## 8\.1.*?```text\n(.*?)```', open('/home/user/soluintel/docs/editorias-conteudo.md', encoding='utf-8').read(), re.S).group(1).rstrip('\n')

# ------------------------------------------------------------------ marcas e placares
def pvmark(t, pv, tip=''):
    lab, base, _ = R.PV[pv]
    return f'<mark class="pv {pv}" data-tip="{E(lab.upper() + " · " + (tip or base))}">{E(t)}</mark>'
def goodmark(t, pv, tip=''):
    tip = tip or R.PV[pv][1]
    cls = 'm-fill' if pv in ('pub', 'pend') else 'm-good'
    if pv == 'pub' and 'Conferir' not in tip: tip += ' Fonte pública lida por trecho: conferir na fonte antes de publicar.'
    if pv == 'pend' and 'Confirmar' not in tip: tip += ' Confirmar com o cliente antes de publicar.'
    return f'<mark class="{cls}" data-tip="{E(tip)}">{E(t)}</mark>'
def bars(total, dims, label):
    rows = []
    for name, mx, got, crit in dims:
        pct = round(100 * got / mx)
        tip = ' · '.join(f"{'✓' if ok else '✗'} {lab}" for lab, ok, p in crit)
        rows.append(f'<div class="scrow"><span class="sl">{E(name)}<span class="hint" data-tip="{E(R.DIM_TIP[name])}">?</span></span>'
                    f'<span class="st"><span class="sf" style="width:{pct}%"></span></span><span class="sv" data-tip="{E(tip)}">{got}<i>/{mx}</i></span></div>')
    return f'<div class="sc"><div class="scnum"><b>{total}</b><span>/100 · {label}</span></div>' + ''.join(rows) + '</div>'
def crit_table(dims):
    r = []
    for name, mx, got, crit in dims:
        cs = ''.join(f'<li class="{"ok" if ok else "no"}">{E(lab)}</li>' for lab, ok, p in crit)
        r.append(f'<tr><td><b>{E(name)}</b></td><td class="num"><b>{got}</b>/{mx}</td><td><ul class="crit">{cs}</ul></td></tr>')
    return '<div class="scroller"><table class="crt"><tr><th>Dimensão</th><th>Pontos</th><th>Critérios</th></tr>' + ''.join(r) + '</table></div>'

def _desc(mk, site):
    hx = 'h2' if site else 'h5'
    o = ['<p>' + ' '.join(mk(t, pv, tip) for t, pv, tip, ids in S.DESC['abertura']) + '</p>']
    for blk in S.DESC['blocos']:
        head, intro, items, as_list = blk[:4]
        o.append(f'<{hx}>{E(head)}</{hx}>')
        if intro: o.append(f'<p>{mk(intro[0], intro[1], intro[2])}</p>')
        if items and as_list: o.append('<ul>' + ''.join(f'<li>{mk(t, pv, tip)}</li>' for t, pv, tip, ids in items) + '</ul>')
        elif items: o.append('<p>' + ' '.join(mk(t, pv, tip) for t, pv, tip, ids in items) + '</p>')
        if len(blk) > 4: o.append('<p>' + ' '.join(mk(t, pv, tip) for t, pv, tip, ids in blk[4]) + '</p>')
    t, pv, tip, ids = S.DESC['cta']
    if site: o.append(f'<p class="pg-cta">{mk(t, pv, tip)}</p><span class="pg-btn" aria-hidden="true">Pedir orçamento no WhatsApp</span>')
    else: o.append(f'<p class="cta">{mk(t, pv, tip)}</p>')
    if S.DESC.get('cta_extra'):
        t, pv, tip, ids = S.DESC['cta_extra']; o.append(f'<p>{mk(t, pv, tip)}</p>')
    return '\n            '.join(o)
def render_desc(): return _desc(goodmark, False)
def render_desc_site(): return _desc(lambda t, pv, tip='': pvmark(t, pv, tip), True)

def render_item(c):
    o = [f'<p><mark class="m-good" data-tip="{E("O título é o H1 da página do site e o nome do item na Solutudo: o termo que a pessoa busca, sem rótulo genérico.")}">{E(c["h1"])}</mark></p>']
    o.append('<p style="margin-top:8px">' + ' '.join(goodmark(t, pv) for t, pv in c['intro']) + '</p>')
    o.append('<ul style="margin-top:8px">' + ''.join(f'<li>{goodmark(t, pv)}</li>' for t, pv in c['bullets']) + '</ul>')
    o.append(f'<p class="cta">{goodmark(*c["cta"])}</p>')
    fq = S.item_faq(c)
    if fq:
        o.append('<div class="ifaq"><span class="ifaq-h">Perguntas desta página</span>' +
                 ''.join(f'<p class="ifaq-q">{E(q)}</p><p class="ifaq-a">{goodmark(a, pv) if a else "<i>Sem resposta publicável hoje.</i>"}</p>' for q, a, pv in fq) + '</div>')
    if c.get('pend'): o.append(f'<p style="margin-top:8px" class="sub"><b>Pendente:</b> {E(c["pend"].rstrip("."))}.</p>')
    if c.get('cond'): o.append(f'<p style="margin-top:8px" class="sub"><b>Sobe quando chegar:</b> {E(c["cond"].rstrip("."))}.</p>')
    return '\n'.join(o)
def render_item_site(c):
    o = [f'<h1>{E(c["h1"])}</h1>']
    o.append('<p>' + ' '.join(pvmark(t, pv) for t, pv in c['intro']) + '</p>')
    o.append('<ul>' + ''.join(f'<li>{pvmark(t, pv)}</li>' for t, pv in c['bullets']) + '</ul>')
    o.append(f'<p class="pg-cta">{pvmark(*c["cta"])}</p><span class="pg-btn" aria-hidden="true">Pedir orçamento no WhatsApp</span>')
    fq = S.item_faq(c)
    if fq:
        o.append('<h2>' + E(c.get('faq_h2', 'Perguntas sobre ' + c['card'].lower())) + '</h2>')
        for q, a, pv in fq:
            o.append(f'<h3 class="pgq">{E(q)}</h3><p>{pvmark(a, pv) if a else "<i>Sem resposta publicável hoje.</i>"}</p>')
    return '\n              '.join(o)
def faq_item(f):
    tg = ''.join(f'<span class="tg">{E(t)}</span>' for t in f['tags'])
    ans = f'<p class="faq-a">{E(f["a"])}</p>' if f['a'] else '<p class="faq-a faq-none">Sem resposta publicável hoje.</p>'
    pd = f'<p class="faq-p"><b>Confirmar:</b> {E(f["pend"])}</p>' if f.get('pend') else ''
    return f'''          <div class="faqi"><h4>{E(f["q"])}</h4>{ans}<div class="faq-m"><span class="tgs">{tg}</span><span class="faq-w">{E(f["why"])}</span></div>{pd}</div>
'''

# ------------------------------------------------------------------ notas
NS = R.now_sents()
NT, ND = R.score(NS[0][0], NS, R.NOW_HEADS, True, NS[-1][0], 'desc', R.NOW_WA, R.UNIQ)
DT, DD = S.score_desc()
IS = {c['key']: S.score_item(c) for c in S.CATALOG if S.scorable(c)}
NOW_ITEMS, NOW_DETAIL = S.now_items()

# ------------------------------------------------------------------ abas
parc = PA.render(NT, DT, S.N_PUB)
dest, fichas = DE.build(S, R, goodmark, bars, render_desc, render_item, IS, NOW_ITEMS, NOW_DETAIL, DT, DD, NT, ND)
dest = dest[:dest.rindex('  </section>')] + fichas + '  </section>'
site = SI.build(S, R, pvmark, crit_table, render_desc_site, render_item_site, faq_item, IS, NOW_ITEMS, DT, DD, NT, SPEC)
cont = CO.build(S, PROMPT)
agt = AG.render(S.AGENTES_EXTRA, S.VERDICT_HTML, S.AUDIT_HTML)

html_ = F.page('Central de Conteúdo — Grupo Execon · Solutudo', 'Central de conteúdo · um dossiê, todos os produtos',
               'Central de Conteúdo — Grupo Execon',
               'Construtoras · São Paulo/SP · ID 23008544 · Força Digital Essencial · fonte: cadastro Solutudo via API + curadoria de 10 agentes · 30/09/2026',
               '\n\n'.join([parc, agt, dest, site, cont]))
import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(html_)
print('ok', len(html_), '· desc', NT, '→', DT, '· itens', {k: v[0] for k, v in IS.items()}, '· agora', NOW_ITEMS)
