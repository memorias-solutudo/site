# -*- coding: utf-8 -*-
"""Aba Solusite da central da Execon: o Solusite atual (reconstituído do cadastro) × o proposto."""
import json, html
E = html.escape

def stt(k, lab): return f'<span class="stt {k}">{lab}</span>'

def build(S, R, pvmark, crit_table, render_desc_site, render_item_site, faq_item, IS, NOW_ITEMS, DT, DD, desc_before, SPEC):
    BASE = 'https://execon.com.br'  # ilustrativo: domínio a definir (gate)
    ready = [c for c in S.CATALOG if c['kind'] in ('cad', 'pronto')]
    cond = [c for c in S.CATALOG if c['kind'] == 'cond']
    avg_now = round(sum(v for v in NOW_ITEMS.values()) / len(NOW_ITEMS))
    pub_items = [c for c in S.CATALOG if c['kind'] in ('cad', 'pronto')]
    avg_new = round(sum(IS[c['key']][0] for c in pub_items) / len(pub_items))

    # ---------------------------------------------------------------- 1 · atual × proposto
    ATUAL = [
     ('Banner', '<i>"Construção de casas de alto padrão e projetos completos de gestão de obras."</i> Apoio: <i>"…para quem deseja construir uma casa de alto padrão em São Paulo, SP e com atual expansão no EUA."</i>',
      'O melhor texto do cadastro, e o único com o posicionamento novo. Mas afirma a expansão para os EUA no lugar mais visível, sem nenhuma fonte além da própria Solutudo, e escreve "no EUA".',
      S.BANNER_NEW, 'pa'),
     ('Texto da empresa', f'A descrição de 13/10/2022, com {R.now_stats()["words"]} palavras: "sonho da casa própria", "9 anos", quatro seções de rótulo e nenhum contato. Nota <b>{desc_before}</b>.',
      'É o texto que o Solusite vai puxar do cadastro se nada mudar.',
      f'O texto 3.0 da aba Destaque, idêntico, com {S.NW} palavras e títulos que são buscas. Nota <b>{DT}</b>.', 'no'),
     ('Produtos', f'Nove produtos, seis com o texto corrompido pelo tradutor, dois disputando a mesma busca e um que é a empresa, não um serviço. Média <b>{avg_now}</b>.',
      '"Canto de obras" e "Gerenciamento de Custódia" iriam para o site novo.',
      f'{len(pub_items)} páginas publicáveis e {len(cond)} condicionadas, cada uma com o mesmo texto da ficha na Solutudo. Média <b>{avg_new}</b>.', 'no'),
     ('Perguntas', 'Não existe bloco de perguntas no cadastro.', 'Sem FAQ, o site não disputa "as pessoas também perguntam" nem resposta de IA.',
      f'{len(S.FAQ)} perguntas gerais, as mesmas da Solutudo, e as perguntas de cada página.', 'no'),
     ('Fotos', '63 fotos no álbum e 7 do Solusite, todas com legenda "Execon Engenharia e Construção" ou "Grupo Execon".', 'Legenda vira texto alternativo. Setenta imagens que dizem só o nome não dizem o que a Execon constrói, nem onde.',
      'Legenda por foto: serviço, condomínio ou bairro, ano. Ex.: "Casa térrea com piscina em condomínio de Pardinho (SP), 2025".', 'pa'),
     ('Contato', 'Três WhatsApp, um deles em formato inválido; horário de 8h às 20h todos os dias; endereço na Paulista com o bairro errado.', 'Três dados de contato em conflito, no bloco que decide se a pessoa chama.',
      'WhatsApp (11) 98454-5681 como botão principal, (13) 98191-2794 como segundo, telefone (14) 99120-9697, e-mail, e a área atendida no lugar do endereço até o cliente confirmar.', 'pa'),
     ('Estados Unidos', 'Só a frase do banner.', 'Não há página, nem versão em inglês.',
      'Uma frase travada no texto e uma página em inglês pronta para subir quando o cliente confirmar estado, empresa e licença (seção 6).', 'pa'),
     ('Idioma e domínio', 'Português. Três domínios da empresa convivendo, e o Solusite seria o quarto.', 'O mesmo conteúdo em quatro endereços faz o buscador escolher um, e não necessariamente o certo.',
      'Um domínio oficial, os outros redirecionando para ele; <code>hreflang</code> pt-BR e en-US quando a página em inglês existir.', 'no'),
    ]
    arow = ''.join(f'<tr><td><b>{b}</b></td><td>{a}<br><small class="bwhy">{w}</small></td><td>{n}</td><td>{stt(k, {"ok":"ok","pa":"ajustar","no":"trocar"}[k])}</td></tr>' for b, a, w, n, k in ATUAL)
    S1 = f'''        <div class="alert">
          <span class="atop"><i aria-hidden="true">!</i> A prévia do Solusite não foi aberta</span>
          <h3>O "atual" abaixo foi reconstituído do cadastro, e não da tela</h3>
          <p><b>O proxy desta sessão bloqueia <code>previa.solusite.com.br</code></b>, e também os três sites da empresa: <code>obrasexecon.com.br</code>, <code>execonobras.com</code> e <code>execoneng.com.br</code>. O Solusite puxa o conteúdo do cadastro: banner, logotipo, descrição, produtos, fotos e contatos. Então o que o site vai mostrar é o que está no cadastro, e isso foi lido inteiro. <b>Layout, menu, ordem dos blocos e textos digitados direto no editor do site não foram vistos.</b> Se houver texto só na prévia, colar aqui para entrar na comparação.</p>
        </div>

        <div class="card" style="border-color:rgba(167,1,253,.28)">
          <span class="badge">Solusite atual × proposto · bloco a bloco</span>
          <h3>O site em montagem vai nascer com o texto de 2022, a menos que o cadastro mude antes</h3>
          <div class="ba">
            <div class="bnow"><h5>Atual, reconstituído do cadastro</h5><p class="bignum" style="margin:0"><b style="color:#C2410C">{round((desc_before + avg_now) / 2)}</b><span>/100 · média do texto ({desc_before}) e dos produtos ({avg_now})</span></p></div>
            <div class="bnext"><h5>Proposto</h5><p class="bignum" style="margin:0"><b style="color:#06724F">{round((DT + avg_new) / 2)}</b><span>/100 · média do texto ({DT}) e das páginas publicáveis ({avg_new})</span></p></div>
          </div>
          <div class="scroller"><table>
            <tr><th>Bloco</th><th>Atual</th><th>Proposto</th><th></th></tr>
            {arow}
          </table></div>
          <div class="note"><b>A ordem certa é esta:</b> primeiro a descrição e os produtos novos entram no cadastro, e depois o Solusite vai ao ar. Ao contrário, o site nasce com o texto de 2022 e com os erros de tradução.</div>
        </div>

        <div class="card">
          <span class="badge">O padrão · uma fonte, duas vitrines, quatro leitores</span>
          <div class="grid2">
            <ul class="clean">
              <li><b>O texto é o mesmo</b> nos detalhes da empresa na Solutudo e na página <code>/sobre</code> do site. O catálogo também: cada item é uma página, e vice-versa.</li>
              <li><b>O site é sempre maior</b>: tem uma página por serviço, as perguntas, a área atendida, o guia e, quando confirmar, a página em inglês.</li>
              <li><b>Cada domínio aponta o canonical para si mesmo.</b></li>
            </ul>
            <ul class="clean">
              <li><b>Pessoas:</b> WhatsApp visível no topo e fixo no celular.</li>
              <li><b>SEO:</b> uma página por intenção, com title, meta e H1 próprios.</li>
              <li><b>AEO:</b> a pergunta como título e a primeira frase respondendo sozinha.</li>
              <li><b>GEO:</b> frases atômicas, com o nome Execon, no HTML servido.</li>
            </ul>
          </div>
        </div>
'''

    # ---------------------------------------------------------------- 2 · texto e métricas
    legend = ''.join(f'<span class="pvl {k}">{E(v[0])}</span>' for k, v in R.PV.items() if k in S.PV_USED)
    fatos_rows = ''.join(f'<tr><td>{E(t)}</td><td><span class="pvl {pv}">{E(R.PV[pv][0])}</span></td><td><code>{E(ids)}</code></td></tr>' for t, pv, tip, ids in S.desc_sents())
    lac = ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in S.LACUNAS)
    cla = ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in S.CLAIMS)
    cit = ''.join(f'<li><span class="cq">{E(c)}</span></li>' for c in S.CIT)
    S2 = f'''        <div class="card">
          <span class="badge mint">O texto da Execon · {S.NW} palavras · o mesmo nas duas vitrines</span>
          <h3>{E(S.DESC["h1"])}</h3>
          <p class="sub">É a página <code>/sobre</code> do site e os detalhes da empresa na página Solutudo. Passe o mouse ou toque em cada frase para ver de onde ela vem. Os títulos dizem o que a pessoa busca, e nenhum é rótulo.</p>
          <div class="pvlegend">{legend}</div>
          <div class="pgf">
            <div class="pgf-bar"><i></i><i></i><i></i><span class="pgf-url">[domínio a definir]/sobre</span></div>
            <div class="pgf-body">
            <span class="pgf-crumb">Início › A Execon</span>
            <h1>{E(S.DESC["h1"])}</h1>
            {render_desc_site()}
            <p class="pgf-upd">Atualizado em 30/09/2026</p>
            </div>
          </div>
        </div>

        <div class="card" style="border-color:rgba(0,181,137,.35)">
          <span class="badge mint">Descrição 3.0 · todas as métricas</span>
          <div class="bignum"><b>{DT}</b><span>/100 na rubrica da Descrição 3.0<br><small>era {desc_before} no texto publicado hoje · critérios à vista, abaixo</small></span></div>
          {crit_table(DD)}
          <div class="note">A nota mede sustentação e forma, não resultado de busca. Frase de fonte pública lida por trecho, ou a confirmar, vale meio ponto; é por isso que "fatos verificáveis" não fecha em 25. Com as respostas do cliente, essas frases sobem para ponto inteiro.</div>

          <h4 style="margin-top:18px">Limites por canal</h4>
          <div class="scroller"><table>
            <tr><th>Canal</th><th>Limite da 3.0</th><th>Medida</th><th></th></tr>
            <tr><td><b>Detalhes da empresa</b> = página /sobre</td><td>proporcional aos fatos · tipicamente 80 a 250 palavras</td><td>{S.NW} palavras</td><td>{stt("ok","ok") if 80 <= S.NW <= 250 else stt("pa","fora do típico")}</td></tr>
            <tr><td><b>Title da página Solutudo</b></td><td>~50 a 60</td><td>{len(S.SOL_TITLE)}</td><td>{stt("ok","ok") if 45 <= len(S.SOL_TITLE) <= 60 else stt("pa","ajustar")}</td></tr>
            <tr><td><b>Meta da página Solutudo</b></td><td>~140 a 160</td><td>{len(S.SOL_META)}</td><td>{stt("ok","ok") if 130 <= len(S.SOL_META) <= 160 else stt("pa","ajustar")}</td></tr>
            <tr><td><b>Title da página /sobre</b></td><td>até ~60</td><td>{len(S.HUB[1]["title"])}</td><td>{stt("ok","ok") if len(S.HUB[1]["title"]) <= 60 else stt("pa","ajustar")}</td></tr>
            <tr><td><b>Meta da página /sobre</b></td><td>até ~155</td><td>{len(S.HUB[1]["meta"])}</td><td>{stt("ok","ok") if len(S.HUB[1]["meta"]) <= 155 else stt("pa","ajustar")}</td></tr>
            <tr><td><b>Bio do Instagram</b></td><td>até 150</td><td>—</td><td>{stt("pa","canal não confirmado")}</td></tr>
          </table></div>
          <p class="bwhy" style="margin-top:8px">Não há texto de Google nem de bio nesta entrega. O Google ficou fora do pedido, e o Instagram declarado no cadastro não aparece em nenhum buscador: a regra da 3.0 é não escrever para canal não confirmado. A bio sugerida está na aba Conteúdo, marcada como dependente de confirmar o perfil.</p>

          <h4 style="margin-top:18px">A mesma enumeração em todos os canais</h4>
          <p class="sub" style="margin-top:4px">{E(S.ENUM_NOTE)}</p>

          <h4 style="margin-top:18px">Essência</h4>
          <div class="txt"><p>{E(" ".join(x[0] for x in S.DESC["abertura"]))}</p></div>

          <h4 style="margin-top:18px">Fatos usados, frase a frase</h4>
          <div class="scroller"><table><tr><th>Afirmação</th><th>Fonte</th><th>Envelope</th></tr>{fatos_rows}</table></div>

          <div class="grid2" style="margin-top:6px">
            <div><h4 style="margin-top:12px">Lacunas, com dono</h4><div class="scroller"><table><tr><th>Lacuna</th><th>Impacto</th><th>Dono</th></tr>{lac}</table></div></div>
            <div><h4 style="margin-top:12px">Claims evitados</h4><div class="scroller"><table><tr><th>O que não entrou</th><th>Por quê</th></tr>{cla}</table></div></div>
          </div>
          <div class="note" style="background:#FFF4E5;color:#5A3200"><b>Revisão humana: sim.</b> {E(S.REVIEW)}</div>
        </div>

        <div class="card">
          <span class="badge">GEO · as frases que uma IA pode citar inteiras</span>
          <ol class="citl">{cit}</ol>
          <div class="note">Cada uma tem sujeito, o nome Execon e um fato. A frase dos Estados Unidos não está na lista de propósito: ela é condicional, e frase condicional não deve ser a que a IA repete.</div>
        </div>
'''

    # ---------------------------------------------------------------- 3 · páginas por item
    sum_rows = ''; det = ''
    KIND = {'cad': stt('ok', 'cadastrado'), 'pronto': stt('ok', 'pronto para subir'), 'cond': stt('pa', 'espera condição'), 'fundir': stt('no', 'fundir')}
    for c in S.CATALOG:
        k = c['key']
        if c['kind'] == 'fundir':
            sum_rows += f'<tr><td><b>Acompanhamento de Obra</b></td><td><code>/acompanhamento-de-obra</code> → 301</td><td class="num">{NOW_ITEMS.get(k, "—")} → —</td><td>{KIND["fundir"]} <small>no 547879</small></td></tr>'
            continue
        if c.get('reservado'):
            sum_rows += f'<tr><td><b>{E(c["card"])}</b></td><td><code>{E(c["url"])}</code> reservada</td><td class="num">{NOW_ITEMS.get(k, "—")} → —</td><td>{KIND["cond"]}</td></tr>'
            det += f'''          <details class="pgd">
            <summary><span class="pgd-sc">—</span><span class="pgd-t"><b>{E(c["h1"])}</b><small><code>{E(c["url"])}</code> · página reservada</small></span>{KIND["cond"]}</summary>
            <div class="pgd-body"><p class="pgd-cond"><b>Sobe quando chegar:</b> {E(c["cond"])}</p>{('<p class="pgd-cond"><b>Enquanto isso:</b> ' + E(c["enquanto"]) + '</p>') if c.get("enquanto") else ''}
              <button type="button" class="backlink" style="margin-top:12px" onclick="openItem('{k}',this)">Abrir o mesmo item na aba Destaque <span aria-hidden="true">→</span></button>
            </div>
          </details>
'''
            continue
        tot, dims = IS[k]
        before = NOW_ITEMS.get(k)
        sum_rows += f'<tr><td><b>{E(c["card"])}</b></td><td><code>{E(c["url"])}</code></td><td class="num">{before if before is not None else "—"} → <b>{tot}</b></td><td>{KIND[c["kind"]]}</td></tr>'
        fq = S.item_faq(c)
        condtxt = f'<p class="pgd-cond"><b>{"Sobe quando chegar" if c.get("cond") else "Pendente"}:</b> {E((c.get("cond") or c.get("pend")).rstrip("."))}.</p>' if (c.get('cond') or c.get('pend')) else ''
        det += f'''          <details class="pgd">
            <summary><span class="pgd-sc">{tot}</span><span class="pgd-t"><b>{E(c["h1"])}</b><small><code>{E(c["url"])}</code> · {len(fq)} pergunta{"s" if len(fq) != 1 else ""} da página</small></span>{KIND[c["kind"]]}</summary>
            <div class="pgd-body">
              <div class="pgd-meta"><span><b>pergunta</b> {E(c.get("q", ""))}</span><span><b>title</b> {E(c["title"])} <span class="cnt">{len(c["title"])}/60</span></span><span><b>meta</b> {E(c["meta"])} <span class="cnt">{len(c["meta"])}/155</span></span><span><b>JSON-LD</b> {E(S.JSONLD_ITEM)}</span></div>
              <div class="pgf"><div class="pgf-bar"><i></i><i></i><i></i><span class="pgf-url">[domínio]{E(c["url"])}</span></div><div class="pgf-body">
              {render_item_site(c)}
              </div></div>
              {condtxt}
              {crit_table(dims)}
              <button type="button" class="backlink" style="margin-top:12px" onclick="openItem('{k}',this)">Abrir o mesmo item na aba Destaque <span aria-hidden="true">→</span></button>
            </div>
          </details>
'''
    S3 = f'''        <div class="card">
          <span class="badge">Um item do catálogo, uma página — e vice-versa</span>
          <h3>{E(S.CAT_HEAD)}</h3>
          <p class="sub">{S.CAT_SUB}</p>
          <div class="scroller"><table>
            <tr><th>Item</th><th>Página</th><th>Nota: cadastrado → proposta</th><th>Status</th></tr>
            {sum_rows}
          </table></div>
        </div>
{det}'''

    # ---------------------------------------------------------------- 4 · perguntas
    perpage = ''.join(f'<tr><td><code>{E(c["url"])}</code></td><td>{"<br>".join(E(q) for q, a, pv in S.item_faq(c)) or "<i>nenhuma com fato hoje</i>"}</td></tr>' for c in S.CATALOG if S.scorable(c))
    gaps = ''.join(f'<tr><td><b>{E(q)}</b></td><td>{E(w)}</td></tr>' for q, w in S.FAQ_GAPS)
    S4 = f'''        <div class="card">
          <span class="badge">O FAQ geral · o mesmo na página Solutudo e em {E(S.HUB[4]["url"])}</span>
          <h3>A primeira frase responde, e o nome Execon está em cada resposta</h3>
          <p class="sub">É o que trechos em destaque, voz e IA extraem. As perguntas saem do que o público de fato pergunta antes de contratar construtora de alto padrão e de construir nos Estados Unidos, levantado pelo agente de reputação e conteúdo.</p>
{"".join(faq_item(f) for f in S.FAQ)}        </div>

        <div class="card">
          <span class="badge">Perguntas por página · só no site</span>
          <h3>Cada página responde às próprias dúvidas</h3>
          <div class="scroller"><table><tr><th>Página</th><th>Perguntas</th></tr>{perpage}</table></div>
          <div class="note">Pergunta só entra com resposta específica da empresa.</div>
        </div>

        <div class="card">
          <span class="badge warn">Perguntas que o site precisa responder e ainda não pode</span>
          <div class="scroller"><table><tr><th>Pergunta</th><th>O que falta, e de quem</th></tr>{gaps}</table></div>
        </div>
'''

    # ---------------------------------------------------------------- 5 · blocos
    brows = ''.join(f'<tr><td><b>{b}</b></td><td>{c}</td><td>{stt(k, lab)}</td><td class="bwhy">{w}</td></tr>' for b, c, k, lab, w in S.BLOCOS)
    S5 = f'''        <div class="card">
          <span class="badge">O formato Solusite, bloco a bloco · na ordem da home</span>
          <h3>O que a Execon leva em cada bloco, e de onde ele vem</h3>
          <p class="sub">A ordem segue as três camadas da página: contato primeiro, confiança depois, profundidade por último. "Replica o Destaque" é o mesmo conteúdo da página Solutudo; "só no site" é o que faz o site maior que ela.</p>
          <div class="scroller"><table>
            <tr><th>Bloco</th><th>O que vai nele</th><th>Origem</th><th>Por quê</th></tr>
            {brows}
          </table></div>
        </div>
'''

    # ---------------------------------------------------------------- 6 · Estados Unidos
    pc4 = ''.join(f'<li>{E(x)}</li>' for x in S.PC4)
    S6 = f'''        <div class="card" style="border-color:rgba(11,127,171,.3)">
          <span class="badge" style="background:var(--tint-cyan);color:#065F73">Hoje · o que o site diz sobre os EUA</span>
          <h3>Uma frase no texto, nenhuma no banner e nenhuma no title</h3>
          <div class="txt"><p>{pvmark(*S.EUA_SENT[:2])}</p></div>
          <p class="sub">É a frase travada pelo verificador. Ela fica no bloco sobre onde a Execon atende, e não na abertura. O banner de 28/09 diz "com atual expansão no EUA" e deve perder a frase até a confirmação: é o lugar mais visível do site, e uma afirmação sem fonte ali é a primeira que um cliente americano ou um buscador confere.</p>
        </div>

        <div class="card">
          <span class="badge">Rascunho pronto · a página em inglês sobe com a pré-condição 4</span>
          <h3>{E(S.EN_PAGE["h1"])}</h3>
          <div class="pgd-meta" style="margin-top:6px"><span><b>url</b> <code>{E(S.EN_PAGE["url"])}</code></span><span><b>title</b> {E(S.EN_PAGE["title"])} <span class="cnt">{len(S.EN_PAGE["title"])}/60</span></span></div>
          <p class="sub">{E(S.EN_PAGE["why"])}</p>
          <div class="grid2">
            <div><h4>O que ela precisa ter</h4><ul class="clean">{"".join(f"<li>{E(x)}</li>" for x in S.EN_PAGE["blocks"])}</ul></div>
            <div><h4>O que destrava a página · pré-condição 4</h4><ol style="padding-left:18px;margin-top:8px;font-size:13.4px;color:var(--g700);line-height:1.6">{pc4}</ol></div>
          </div>
          <div class="note"><b>Técnica:</b> a página em inglês é uma URL própria, com <code>hreflang="en-US"</code>, e aponta para a versão em português com <code>hreflang="pt-BR"</code>. As duas levam <code>x-default</code> para a home em português. Sem a página em inglês, o <code>hreflang</code> não entra.</div>
        </div>
'''

    # ---------------------------------------------------------------- 7 · além do Destaque
    acards = ''.join(f'''          <div class="alem"><div class="alem-h"><b>{E(t)}</b>{stt(k, E(prio))}</div><p>{E(o)}</p><p class="bwhy">{E(w)}</p><p class="alem-f"><span>precisa: <b>{E(nd)}</b></span><span>dono: <b>{E(dn)}</b></span></p></div>
''' for t, o, w, nd, dn, k, prio in S.ALEM)
    S7 = f'''        <div class="card">
          <span class="badge">Além do Destaque · o que só um site próprio pode ter</span>
          <h3>{len(S.ALEM)} recomendações para o Solusite da Execon, com prioridade e dono</h3>
          <p class="sub">Construção de alto padrão é compra consultiva e de ticket alto: o cliente pesquisa por semanas, confere obra entregue e registro profissional, e só depois chama. A prioridade sai disso.</p>
          <div class="alem-g">
{acards}          </div>
        </div>
'''

    # ---------------------------------------------------------------- 8 · mapa do site
    def prow(p, is_item=False):
        if is_item:
            st_ = {'cad': stt('ok', 'pronta'), 'pronto': stt('ok', 'pronta'), 'cond': stt('pa', 'reservada')}[p['kind']]
            menu = 'Construção e reforma ›'
        else:
            st_ = stt(p['st'], E(p['stl'])); menu = p['menu']
        qq = p.get('q', '')
        return (f'<tr><td>{E(menu)}</td><td><code>{E(p["url"])}</code></td><td>{E(p["h1"])}<br><small class="bwhy">busca: {E(qq)}</small></td>'
                f'<td>{E(p["title"])} <span class="cnt">{len(p["title"])}/60</span></td>'
                f'<td>{E(p["meta"])} <span class="cnt">{len(p["meta"])}/155</span></td><td>{st_}</td></tr>')
    items_pg = [c for c in S.CATALOG if S.scorable(c) or (c.get('reservado') and c.get('title'))]
    maprows = ''.join(prow(p) for p in S.HUB) + ''.join(prow(c, True) for c in items_pg)
    S8 = f'''        <div class="card">
          <span class="badge">Mapa do site · {len(S.HUB) + len(items_pg)} páginas</span>
          <h3>{len(S.HUB)} páginas de entrada e {len(items_pg)} de construção e reforma, cada uma com título que diz o que a pessoa busca</h3>
          <p class="sub">O menu usa rótulos curtos e específicos: "Construção e reforma", "Dúvidas sobre obra", nunca "Serviços" ou "Perguntas". Página que ainda não existe fica fora do menu, para não haver link quebrado. O H1 e o title de cada página levam o termo de busca. Caracteres contados. O nome da entidade é <b>Execon Engenharia e Construção</b>; <b>Grupo Execon</b>, que é o nome da página na Solutudo, entra como nome alternativo no JSON-LD e em nenhum texto sugere grupo de empresas.</p>
          <div class="scroller"><table class="pgtbl">
            <tr><th>Menu</th><th>URL</th><th>H1</th><th>Title</th><th>Meta description</th><th>Status</th></tr>
            {maprows}
          </table></div>
          <h4 style="margin-top:16px">JSON-LD esperado em cada página de entrada · gerado pela aplicação</h4>
          <div class="scroller"><table><tr><th>Página</th><th>Grafo</th></tr>{''.join(f'<tr><td><code>{E(h["url"])}</code></td><td>{E(h["ld"])}</td></tr>' for h in S.HUB)}<tr><td><b>As 8 páginas de serviço</b></td><td>{E(S.JSONLD_ITEM)}</td></tr></table></div>
          <div class="note"><b>Página por condomínio</b> fica de fora até existir fato próprio de cada um: obra entregue ali, com foto e ano. Sem isso, seria página que só troca o nome, o padrão que as atualizações de spam do Google derrubam. Ninho Verde II e Riviera de Santa Cristina XIII entram juntos na página da área atendida.</div>
        </div>
'''

    # ---------------------------------------------------------------- 9 · técnica
    JSONLD = {"@context": "https://schema.org", "@graph": [
      {"@type": "WebSite", "@id": f"{BASE}/#site", "url": f"{BASE}/", "name": "Execon Engenharia e Construção", "alternateName": ["Execon", "Grupo Execon"], "inLanguage": "pt-BR"},
      {"@type": "GeneralContractor", "@id": f"{BASE}/#execon", "name": "Execon Engenharia e Construção", "alternateName": ["Execon", "Grupo Execon"],
       "description": S.DESC['abertura'][0][0], "url": f"{BASE}/", "telephone": "+55 11 98454-5681", "email": "contato@execoneng.com.br",
       "areaServed": [{"@type": "City", "name": "São Paulo, SP"}, {"@type": "AdministrativeArea", "name": "Região Metropolitana de São Paulo"},
                      {"@type": "State", "name": "São Paulo"}],
       "knowsAbout": S.KNOWS,
       "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Construção e reforma", "itemListElement": [
         {"@type": "Offer", "itemOffered": {"@type": "Service", "name": c['card'], "url": f"{BASE}{c['url']}"}} for c in ready]},
       "sameAs": ["https://www.facebook.com/execonengconstrucao/"]},
      {"@type": "WebPage", "@id": f"{BASE}/sobre#pagina", "url": f"{BASE}/sobre", "name": S.DESC['h1'], "isPartOf": {"@id": f"{BASE}/#site"}, "about": {"@id": f"{BASE}/#execon"}, "inLanguage": "pt-BR", "dateModified": "2026-09-30"},
      {"@type": "BreadcrumbList", "itemListElement": [
         {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{BASE}/"},
         {"@type": "ListItem", "position": 2, "name": "A Execon", "item": f"{BASE}/sobre"}]}]}
    JT = json.dumps(JSONLD, ensure_ascii=False, indent=2); json.loads(JT)
    FQ = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
      {"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in S.FAQ[:2] if f['a']]}, ensure_ascii=False, indent=2)
    ROBOTS = '''# Busca: estes precisam entrar para o site aparecer
User-agent: Googlebot
User-agent: Bingbot
User-agent: OAI-SearchBot
User-agent: Claude-SearchBot
User-agent: PerplexityBot
Allow: /

# Demais robôs, inclusive os de treinamento de IA
# (GPTBot, ClaudeBot, Google-Extended): decisão do parceiro
User-agent: *
Allow: /

Sitemap: https://[domínio]/sitemap.xml'''
    S9 = f'''        <div class="card">
          <span class="badge">JSON-LD da página /sobre · gerado pela aplicação, por código</span>
          <h3>O mesmo fato do texto, em formato que a máquina lê</h3>
          <p class="sub">O tipo é <code>GeneralContractor</code>, o mais específico do schema.org para construtora, e não o genérico <code>LocalBusiness</code>. <b>Não há <code>address</code> nem <code>geo</code>:</b> o endereço está em conflito e em prédio de escritório compartilhado, então a empresa entra como prestador por área atendida (<code>areaServed</code>) até o cliente confirmar atendimento presencial. <b>Não há <code>foundingDate</code></b>: o ano é lacuna. O Instagram fica fora do <code>sameAs</code> porque não foi confirmado. O domínio é ilustrativo.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'ld-sobre','Copiar o JSON-LD')">Copiar o JSON-LD</button>
          <pre class="prompt codeb" id="ld-sobre">{E(JT)}</pre>
          <div class="note"><b>Quando o cliente confirmar:</b> endereço com atendimento presencial entra como <code>address</code> com bairro Bela Vista; o ano entra como <code>foundingDate</code>; o responsável técnico com CREA entra como <code>employee</code> com <code>hasCredential</code>, sem nome no texto se ele preferir; e a expansão para os EUA entra no <code>areaServed</code> só com o estado confirmado.</div>
        </div>

        <div class="card">
          <span class="badge">FAQPage da página de perguntas · trecho</span>
          <pre class="prompt codeb">{E(FQ)}</pre>
          <p class="bwhy" style="margin-top:8px">O texto do JSON-LD é idêntico ao texto visível. Cada página de serviço marca as próprias perguntas do mesmo jeito.</p>
        </div>

        <div class="card">
          <span class="badge">robots.txt, indexação, velocidade e frescor</span>
          <div class="grid2">
            <div>
              <pre class="prompt codeb">{E(ROBOTS)}</pre>
              <p class="bwhy" style="margin-top:8px">Liberar no <code>robots.txt</code> não basta: <b>conferir se a CDN ou o firewall bloqueiam robôs de IA por padrão</b>.</p>
            </div>
            <ul class="clean">
              <li><b>Tudo no HTML servido.</b> Desligue o JavaScript: se o texto sumir, está errado.</li>
              <li><b>Um domínio só.</b> Os três domínios da empresa redirecionam (301) para o oficial, e a página duplicada na Solutudo também.</li>
              <li><b>Contato clicável e visível:</b> <code>tel:</code> e <code>wa.me</code> em texto; WhatsApp fixo no celular.</li>
              <li><b>meta robots</b> <code>index, follow, max-snippet:-1, max-image-preview:large</code> e canonical para si mesmo em toda página.</li>
              <li><b>Core Web Vitals no p75:</b> LCP até 2,5 s · INP até 200 ms · CLS até 0,1. Foto de obra pesa: WebP, tamanho certo e carregamento preguiçoso abaixo da dobra.</li>
              <li><b>Imagens:</b> <code>alt</code> com serviço, lugar e ano, nunca só o nome da empresa.</li>
              <li><b>Frescor:</b> "Atualizado em" visível, <code>dateModified</code> no <code>WebPage</code> e IndexNow para o Bing.</li>
            </ul>
          </div>
        </div>
'''

    # ---------------------------------------------------------------- 10 · publicar
    grow = ''.join(f'<tr><td><b>{q}</b></td><td>{w}</td><td>{o}</td><td>{stt(k, l)}</td></tr>' for q, w, o, k, l in S.GATE)
    S10 = f'''        <div class="card">
          <span class="badge warn">O que falta para a Execon ir ao ar</span>
          <h3>Três bloqueios de verdade, e o resto são ajustes</h3>
          <div class="scroller"><table><tr><th>Pendência</th><th>O que é</th><th>Dono</th><th>Efeito</th></tr>{grow}</table></div>
        </div>

        <div class="card">
          <span class="badge">§7 de <code style="text-transform:none;letter-spacing:0">docs/solusite-padrao.md</code> · texto vigente</span>
          <h3>O padrão do Solusite, para quem monta o site</h3>
          <p class="sub">A versão de bolso do padrão, copiada do arquivo-fonte na íntegra.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'spec-text','Copiar a especificação')">Copiar a especificação</button>
          <pre class="prompt" id="spec-text">{E(SPEC)}</pre>
        </div>
'''

    def sec(id_, n, title, sub, body):
        return f'''      <div class="csec" id="{id_}">
        <div class="csh"><span class="csn">{n}</span><div><h3>{title}</h3><p>{sub}</p></div></div>
{body}      </div>

'''
    items = [('s-atual', 'Atual × proposto'), ('s-conteudo', 'Texto e métricas'), ('s-paginas', 'Uma página por serviço'), ('s-faq', 'Perguntas'),
             ('s-blocos', 'Bloco a bloco'), ('s-eua', 'Estados Unidos'), ('s-alem', 'Além do Destaque'), ('s-mapa', 'Mapa do site'),
             ('s-tecnica', 'Camada técnica'), ('s-gate', 'Antes de publicar')]
    menu = '    <nav class="cont-menu" aria-label="Seções da aba Solusite">\n      <span class="cm-title">Nesta aba</span>\n' + ''.join(
        f'      <a href="#{i}" class="cm-i{" on" if n == 0 else ""}"><b>{n+1}</b>{t}</a>\n' for n, (i, t) in enumerate(items)) + '    </nav>\n'
    body = (sec('s-atual', 1, 'O Solusite atual × o proposto', 'O que o site em montagem vai mostrar, reconstituído do cadastro, e o que ele deveria mostrar.', S1)
            + sec('s-conteudo', 2, 'O texto da Execon e as métricas', 'O texto dos detalhes da empresa e da página /sobre, com a rubrica, os limites, os fatos, as lacunas e os claims evitados.', S2)
            + sec('s-paginas', 3, 'Uma página por serviço', 'Cada item do catálogo da Solutudo é uma página do site, com o mesmo texto e as próprias perguntas.', S3)
            + sec('s-faq', 4, 'Perguntas', 'O FAQ geral, idêntico nas duas vitrines, e as perguntas de cada página.', S4)
            + sec('s-blocos', 5, 'Bloco a bloco', 'O que a Execon leva em cada bloco do Solusite, e o que é só do site.', S5)
            + sec('s-eua', 6, 'Estados Unidos', 'O que o site diz hoje, a página em inglês pronta e o que destrava cada nível.', S6)
            + sec('s-alem', 7, 'Além do Destaque', 'O que só um site próprio pode ter, com prioridade e dono.', S7)
            + sec('s-mapa', 8, 'Mapa do site', 'Todas as páginas, com URL, H1, title e meta contados.', S8)
            + sec('s-tecnica', 9, 'Camada técnica', 'JSON-LD, robots.txt, velocidade e frescor.', S9)
            + sec('s-gate', 10, 'Antes de publicar', 'Os bloqueios, os ajustes e a especificação para quem monta.', S10))
    return f'''  <section id="p-site" class="panel">

    <div class="sec first">
      <span class="eyebrow">Produto · Site Profissional (Solusite)</span>
      <h2>O Solusite da Execon está sendo montado agora, e vai puxar o texto de 2022 se o cadastro não mudar antes</h2>
      <p class="secsub">Esta aba compara o Solusite atual, reconstituído do cadastro porque a prévia não abriu, com o proposto. O proposto segue o padrão: o texto e o catálogo da aba Destaque, uma página por serviço, as perguntas, os blocos do formato Solusite, a página em inglês para os EUA e o que vai além da página Solutudo. O padrão completo está em <code>docs/solusite-padrao.md</code>.</p>
    </div>

    <div class="cont-layout">
{menu}    <div class="cont-body">

{body}    </div>
    </div>

  </section>'''
