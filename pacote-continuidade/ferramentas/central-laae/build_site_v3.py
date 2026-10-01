# -*- coding: utf-8 -*-
import re, html, json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad')
import laae_src as L
from laae_src import E, PV, DESC, FAQ, CATALOG, CATD, WA
P = '/home/user/soluintel/artefatos/parceiros/laae-laboratorio/index.html'
DOC = '/home/user/soluintel/docs/solusite-padrao.md'
s = open(P, encoding='utf-8').read()
SPEC = re.search(r'## 7\..*?```text\n(.*?)```', open(DOC, encoding='utf-8').read(), re.S).group(1).rstrip('\n')
def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, f'anchor x{n}: {old[:90]!r}'
    s = s.replace(old, new)
def pvmark(t, pv, tip=''):
    lab, base, _ = PV[pv]
    return f'<mark class="pv {pv}" data-tip="{E(lab.upper() + " · " + (tip or base))}">{E(t)}</mark>'
def stt(k, lab): return f'<span class="stt {k}">{lab}</span>'
def crit_table(dims):
    r = []
    for name, mx, got, crit in dims:
        cs = ''.join(f'<li class="{"ok" if ok else "no"}">{E(lab)}</li>' for lab, ok, p in crit)
        r.append(f'<tr><td><b>{E(name)}</b></td><td class="num"><b>{got}</b>/{mx}</td><td><ul class="crit">{cs}</ul></td></tr>')
    return '<div class="scroller"><table class="crt"><tr><th>Dimensão</th><th>Pontos</th><th>Critérios</th></tr>' + ''.join(r) + '</table></div>'
def render_desc_site():
    o = ['<p>' + ' '.join(pvmark(*x) for x in DESC['abertura']) + '</p>']
    for head, intro, items, as_list in DESC['blocos']:
        o.append(f'<h2>{E(head)}</h2>')
        if intro: o.append(f'<p>{pvmark(*intro)}</p>')
        if as_list: o.append('<ul>' + ''.join(f'<li>{pvmark(*x)}</li>' for x in items) + '</ul>')
        else: o.append('<p>' + ' '.join(pvmark(*x) for x in items) + '</p>')
    o.append(f'<p class="pg-cta">{pvmark(*DESC["cta"])}</p><span class="pg-btn" aria-hidden="true">Pedir análise no WhatsApp</span>')
    return '\n            '.join(o)
def render_item_site(c):
    o = [f'<h1>{E(c["h1"])}</h1>']
    o.append('<p>' + ' '.join(pvmark(t, pv) for t, pv in c['intro']) + '</p>')
    o.append('<ul>' + ''.join(f'<li>{pvmark(t, pv)}</li>' for t, pv in c['bullets']) + '</ul>')
    o.append(f'<p class="pg-cta">{pvmark(*c["cta"])}</p><span class="pg-btn" aria-hidden="true">Pedir no WhatsApp</span>')
    fq = L.item_faq(c)
    if fq:
        o.append('<h2>Perguntas sobre ' + E(c['card'].lower() if c['kind'] != 'cad' else c['h1'].split(' em Montes')[0].lower()) + '</h2>')
        for q, a, pv in fq:
            o.append(f'<h3 class="pgq">{E(q)}</h3><p>{pvmark(a, pv) if a else "<i>Sem resposta publicável hoje.</i>"}</p>')
    return '\n              '.join(o)

DT, DD = L.score_desc()
IS = {c['key']: L.score_item(c) for c in CATALOG}
OLD = {'p711909': 92, 'p711908': 92, 'p711409': 91, 'p711410': 90, 's-coleta': 92, 's-poco': 91, 's-monitoramento': 93, 's-potabilidade': 93, 's-agro': 90, 's-hemodialise': None}
NOW = {'p711909': 30, 'p711908': 31, 'p711409': 52, 'p711410': 28}

HUB = [
 dict(menu='Início', url='/', h1='LAAE: análise de água e efluentes com coleta própria em nove cidades de Minas Gerais',
      title='LAAE · Análise de água e efluentes · Montes Claros (MG)',
      meta='Laboratório com serviços acreditados pela CGCRE/Inmetro e coleta própria em nove cidades de Minas Gerais. Água potável, de poço e efluentes.',
      q='laboratório de análise de água em Montes Claros', st='ok', stl='pronta'),
 dict(menu='O laboratório', url='/laboratorio', h1=DESC['h1'], title='LAAE · laboratório de água e efluentes desde 2003',
      meta='Laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003, com serviços acreditados pela CGCRE/Inmetro.',
      q='o LAAE é confiável? desde quando existe?', st='ok', stl='pronta · o texto do laboratório'),
 dict(menu='Análises', url='/analises', h1='Análises de água e efluentes do LAAE', title='Análises de água e efluentes em Montes Claros · LAAE',
      meta='Análises físico-químicas e microbiológicas de água potável, de poço, superficial e de processo, e de efluentes industriais e sanitários.',
      q='que análise de água eu preciso?', st='ok', stl='pronta · leva às 10 páginas'),
 dict(menu='Perguntas', url='/perguntas-sobre-analise-de-agua', h1='Perguntas sobre análise de água, coleta e laudo', title='Perguntas sobre análise de água, coleta e laudo · LAAE',
      meta='Prazo da amostra, acreditação, poço artesiano, físico-química ou microbiológica, laudo no portal e orçamento: as respostas do LAAE.',
      q='as dúvidas antes de contratar', st='ok', stl='pronta · 7 de 8 respostas'),
 dict(menu='Guia', url='/guia', h1='Guia de análise de água e efluentes', title='Guia de análise de água e efluentes · LAAE',
      meta='Artigos do laboratório sobre análise de água e efluentes, laudos e coleta, escritos a partir das dúvidas de quem contrata.',
      q='as buscas de cauda longa', st='pa', stl='abre com os 4 temas da E6'),
 dict(menu='Como pedir', url='/como-pedir', h1='Como pedir uma análise de água ao LAAE', title='Como pedir uma análise de água · LAAE',
      meta='WhatsApp (38) 98405-5391, de segunda a sexta, das 8h às 12h e das 13h às 17h. Sede na Av. Professor Vicente Guimarães, 1095, Montes Claros.',
      q='telefone, horário e endereço do LAAE', st='ok', stl='pronta'),
]
for p in HUB + CATALOG:
    assert len(p['title']) <= 60, (p['url'], len(p['title'])); assert len(p['meta']) <= 155, (p['url'], len(p['meta']))

# ------------------------------------------------------------------ seção 1
CENTRAIS = [
 ('Pizza Frita Semião', 'pa','parcial', 'pa','parcial', 'pa','via Destaque', 'pa','home + 2', 'no','não tem'),
 ('Porto Certo Consórcio', 'pa','parcial', 'pa','parcial', 'pa','via Destaque', 'pa','só a home', 'no','não tem'),
 ('EA3 Engenharia', 'no','orientação', 'pa','frase do banner', 'no','não tem', 'no','não tem', 'no','não tem'),
 ('Blocok O Original', 'pa','parcial', 'no','não tem', 'pa','via Destaque', 'pa','home + URLs', 'no','não tem'),
 ('LAAE · antes', 'pa','parcial', 'no','não tem', 'pa','via Destaque', 'pa','home + 1', 'pa','2 regras'),
 ('LAAE · agora', 'ok','16 páginas', 'ok','8 frases', 'ok','8 + por página', 'ok','16 páginas', 'ok','especificada'),
]
rows = ''.join(f'<tr><td><b>{c[0]}</b></td>' + ''.join(f'<td>{stt(c[i], c[i+1])}</td>' for i in (1,3,5,7,9)) + '</tr>' for c in CENTRAIS)
S1 = f'''        <div class="card" style="border-color:rgba(167,1,253,.28)">
          <span class="badge">O padrão · a partir da LAAE, para todas</span>
          <h3>O site replica a página Solutudo — texto, catálogo e perguntas — e é maior que ela</h3>
          <p class="sub">O texto do laboratório, cada item do catálogo e o FAQ são <b>os mesmos</b> na página Solutudo e no site: mesmos fatos, mesmas frases, mesma ordem. Muda a forma do contato — texto por extenso na Solutudo, botão com link no site. E o site acrescenta o que só ele pode ter: uma página por análise, perguntas por página, guia e área do cliente. O formato vem do caso de referência <a href="../../sobre-empresa-new-rock/" target="_blank" rel="noopener">New Rock</a>, e todo texto passa pelas métricas da Descrição 3.0.</p>
          <div class="vit">
            <div class="vit-c"><span class="vit-h">Página Solutudo · aba Destaque</span><div class="vit-sh">texto do laboratório · catálogo · FAQ</div><ul><li>contato em texto, sem link</li><li>avaliações nativas, com marcação</li><li>selo de procedência</li></ul></div>
            <div class="vit-m" aria-hidden="true"><span>uma fonte,<br>as duas vitrines</span></div>
            <div class="vit-c"><span class="vit-h">Solusite · lablaae.com.br</span><div class="vit-sh">texto do laboratório · catálogo · FAQ</div><ul><li>um item do catálogo, uma página</li><li>perguntas por página, guia e área do cliente</li><li>botões com link e WhatsApp fixo</li></ul></div>
          </div>
          <div class="note"><b>O custo conhecido, e como ele é pago.</b> Texto idêntico em dois domínios faz o buscador mostrar um deles para aquela busca — não é penalidade, é escolha. Por isso o site é sempre <b>maior</b> que a página: quem busca o LAAE pelo nome encontra os dois; quem busca "análise de efluente" encontra a página da análise no site, com as perguntas dela. Cada domínio aponta o canonical para si mesmo.</div>
        </div>

        <div class="rd4">
          <div class="rd"><span class="rd-k">Pessoas</span><b>decidem e chamam</b><p>Contato no topo, WhatsApp fixo no celular, página rápida. O dono reclamou do site atual: <i>"leva um tempo para carregar"</i> e <i>"não tem o seu telefone"</i>.</p></div>
          <div class="rd"><span class="rd-k">SEO</span><b>encontra e ordena</b><p>Google e Bing. Uma página por intenção de busca, com título que diz o que a pessoa procura. O Bing pesa mais do que parece: é por onde a busca do ChatGPT descobre páginas.</p></div>
          <div class="rd"><span class="rd-k">AEO</span><b>responde</b><p>Trechos em destaque, "as pessoas também perguntam" e voz. A pergunta vira título; a primeira frase responde sozinha — no FAQ geral e em cada página.</p></div>
          <div class="rd"><span class="rd-k">GEO</span><b>cita</b><p>ChatGPT, Perplexity, Claude, Gemini e AI Overviews. Frases atômicas com o nome, o que faz e o fato — no HTML servido, porque os robôs de IA não executam JavaScript.</p></div>
        </div>

        <div class="card">
          <span class="badge">Como estamos hoje nas cinco centrais</span>
          <h3>Todas têm os blocos do site. Nenhuma tratava GEO nem a camada técnica.</h3>
          <p class="sub">O SEO se resumia ao title e à meta da home, o FAQ do site só remetia ao da aba Destaque e o catálogo não virava página. A LAAE é a primeira central refeita no padrão; as outras quatro ficam como estão até serem retomadas uma a uma.</p>
          <div class="scroller"><table>
            <tr><th>Central</th><th>Texto final por página</th><th>Frases citáveis · GEO</th><th>FAQ resposta-primeiro · AEO</th><th>Title, meta e H1 · SEO</th><th>Camada técnica</th></tr>
            {rows}
          </table></div>
        </div>
'''

# ------------------------------------------------------------------ seção 2 · o texto e as métricas
legend = ''.join(f'<span class="pvl {k}">{E(v[0])}</span>' for k, v in PV.items())
NW = sum(len(x[0].split()) for x in L.desc_sents())
g250 = L.GOOGLE[:250]; grest = L.GOOGLE[250:]
low_desc = ' '.join(x[0] for x in L.desc_sents()).lower()
enum_rows = ''.join(f'<tr><td>{E(e)}</td><td>{stt("ok","sim") if e.lower() in low_desc else stt("no","não")}</td><td>{stt("ok","sim") if e.lower() in L.GOOGLE.lower() else stt("no","não")}</td></tr>' for e in L.ENUM)
fatos_rows = ''.join(f'<tr><td>{E(t)}</td><td><span class="pvl {pv}">{E(PV[pv][0])}</span></td></tr>' for t, pv, *_ in L.desc_sents())
LACUNAS = [
 ('Escopo de acreditação: a lista de parâmetros', 'sem ela, nenhum parâmetro é publicado; quatro páginas de análise e uma pergunta ficam rasas', 'laboratório'),
 ('Prazo de cada ensaio', 'a frase das 24 horas vale para "boa parte dos ensaios"; as exceções não estão no material', 'laboratório'),
 ('Fatos do site oficial', 'água industrial de processo, temperatura monitorada, controles de qualidade e hemodiálise vieram de um resumo colado', 'nós'),
 ('Nome da entidade', 'LAAE ou LabLAAE em todos os canais — hoje o texto liga os dois na primeira frase', 'cliente'),
 ('Frequência da rota por cidade', 'é o fato que justificaria uma página por cidade', 'laboratório'),
 ('URL do portal de resultados', 'sem ela, não há área do cliente no site', 'cliente'),
 ('Número da acreditação', 'sem ele, não há link para o registro oficial', 'laboratório'),
 ('Fotos da operação', 'o texto fica de pé, mas a página perde a prova visual', 'cliente'),
 ('Autorização dos depoimentos', 'SEAM, Hospital do Câncer do Norte de Minas e Tânia Botelho', 'cliente'),
]
lac_rows = ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in LACUNAS)
CLAIMS = [('"Há mais de 20 anos"', 'datação relativa envelhece; o texto usa "desde 2003"'),
          ('"Milhares de clientes"', 'número sem fonte, do site'),
          ('"Atuação em 11 estados"', 'alcance de franqueadora, em conflito com o dossiê'),
          ('"90% do mercado regional"', 'dito na reunião, sem fonte publicável'),
          ('"Laboratório acreditado"', 'sem a ressalva do escopo; o texto diz "serviços acreditados, conforme os escopos"'),
          ('"Toda a região do Norte de Minas"', 'promete cobertura sem fato; a região nem contém três das nove cidades'),
          ('"Experiência, qualidade, confiabilidade e compromisso"', 'adjetivos do texto atual, sem fato que os sustente')]
cl_rows = ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in CLAIMS)
CIT = ['O LAAE (LabLAAE) é um laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003.',
       'O LAAE tem serviços acreditados pela CGCRE do Inmetro, conforme os escopos dos certificados.',
       'O LAAE coleta amostras com equipe própria em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora.',
       'O LAAE faz análises físico-químicas e microbiológicas de água e de efluentes, conforme a origem e o uso.',
       'O laudo do LAAE fica disponível no portal de resultados, com login e senha.',
       'O LAAE atende de segunda a sexta, das 8h às 12h e das 13h às 17h, pelo WhatsApp (38) 98405-5391.',
       'Para boa parte dos ensaios, a amostra de água precisa chegar ao laboratório em até 24 horas depois de coletada.',
       'Quem capta água fora da rede pública responde pela qualidade dela.']
cit = ''.join(f'<li><span class="cq">{E(c)}</span></li>' for c in CIT)
S2 = f'''        <div class="card">
          <span class="badge mint">O texto do laboratório · {NW} palavras · o mesmo nas duas vitrines</span>
          <h3>{E(DESC["h1"])}</h3>
          <p class="sub">É a página <code>/laboratorio</code> do site e os detalhes da empresa na página Solutudo. Passe o mouse ou toque em cada frase para ver de onde ela vem. Os títulos dizem o que a pessoa busca — nenhum rótulo como "Serviços" ou "Sobre".</p>
          <div class="pvlegend">{legend}</div>
          <div class="pgf">
            <div class="pgf-bar"><i></i><i></i><i></i><span class="pgf-url">lablaae.com.br/laboratorio</span></div>
            <div class="pgf-body">
            <span class="pgf-crumb">Início › O laboratório</span>
            <h1>{E(DESC["h1"])}</h1>
            {render_desc_site()}
            <p class="pgf-upd">Atualizado em 29/09/2026</p>
            </div>
          </div>
        </div>

        <div class="card" style="border-color:rgba(0,181,137,.35)">
          <span class="badge mint">Descrição 3.0 · todas as métricas</span>
          <div class="bignum"><b>{DT}</b><span>/100 na rubrica da Descrição 3.0<br><small>era 47 no texto publicado hoje · critérios à vista, abaixo</small></span></div>
          {crit_table(DD)}
          <div class="note">A nota mede sustentação e forma, não resultado de busca. Frase do site não lido ou a confirmar vale meio ponto — é por isso que "fatos verificáveis" não fecha em 25.</div>

          <h4 style="margin-top:18px">Limites por canal</h4>
          <div class="scroller"><table>
            <tr><th>Canal</th><th>Limite da 3.0</th><th>Medida</th><th></th></tr>
            <tr><td><b>Detalhes da empresa</b> = página do laboratório</td><td>proporcional aos fatos · tipicamente 80 a 250 palavras</td><td>{NW} palavras</td><td>{stt("pa","acima do típico")}</td></tr>
            <tr><td><b>Perfil do Google</b></td><td>até 750 caracteres · essencial nos ~250 primeiros</td><td>{len(L.GOOGLE)}/750</td><td>{stt("ok","ok")}</td></tr>
            <tr><td><b>Bio do Instagram</b></td><td>até 150 caracteres</td><td>{len(L.BIO)}/150</td><td>{stt("ok","ok")}</td></tr>
            <tr><td><b>Title da página Solutudo</b></td><td>~50 a 60</td><td>{len(L.SOL_TITLE)}</td><td>{stt("ok","ok")}</td></tr>
            <tr><td><b>Meta da página Solutudo</b></td><td>~140 a 160</td><td>{len(L.SOL_META)}</td><td>{stt("ok","ok")}</td></tr>
            <tr><td><b>Title da página do laboratório</b></td><td>até ~60</td><td>{len(HUB[1]["title"])}</td><td>{stt("ok","ok")}</td></tr>
            <tr><td><b>Meta da página do laboratório</b></td><td>até ~155</td><td>{len(HUB[1]["meta"])}</td><td>{stt("ok","ok")}</td></tr>
          </table></div>
          <p class="bwhy" style="margin-top:8px">O texto passa do típico com {NW} palavras, e cada frase carrega um fato: não há frase de enchimento para cortar. O detalhe de campo — multiparâmetro, temperatura, controles de qualidade — foi para a página de coleta, que é onde ele responde uma busca.</p>

          <h4 style="margin-top:18px">A mesma enumeração em todos os canais</h4>
          <div class="grid2">
            <div class="scroller"><table>
              <tr><th>Termo</th><th>Texto do laboratório</th><th>Google</th></tr>
              {enum_rows}
            </table></div>
            <div>
              <p class="sub" style="margin-top:0"><b>Descrição do Google</b>, com os ~250 primeiros caracteres destacados — é o que aparece antes do "Mais":</p>
              <div class="txt"><p><mark class="g250">{E(g250)}</mark>{E(grest)}</p></div>
              <p class="sub"><b>Bio do Instagram:</b> {E(L.BIO)}</p>
              <p class="bwhy">A bio resume em "análise de água e efluentes": em 150 caracteres, a lista não cabe, e ela não inventa uma lista menor.</p>
            </div>
          </div>

          <h4 style="margin-top:18px">Essência</h4>
          <div class="txt"><p>{E(" ".join(x[0] for x in DESC["abertura"]))}</p></div>

          <h4 style="margin-top:18px">Fatos usados, frase a frase</h4>
          <div class="scroller"><table><tr><th>Afirmação</th><th>Fonte</th></tr>{fatos_rows}</table></div>

          <div class="grid2" style="margin-top:6px">
            <div><h4 style="margin-top:12px">Lacunas, com dono</h4><div class="scroller"><table><tr><th>Lacuna</th><th>Impacto</th><th>Dono</th></tr>{lac_rows}</table></div></div>
            <div><h4 style="margin-top:12px">Claims evitados</h4><div class="scroller"><table><tr><th>O que não entrou</th><th>Por quê</th></tr>{cl_rows}</table></div></div>
          </div>
          <div class="note" style="background:#FFF4E5;color:#5A3200"><b>Revisão humana: sim.</b> Acreditação é alegação regulada; o prazo de 24 horas precisa ser confirmado por ensaio; e quatro fatos vieram do site, que não foi aberto. Nada disso impede o texto de existir — impede de publicar sem conferência.</div>
        </div>

        <div class="card">
          <span class="badge">GEO · as frases que uma IA pode citar inteiras</span>
          <ol class="citl">{cit}</ol>
          <div class="note">As duas últimas não levam o nome do LAAE de propósito: são fatos do setor que o laboratório explica, e a IA os cita atribuindo a fonte pela página. As seis primeiras são fatos da empresa e carregam o nome.</div>
        </div>
'''

# ------------------------------------------------------------------ seção 3 · análises
sum_rows = ''
det = ''
for c in CATALOG:
    k = c['key']; tot, dims = IS[k]
    kind = {'cad': stt('ok', 'cadastrado'), 'pronto': stt('ok', 'pronto para subir'), 'cond': stt('pa', 'espera confirmação')}[c['kind']]
    before = NOW.get(k)
    sum_rows += f'<tr><td><b>{E(c["card"])}</b></td><td><code>{E(c["url"])}</code></td><td class="num">{before if before is not None else "—"} → <b>{tot}</b></td><td>{kind}</td></tr>'
    fq = L.item_faq(c)
    cond = f'<p class="pgd-cond"><b>{"Sobe quando chegar" if c.get("cond") else "Pendente"}:</b> {E(c.get("cond") or c.get("pend"))}.</p>' if (c.get('cond') or c.get('pend')) else ''
    det += f'''          <details class="pgd">
            <summary><span class="pgd-sc">{tot}</span><span class="pgd-t"><b>{E(c["h1"])}</b><small><code>{E(c["url"])}</code> · {len(fq)} pergunta{"s" if len(fq)!=1 else ""} da página</small></span>{kind}</summary>
            <div class="pgd-body">
              <div class="pgd-meta"><span><b>title</b> {E(c["title"])} <span class="cnt">{len(c["title"])}/60</span></span><span><b>meta</b> {E(c["meta"])} <span class="cnt">{len(c["meta"])}/155</span></span></div>
              <div class="pgf"><div class="pgf-bar"><i></i><i></i><i></i><span class="pgf-url">lablaae.com.br{E(c["url"])}</span></div><div class="pgf-body">
              {render_item_site(c)}
              </div></div>
              {cond}
              {crit_table(dims)}
              <button type="button" class="backlink" style="margin-top:12px" onclick="openItem('{k}',this)">Abrir o mesmo item na aba Destaque <span aria-hidden="true">→</span></button>
            </div>
          </details>
'''
S3 = f'''        <div class="card">
          <span class="badge">Um item do catálogo, uma página — e vice-versa</span>
          <h3>As dez análises da página Solutudo são as dez páginas de análise do site</h3>
          <p class="sub">O texto de cada página é o mesmo da ficha do item na aba Destaque, gerado da mesma fonte. O caminho inverso também vale: a <b>água de hemodiálise</b>, que o site oficial nomeia, entrou no catálogo da Solutudo como item condicionado. Cada página tem as próprias perguntas, e a nota de cada uma usa a rubrica da 3.0 com os critérios à vista.</p>
          <div class="scroller"><table>
            <tr><th>Item</th><th>Página</th><th>Nota: cadastrado → proposta</th><th>Status</th></tr>
            {sum_rows}
          </table></div>
          <div class="note">As notas das propostas mudaram em relação à versão anterior porque agora saem de critérios explícitos. Um exemplo do que isso corrigiu: a ficha de efluentes tinha 15 de 15 em "entidade e local" sem citar o nome LAAE uma vez. Agora toda página começa pelo nome da empresa.</div>
        </div>
{det}'''

# ------------------------------------------------------------------ seção 4 · perguntas
def faq_item(f):
    tg = ''.join(f'<span class="tg">{E(t)}</span>' for t in f['tags'])
    ans = f'<p class="faq-a">{E(f["a"])}</p>' if f['a'] else '<p class="faq-a faq-none">Sem resposta publicável hoje.</p>'
    pd = f'<p class="faq-p"><b>Confirmar:</b> {E(f["pend"])}</p>' if f.get('pend') else ''
    return f'''          <div class="faqi"><h4>{E(f["q"])}</h4>{ans}<div class="faq-m"><span class="tgs">{tg}</span><span class="faq-w">{E(f["why"])}</span></div>{pd}</div>
'''
perpage = ''.join(f'<tr><td><code>{E(c["url"])}</code></td><td>{"<br>".join(E(q) for q, a, pv in L.item_faq(c)) or "<i>nenhuma com fato hoje</i>"}</td></tr>' for c in CATALOG)
gaps = ''.join(f'<tr><td><b>{E(q)}</b></td><td>{E(w)}</td></tr>' for q, w in L.FAQ_GAPS)
S4 = f'''        <div class="card">
          <span class="badge">O FAQ geral · o mesmo na página Solutudo e em /perguntas-sobre-analise-de-agua</span>
          <h3>A primeira frase responde, e o nome do LAAE está em cada resposta</h3>
          <p class="sub">É o que trechos em destaque, voz e IA extraem. Estas oito perguntas agora são idênticas na aba Destaque — antes, as duas versões divergiam.</p>
{"".join(faq_item(f) for f in FAQ)}        </div>

        <div class="card">
          <span class="badge">Perguntas por página · só no site</span>
          <h3>Cada página de análise responde às próprias dúvidas</h3>
          <div class="scroller"><table><tr><th>Página</th><th>Perguntas</th></tr>{perpage}</table></div>
          <div class="note">Pergunta só entra com resposta específica da empresa. É por isso que a página de agronegócio e a de hemodiálise ainda não têm nenhuma: nada no material responde por elas.</div>
        </div>

        <div class="card">
          <span class="badge warn">Perguntas que o site precisa responder e ainda não pode</span>
          <div class="scroller"><table><tr><th>Pergunta</th><th>O que falta, e de quem</th></tr>{gaps}</table></div>
        </div>
'''

# ------------------------------------------------------------------ seção 5 · bloco a bloco
BLOCOS = [
 ('Banner, desktop e mobile', 'Frase: <i>"Análise de água e efluentes com coleta própria em nove cidades de Minas Gerais"</i> · apoio: <i>"Serviços acreditados pela CGCRE/Inmetro, conforme os escopos dos certificados."</i> · botões Pedir análise no WhatsApp e Ver as análises', 'pa', 'só no site · corrigir', 'A legenda cadastrada cita Montes Claros, Jaíba e Diamantina "e região": meia lista numa peça fixa.'),
 ('Ícones', '<b>Coleta própria</b> · a equipe coleta na sua unidade, em nove cidades<br><b>Acreditação CGCRE/Inmetro</b> · serviços acreditados, conforme os escopos<br><b>Laudo no portal</b> · com login e senha<br><b>Desde 2003</b> · sede em Montes Claros (MG)', 'pa', 'só no site · corrigir', 'Hoje o campo "[Solusite] Ícones" guarda os três depoimentos. Eles saem daqui e ganham bloco próprio.'),
 ('O laboratório', 'O texto da seção 2, inteiro, em <code>/laboratorio</code>, com o resumo de três frases na home', 'ok', 'replica o Destaque', 'Idêntico aos detalhes da empresa.'),
 ('Análises', 'Um cartão por item do catálogo na home e em <code>/analises</code>, cada um levando à sua página', 'ok', 'replica o Destaque', 'As dez páginas da seção 3.'),
 ('Como é feita a coleta', 'A coleta com equipe própria e o prazo de 24 horas — o tema único do caso', 'ok', 'replica o Destaque', 'É o bloco que explica o preço e a exclusividade regional.'),
 ('Cidades onde o LAAE faz a coleta', 'As nove, por extenso, com link para <code>/onde-coletamos</code>', 'ok', 'replica o Destaque', 'Tudo ou nada: nunca meia lista.'),
 ('Perguntas', 'As três primeiras do FAQ na home; as oito em <code>/perguntas-sobre-analise-de-agua</code>; as de cada página nas páginas', 'ok', 'replica o Destaque + só no site', ''),
 ('Quem já confia no LAAE', 'SEAM Engenharia e Meio Ambiente, Hospital do Câncer do Norte de Minas e Tânia Botelho, com nome e empresa', 'pa', 'só no site · após autorização', 'Os depoimentos já estão publicados no site atual da empresa.'),
 ('Avaliações', 'As avaliações nativas da Solutudo e do Google, exibidas', 'ok', 'replica o Destaque', 'Sem marcação de avaliação de si mesma no próprio site.'),
 ('Fotos', 'Bancada, coleta em campo, caixa térmica, equipe e fachada da sede, com <code>alt</code> descritivo', 'no', 'replica o Destaque · falta a foto', 'Nenhuma foto da operação no cadastro.'),
 ('Como pedir uma análise de água ao LAAE', 'WhatsApp, fixo, e-mail, horário em dois turnos, pagamento, endereço da sede em <code>&lt;address&gt;</code>, mapa e "Atualizado em"', 'ok', 'replica o Destaque', 'Os mesmos dados em todos os canais.'),
 ('Características', 'Ar-condicionado e sala de espera, as duas cadastradas', 'pa', 'replica o Destaque · pouco útil', 'Verdadeiras, mas não decidem a compra. Os ícones fazem esse trabalho melhor.'),
]
brows = ''.join(f'<tr><td><b>{b}</b></td><td>{c}</td><td>{stt(k, lab)}</td><td class="bwhy">{w}</td></tr>' for b, c, k, lab, w in BLOCOS)
S5 = f'''        <div class="card">
          <span class="badge">O formato Solusite, bloco a bloco · na ordem da home</span>
          <h3>O que a LAAE leva em cada bloco, e de onde ele vem</h3>
          <p class="sub">A ordem segue as três camadas da página: contato primeiro, confiança depois, profundidade por último. Os blocos marcados "replica o Destaque" usam o mesmo conteúdo da página Solutudo; os marcados "só no site" são o que faz o site ser maior que ela.</p>
          <div class="scroller"><table>
            <tr><th>Bloco</th><th>O que vai nele</th><th>Origem</th><th>Por quê</th></tr>
            {brows}
          </table></div>
        </div>
'''

# ------------------------------------------------------------------ seção 6 · além do Destaque
ALEM = [
 ('Área do cliente', 'Um link fixo no menu para o portal de resultados, onde o cliente entra com login e senha.', 'Quem já é cliente volta ao site para buscar laudo. É tráfego recorrente e mostra a operação funcionando — e o portal é hoje o diferencial menos visível.', 'a URL do portal', 'cliente', 'ok', 'alta'),
 ('Pedido de análise guiado', 'Um formulário de quatro campos — origem da água, uso, cidade e número de pontos — que abre o WhatsApp com a mensagem pronta.', 'São os dados que o comercial pede de qualquer jeito. Encurta o orçamento, e cada pedido passa a ser contado.', 'nada além do WhatsApp', 'nós', 'ok', 'alta'),
 ('Acreditação com prova', 'Uma página sobre a acreditação e o escopo do LAAE, com link para o registro oficial na CGCRE/Inmetro e para o reconhecimento da Rede Metrológica RS.', 'O público técnico confere a credencial antes de contratar. Para IA, link para a fonte oficial é o sinal mais forte de que o fato é verdadeiro.', 'o número da acreditação e o escopo', 'laboratório', 'pa', 'alta'),
 ('Guia', 'O blog com os 24 temas da aba Conteúdo, começando pelos quatro da E6, que são perguntas.', 'Resolve a queixa de "site estacionado" e captura as buscas de cauda longa. Cada post termina na página da análise certa.', 'produção dos textos', 'nós', 'ok', 'média'),
 ('Link de WhatsApp rastreável', 'Um link diferente por origem: site, perfil do Google e página Solutudo.', 'Transforma "acho que não deu resultado" em número — e é a evidência que o cliente aceita na hora de renovar.', 'configuração', 'nós', 'ok', 'alta'),
 ('Depoimentos com nome', 'Os três do cadastro, com nome, empresa e cargo, em bloco próprio.', 'Venda técnica compra por referência. Um deles declara 15 anos de relação.', 'autorização de uso', 'cliente', 'pa', 'média'),
 ('Fotos da operação', 'Galeria real: bancada, coleta em campo, caixa térmica, equipe e fachada.', 'Laboratório sem foto de laboratório não passa a confiança que vende.', 'uma sessão de fotos', 'cliente', 'pa', 'média'),
 ('Franquias', 'Se a rede quer captar franqueados pelo site, uma página separada, que não mistura com a matriz.', 'A reunião registra duas franquias ativas e oito vendidas. "11 estados" fica fora até esclarecer o que conta como atuação.', 'decisão do dono', 'cliente', 'no', 'a decidir'),
 ('Página por cidade', 'Uma página própria para cada cidade da rota.', 'Só com fato próprio da cidade — a frequência da rota, um cliente de lá com autorização. Sem isso, seria página que só troca o nome.', 'a frequência da rota', 'laboratório', 'no', 'depois'),
]
acards = ''.join(f'''          <div class="alem"><div class="alem-h"><b>{E(t)}</b>{stt(k, E(prio))}</div><p>{E(o)}</p><p class="bwhy">{E(w)}</p><p class="alem-f"><span>precisa: <b>{E(nd)}</b></span><span>dono: <b>{E(dn)}</b></span></p></div>
''' for t, o, w, nd, dn, k, prio in ALEM)
S6 = f'''        <div class="card">
          <span class="badge">Além do Destaque · o que só um site próprio pode ter</span>
          <h3>Nove recomendações para o Solusite da LAAE, com prioridade e dono</h3>
          <p class="sub">A prioridade sai de duas perguntas: quanto aquilo ajuda a vender para um público técnico que confere antes de chamar, e quanto depende de algo que ainda não chegou.</p>
          <div class="alem-g">
{acards}          </div>
        </div>
'''

# ------------------------------------------------------------------ seção 7 · mapa do site
def prow(p, is_item=False):
    if is_item:
        tot = IS[p['key']][0]
        st_ = {'cad': stt('ok','pronta'), 'pronto': stt('ok','pronta'), 'cond': stt('pa','condicional')}[p['kind']]
        menu = 'Análises ›'
        q = p['card']
    else:
        st_ = stt(p['st'], E(p['stl'])); menu = p['menu']; q = p['q']
    return (f'<tr><td>{E(menu)}</td><td><code>{E(p["url"])}</code></td><td>{E(p["h1"])}</td>'
            f'<td>{E(p["title"])} <span class="cnt">{len(p["title"])}/60</span></td>'
            f'<td>{E(p["meta"])} <span class="cnt">{len(p["meta"])}/155</span></td><td>{st_}</td></tr>')
maprows = ''.join(prow(p) for p in HUB) + ''.join(prow(c, True) for c in CATALOG)
S7 = f'''        <div class="card">
          <span class="badge">Mapa do site · {len(HUB) + len(CATALOG)} páginas</span>
          <h3>Seis páginas de entrada e dez de análise, cada uma com título que diz o que a pessoa busca</h3>
          <p class="sub">O menu usa rótulos curtos, mas específicos — "Análises", nunca "Serviços". O H1 e o title de cada página levam o termo de busca. Caracteres contados. O nome da entidade é <b>LAAE</b>; <b>LabLAAE</b> entra ligado a ele na primeira frase do texto e no nome alternativo do JSON-LD.</p>
          <div class="scroller"><table class="pgtbl">
            <tr><th>Menu</th><th>URL</th><th>H1</th><th>Title</th><th>Meta description</th><th>Status</th></tr>
            {maprows}
          </table></div>
          <div class="note"><b>Área do cliente</b> entra no menu como link para o portal de resultados, não como página. <b>Páginas por cidade</b> ficam de fora até existir a frequência da rota: sem fato próprio de cada cidade, seriam páginas que só trocam o nome, o padrão que as atualizações de spam do Google derrubam.</div>
        </div>

        <div class="card">
          <span class="badge">SEO · AEO · GEO · o que cada tipo de página faz por cada leitor</span>
          <div class="scroller"><table>
            <tr><th>Página</th><th>O que a pessoa busca</th><th>SEO · encontra</th><th>AEO · responde</th><th>GEO · cita</th></tr>
            <tr><td><b>O laboratório</b></td><td><i>laboratório de análise de água em Montes Claros</i></td><td>categoria e sede no title, no H1 e na 1ª frase</td><td>—</td><td>a frase de entidade, inteira</td></tr>
            <tr><td><b>Páginas de análise</b></td><td><i>análise de efluente</i> · <i>exame bacteriológico da água</i></td><td>uma página por análise, com o termo no H1</td><td>as perguntas da página</td><td>a 1ª frase, com o nome e o serviço</td></tr>
            <tr><td><b>Coleta e amostragem</b></td><td><i>quanto tempo a amostra de água dura</i></td><td>página própria</td><td>a resposta de uma frase</td><td>o prazo, com a fonte na página</td></tr>
            <tr><td><b>Cidades onde coleta</b></td><td><i>análise de água em Janaúba</i></td><td>as nove cidades no H1, na meta e no corpo</td><td>"o LAAE coleta na minha cidade?"</td><td>a lista de cidades</td></tr>
            <tr><td><b>Perguntas</b></td><td>as dúvidas antes de contratar</td><td>página própria, com <code>FAQPage</code></td><td>respostas de uma frase</td><td>cada resposta, com o nome</td></tr>
            <tr><td><b>Guia</b></td><td>as buscas de cauda longa</td><td>uma página por tema</td><td>a 1ª frase de cada post</td><td>frescor: conteúdo recente é mais citado</td></tr>
          </table></div>
        </div>
'''

# ------------------------------------------------------------------ seção 8 · técnica
BASE = 'https://lablaae.com.br'
READY = [c for c in CATALOG if c['kind'] != 'cond']
JSONLD = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebSite", "@id": f"{BASE}/#site", "url": f"{BASE}/", "name": "LAAE", "alternateName": "LabLAAE", "inLanguage": "pt-BR"},
  {"@type": "LocalBusiness", "@id": f"{BASE}/#laae", "name": "LAAE Laboratório de Análise de Água e Efluentes", "alternateName": "LabLAAE",
   "description": DESC['abertura'][0][0], "url": f"{BASE}/", "telephone": "+55 38 98405-5391", "email": "comercial@lablaae.com.br",
   "address": {"@type": "PostalAddress", "streetAddress": "Av. Professor Vicente Guimarães, 1095, Vicente Guimarães", "addressLocality": "Montes Claros", "addressRegion": "MG", "postalCode": "39401-781", "addressCountry": "BR"},
   "geo": {"@type": "GeoCoordinates", "latitude": -16.7425054, "longitude": -43.8754184},
   "openingHoursSpecification": [
     {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "12:00"},
     {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "13:00", "closes": "17:00"}],
   "foundingDate": "2003", "areaServed": [{"@type": "City", "name": f"{c}, MG"} for c in L.CIDADES],
   "knowsAbout": ["análise de água", "análise físico-química", "análise microbiológica", "análise de efluentes", "amostragem de água", "monitoramento ambiental"],
   "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Análises de água e efluentes", "itemListElement": [
     {"@type": "Offer", "itemOffered": {"@type": "Service", "name": c['h1'].split(' em Montes Claros')[0], "url": f"{BASE}{c['url']}"}} for c in READY]},
   "sameAs": ["https://www.instagram.com/lablaae"]},
  {"@type": "WebPage", "@id": f"{BASE}/laboratorio#pagina", "url": f"{BASE}/laboratorio", "name": DESC['h1'], "isPartOf": {"@id": f"{BASE}/#site"}, "about": {"@id": f"{BASE}/#laae"}, "inLanguage": "pt-BR", "dateModified": "2026-09-29"},
  {"@type": "BreadcrumbList", "itemListElement": [
     {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{BASE}/"},
     {"@type": "ListItem", "position": 2, "name": "O laboratório", "item": f"{BASE}/laboratorio"}]}]}
JT = json.dumps(JSONLD, ensure_ascii=False, indent=2); json.loads(JT)
FQ = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
  {"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in FAQ[:2] if f['a']]}, ensure_ascii=False, indent=2)
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

Sitemap: https://lablaae.com.br/sitemap.xml'''
S8 = f'''        <div class="card">
          <span class="badge">JSON-LD da página /laboratorio · gerado pela aplicação, por código</span>
          <h3>O mesmo fato do texto, em formato que a máquina lê</h3>
          <p class="sub">Não há tipo dedicado a laboratório ambiental no schema.org, então o nó do negócio é <code>LocalBusiness</code>. <code>DiagnosticLab</code> não serve: é laboratório médico. O catálogo entra como <code>OfferCatalog</code> com as sete páginas prontas; as três condicionadas entram quando subirem. Nenhum <code>aggregateRating</code>: empresa marcando avaliação de si no próprio site é inelegível.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'ld-sobre','Copiar o JSON-LD')">Copiar o JSON-LD</button>
          <pre class="prompt codeb" id="ld-sobre">{E(JT)}</pre>
          <div class="note"><b>Três ressalvas.</b> O domínio só é <code>lablaae.com.br</code> se o Solusite substituir o site atual. O <code>sameAs</code> do Instagram vem do cadastro; o perfil não foi aberto. E <code>dateModified</code> muda só em mudança material do conteúdo.</div>
        </div>

        <div class="card">
          <span class="badge">FAQPage da página de perguntas · trecho</span>
          <pre class="prompt codeb">{E(FQ)}</pre>
          <p class="bwhy" style="margin-top:8px">O texto do JSON-LD é idêntico ao texto visível. Cada página de análise marca as próprias perguntas do mesmo jeito.</p>
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
              <li><b>Contato clicável e visível:</b> <code>tel:</code> e <code>wa.me</code> em texto; WhatsApp fixo no celular.</li>
              <li><b>meta robots</b> <code>index, follow, max-snippet:-1, max-image-preview:large</code> e canonical para si mesmo em toda página.</li>
              <li><b>sitemap.xml</b> só com as páginas que estiverem no ar.</li>
              <li><b>Core Web Vitals no p75:</b> LCP até 2,5 s · INP até 200 ms · CLS até 0,1. Aqui é a queixa do cliente: <i>"ele leva um tempo para carregar"</i>.</li>
              <li><b>Frescor:</b> "Atualizado em" visível, <code>dateModified</code> no <code>WebPage</code> e IndexNow para o Bing a cada mudança material.</li>
              <li><b>Imagens:</b> <code>alt</code> descrevendo o que a foto mostra.</li>
            </ul>
          </div>
        </div>
'''

# ------------------------------------------------------------------ seção 9 · publicar
GATE = [
 ('O Solusite existe?', 'O campo Solusite está <code>false</code>, mas o cadastro guarda seis imagens de Solusite com legendas prontas.', 'CS', 'no', 'bloqueia tudo'),
 ('Qual domínio?', 'O Solusite substitui <code>lablaae.com.br</code> ou convive com ele? Convivendo, são três vitrines com o mesmo texto.', 'produto + cliente', 'no', 'bloqueia tudo'),
 ('Um nome só', 'LAAE ou LabLAAE em todos os canais. O texto liga os dois na primeira frase até a decisão.', 'cliente', 'pa', 'ajusta títulos'),
 ('Escopo de acreditação', 'A lista de parâmetros acreditados. Sem ela, as páginas de análise não descem ao parâmetro.', 'laboratório', 'pa', 'limita 4 páginas'),
 ('As 24 horas por ensaio', 'Quais ensaios têm prazo diferente.', 'laboratório', 'pa', 'ajusta 3 frases'),
 ('Fatos do site atual', 'Água industrial de processo, temperatura monitorada, controles de qualidade e hemodiálise vieram de um resumo colado.', 'nós', 'pa', 'conferir na fonte'),
 ('URL do portal e número da acreditação', 'Para a área do cliente e para a acreditação com prova.', 'cliente + laboratório', 'pa', 'bloqueia 2 recomendações'),
 ('Fotos da operação', 'Nenhuma no cadastro.', 'cliente', 'pa', 'limita a home'),
 ('Depoimentos', 'Autorização para o Solusite.', 'cliente', 'pa', 'bloqueia 1 bloco'),
 ('Robôs de IA na CDN', 'Conferir se a hospedagem bloqueia robôs de IA por padrão.', 'técnico', 'pa', 'antes de publicar'),
 ('Velocidade, antes e depois', 'Medir o site atual e o Solusite com os mesmos critérios. É a primeira prova de resultado para o cliente.', 'nós', 'ok', 'recomendado'),
]
grow = ''.join(f'<tr><td><b>{q}</b></td><td>{w}</td><td>{o}</td><td>{stt(k, l)}</td></tr>' for q, w, o, k, l in GATE)
S9 = f'''        <div class="card">
          <span class="badge warn">O que falta para a LAAE ir ao ar</span>
          <h3>Dois bloqueios de verdade, e o resto são ajustes</h3>
          <div class="scroller"><table><tr><th>Pendência</th><th>O que é</th><th>Dono</th><th>Efeito</th></tr>{grow}</table></div>
        </div>

        <div class="card">
          <span class="badge">Checklist de bolso · antes de publicar qualquer página</span>
          <ul class="chk">
            <li>Telefone e WhatsApp visíveis, grandes e clicáveis, sem clique para revelar?</li>
            <li>Desligando o JavaScript, o conteúdo principal continua na tela?</li>
            <li>Todo texto importante é texto de verdade, não imagem?</li>
            <li>A primeira frase diz o que a empresa é, a categoria e a sede?</li>
            <li>Nenhum título é rótulo genérico como "Serviços" ou "Sobre"?</li>
            <li>O texto é o mesmo da página Solutudo, e o catálogo bate item a item?</li>
            <li>A página responde às próprias perguntas, com fato?</li>
            <li>Nota da rubrica calculada, com os critérios à vista?</li>
            <li>JSON-LD espelhando o texto visível, sem avaliação de si mesma?</li>
            <li>Página leve, dentro dos Core Web Vitals, e "Atualizado em" visível?</li>
          </ul>
        </div>
'''

S10 = f'''        <div class="card">
          <span class="badge">§7 de <code style="text-transform:none;letter-spacing:0">docs/solusite-padrao.md</code> · texto vigente</span>
          <h3>O padrão do Solusite, para quem monta o site</h3>
          <p class="sub">A versão de bolso do padrão. Serve para a pessoa que monta o site e para um agente que gere o site a partir do cadastro. Copiado do arquivo-fonte na íntegra.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'spec-text','Copiar a especificação')">Copiar a especificação</button>
          <pre class="prompt" id="spec-text">{E(SPEC)}</pre>
        </div>
'''

def sec(id_, n, title, sub, body):
    return f'''      <div class="csec" id="{id_}">
        <div class="csh"><span class="csn">{n}</span><div><h3>{title}</h3><p>{sub}</p></div></div>
{body}      </div>

'''
MENU = '''    <nav class="cont-menu" aria-label="Seções da aba Solusite">
      <span class="cm-title">Nesta aba</span>
      <a href="#s-padrao" class="cm-i on"><b>1</b>O que esperamos</a>
      <a href="#s-conteudo" class="cm-i"><b>2</b>Texto e métricas</a>
      <a href="#s-analises" class="cm-i"><b>3</b>Uma página por análise</a>
      <a href="#s-faq" class="cm-i"><b>4</b>Perguntas</a>
      <a href="#s-blocos" class="cm-i"><b>5</b>Bloco a bloco</a>
      <a href="#s-alem" class="cm-i"><b>6</b>Além do Destaque</a>
      <a href="#s-paginas" class="cm-i"><b>7</b>Mapa do site</a>
      <a href="#s-tecnica" class="cm-i"><b>8</b>Camada técnica</a>
      <a href="#s-gate" class="cm-i"><b>9</b>Antes de publicar</a>
      <a href="#s-spec" class="cm-i"><b>10</b>Especificação</a>
    </nav>
'''
SITE = f'''  <section id="p-site" class="panel">

    <div class="sec first">
      <span class="eyebrow">Produto · Site Profissional (Solusite)</span>
      <h2>O site que pessoas, buscadores e IAs encontram — com o mesmo texto, catálogo e perguntas da página Solutudo</h2>
      <p class="secsub">Esta aba é o padrão do Solusite aplicado à LAAE: o texto do laboratório com todas as métricas da Descrição 3.0, uma página por item do catálogo, as perguntas, os blocos do formato Solusite e o que vai além da página Solutudo. O padrão completo está em <code>docs/solusite-padrao.md</code>. <b>Comece pela seção 9</b> se a pergunta for "dá para publicar?".</p>
    </div>

    <div class="cont-layout">
{MENU}    <div class="cont-body">

{sec('s-padrao', 1, 'O que esperamos do Solusite', 'Uma fonte, duas vitrines, quatro leitores — e onde as cinco centrais estavam antes deste padrão.', S1)}{sec('s-conteudo', 2, 'O texto do laboratório e as métricas', 'O texto dos detalhes da empresa e da página /laboratorio, com a rubrica, os limites por canal, os fatos, as lacunas e os claims evitados.', S2)}{sec('s-analises', 3, 'Uma página por análise', 'Os dez itens do catálogo, cada um com a sua página, o mesmo texto da ficha, as perguntas próprias e a nota com critérios.', S3)}{sec('s-faq', 4, 'Perguntas', 'O FAQ geral, igual nas duas vitrines, as perguntas de cada página e as que ainda não têm resposta.', S4)}{sec('s-blocos', 5, 'O formato Solusite, bloco a bloco', 'O que a LAAE leva em cada bloco do Solusite, e o que replica a página Solutudo.', S5)}{sec('s-alem', 6, 'Além do Destaque', 'O que só o site pode ter, com prioridade, o que falta e o dono.', S6)}{sec('s-paginas', 7, 'Mapa do site', 'As dezesseis páginas com menu, URL, H1, title e meta — e o que cada tipo de página faz por SEO, AEO e GEO.', S7)}{sec('s-tecnica', 8, 'Camada técnica', 'O que a aplicação precisa gerar: JSON-LD, robots.txt, indexação, velocidade e frescor.', S8)}{sec('s-gate', 9, 'Antes de publicar', 'O que ainda bloqueia a LAAE, com dono, e o checklist que vale para qualquer página.', S9)}{sec('s-spec', 10, 'Especificação', 'O padrão do Solusite em texto corrido, com botão de copiar.', S10)}    </div>
    </div>

  </section>

'''
i0 = s.index('  <section id="p-site" class="panel">'); i1 = s.index('  <section id="p-gmb" class="panel">')
s = s[:i0] + SITE + s[i1:]

CSS = r'''  /* aba Solusite v3 · métricas, páginas de análise e recomendações */
  .bignum{display:flex;align-items:center;gap:14px;margin-top:12px}
  .bignum b{font-size:44px;font-weight:800;letter-spacing:-.04em;color:#06845a;line-height:1}
  .bignum span{font-size:13px;color:var(--g700);font-weight:700;line-height:1.35}
  .bignum small{font-weight:600;color:var(--g600)}
  table.crt td{vertical-align:top}
  table.crt td.num,td.num{white-space:nowrap;font-variant-numeric:tabular-nums}
  ul.crit{list-style:none;margin:0;display:flex;flex-direction:column;gap:3px}
  ul.crit li{position:relative;padding-left:20px;font-size:12.6px;line-height:1.4;color:var(--g700)}
  ul.crit li::before{position:absolute;left:0;top:0;font-weight:800}
  ul.crit li.ok::before{content:"✓";color:#06845a}
  ul.crit li.no::before{content:"✗";color:#C2410C}
  mark.g250{background:var(--tint-mint);color:#0A4A36;font-weight:600;cursor:default}
  .sv[data-tip]{cursor:help}
  .sv[data-tip]:hover::after{left:auto;right:0}
  .sv[data-tip]:hover::before{left:auto;right:10px}
  .ifaq{margin-top:10px;border-top:var(--line);padding-top:8px}
  .ifaq-h{display:block;font-size:10.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--g600)}
  .ifaq-q{font-weight:800;margin-top:6px}
  .ifaq-a{margin-top:2px}
  details.pgd{border:var(--line);border-radius:14px;background:var(--white);margin-top:10px;box-shadow:var(--shadow-card)}
  details.pgd summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;padding:12px 16px}
  details.pgd summary::-webkit-details-marker{display:none}
  details.pgd[open] summary{border-bottom:var(--line)}
  .pgd-sc{flex:none;width:44px;height:44px;border-radius:12px;background:var(--tint-mint);color:#06845a;font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center}
  .pgd-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
  .pgd-t b{font-size:14.2px;letter-spacing:-.015em;line-height:1.3}
  .pgd-t small{font-size:11.8px;color:var(--g600);font-weight:600}
  .pgd-body{padding:12px 16px 16px}
  .pgd-meta{display:flex;flex-direction:column;gap:5px;font-size:12.6px;color:var(--g700)}
  .pgd-meta b{font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--g600);margin-right:6px}
  .pgd-cond{margin-top:10px;font-size:12.8px;background:var(--tint-peach);color:#7a3a16;border-radius:10px;padding:8px 12px}
  .pgf-body h3.pgq{font-size:14.4px;font-weight:800;margin-top:10px}
  button.backlink{font:inherit;font-size:13px;font-weight:800;cursor:pointer}
  .alem-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:14px}
  @media(max-width:1200px){.alem-g{grid-template-columns:1fr 1fr}}
  @media(max-width:640px){.alem-g{grid-template-columns:1fr}}
  .alem{border:var(--line);border-radius:14px;padding:14px 16px;background:var(--white);display:flex;flex-direction:column;gap:6px}
  .alem-h{display:flex;align-items:flex-start;justify-content:space-between;gap:8px}
  .alem-h b{font-size:14.6px;letter-spacing:-.02em;line-height:1.3}
  .alem p{font-size:13px;color:var(--ink);line-height:1.5}
  .alem-f{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:11.8px;color:var(--g600);margin-top:auto;border-top:var(--line);padding-top:7px}
'''
rep('  /* aba Solusite · padrão do site */', CSS + '  /* aba Solusite · padrão do site */')
open(P, 'w', encoding='utf-8').write(s)
print('solusite v3 ok')
