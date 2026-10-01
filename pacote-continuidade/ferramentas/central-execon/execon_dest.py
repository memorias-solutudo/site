# -*- coding: utf-8 -*-
"""Aba Destaque: a página da Execon na Solutudo, como está × como deveria, frase a frase."""
import html
E = html.escape

def build(S, R, goodmark, bars, render_desc, render_item, IS, NOW_ITEMS, NOW_DETAIL, DT, DD, NT, ND):
    # ---------- texto de hoje, marcado
    def mark_now(t, pv, tip):
        cls = 'm-good' if pv == 'cad' else 'm-bad'
        return f'<mark class="{cls}" data-tip="{E(R.PV[pv][0].upper() + " · " + tip)}">{E(t)}</mark>'
    now = []
    for blk in R.NOW_P:
        if isinstance(blk, tuple):
            t, kind, tip = blk
            if t == 'LISTA':
                continue
            now.append(f'<p class="nh"><mark class="m-bad" data-tip="{E("TÍTULO · " + tip)}">{E(t)}</mark></p>')
        else:
            now.append('<p>' + ' '.join(mark_now(*x) for x in blk) + '</p>')
    now.append('<p><span class="lbl">Não aparece em lugar nenhum</span> ' + ' '.join(f'<mark class="m-fill" data-tip="{E(w)}">{E(k)}</mark>' for k, w in R.MISSING) + '</p>')
    now_html = '\n          '.join(now)

    faq_html = []
    for f in S.FAQ:
        if f['a']:
            faq_html.append(f'        <h4>{E(f["q"])}</h4>\n        <p>{goodmark(f["a"], f["pv"], f["why"])}</p>')
        else:
            faq_html.append(f'        <h4 style="color:#A3200F">{E(f["q"])}</h4>\n        <p><b>Sem resposta publicável hoje.</b> {E(f.get("pend", ""))}</p>')

    # ---------- catálogo
    TAG = {'cad': ('reg', 'Produto cadastrado'), 'pronto': ('sug', 'Sugerido'), 'cond': ('sug', 'Espera condição'), 'fundir': ('reg', 'Fundir')}
    cards = ''
    fichas = ''
    for c in S.CATALOG:
        k = c['key']; tg, tl = TAG[c['kind']]
        st = c.get('idl') or c.get('tagline', '')
        before = NOW_ITEMS.get(k)
        if c['kind'] == 'fundir' or c.get('reservado'):
            after = '—'
        else:
            after = IS[k][0]
        prev = f'"{E(c["prev"])}"' if c.get('prev') else f'<em>{E(c.get("prev_sug", "Não existe no cadastro."))}</em>'
        sc_now = f'<span class="catsc now">{before}</span>' if before is not None else '<span class="catsc now zero">—</span>'
        cards += f'''        <button class="catcard" onclick="openItem('{k}',this)" aria-haspopup="dialog">
          <span class="cattop"><span class="cattag {tg}">{tl}</span><span class="cattag st">{E(st)}</span></span>
          <span class="catname">{E(c["card"])}</span>
          <span class="catprev">{prev}</span>
          <span class="catfoot">{sc_now}<span class="catarrow">→</span><span class="catsc next">{after}</span><span class="catopen">ver ficha</span></span>
        </button>
'''
        # coluna de hoje
        if before is not None:
            nd = NOW_DETAIL[k]
            now_col = (f'<div class="col now"><div class="colh">● Cadastrado hoje</div><div class="colb"><p><b>{E(nd["title"])}</b></p>'
                       f'<p style="margin-top:8px">{E(c.get("nota_atual", ""))}</p>'
                       f'<p style="margin-top:8px" class="sub">Frases do texto de hoje: {nd["mix"]}.</p></div>{bars(before, nd["dims"], "texto atual")}</div>')
        else:
            now_col = (f'<div class="col now"><div class="colh">● Hoje</div><div class="colb"><p><b>Não existe no cadastro.</b></p>'
                       f'<p style="margin-top:8px">{E(c.get("nota_atual", ""))}</p></div><div class="sc"><div class="scnum"><b>—</b><span>/100 · sem conteúdo</span></div></div></div>')
        if c['kind'] == 'fundir':
            next_col = (f'<div class="col next"><div class="colh">● Proposta · fundir em {E(c.get("into", ""))}</div><div class="colb"><p>{E(c.get("fundir_why", ""))}</p>'
                        f'<p style="margin-top:8px" class="sub"><b>O que fazer:</b> tirar o item do catálogo e redirecionar a página dele para a do item que fica.</p></div></div>')
            delta = '<span class="delta">Sai do catálogo · a busca fica com um item só</span>'
        elif c.get('reservado'):
            extra = ''
            if c.get('ja_pode'): extra += f'<p style="margin-top:8px" class="sub"><b>O que vai ao ar com a confirmação escrita do cliente (PC4a), fora do catálogo:</b> a frase da descrição, "A Execon Engenharia e Construção está em expansão para os Estados Unidos.", com validade até 31/12/2026.</p>'
            if c.get('perguntas'): extra += f'<p style="margin-top:8px" class="sub"><b>Perguntas que a página vai responder:</b> {E(c["perguntas"].split(": ", 1)[-1])}</p>'
            if c.get('enquanto'): extra += f'<p style="margin-top:8px" class="sub"><b>Enquanto isso:</b> {E(c["enquanto"])}</p>'
            next_col = (f'<div class="col next"><div class="colh">● Proposta · página reservada {E(c["url"])}</div><div class="colb">'
                        + (f'<p><mark class="m-fill" data-tip="{E("Título reservado: só é publicado quando a condição chegar.")}">{E(c["h1"])}</mark></p>' if c.get('title') else '')
                        + f'<p style="margin-top:8px"><b>Sobe quando chegar:</b> {E(c["cond"])}</p>{extra}</div>'
                        + '<div class="sc"><div class="scnum"><b>—</b><span>/100 · sem texto publicável hoje</span></div></div></div>')
            delta = '<span class="delta">Reservado · nenhuma frase tem fato publicável hoje</span>'
        else:
            tot, dims = IS[k]
            next_col = f'<div class="col next"><div class="colh">● Proposta · página {E(c["url"])}</div><div class="colb">{render_item(c)}</div>{bars(tot, dims, "proposta")}</div>'
            if before is not None:
                delta = f'<span class="delta">Ganho de {tot - before} pontos · {before} → {tot}</span>'
            elif c['kind'] == 'cond':
                delta = f'<span class="delta">De zero a {tot} · condicionado</span>'
            else:
                delta = f'<span class="delta">De zero a {tot} · item que hoje não disputa busca nenhuma</span>'
        title_d = f'{c["card"]} · {"ID " + k[1:] if k.startswith("p") else tl.lower()}'.replace('— (sai do catálogo) · ', 'Acompanhamento de Obra · sai do catálogo · ')
        fichas += f'  <div class="itemfull" id="if-{k}" data-title="{E(title_d)}"><div class="cmp">{now_col}{next_col}</div>{delta}</div>\n'

    n = {kd: sum(1 for c in S.CATALOG if c['kind'] == kd) for kd in ('cad', 'pronto', 'cond', 'fundir')}
    panel = f'''  <section id="p-dest" class="panel">

    <div class="sec first">
      <span class="eyebrow">Produto · Força Digital Essencial</span>
      <h2>Página da empresa na Solutudo</h2>
      <p class="secsub">Descrição 3.0, FAQ e catálogo reescritos a partir do envelope de fatos que o verificador aprovou. Três regras mandam em tudo aqui: <b>nenhum ano e nenhum número</b> até o cliente confirmar; <b>"alto padrão" sem exclusividade e sem superlativo</b>; e <b>os Estados Unidos numa frase só</b>, fora da abertura e do title.</p>
    </div>

    <div class="card">
      <div class="chips">
        <span class="chip peach">Marcação laranja<span class="hint" data-tip="Trecho que enfraquece o texto: adjetivo sem fato, promessa, número em conflito, título de rótulo.">?</span></span>
        <span class="chip lav">Marcação roxa<span class="hint" data-tip="Fato que existe e não foi usado, ou frase que depende de confirmação antes de publicar.">?</span></span>
        <span class="chip mint">Marcação verde<span class="hint" data-tip="Trecho que carrega fato com fonte no envelope verificado.">?</span></span>
        <span class="chip">Score de 0 a 100<span class="hint" data-tip="Seis dimensões somam 100: entidade e local (15), fatos verificáveis (25), resposta direta (20), estrutura extraível (15), unicidade (15) e contato (10). Passe o mouse sobre cada número para ver os critérios.">?</span></span>
      </div>
    </div>

    <div class="card">
      <span class="badge">Detalhes da empresa na Solutudo — como está × como deveria</span>
      <h3>A descrição do perfil, auditada frase a frase</h3>
      <p class="sub">O cadastro não traz nota calculada, então as duas foram apuradas aqui, pela mesma régua e pelo mesmo código. O texto de hoje tem <b>{R.now_stats()["words"]} palavras</b>, e <b>{R.now_stats()["zero"]} das {R.now_stats()["n"]} frases não carregam fato</b>, trazem número em conflito ou afirmam o que o verificador barrou. Ele pontua cheio em entidade, porque diz o nome, a categoria e a cidade logo no começo, e <b>zera em contato</b>: não há um telefone nem um WhatsApp.</p>
      <div class="cmp">
      <div class="col now"><div class="colh">● Publicado hoje no cadastro · 13/10/2022</div><div class="colb">
          {now_html}
        </div>{bars(NT, ND, "texto atual")}</div>
      <div class="col next"><div class="colh">● Descrição 3.0</div><div class="colb">
        {render_desc()}
        </div>{bars(DT, DD, "Descrição 3.0")}
      </div>
      </div>
      <span class="delta">Ganho de {DT - NT} pontos · {NT} → {DT}</span>
      <div class="selo"><b>Selo de procedência · {E(S.SELO[0])}</b>{E(S.SELO[1])}</div>
      <div class="note" style="background:var(--tint-lav);color:#4A1080"><b>Este é o mesmo texto da página /sobre do Solusite</b> — um conteúdo, duas vitrines (<a href="#s-conteudo" onclick="return goSec('s-conteudo')">aba Solusite, seção 2</a>, com todas as métricas da Descrição 3.0).</div>
      <div class="note"><b>O que a 3.0 deliberadamente NÃO faz aqui.</b> {S.NAO_FAZ}</div>
    </div>

    <div class="card">
      <span class="badge">SEO da página</span>
      <dl class="kv">
        <dt>seo.title <span class="cnt">{len(S.SOL_TITLE)}/60</span></dt><dd>{E(S.SOL_TITLE)}</dd>
        <dt>seo.meta <span class="cnt">{len(S.SOL_META)}/160</span></dt><dd>{E(S.SOL_META)}</dd>
      </dl>
    </div>

    <div class="card">
      <span class="badge">FAQ — respondendo o que as pessoas realmente buscam</span>
      <h3>{E(S.FAQ_HEAD)}</h3>
      <p class="sub">O campo de palavras-chave da empresa está vazio. As perguntas saem do que o público pergunta antes de contratar construtora de alto padrão em São Paulo e de construir nos Estados Unidos, levantado pelo agente de reputação e conteúdo. São as mesmas do Solusite.</p>
      <div class="txt">
{chr(10).join(faq_html)}
      </div>
    </div>

    <div class="card">
      <span class="badge">Catálogo de produtos e serviços — como está × como deveria</span>
      <h3>{E(S.CAT_HEAD)}</h3>
      <p class="sub">{S.CAT_SUB} <b>Um item, uma página:</b> o texto de cada ficha é o mesmo da página do item no Solusite.</p>
      <div class="cat">
{cards}      </div>
      <div class="note">{S.CAT_NOTE}</div>
    </div>

  </section>'''
    return panel, fichas
