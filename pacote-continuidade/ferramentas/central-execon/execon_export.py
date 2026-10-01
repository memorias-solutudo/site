# -*- coding: utf-8 -*-
"""Exporta os textos finais da fonte única para o dossiê (36-textos-finais.md), com as notas medidas."""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad')
import execon_src as S, execon_rubric as R
D = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/dossie-grupo-execon/'
o = ['# 36 · Textos finais (exportados da fonte única, depois do retrabalho do auditor)', '',
     'Gerado por código a partir de `execon_src.py`. É exatamente o que a central publica. Formato: `frase | fonte | ids`.', '']
def score_block(t, d):
    o.append(f'**Nota: {t}/100**')
    for n, m, g, c in d:
        o.append(f'- {n}: {g}/{m} · ' + ' · '.join(("✓ " if ok else "✗ ") + lab for lab, ok, p in c))
    o.append('')
o += ['## 1. Descrição (Solutudo = /sobre)', '', f'H1: {S.DESC["h1"]}', '']
for t, pv, tip, ids in S.DESC['abertura']: o.append(f'{t} | {pv} | {ids}')
for b in S.DESC['blocos']:
    o += ['', f'H2: {b[0]}']
    if b[1]: o.append(f'{b[1][0]} | {b[1][1]} | {b[1][3]}')
    for t, pv, tip, ids in b[2]: o.append(f'- {t} | {pv} | {ids}')
    if len(b) > 4:
        for t, pv, tip, ids in b[4]: o.append(f'{t} | {pv} | {ids}')
for k in ('cta', 'cta_extra'):
    t, pv, tip, ids = S.DESC[k]; o.append(f'{t} | {pv} | {ids}')
o += ['', f'Selo ({S.SELO[0]}): {S.SELO[1]}', f'seo.title ({len(S.SOL_TITLE)}): {S.SOL_TITLE}', f'seo.meta ({len(S.SOL_META)}): {S.SOL_META}', f'Palavras: {S.NW}', '']
score_block(*S.score_desc())
ns = R.now_sents(); score_block(*R.score(ns[0][0], ns, R.NOW_HEADS, True, ns[-1][0], 'desc', R.NOW_WA, R.UNIQ)) if False else None
o += ['## 2. FAQ geral', '']
for f in S.FAQ:
    o.append(f'### {f["q"]}'); o.append(f'{f["a"] or "SEM RESPOSTA PUBLICÁVEL: " + f.get("pend", "")} | {f["pv"]}'); o.append('')
o += ['## 3. Catálogo = páginas', '']
for c in S.CATALOG:
    o.append(f'### {c["key"]} · {c["kind"]} · {c["card"]}')
    if S.scorable(c):
        o += [f'- url: {c["url"]}', f'- pergunta: {c.get("q", "")}', f'- h1: {c["h1"]}', f'- title ({len(c["title"])}): {c["title"]}', f'- meta ({len(c["meta"])}): {c["meta"]}']
        for t, pv in c['intro']: o.append(f'- intro: {t} | {pv}')
        for t, pv in c['bullets']: o.append(f'- bullet: {t} | {pv}')
        o.append(f'- cta: {c["cta"][0]} | {c["cta"][1]}')
        for q, a, pv in c.get('faq', []): o.append(f'- faq: {q} → {a} | {pv}')
        t, d = S.score_item(c); o.append(''); score_block(t, d)
    elif c.get('reservado'):
        o += [f'- reservada: {c["url"]}', f'- condição: {c["cond"]}', '']
    else:
        o += [f'- fundida em {c.get("into")}: {c.get("fundir_why", "")}', '']
o += ['## 4. Páginas de entrada do Solusite (HUB)', '', '| menu | url | h1 | title | meta | busca | JSON-LD | status |', '|---|---|---|---|---|---|---|---|']
for h in S.HUB:
    o.append(f'| {h["menu"]} | {h["url"]} | {h["h1"]} | {h["title"]} ({len(h["title"])}) | {h["meta"]} ({len(h["meta"])}) | {h.get("q", "")} | {h.get("ld", "")} | {h["stl"]} |')
open(D + '36-textos-finais.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print('36 ok', len(o))
