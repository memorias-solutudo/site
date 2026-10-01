# -*- coding: utf-8 -*-
"""Aba Conteúdo: editorias, temas, datas, destaques, fixados, assinatura e o prompt vigente."""
import html, re
E = html.escape

def stt(k, lab): return f'<span class="stt {k}">{lab}</span>'

# leitura para o CS: os códigos do envelope ficam no dossiê; na tela, texto
_IDS = re.compile(r'\s*\((?:(?:fact|int)\.[a-z_]+\.\d{3}|[BC]\d{2}(?:[–-][BC]\d{2})?|P\d|D\d)(?:[,;]?\s*(?:e\s*)?(?:(?:fact|int)\.[a-z_]+\.\d{3}|[BC]\d{2}(?:[–-][BC]\d{2})?|P\d|D\d))*\)')
_CODES = [(r'\bPC4 \(b\) a \(h\)', 'estado, empresa e licença nos EUA'), (r'\bPC4a\b', 'confirmação escrita dos EUA'), (r'\bPC4\b', 'pré-condição dos EUA'),
          (r'\bPC1\b', 'CREA conferido'), (r'\bPC2\b', 'CAU conferido'), (r'\bPC3\b', 'atos técnicos com ART'),
          (r'\bC01\b', 'ano de início'), (r'\bC02\b', 'lista de obras com data'), (r'\bC03\b', 'se ainda faz médio padrão'), (r'\bC04\b', 'endereço'),
          (r'\bC07\b', 'horário do WhatsApp'), (r'\bC08\b', 'se o (14) tem WhatsApp'), (r'\bC11\b', 'composição da equipe')]
def hum(t):
    t = _IDS.sub('', t or '')
    for rx, w in _CODES: t = re.sub(rx, w, t)
    t = t.replace('com ART, com ART', 'com ART')
    return re.sub(r'\s{2,}', ' ', t).strip()
ICON = {
 'sobre': '<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M10 21v-6h4v6"/>',
 'oferta': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 4v5"/>',
 'dif': '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
 'prova': '<path d="M4 21v-2a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2"/><circle cx="12" cy="7" r="4"/>',
 'contato': '<path d="M21 12a9 9 0 0 1-13.4 7.9L3 21l1.1-4.6A9 9 0 1 1 21 12z"/>',
 'onde': '<path d="M12 21s7-6.1 7-11a7 7 0 0 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}

def build(S, PROMPT):
    if not getattr(S, 'READY', False):
        return '''  <section id="p-cont" class="panel">

    <div class="sec first">
      <span class="eyebrow">Conteúdo · editorias, temas e peças fixas</span>
      <h2>Em produção: o planejador de pauta ainda está escrevendo</h2>
      <p class="secsub">As seis editorias, os 24 temas, as datas, os cinco destaques, os três fixados, a assinatura e a bio saem do mesmo envelope de fatos das outras abas. Esta aba sobe na próxima atualização da central, depois da conferência do supervisor.</p>
    </div>

  </section>'''
    def sec(id_, n, title, sub, body):
        return f'''      <div class="csec" id="{id_}">
        <div class="csh"><span class="csn">{n}</span><div><h3>{title}</h3><p>{sub}</p></div></div>
{body}      </div>

'''
    # 1 · fontes
    frows = ''.join(f'<tr><td><b>{a}</b><br><small>{b}</small></td><td>{stt(k, lab)}</td><td>{w}</td></tr>' for a, b, k, lab, w in S.CONT_FONTES)
    C1 = f'''        <div class="alert">
          <span class="atop"><i aria-hidden="true">!</i> Declaração de acesso às fontes · leia antes de tudo</span>
          <h3>O Instagram da Execon não foi aberto, e nem aparece nos buscadores</h3>
          <p><b>Receber um link não é ter lido o link.</b> O perfil <code>/execonengconstrucao/</code> está no cadastro, mas o proxy desta sessão bloqueia o Instagram e nenhum buscador indexa o perfil. Os destaques, os fixados, a assinatura e a bio desta aba são <b>recomendação a partir do cadastro e do envelope de fatos</b>, não uma reforma do que está no ar. Se já houver destaques publicados, comparar antes de trocar.</p>
          <div class="scroller"><table><tr><th>Fonte</th><th>Status</th><th>O que isso muda</th></tr>{frows}</table></div>
        </div>
        <div class="card">
          <span class="badge">A regra que decide se uma editoria existe</span>
          <p class="sub"><b>Editoria não é tema: é um eixo de fatos que a empresa sustenta o ano inteiro.</b> Cada uma precisa de pelo menos dois fatos do envelope verificado. Aqui a régua pesa mais que o normal, porque o envelope da Execon é enxuto: 23 fatos publicáveis, nenhum ano, nenhum número de obras. {S.CONT_NOTA}</p>
        </div>
'''
    # 2 · editorias e temas
    eds = ''
    for i, ed in enumerate(S.ED, 1):
        CH = ' <span class="chip" style="font-size:10px;padding:2px 8px;background:var(--tint-yellow);color:#7A5A00">'
        cont = ''.join('<li>' + E(hum(t)) + ((CH + 'depende de: ' + E(hum(cnd)) + '</span>') if cnd else '') + '</li>' for t, cnd in ed['conteudos'])
        temas = ''
        for j, (tt, td, flags) in enumerate(ed['temas'], 1):
            fl = ''.join(f' <span class="chip {"mint" if f == "tema único" else "lav"}" style="font-size:10px;padding:2px 8px">{E(f)}</span>' for f in flags)
            temas += f'<div class="tema"><span class="ed ed{i}"><i></i>E{i}</span><span><span class="tt">{(i-1)*4+j} · {E(hum(tt))}</span>{fl}<span class="td" style="display:block">{E(hum(td))}</span></span></div>'
        eds += f'''        <div class="card"><span class="ed ed{i}"><i></i>E{i} · {E(ed["nome"])}</span><p class="sub" style="margin-top:8px">Slot <b>{E(ed["slot"])}</b> · {E(ed["objetivo"])}</p>
          <div class="grid2" style="margin-top:6px">
            <div><h4>Conteúdos</h4><ul class="clean">{cont}</ul></div>
            <div><h4>Temas do ano</h4>{temas}</div>
          </div>
          <p class="sub" style="margin-top:10px"><b>Essa editoria responde:</b> <i>"{E(ed["pergunta"])}"</i> · <small>fatos: <code>{E(ed["ids"])}</code></small></p>
        </div>
'''
    C2 = eds
    # 3 · datas
    drows = ''.join(f'<tr><td><b>{E(d)}</b></td><td>{E(fr)}</td><td>{E(hum(x))}</td><td>{E(ed)}</td></tr>' for d, fr, x, ed in S.DATAS)
    xrows = ''.join(f'<tr><td><b>{E(d)}</b></td><td>{E(hum(w))}</td></tr>' for d, w in S.DATAS_OUT)
    C3 = f'''        <div class="card">
          <span class="badge">A data é o gancho, não o assunto</span>
          <h3>{E(S.DATAS_HEAD)}</h3>
          <div class="scroller"><table><tr><th>Data</th><th>Frente</th><th>O cruzamento com um fato da Execon</th><th>Editoria</th></tr>{drows}</table></div>
          <h4 style="margin-top:14px">Descartadas, e por quê</h4>
          <div class="scroller"><table><tr><th>Data</th><th>Motivo</th></tr>{xrows}</table></div>
          <div class="note">{S.DATAS_NOTE}</div>
        </div>
'''
    # 4 · destaques
    hls = ''
    for n, h in enumerate(S.HL, 1):
        dentro = ''.join(f'<li>{E(hum(x))}</li>' for x in h['dentro'])
        hls += f'''          <div class="hl">
            <div class="hlt"><span class="hlc"><i><svg viewBox="0 0 24 24" aria-hidden="true">{ICON[h["icon"]]}</svg></i></span><b>{E(h["titulo"])}</b><small>{n} · {E(h["funcao"])} · slot {E(h["slot"])}</small></div>
            <p class="hlw">{E(h["why"])}</p>
            <h5>O que vai dentro</h5><ol>{dentro}</ol>
            <p class="hlw" style="margin-top:6px"><b>Não entra:</b> {E(hum(h["nao"]))}</p>
          </div>
'''
    alt = ''.join(f'<li><b>{E(a)}</b> {E(hum(b))}</li>' for a, b in S.HL_OUT)
    C4 = f'''        <div class="card" style="border-color:rgba(167,1,253,.28)">
          <span class="badge">Por que os destaques importam aqui</span>
          <h3>{E(S.HL_HEAD)}</h3>
          <div class="note" style="background:#FFF4E5;color:#5A3200"><b>Depende de fonte não lida:</b> o perfil não foi acessado. O que vem abaixo é recomendação a partir do cadastro. Ver a declaração na seção 1.</div>
          <p class="sub">{S.HL_WHY}</p>
        </div>
        <div class="hlgrid">
{hls}        </div>
        <div class="card"><span class="badge">Alternativas descartadas</span><ul class="clean">{alt}</ul></div>
'''
    # 5 · fixados
    crows = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in S.CIDADES_RULE)
    fx = ''
    for n, f in enumerate(S.FIX, 1):
        img = ''.join(f'<li>{E(x)}</li>' for x in f['imagem'])
        txt = ''.join(f'<li><b>{E(a)}</b>{(" · " + E(b)) if b else ""}</li>' for a, b in f['texto'])
        fx += f'''        <div class="card">
          <span class="badge">Fixado {n} · {E(f["funcao"])} · slot {E(f["slot"])}</span>
          <h3>{E(f["titulo"])}</h3>
          <div class="grid3" style="margin-top:10px">
            <div class="blk"><h4>Legenda</h4><div class="txt"><p style="white-space:pre-line">{E(f["legenda"])}</p></div></div>
            <div class="blk"><h4>Sugestão de imagem</h4><ul class="clean">{img}</ul></div>
            <div class="blk"><h4>Texto na imagem</h4><ul class="clean">{txt}</ul></div>
          </div>
        </div>
'''
    C5 = f'''        <div class="card" style="border-color:rgba(180,83,9,.35);background:linear-gradient(180deg,#FFFBF0 0%,var(--white) 60%)">
          <span class="badge warn">Regra das cidades · vale para as peças fixas</span>
          <h3>{E(S.CIDADES_HEAD)}</h3>
          <div class="scroller"><table><tr><th>Onde</th><th>O que entra</th><th>Por quê</th></tr>{crows}</table></div>
        </div>
{fx}        <div class="note"><b>Operação:</b> o Instagram coloca o último post fixado na primeira posição. Fixe na ordem 3 → 2 → 1, para o fixado 1 ficar à esquerda, e confira na tela depois.</div>
'''
    # 6 · assinatura
    srows = ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in S.SIG_ROWS)
    C6 = f'''        <div class="card" style="border-color:rgba(167,1,253,.28)">
          <span class="badge">Assinatura recomendada · {len(S.SIG_TEXT)} caracteres</span>
          <div class="sigbar">{S.SIG_HTML}<small>faixa inferior de toda imagem publicada · mesma posição, sempre</small></div>
          <p class="sub" style="margin-top:12px">{S.SIG_WHY}</p>
          <div class="scroller"><table><tr><th>Parte</th><th>Escolha</th><th>Por quê</th><th>Descartado</th></tr>{srows}</table></div>
        </div>
        <div class="card">
          <span class="badge">Bio sugerida · {S.BIO_N}/150 · depende de confirmar o perfil</span>
          <div class="txt"><p>{E(S.BIO)}</p></div>
          <p class="bwhy" style="margin-top:6px">{E(S.BIO_WHY)}</p>
        </div>
'''
    # 7 · filtros e pendências
    frs = ''.join(f'<tr><td><b>{E(hum(a))}</b></td><td>{E(hum(b))}</td></tr>' for a, b in S.FILTROS)
    prs = ''.join(f'<li>{E(hum(x))}</li>' for x in S.PEND_CONT)
    C7 = f'''        <div class="card">
          <span class="badge">Filtros · o que caiu antes de virar pauta</span>
          <div class="scroller"><table><tr><th>Tema descartado</th><th>Por quê</th></tr>{frs}</table></div>
        </div>
        <div class="card">
          <span class="badge warn">Pendências para o CS</span>
          <ul class="clean">{prs}</ul>
          <div class="note"><b>Repetindo a declaração de fontes:</b> o Instagram, os três sites e a prévia do Solusite não foram abertos. Nada que dependa deles foi afirmado como fato.</div>
        </div>
'''
    C8 = f'''        <div class="card">
          <span class="badge">§8.1 de <code style="text-transform:none;letter-spacing:0">docs/editorias-conteudo.md</code> · texto vigente</span>
          <h3>O prompt padrão do planejador de pauta</h3>
          <p class="sub">É o atalho do pipeline: recebe o JSON cru da API do cadastro e devolve editorias, temas e peças fixas. Nesta central, o conteúdo veio do caminho completo, com o envelope verificado; o prompt fica aqui para os próximos parceiros.</p>
          <button type="button" class="copybtn" onclick="copyPrompt(this)">Copiar o prompt</button>
          <pre class="prompt" id="prompt-text">{E(PROMPT)}</pre>
        </div>
'''
    items = [('c-fontes', 'Fontes e regra'), ('c-editorias', 'Editorias e temas'), ('c-datas', 'Datas comemorativas'), ('c-destaques', 'Destaques'),
             ('c-fixados', 'Posts fixados'), ('c-assinatura', 'Assinatura e bio'), ('c-uso', 'Filtros e pendências'), ('c-prompt', 'O prompt vigente')]
    menu = '    <nav class="cont-menu" aria-label="Seções da aba Conteúdo">\n      <span class="cm-title">Nesta aba</span>\n' + ''.join(
        f'      <a href="#{i}" class="cm-i{" on" if n == 0 else ""}"><b>{n+1}</b>{t}</a>\n' for n, (i, t) in enumerate(items)) + '    </nav>\n'
    body = (sec('c-fontes', 1, 'Fontes e regra', 'O que foi lido, o que não foi, e a regra que decide se uma editoria existe.', C1)
            + sec('c-editorias', 2, 'Editorias e temas', 'Seis eixos, com o banco de conteúdos e quatro temas em cada um: 24 no ano, dois por mês. O tema único e a série recorrente estão marcados; o que depende de confirmação leva a condição escrita.', C2)
            + sec('c-datas', 3, 'Datas comemorativas', 'Datas que cruzam com um fato da Execon, pelas cinco frentes. Não ocupam editoria própria.', C3)
            + sec('c-destaques', 4, 'Destaques do Instagram', 'Cinco círculos, na ordem em que quem chega pergunta.', C4)
            + sec('c-fixados', 5, 'Posts fixados', 'Os três primeiros posts do feed, cada um com legenda, sugestão de imagem e texto na imagem. O rodapé de todos é a assinatura da seção 6.', C5)
            + sec('c-assinatura', 6, 'Assinatura de rodapé e bio', 'Definida aqui, e só aqui. Toda imagem publicada fecha com esta faixa.', C6)
            + sec('c-uso', 7, 'Filtros e pendências', 'O que caiu antes de virar pauta e o que só o cliente resolve.', C7)
            + sec('c-prompt', 8, 'O prompt vigente', 'Colado na íntegra, com botão de copiar.', C8))
    return f'''  <section id="p-cont" class="panel">

    <div class="sec first">
      <span class="eyebrow">Conteúdo · editorias, temas e peças fixas</span>
      <h2>{E(S.CONT_H2)}</h2>
      <p class="secsub">{S.CONT_SUB}</p>
    </div>

    <div class="cont-layout">
{menu}    <div class="cont-body">

{body}    </div>
    </div>

  </section>'''
