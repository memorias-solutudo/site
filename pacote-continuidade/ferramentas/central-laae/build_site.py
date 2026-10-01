import re, html, json
P = '/home/user/soluintel/artefatos/parceiros/laae-laboratorio/index.html'
DOC = '/home/user/soluintel/docs/solusite-padrao.md'
s = open(P, encoding='utf-8').read()
d = open(DOC, encoding='utf-8').read()
SPEC = re.search(r'## 7\..*?```text\n(.*?)```', d, re.S).group(1).rstrip('\n')
E = html.escape
def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, f'anchor x{n}: {old[:90]!r}'
    s = s.replace(old, new)

# =====================================================================
# 1. O CONTEÚDO ÚNICO — fonte da aba Solusite E da aba Destaque
#    cada frase: (texto, procedência, explicação)
# =====================================================================
PV = {
 'cad':  ('cadastro', 'Fato do cadastro Solutudo, fornecido pela empresa.'),
 'reu':  ('reunião', 'Dito pelo dono na reunião comercial gravada.'),
 'site': ('site · conferir', 'Veio do resumo colado do site oficial, que não foi aberto. Conferir na fonte antes de publicar.'),
 'pend': ('confirmar', 'Depende de confirmação do laboratório antes de publicar.'),
}
ABERTURA = [
 ('O LAAE é um laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003.', 'cad',
  'Entidade primeiro: o que é, a categoria, a sede e o ano, numa frase que a IA cita inteira. "Sede", não cobertura: a coleta vai a nove cidades.'),
 ('A matriz tem serviços acreditados pela CGCRE do Inmetro, conforme os escopos dos certificados, e reconhecimento pela Rede Metrológica do Rio Grande do Sul segundo a ABNT NBR ISO/IEC 17025.', 'cad',
  'A credencial com o órgão nomeado e a ressalva do escopo. "A matriz" importa: a rede tem franquias, e a acreditação é desta unidade.'),
 ('A coleta das amostras é feita pela equipe do próprio laboratório, em nove cidades de Minas Gerais.', 'reu',
  'O diferencial operacional na abertura. "Nove cidades de Minas Gerais", não "Norte de Minas": Diamantina, Curvelo e Araçuaí ficam fora dessa região.'),
]
ANALISES_INTRO = 'Fazemos análises físico-químicas e microbiológicas de água e de efluentes, conforme a origem e o uso:'
ANALISES = [
 ('Água para consumo humano e água potável.', 'cad', 'As quatro origens de água vêm do cadastro.'),
 ('Águas subterrâneas, como a de poço artesiano, e águas superficiais.', 'cad', 'Poço artesiano é o público declarado na reunião e a busca curada da categoria.'),
 ('Água industrial de processo.', 'site', 'Aplicação nomeada pelo site oficial, que não foi aberto: conferir na fonte.'),
 ('Efluentes industriais e sanitários, para acompanhamento de sistemas de tratamento.', 'cad', 'Os dois tipos de efluente do cadastro, com o uso que justifica o ensaio.'),
 ('Programas de monitoramento ambiental, para acompanhar a mesma água ou o mesmo efluente ao longo do tempo.', 'cad', 'Monitoramento é a categoria Engenharia Ambiental do cadastro — e o contrato recorrente que a reunião pede.'),
]
COMO = [
 ('A coleta é feita pela nossa equipe.', 'reu', 'Coleta própria: dito na reunião, ausente de todo texto público até aqui.'),
 ('Para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas depois de coletada.', 'pend',
  'O fato que explica o negócio inteiro. "Boa parte dos ensaios", e não "toda amostra": o prazo muda de ensaio para ensaio. Confirmar com o laboratório quais têm prazo diferente.'),
 ('Em campo, usamos equipamento multiparâmetro, e a temperatura da amostra é monitorada durante o transporte.', 'site',
  'O multiparâmetro foi dito na reunião; a temperatura monitorada vem do resumo do site, que não foi aberto. Conferir na fonte.'),
 ('O laudo fica disponível no nosso portal de resultados, com login e senha.', 'reu', 'O portal é diferencial operacional dito na reunião e destaque no site oficial.'),
]
ONDE = ('Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora. Para outras cidades, consulte pelo WhatsApp.', 'cad',
        'As nove, por extenso: ou a lista inteira, ou nenhuma. Saiu "e demais cidades do Norte de Minas", que prometia cobertura sem fato.')
QUEM = ('Indústrias, agronegócio, consultorias ambientais, hospitais, clínicas, hotéis e restaurantes — e toda empresa que usa água que não vem da concessionária, como a de poço artesiano.', 'reu',
        'Os públicos declarados pelo dono na reunião, e o critério que define o cliente em uma frase.')
ATEND = [
 ('De segunda a sexta, das 8h às 12h e das 13h às 17h.', 'cad', 'Horário do cadastro, em dois turnos.'),
 ('Pagamento em boleto, Pix, dinheiro e cartões de crédito e débito.', 'cad', 'Boleto primeiro: é como indústria e hospital compram.'),
]
CTA = ('Precisa de uma análise? Fale com o LAAE pelo WhatsApp (38) 98405-5391 e diga a origem da água, o uso e a cidade.', 'cad',
       'Fecha em ação, com o nome da empresa e os três dados que o comercial pede de qualquer jeito. Na Solutudo é texto; no site, botão com link.')

def plain_words():
    parts = [t for t,_,_ in ABERTURA] + [ANALISES_INTRO] + [t for t,_,_ in ANALISES] + [t for t,_,_ in COMO] + [ONDE[0], QUEM[0]] + [t for t,_,_ in ATEND] + [CTA[0]]
    return len(' '.join(parts).split())
NWORDS = plain_words()

def pvmark(t, pv, tip):
    lab, _ = PV[pv]
    return f'<mark class="pv {pv}" data-tip="{E(lab.upper()+" · "+tip)}">{E(t)}</mark>'
def goodmark(t, pv, tip):
    extra = ' Conferir na fonte antes de publicar.' if pv == 'site' else (' Confirmar com o laboratório.' if pv == 'pend' else '')
    cls = 'm-fill' if pv in ('site','pend') else 'm-good'
    return f'<mark class="{cls}" data-tip="{E(tip + ("" if extra.strip() in tip else extra))}">{E(t)}</mark>'

def render(mk, site=True):
    """mk = função de marcação. site=True: versão da página Sobre (com botão); False: versão Solutudo (CTA em texto)."""
    h2 = 'h2' if site else 'h5'
    o = []
    o.append('<p>' + ' '.join(mk(*x) for x in ABERTURA) + '</p>')
    o.append(f'<{h2}>O que analisamos</{h2}>')
    o.append(f'<p>{E(ANALISES_INTRO)}</p>')
    o.append('<ul>' + ''.join(f'<li>{mk(*x)}</li>' for x in ANALISES) + '</ul>')
    o.append(f'<{h2}>Como trabalhamos</{h2}>')
    o.append('<ul>' + f'<li>{mk(*COMO[0])} {mk(*COMO[1])}</li>' + ''.join(f'<li>{mk(*x)}</li>' for x in COMO[2:]) + '</ul>')
    o.append(f'<{h2}>Onde coletamos</{h2}>')
    o.append(f'<p>{mk(*ONDE)}</p>')
    o.append(f'<{h2}>Quem atendemos</{h2}>')
    o.append(f'<p>{mk(*QUEM)}</p>')
    o.append(f'<{h2}>Atendimento e pagamento</{h2}>')
    o.append('<p>' + ' '.join(mk(*x) for x in ATEND) + '</p>')
    if site:
        o.append(f'<p class="pg-cta">{mk(*CTA)}</p>')
        o.append('<span class="pg-btn" aria-hidden="true">Pedir análise no WhatsApp</span>')
    else:
        o.append(f'<p class="cta">{mk(*CTA)}</p>')
    return '\n            '.join(o)

# =====================================================================
# 2. PÁGINAS DO SITE
# =====================================================================
PAGES = [
 dict(url='/', h1='LAAE — laboratório de análise de água e efluentes', title='LAAE · Análise de água e efluentes · Montes Claros (MG)',
      meta='Laboratório com serviços acreditados pela CGCRE/Inmetro e coleta própria em nove cidades de Minas Gerais. Água potável, de poço e efluentes.',
      q='laboratório de análise de água em Montes Claros', st='ok', stl='pronta'),
 dict(url='/sobre', h1='Sobre o LAAE', title='Sobre o LAAE · laboratório de água e efluentes desde 2003',
      meta='Laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003, com serviços acreditados pela CGCRE/Inmetro.',
      q='o LAAE é confiável? desde quando existe?', st='ok', stl='pronta · é o conteúdo único'),
 dict(url='/analises', h1='O que o LAAE analisa', title='Análises de água e efluentes · LAAE',
      meta='Análises físico-químicas e microbiológicas de água potável, de poço, superficial e de processo, e de efluentes industriais e sanitários.',
      q='que tipo de análise de água eu preciso?', st='ok', stl='pronta'),
 dict(url='/analises/fisico-quimica', h1='Análise físico-química da água', title='Análise físico-química da água · LAAE',
      meta='Avalia as características químicas e físicas da água potável, de consumo, superficial e subterrânea. Coleta pela nossa equipe e laudo no portal.',
      q='análise físico-química da água', st='pa', stl='pronta · parâmetros após o escopo'),
 dict(url='/analises/microbiologica', h1='Análise microbiológica da água', title='Análise microbiológica da água (bacteriológica) · LAAE',
      meta='Verifica a presença de microrganismos na água de poço, caixa d’água, reservatório e caminhão-pipa. Coleta própria em nove cidades de MG.',
      q='exame bacteriológico da água', st='pa', stl='pronta · parâmetros após o escopo'),
 dict(url='/analises/efluentes', h1='Análise de efluentes industriais e sanitários', title='Análise de efluentes industriais e sanitários · LAAE',
      meta='Análise de efluentes para acompanhamento de sistemas de tratamento, com coleta pela equipe do laboratório em nove cidades de Minas Gerais.',
      q='análise de efluente industrial', st='pa', stl='pronta · parâmetros após o escopo'),
 dict(url='/analises/agua-de-poco', h1='Análise da água do poço artesiano', title='Análise de água de poço artesiano · LAAE',
      meta='Quem capta água fora da rede pública responde pela qualidade dela. O LAAE indica os ensaios conforme o uso: consumo, produção ou irrigação.',
      q='preciso analisar a água do meu poço?', st='ok', stl='pronta'),
 dict(url='/monitoramento-ambiental', h1='Programa de monitoramento ambiental', title='Monitoramento ambiental de água e efluentes · LAAE',
      meta='Coleta e laudo no calendário: pontos, frequência e ensaios definidos com a sua equipe técnica, com os laudos disponíveis no portal.',
      q='monitoramento de efluentes', st='ok', stl='pronta'),
 dict(url='/coleta-e-amostragem', h1='Coleta e amostragem: onde e como coletamos', title='Coleta de água e efluentes em 9 cidades de MG · LAAE',
      meta='Coleta pela equipe do laboratório em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora.',
      q='vocês coletam na minha cidade?', st='ok', stl='pronta · substitui as 9 páginas de cidade'),
 dict(url='/perguntas-frequentes', h1='Perguntas frequentes', title='Perguntas sobre análise de água e laudos · LAAE',
      meta='Prazo da amostra, acreditação, poço artesiano, físico-química ou microbiológica, laudo no portal e orçamento: as respostas do LAAE.',
      q='as dúvidas antes de contratar', st='ok', stl='pronta · 7 de 8 respostas'),
 dict(url='/blog', h1='Blog do LAAE', title='Blog · água, efluentes e laudos · LAAE',
      meta='Artigos do laboratório sobre análise de água e efluentes, laudos e coleta, escritos a partir das dúvidas de quem contrata.',
      q='as buscas de cauda longa', st='pa', stl='abre com os 4 temas da E6'),
 dict(url='/contato', h1='Fale com o LAAE', title='Contato e como pedir uma análise · LAAE',
      meta='WhatsApp (38) 98405-5391, de segunda a sexta, das 8h às 12h e das 13h às 17h. Sede na Av. Professor Vicente Guimarães, 1095, Montes Claros.',
      q='telefone e endereço do LAAE', st='ok', stl='pronta'),
]
COND = [
 ('/analises/laudo-de-potabilidade', 'Laudo de potabilidade', 'a versão vigente da portaria e quais parâmetros do padrão estão no escopo acreditado — a norma é citada pelo número'),
 ('/analises/agronegocio', 'Água para irrigação, piscicultura e reuso', 'os parâmetros de cada uso, e se piscicultura e reuso são de fato atendidos'),
 ('/analises/agua-de-hemodialise', 'Água de hemodiálise', 'o escopo de acreditação para o ensaio. É o achado de maior valor do caso, e vem do site, que não foi aberto'),
]
for p in PAGES:
    assert len(p['title']) <= 60, (p['url'], len(p['title']))
    assert len(p['meta']) <= 155, (p['url'], len(p['meta']))

# =====================================================================
# 3. FAQ — resposta primeiro, nome da empresa em cada resposta
# =====================================================================
FAQ = [
 ('O LAAE coleta na minha cidade?',
  'O LAAE coleta em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora, com equipe própria. Para outras cidades, a consulta é pelo WhatsApp (38) 98405-5391.',
  ['Local','Conversão','Voz'], 'A intenção local pura. A lista inteira responde sem depender de página por cidade.', None),
 ('Quanto tempo a amostra de água vale depois de coletada?',
  'Para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas. É por isso que o LAAE faz a coleta com equipe própria e atende uma região definida.',
  ['IA','AEO'], 'O tema único do caso, em formato de resposta. Nenhum laboratório de fora da região publica isso.', 'confirmar quais ensaios têm prazo diferente'),
 ('O LAAE é acreditado?',
  'O LAAE tem serviços acreditados pela CGCRE do Inmetro: a acreditação vale para os ensaios listados nos escopos dos certificados da matriz. O laboratório também tem reconhecimento pela Rede Metrológica do Rio Grande do Sul segundo a ABNT NBR ISO/IEC 17025.',
  ['IA','Confiança'], 'Não começa com "sim": seria afirmar acreditação para tudo. A primeira frase responde e já carrega a ressalva.', None),
 ('Preciso analisar a água do meu poço artesiano?',
  'Quem capta água fora da rede pública responde pela qualidade dela, e a análise é o que mostra se a água do poço serve ao uso pretendido: consumo, produção ou irrigação. O LAAE indica os ensaios conforme o uso.',
  ['SEO','IA','Conversão'], 'O critério do dono ("quem usa água que não é da concessionária") transformado em resposta. Cauda longa real da categoria.', None),
 ('Qual a diferença entre análise físico-química e microbiológica?',
  'A análise físico-química mede características químicas e físicas da água; a microbiológica verifica a presença de microrganismos. Para o laudo de potabilidade, as duas são feitas juntas.',
  ['IA','AEO'], 'Pergunta definitória: o formato que IA e "as pessoas também perguntam" mais consomem. É a maior aposta de citação.', None),
 ('Como recebo o laudo do LAAE?',
  'O laudo do LAAE fica disponível no portal de resultados, com login e senha.',
  ['Conversão','Voz'], 'Uma frase, um fato. O portal é diferencial que nunca tinha sido publicado.', None),
 ('Quanto custa uma análise de água?',
  'O valor depende dos ensaios e do número de pontos de coleta. O orçamento do LAAE é feito pelo WhatsApp (38) 98405-5391, informando a origem da água, o uso e a cidade.',
  ['Conversão'], 'Fundo de funil. Responde sem inventar preço e já diz o que informar.', 'faixa de preço, se o laboratório quiser publicar'),
 ('Quais parâmetros o LAAE analisa?',
  None,
  ['SEO','IA'], 'Sem resposta publicável até o escopo de acreditação chegar. Quando chegar, cada parâmetro vira uma busca própria: "análise de coliformes em Montes Claros", "DBO de efluente", "turbidez da água".', 'a lista do escopo acreditado — bloqueia esta resposta'),
]
FAQ_GAPS = [
 ('Em quanto tempo o laudo fica pronto?', 'prazo por tipo de análise — laboratório'),
 ('Com que frequência a equipe passa em cada cidade?', 'rota e frequência — laboratório. É o fato que justificaria uma página por cidade'),
 ('O LAAE atende fora de Minas Gerais?', 'o papel das franquias da Bahia na resposta — "11 estados" do site é alcance de franqueadora e está em conflito'),
]

# =====================================================================
# 4. JSON-LD esperado da página /sobre (gerado pela aplicação)
# =====================================================================
BASE = 'https://lablaae.com.br'
CIDADES = ['Montes Claros','Jaíba','Janaúba','Januária','Diamantina','Curvelo','Salinas','Araçuaí','Pirapora']
JSONLD = {
 "@context": "https://schema.org",
 "@graph": [
  {"@type":"WebSite","@id":f"{BASE}/#site","url":f"{BASE}/","name":"LAAE","alternateName":"LabLAAE","inLanguage":"pt-BR"},
  {"@type":"LocalBusiness","@id":f"{BASE}/#laae",
   "name":"LAAE Laboratório de Análise de Água e Efluentes","alternateName":"LabLAAE",
   "description":ABERTURA[0][0],
   "url":f"{BASE}/","telephone":"+55 38 98405-5391","email":"comercial@lablaae.com.br",
   "address":{"@type":"PostalAddress","streetAddress":"Av. Professor Vicente Guimarães, 1095, Vicente Guimarães","addressLocality":"Montes Claros","addressRegion":"MG","postalCode":"39401-781","addressCountry":"BR"},
   "geo":{"@type":"GeoCoordinates","latitude":-16.7425054,"longitude":-43.8754184},
   "openingHoursSpecification":[
     {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"12:00"},
     {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"13:00","closes":"17:00"}],
   "foundingDate":"2003",
   "areaServed":[{"@type":"City","name":f"{c}, MG"} for c in CIDADES],
   "knowsAbout":["análise de água","análise físico-química","análise microbiológica","análise de efluentes","amostragem de água","monitoramento ambiental"],
   "hasOfferCatalog":{"@type":"OfferCatalog","name":"Análises","itemListElement":[
     {"@type":"Offer","itemOffered":{"@type":"Service","name":n,"url":f"{BASE}{u}"}} for n,u in [
       ("Análise físico-química da água","/analises/fisico-quimica"),("Análise microbiológica da água","/analises/microbiologica"),
       ("Análise de efluentes industriais e sanitários","/analises/efluentes"),("Análise da água do poço artesiano","/analises/agua-de-poco"),
       ("Programa de monitoramento ambiental","/monitoramento-ambiental"),("Coleta e amostragem","/coleta-e-amostragem")]]},
   "sameAs":["https://www.instagram.com/lablaae"]},
  {"@type":"WebPage","@id":f"{BASE}/sobre#pagina","url":f"{BASE}/sobre","name":"Sobre o LAAE","isPartOf":{"@id":f"{BASE}/#site"},"about":{"@id":f"{BASE}/#laae"},"inLanguage":"pt-BR","dateModified":"2026-09-29"},
  {"@type":"BreadcrumbList","itemListElement":[
     {"@type":"ListItem","position":1,"name":"Início","item":f"{BASE}/"},
     {"@type":"ListItem","position":2,"name":"Sobre","item":f"{BASE}/sobre"}]}
 ]}
JSONLD_TXT = json.dumps(JSONLD, ensure_ascii=False, indent=2)
json.loads(JSONLD_TXT)
FAQLD = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,*_ in FAQ[:2] if a]}
FAQLD_TXT = json.dumps(FAQLD, ensure_ascii=False, indent=2)
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

# =====================================================================
# 5. HTML da aba Solusite
# =====================================================================
def sec(id_, n, title, sub, body):
    return f'''      <div class="csec" id="{id_}">
        <div class="csh"><span class="csn">{n}</span><div><h3>{title}</h3><p>{sub}</p></div></div>
{body}      </div>

'''
def stt(k, lab):
    return f'<span class="stt {k}">{lab}</span>'

MENU = '''    <nav class="cont-menu" aria-label="Seções da aba Solusite">
      <span class="cm-title">Nesta aba</span>
      <a href="#s-padrao" class="cm-i on"><b>1</b>O que esperamos</a>
      <a href="#s-conteudo" class="cm-i"><b>2</b>O conteúdo</a>
      <a href="#s-paginas" class="cm-i"><b>3</b>Páginas do site</a>
      <a href="#s-faq" class="cm-i"><b>4</b>Perguntas (AEO)</a>
      <a href="#s-leitores" class="cm-i"><b>5</b>Como é encontrado</a>
      <a href="#s-tecnica" class="cm-i"><b>6</b>Camada técnica</a>
      <a href="#s-gate" class="cm-i"><b>7</b>Antes de publicar</a>
      <a href="#s-spec" class="cm-i"><b>8</b>Especificação</a>
    </nav>
'''

# --- seção 1
CENTRAIS = [
 ('Pizza Frita Semião', 'pa','parcial', 'pa','parcial', 'pa','via Destaque', 'pa','home + 2', 'no','não tem'),
 ('Porto Certo Consórcio', 'pa','parcial', 'pa','parcial', 'pa','via Destaque', 'pa','só a home', 'no','não tem'),
 ('EA3 Engenharia', 'no','orientação', 'pa','frase do banner', 'no','não tem', 'no','não tem', 'no','não tem'),
 ('Blocok O Original', 'pa','parcial', 'no','não tem', 'pa','via Destaque', 'pa','home + URLs', 'no','não tem'),
 ('LAAE · antes', 'pa','parcial', 'no','não tem', 'pa','via Destaque', 'pa','home + 1', 'pa','2 regras'),
 ('LAAE · agora', 'ok','completo', 'ok','8 frases', 'ok','8 perguntas', 'ok','12 páginas', 'ok','especificada'),
]
rows = ''.join(f'<tr><td><b>{c[0]}</b></td>' + ''.join(f'<td>{stt(c[i], c[i+1])}</td>' for i in (1,3,5,7,9)) + '</tr>' for c in CENTRAIS)
S1 = f'''        <div class="card" style="border-color:rgba(167,1,253,.28)">
          <span class="badge">O padrão · a partir da LAAE, para todas</span>
          <h3>O site é o mesmo conteúdo dos detalhes da empresa — e é maior que eles</h3>
          <p class="sub">O conteúdo da seção 2 é o texto que vai para a <b>página Sobre do site</b> e para os <b>detalhes da empresa na página Solutudo</b>: mesmos fatos, mesmas frases, mesma ordem. Muda só a forma do contato — texto por extenso na Solutudo, botão com link no site. O formato vem do caso de referência <a href="../../sobre-empresa-new-rock/" target="_blank" rel="noopener">New Rock</a>: entidade primeiro, FAQ ancorado em fato, as três camadas da página e as regras de indexação.</p>
          <div class="vit">
            <div class="vit-c"><span class="vit-h">Página Solutudo · detalhes da empresa</span><div class="vit-sh">conteúdo único</div><ul><li>contato em texto, sem link</li><li>avaliações nativas, com marcação</li><li>selo de procedência</li></ul></div>
            <div class="vit-m" aria-hidden="true"><span>gerado uma vez,<br>publicado nas duas</span></div>
            <div class="vit-c"><span class="vit-h">Solusite · lablaae.com.br</span><div class="vit-sh">conteúdo único <small>= página Sobre</small></div><ul><li>botões com link e WhatsApp fixo</li><li>uma página por análise, coleta, perguntas, blog</li><li>avaliações exibidas, sem marcação</li></ul></div>
          </div>
          <div class="note"><b>O custo conhecido, e como ele é pago.</b> Texto idêntico em dois domínios faz o buscador mostrar um deles para aquela busca — não é penalidade, é escolha. Por isso o site é sempre <b>maior</b> que a página: quem busca o LAAE pelo nome encontra os dois; quem busca "análise de efluente" encontra a página da análise, que só existe no site. Cada domínio aponta o canonical para si mesmo. A Descrição 3.0 tinha deixado essa decisão em aberto; ela está registrada em <code>docs/solusite-padrao.md</code>.</div>
        </div>

        <div class="rd4">
          <div class="rd"><span class="rd-k">Pessoas</span><b>decidem e chamam</b><p>Contato no topo, WhatsApp fixo no celular, página rápida. O dono reclamou do site atual: <i>"leva um tempo para carregar"</i> e <i>"não tem o seu telefone"</i>.</p></div>
          <div class="rd"><span class="rd-k">SEO</span><b>encontra e ordena</b><p>Google e Bing. Uma página por intenção de busca, com title, meta e H1 próprios. O Bing pesa mais do que parece: é por onde a busca do ChatGPT descobre páginas.</p></div>
          <div class="rd"><span class="rd-k">AEO</span><b>responde</b><p>Trechos em destaque, "as pessoas também perguntam" e voz. A pergunta vira título; a primeira frase responde sozinha.</p></div>
          <div class="rd"><span class="rd-k">GEO</span><b>cita</b><p>ChatGPT, Perplexity, Claude, Gemini e AI Overviews. Frases atômicas com o nome, o que faz e o fato — no HTML servido, porque os robôs de IA não executam JavaScript.</p></div>
        </div>

        <div class="card">
          <span class="badge">Como estamos hoje nas cinco centrais</span>
          <h3>Todas têm os blocos do site. Nenhuma tratava GEO nem a camada técnica.</h3>
          <p class="sub">O SEO se resumia ao title e à meta da home, e o FAQ do site apontava para o da página de Destaque, sem regra de resposta. A LAAE é a primeira central refeita no padrão; as outras quatro ficam como estão até serem retomadas uma a uma.</p>
          <div class="scroller"><table>
            <tr><th>Central</th><th>Texto final por página</th><th>Frases citáveis · GEO</th><th>FAQ resposta-primeiro · AEO</th><th>Title, meta e H1 · SEO</th><th>Camada técnica</th></tr>
            {rows}
          </table></div>
        </div>
'''

# --- seção 2
legend = ''.join(f'<span class="pvl {k}">{E(v[0])}</span>' for k,v in PV.items())
S2 = f'''        <div class="card">
          <span class="badge mint">O texto · {NWORDS} palavras · uma fonte, duas vitrines</span>
          <h3>Sobre o LAAE — o conteúdo recomendado para o site e para os detalhes da empresa</h3>
          <p class="sub">Passe o mouse ou toque em cada frase para ver de onde ela vem e por que está ali. A aba Destaque mostra exatamente este texto na versão Solutudo, gerado da mesma fonte.</p>
          <div class="pvlegend">{legend}</div>
          <div class="pgf">
            <div class="pgf-bar"><i></i><i></i><i></i><span class="pgf-url">lablaae.com.br/sobre</span></div>
            <div class="pgf-body">
            <span class="pgf-crumb">Início › Sobre</span>
            <h1>Sobre o LAAE</h1>
            {render(pvmark, site=True)}
            <p class="pgf-upd">Atualizado em 29/09/2026</p>
            </div>
          </div>
          <div class="grid2">
            <div class="blk"><h4>Na página Solutudo</h4><p class="bwhy">O mesmo texto, com o contato por extenso — a regra da casa é CTA sem link. Fecha com o selo de procedência.</p></div>
            <div class="blk"><h4>No Solusite</h4><p class="bwhy">O mesmo texto, com o botão "Pedir análise no WhatsApp" apontando para <code>wa.me/5538984055391</code>, com mensagem pronta, e o WhatsApp fixo no celular. Fecha com "Atualizado em".</p></div>
          </div>
        </div>

        <div class="card">
          <span class="badge">O que mudou em relação à versão anterior</span>
          <ul class="clean">
            <li><b>Saiu "e demais cidades do Norte de Minas".</b> Prometia cobertura sem fato. A lista das nove fica inteira, e o resto é "consulte".</li>
            <li><b>"Norte de Minas" deixou de nomear a cobertura.</b> Diamantina, Curvelo e Araçuaí não ficam no Norte de Minas; o texto diz "nove cidades de Minas Gerais".</li>
            <li><b>O prazo de 24 horas ganhou precisão.</b> "Para boa parte dos ensaios", porque o prazo muda de ensaio para ensaio. Confirmar com o laboratório quais são as exceções.</li>
            <li><b>Entraram "Quem atendemos" e "Atendimento e pagamento"</b> como blocos próprios. A abertura passou a carregar a coleta, que é o diferencial.</li>
            <li><b>Entrou "água industrial de processo"</b>, do site oficial, marcada para conferência. A água de hemodiálise ficou fora do texto até o escopo chegar.</li>
            <li><b>A meta da home antiga dizia "Acreditação CGCRE/Inmetro desde 2003".</b> Estava errado: 2003 é o ano de fundação, não o da acreditação. Corrigido.</li>
            <li><b>A aba Destaque passou a mostrar este mesmo texto.</b> A meta da página Solutudo também foi corrigida: dizia "acreditado pela CGCRE/Inmetro" sem a ressalva do escopo e citava só quatro das nove cidades.</li>
          </ul>
        </div>
'''

# --- seção 3
prow = ''.join(
  f'<tr><td><code>{E(p["url"])}</code></td><td>{E(p["h1"])}</td>'
  f'<td>{E(p["title"])} <span class="cnt">{len(p["title"])}/60</span></td>'
  f'<td>{E(p["meta"])} <span class="cnt">{len(p["meta"])}/155</span></td>'
  f'<td><i>{E(p["q"])}</i></td><td>{stt(p["st"], E(p["stl"]))}</td></tr>' for p in PAGES)
crow = ''.join(f'<tr><td><code>{E(u)}</code></td><td>{E(t)}</td><td>{E(w)}</td></tr>' for u,t,w in COND)
S3 = f'''        <div class="card">
          <span class="badge">Mapa do site · {len(PAGES)} páginas prontas ou quase</span>
          <h3>Uma página por intenção de busca, cada uma com title, meta e H1 próprios</h3>
          <p class="sub">Caracteres contados, não estimados. O nome da entidade é <b>LAAE</b> em todas as páginas; <b>LabLAAE</b>, o domínio e o Instagram, entra uma vez, como nome alternativo — IA reconhece empresa por nome consistente.</p>
          <div class="scroller"><table class="pgtbl">
            <tr><th>URL</th><th>H1</th><th>Title</th><th>Meta description</th><th>Responde a</th><th>Status</th></tr>
            {prow}
          </table></div>
          <h4 style="margin-top:18px">Páginas que esperam confirmação</h4>
          <div class="scroller"><table>
            <tr><th>URL</th><th>Página</th><th>Sobe quando chegar</th></tr>
            {crow}
          </table></div>
        </div>

        <div class="card" style="border-color:rgba(180,83,9,.35);background:linear-gradient(180deg,#FFFBF0 0%,var(--white) 60%)">
          <span class="badge warn">Mudança de recomendação · as nove páginas de cidade</span>
          <h3>Uma página de coleta com as nove cidades, e não nove páginas de cidade</h3>
          <p class="sub">A versão anterior desta aba recomendava <code>/analise-de-agua-em-jaiba</code>, <code>/janauba</code>, <code>/januaria</code> e assim por diante. Sem um fato próprio de cada cidade, essas páginas só trocariam o nome — e é exatamente esse padrão que as atualizações de spam do Google derrubam desde 2024, como registra a auditoria do caso New Rock. O cadastro não traz a frequência da rota, o cliente atendido nem o ponto de coleta de cada cidade.</p>
          <div class="note"><b>Quando vale criar a página da cidade:</b> no dia em que ela tiver pelo menos um fato só dela — a frequência com que a equipe passa, um cliente de lá com autorização, o tipo de água que mais se analisa ali. Até lá, <code>/coleta-e-amostragem</code> responde "vocês coletam na minha cidade?" para as nove, e a meta dela já lista todas.</div>
        </div>

        <div class="card">
          <span class="badge">A home, bloco a bloco · na ordem das três camadas</span>
          <h3>Contato primeiro, confiança depois, profundidade por último</h3>
          <div class="scroller"><table>
            <tr><th>#</th><th>Bloco</th><th>O que vai nele</th><th>Camada</th></tr>
            <tr><td>1</td><td><b>Topo</b></td><td>H1 com a entidade, a linha <i>"A coleta vai até você. O laudo fica no seu portal."</i>, botões <b>Pedir análise no WhatsApp</b> e <b>Ver o que analisamos</b>, e o horário</td><td>{stt('ok','consumo')}</td></tr>
            <tr><td>2</td><td><b>O que analisamos</b></td><td>As cinco aplicações do conteúdo único, cada uma com link para a sua página</td><td>{stt('ok','consumo')}</td></tr>
            <tr><td>3</td><td><b>A coleta e as 24 horas</b></td><td>O tema único do caso: por que a coleta é própria e o atendimento é regional</td><td>{stt('pa','confiança')}</td></tr>
            <tr><td>4</td><td><b>Onde coletamos</b></td><td>As nove cidades, com link para <code>/coleta-e-amostragem</code></td><td>{stt('ok','consumo')}</td></tr>
            <tr><td>5</td><td><b>Credencial</b></td><td>CGCRE/Inmetro com a ressalva do escopo e a Rede Metrológica RS</td><td>{stt('pa','confiança')}</td></tr>
            <tr><td>6</td><td><b>Quem confia</b></td><td>SEAM, Hospital do Câncer do Norte de Minas e Tânia Botelho — <b>após autorização</b></td><td>{stt('pa','confiança')}</td></tr>
            <tr><td>7</td><td><b>Perguntas</b></td><td>As três primeiras do FAQ, com link para a página inteira</td><td>{stt('pa','confiança')}</td></tr>
            <tr><td>8</td><td><b>Do blog</b></td><td>Os posts mais recentes — a prova de site vivo, que era a queixa do dono</td><td>{stt('no','profundidade')}</td></tr>
            <tr><td>9</td><td><b>Contato</b></td><td>WhatsApp, fixo, e-mail, endereço da sede em <code>&lt;address&gt;</code>, mapa e "Atualizado em"</td><td>{stt('ok','consumo')}</td></tr>
          </table></div>
          <div class="note">O blog publica os 24 temas da <a href="#c-editorias" onclick="return goSec('c-editorias')">aba Conteúdo</a>, começando pelos quatro da E6, que são os que capturam busca. É o bloco que resolve a queixa de <i>"site estacionado"</i>.</div>
        </div>
'''

# --- seção 4
def faq_item(q, a, tags, why, pend):
    tg = ''.join(f'<span class="tg">{E(t)}</span>' for t in tags)
    ans = (f'<p class="faq-a">{E(a)}</p>' if a else '<p class="faq-a faq-none">Sem resposta publicável hoje.</p>')
    pd = f'<p class="faq-p"><b>Confirmar:</b> {E(pend)}</p>' if pend else ''
    return f'''          <div class="faqi">
            <h4>{E(q)}</h4>
            {ans}
            <div class="faq-m"><span class="tgs">{tg}</span><span class="faq-w">{E(why)}</span></div>
            {pd}
          </div>
'''
FAQH = ''.join(faq_item(*f) for f in FAQ)
gaps = ''.join(f'<tr><td><b>{E(q)}</b></td><td>{E(w)}</td></tr>' for q,w in FAQ_GAPS)
S4 = f'''        <div class="card">
          <span class="badge">Perguntas frequentes · a página /perguntas-frequentes</span>
          <h3>A primeira frase responde, e o nome do LAAE está em cada resposta</h3>
          <p class="sub">É o que trechos em destaque, voz e IA extraem: uma resposta que se sustenta sozinha, fora da página. As mesmas perguntas e respostas aparecem na página Solutudo. As etiquetas dizem quem cada uma serve.</p>
{FAQH}        </div>

        <div class="card">
          <span class="badge warn">Perguntas que o site precisa responder e ainda não pode</span>
          <div class="scroller"><table>
            <tr><th>Pergunta</th><th>O que falta, e de quem</th></tr>
            {gaps}
          </table></div>
          <div class="note">Regra da casa: pergunta sem resposta específica da empresa não entra no FAQ. Ficam aqui como pendência, não como texto genérico.</div>
        </div>
'''

# --- seção 5
CITAVEIS = [
 'O LAAE é um laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003.',
 'O LAAE tem serviços acreditados pela CGCRE do Inmetro, conforme os escopos dos certificados.',
 'O LAAE coleta amostras com equipe própria em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora.',
 'O LAAE faz análises físico-químicas e microbiológicas de água potável, superficial e subterrânea, e de efluentes industriais e sanitários.',
 'Os laudos do LAAE ficam disponíveis em um portal de resultados, com login e senha.',
 'O LAAE atende de segunda a sexta, das 8h às 12h e das 13h às 17h, pelo WhatsApp (38) 98405-5391.',
 'Para boa parte dos ensaios, a amostra de água precisa chegar ao laboratório em até 24 horas depois de coletada.',
 'Quem capta água fora da rede pública responde pela qualidade dela.',
]
cit = ''.join(f'<li><span class="cq">{E(c)}</span></li>' for c in CITAVEIS)
S5 = f'''        <div class="card">
          <span class="badge">GEO · as frases que uma IA pode citar inteiras</span>
          <h3>Oito frases que se sustentam fora da página</h3>
          <p class="sub">Cada uma tem sujeito explícito, um fato só e nenhum "isso" apontando para trás. É o que ChatGPT, Perplexity, Claude e o AI Overview do Google extraem quando alguém pergunta sobre análise de água na região. Todas estão no texto das seções 2 e 4 — nenhuma foi escrita só para máquina.</p>
          <ol class="citl">{cit}</ol>
          <div class="note">As duas últimas não levam o nome do LAAE de propósito: são fatos do setor que o laboratório explica, e a IA os cita como resposta atribuindo a fonte pela página. As seis primeiras são fatos da empresa e carregam o nome.</div>
        </div>

        <div class="card">
          <span class="badge">SEO · AEO · GEO · o que cada bloco faz por cada leitor</span>
          <div class="scroller"><table>
            <tr><th>Bloco ou página</th><th>O que a pessoa busca</th><th>SEO · encontra</th><th>AEO · responde</th><th>GEO · cita</th></tr>
            <tr><td><b>Abertura do Sobre</b></td><td><i>laboratório de análise de água em Montes Claros</i></td><td>categoria e sede no title, no H1 e na 1ª frase</td><td>—</td><td>a frase de entidade, inteira</td></tr>
            <tr><td><b>Páginas de análise</b></td><td><i>análise físico-química da água</i> · <i>análise de efluente</i></td><td>uma página por análise, com link da home</td><td>"qual a diferença entre…"</td><td>a lista de aplicações com o nome</td></tr>
            <tr><td><b>Coleta e as 24 horas</b></td><td><i>quanto tempo a amostra de água dura</i></td><td>página de coleta indexável</td><td>a resposta de uma frase</td><td>o prazo, com a fonte na página</td></tr>
            <tr><td><b>Coleta e amostragem</b></td><td><i>análise de água em Janaúba</i></td><td>as nove cidades na meta e no corpo</td><td>"vocês coletam na minha cidade?"</td><td>a lista de cidades</td></tr>
            <tr><td><b>Perguntas frequentes</b></td><td>as dúvidas antes de contratar</td><td>página própria, com <code>FAQPage</code></td><td>respostas de uma frase</td><td>cada resposta, com o nome</td></tr>
            <tr><td><b>Blog</b></td><td>as buscas de cauda longa</td><td>uma página indexável por tema</td><td>a 1ª frase de cada post</td><td>frescor: conteúdo recente é mais citado</td></tr>
          </table></div>
        </div>
'''

# --- seção 6
S6 = f'''        <div class="card">
          <span class="badge">JSON-LD da página /sobre · gerado pela aplicação, por código</span>
          <h3>O mesmo fato do texto, em formato que a máquina lê</h3>
          <p class="sub">Não há tipo dedicado a laboratório ambiental no schema.org, então o nó do negócio é <code>LocalBusiness</code>. <code>DiagnosticLab</code> não serve: é laboratório médico. Nada aqui que não esteja visível na página, e <b>nenhum <code>aggregateRating</code></b> — empresa marcando avaliação de si no próprio site é inelegível.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'ld-sobre','Copiar o JSON-LD')">Copiar o JSON-LD</button>
          <pre class="prompt codeb" id="ld-sobre">{E(JSONLD_TXT)}</pre>
          <div class="note"><b>Três ressalvas.</b> O domínio só é <code>lablaae.com.br</code> se o Solusite substituir o site atual — ver a seção 7. O <code>sameAs</code> do Instagram vem do cadastro; o perfil não foi aberto. E a data de <code>dateModified</code> muda só em mudança material do conteúdo, nunca para parecer recente.</div>
        </div>

        <div class="card">
          <span class="badge">FAQPage da página /perguntas-frequentes · trecho</span>
          <pre class="prompt codeb">{E(FAQLD_TXT)}</pre>
          <p class="bwhy" style="margin-top:8px">O texto do JSON-LD é idêntico ao texto visível — é a regra. A marcação não dá mais estrela no Google para empresa comum desde 2023; ela vale pelo que ajuda a máquina a separar pergunta de resposta.</p>
        </div>

        <div class="card">
          <span class="badge">robots.txt, indexação, velocidade e frescor</span>
          <div class="grid2">
            <div>
              <pre class="prompt codeb">{E(ROBOTS)}</pre>
              <p class="bwhy" style="margin-top:8px">Liberar no <code>robots.txt</code> não basta: <b>conferir se a CDN ou o firewall bloqueiam robôs de IA por padrão</b>. É comum, e ninguém percebe até o site sumir das respostas.</p>
            </div>
            <ul class="clean">
              <li><b>Tudo no HTML servido.</b> Desligue o JavaScript: se o texto sumir, está errado.</li>
              <li><b>Contato clicável e visível:</b> <code>tel:</code> e <code>wa.me</code> em texto, sem "ver telefone"; WhatsApp fixo no celular.</li>
              <li><b>meta robots</b> <code>index, follow, max-snippet:-1, max-image-preview:large</code> e canonical para si mesmo em toda página.</li>
              <li><b>sitemap.xml</b> só com as páginas da seção 3 que estiverem no ar.</li>
              <li><b>Core Web Vitals no p75:</b> LCP até 2,5 s · INP até 200 ms · CLS até 0,1. Aqui isso é a queixa do cliente, não um detalhe técnico: <i>"ele leva um tempo para carregar"</i>.</li>
              <li><b>Frescor:</b> "Atualizado em" visível, <code>dateModified</code> no <code>WebPage</code> e IndexNow para o Bing a cada mudança material.</li>
              <li><b>Imagens:</b> <code>alt</code> descrevendo o que a foto mostra — e hoje não há foto da operação para descrever.</li>
            </ul>
          </div>
        </div>
'''

# --- seção 7
GATE = [
 ('O Solusite existe?', 'O campo Solusite está <code>false</code>, mas o cadastro guarda seis imagens de Solusite com legendas prontas. Alguém começou a montar.', 'CS', 'no', 'bloqueia tudo'),
 ('Qual domínio?', 'O Solusite substitui <code>lablaae.com.br</code> ou convive com ele? Convivendo, são três vitrines com o mesmo texto: o site atual, o Solusite e a página Solutudo.', 'produto + cliente', 'no', 'bloqueia tudo'),
 ('Um nome só', 'LAAE ou LabLAAE em todos os canais? A recomendação é LAAE, com LabLAAE como nome alternativo.', 'cliente', 'pa', 'ajusta títulos'),
 ('Escopo de acreditação', 'A lista de parâmetros acreditados. Sem ela, as páginas de análise não descem ao parâmetro e uma pergunta do FAQ fica sem resposta.', 'laboratório', 'pa', 'limita 3 páginas'),
 ('As 24 horas por ensaio', 'Quais ensaios têm prazo diferente de 24 horas.', 'laboratório', 'pa', 'ajusta 2 frases'),
 ('Fatos do site atual', 'Água industrial de processo, temperatura monitorada e o portal vieram de um resumo colado; o site não foi aberto.', 'nós', 'pa', 'conferir na fonte'),
 ('Fotos da operação', 'Nenhuma no cadastro. O site fica de pé sem elas, mas a home e as páginas de análise perdem a prova visual.', 'cliente', 'pa', 'limita a home'),
 ('Depoimentos', 'SEAM, Hospital do Câncer do Norte de Minas e Tânia Botelho: autorização para o Solusite.', 'cliente', 'pa', 'bloqueia o bloco 6'),
 ('Robôs de IA na CDN', 'Conferir se a hospedagem bloqueia robôs de IA por padrão.', 'técnico', 'pa', 'antes de publicar'),
 ('Velocidade, antes e depois', 'Medir o site atual e o Solusite com os mesmos critérios. É a primeira prova de resultado para o cliente.', 'nós', 'ok', 'recomendado'),
]
grow = ''.join(f'<tr><td><b>{q}</b></td><td>{w}</td><td>{o}</td><td>{stt(k, l)}</td></tr>' for q,w,o,k,l in GATE)
S7 = f'''        <div class="card">
          <span class="badge warn">O que falta para a LAAE ir ao ar</span>
          <h3>Dois bloqueios de verdade, e o resto são ajustes</h3>
          <div class="scroller"><table>
            <tr><th>Pendência</th><th>O que é</th><th>Dono</th><th>Efeito</th></tr>
            {grow}
          </table></div>
        </div>

        <div class="card">
          <span class="badge">Checklist de bolso · antes de publicar qualquer página</span>
          <ul class="chk">
            <li>Telefone e WhatsApp visíveis, grandes e clicáveis, sem clique para revelar?</li>
            <li>Desligando o JavaScript, o conteúdo principal continua na tela?</li>
            <li>Todo texto importante é texto de verdade, não imagem?</li>
            <li>A ação de contato é a primeira coisa que se lê?</li>
            <li>A primeira frase da página diz o que a empresa é, a categoria e a sede?</li>
            <li>Toda afirmação tem fonte, e toda lacuna tem dono?</li>
            <li>Title, meta e H1 próprios, com os caracteres contados?</li>
            <li>JSON-LD gerado pela aplicação, espelhando o texto visível, sem avaliação de si mesma?</li>
            <li>Página leve, dentro dos Core Web Vitals, e boa no celular?</li>
            <li>"Atualizado em" visível?</li>
          </ul>
        </div>
'''

# --- seção 8
S8 = f'''        <div class="card">
          <span class="badge">§7 de <code style="text-transform:none;letter-spacing:0">docs/solusite-padrao.md</code> · texto vigente</span>
          <h3>O padrão do Solusite, para quem monta o site</h3>
          <p class="sub">A versão de bolso deste padrão. Serve para a pessoa que monta o site e para um agente que gere o site a partir do cadastro. Copiado do arquivo-fonte na íntegra — quando o padrão mudar, esta página é regenerada.</p>
          <button type="button" class="copybtn" onclick="copyBlock(this,'spec-text','Copiar a especificação')">Copiar a especificação</button>
          <pre class="prompt" id="spec-text">{E(SPEC)}</pre>
        </div>
'''

SITE = f'''  <section id="p-site" class="panel">

    <div class="sec first">
      <span class="eyebrow">Produto · Site Profissional (Solusite)</span>
      <h2>O site que pessoas, buscadores e IAs encontram — com o mesmo conteúdo dos detalhes da empresa</h2>
      <p class="secsub">Esta aba é o padrão do Solusite aplicado à LAAE: o conteúdo recomendado para o site, que é o mesmo dos detalhes da empresa na página Solutudo, organizado para SEO, AEO e GEO. O formato segue o caso de referência New Rock; o padrão completo está em <code>docs/solusite-padrao.md</code>. <b>Comece pela seção 7</b> se a pergunta for "dá para publicar?".</p>
    </div>

    <div class="cont-layout">
{MENU}    <div class="cont-body">

{sec('s-padrao', 1, 'O que esperamos do Solusite', 'Um conteúdo, duas vitrines, quatro leitores — e onde as cinco centrais estavam antes deste padrão.', S1)}{sec('s-conteudo', 2, 'O conteúdo', 'O texto da página Sobre do site, que é o mesmo dos detalhes da empresa na Solutudo. Cada frase marcada com a sua fonte.', S2)}{sec('s-paginas', 3, 'Páginas do site', 'URL, H1, title, meta e a pergunta que cada página responde. E por que as nove páginas de cidade saíram.', S3)}{sec('s-faq', 4, 'Perguntas · AEO', 'Oito perguntas com a resposta na primeira frase, e as três que o site ainda não pode responder.', S4)}{sec('s-leitores', 5, 'Como é encontrado', 'As frases que uma IA cita inteiras, e o que cada bloco faz por cada leitor.', S5)}{sec('s-tecnica', 6, 'Camada técnica', 'O que a aplicação precisa gerar: JSON-LD, robots.txt, indexação, velocidade e frescor.', S6)}{sec('s-gate', 7, 'Antes de publicar', 'O que ainda bloqueia a LAAE, com dono, e o checklist que vale para qualquer página.', S7)}{sec('s-spec', 8, 'Especificação', 'O padrão do Solusite em texto corrido, com botão de copiar, para quem monta o site.', S8)}    </div>
    </div>

  </section>

'''

i0 = s.index('  <section id="p-site" class="panel">')
i1 = s.index('  <section id="p-gmb" class="panel">')
s = s[:i0] + SITE + s[i1:]

# =====================================================================
# 6. ABA DESTAQUE — o mesmo texto, versão Solutudo
# =====================================================================
a = s.index('<div class="col next"><div class="colh">● Descrição 3.0</div><div class="colb">')
a2 = s.index('<div class="colb">', a) + len('<div class="colb">')
b = s.index('</div><div class="sc"><div class="scnum"><b>94</b>', a2)
s = s[:a2] + '\n        ' + render(goodmark, site=False) + '\n        ' + s[b:]

rep('''<div class="selo"><b>Selo de procedência · variante A (parceiro)</b> Informações fornecidas pela empresa no cadastro Solutudo, no contrato e na reunião comercial gravada · verificadas em 08/09/2026. Após reconfirmação via CS, atualizar a data.</div>''',
    '''<div class="selo"><b>Selo de procedência · variante A (parceiro)</b> Informações fornecidas pela empresa no cadastro Solutudo, no contrato e na reunião comercial gravada · verificadas em 08/09/2026. Após reconfirmação via CS, atualizar a data.</div>
      <div class="note" style="background:var(--tint-lav);color:#4A1080"><b>Este é o mesmo texto da página Sobre do site</b> — um conteúdo, duas vitrines (<a href="#s-conteudo" onclick="return goSec('s-conteudo')">aba Solusite, seção 2</a>). Revisado em 29/09/2026: a cobertura passou a ser a lista das nove cidades, sem "demais cidades do Norte de Minas"; o prazo de 24 horas ganhou a ressalva de ensaio; entraram "Quem atendemos" e "Atendimento e pagamento". As notas acima foram mantidas: as mudanças corrigem precisão, não estrutura. As marcações em roxo pedem confirmação antes de publicar.</div>''')
OLD_META = 'Laboratório de análise de água e efluentes acreditado pela CGCRE/Inmetro. Coleta própria em Montes Claros, Jaíba, Janaúba, Januária e Norte de Minas.<span class="cnt">149/160</span>'
NEW_META_T = 'Laboratório de análise de água e efluentes em Montes Claros (MG), com serviços acreditados pela CGCRE/Inmetro e coleta própria em nove cidades.'
assert len(NEW_META_T) <= 160
rep(OLD_META, f'{NEW_META_T}<span class="cnt">{len(NEW_META_T)}/160</span>')

# =====================================================================
# 7. CSS
# =====================================================================
CSS = r'''  /* aba Solusite · padrão do site */
  .vit{display:grid;grid-template-columns:minmax(0,1fr) 120px minmax(0,1fr);gap:12px;align-items:stretch;margin-top:14px}
  .vit-c{border:var(--line);border-radius:14px;padding:14px 16px;background:var(--white)}
  .vit-h{display:block;font-size:10.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--g600)}
  .vit-sh{margin-top:8px;border-radius:10px;padding:9px 12px;background:var(--tint-mint);color:#06724F;font-weight:800;font-size:13.4px}
  .vit-sh small{font-weight:700;opacity:.8}
  .vit-c ul{margin:9px 0 0 18px;font-size:12.8px;color:var(--g700);line-height:1.5}
  .vit-m{display:flex;align-items:center;justify-content:center;text-align:center;font-size:11.5px;font-weight:800;color:#06724F;position:relative}
  .vit-m::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:2px dashed #7fd8bf;z-index:0}
  .vit-m span{position:relative;z-index:1;background:var(--white);padding:4px 6px;border-radius:8px;line-height:1.3}
  @media(max-width:760px){.vit{grid-template-columns:1fr}.vit-m::before{display:none}}
  .rd4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:14px}
  @media(max-width:1200px){.rd4{grid-template-columns:1fr 1fr}}
  @media(max-width:560px){.rd4{grid-template-columns:1fr}}
  .rd{border:var(--line);border-radius:16px;padding:15px 16px;background:var(--white);box-shadow:var(--shadow-card)}
  .rd-k{display:inline-block;font-size:10.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;background:var(--ink);color:#fff;border-radius:var(--pill);padding:3px 10px}
  .rd b{display:block;font-size:15px;font-weight:800;margin-top:8px;letter-spacing:-.02em}
  .rd p{font-size:12.8px;color:var(--g700);margin-top:5px;line-height:1.5}
  .pvlegend{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
  .pvl{font-size:11px;font-weight:800;padding:3px 10px;border-radius:var(--pill);background:var(--g100);color:var(--g700)}
  .pvl.cad{box-shadow:inset 0 -2px 0 #00B589}.pvl.reu{box-shadow:inset 0 -2px 0 var(--brand-purple)}
  .pvl.site{background:#FFF4E5;box-shadow:inset 0 -2px 0 #B45309}.pvl.pend{background:var(--tint-peach);box-shadow:inset 0 -2px 0 var(--brand-orange)}
  mark.pv{background:transparent;color:inherit;font-weight:inherit;padding:0 1px;border-radius:3px}
  mark.pv.cad{box-shadow:inset 0 -2px 0 #00B589}
  mark.pv.reu{box-shadow:inset 0 -2px 0 var(--brand-purple)}
  mark.pv.site{background:#FFF4E5;box-shadow:inset 0 -2px 0 #B45309}
  mark.pv.pend{background:var(--tint-peach);box-shadow:inset 0 -2px 0 var(--brand-orange)}
  .pgf{border:var(--line);border-radius:16px;overflow:hidden;margin-top:14px;background:var(--white);box-shadow:var(--shadow-card);max-width:880px}
  .pgf-bar{display:flex;align-items:center;gap:6px;padding:9px 12px;background:var(--g100);border-bottom:var(--line)}
  .pgf-bar i{width:9px;height:9px;border-radius:50%;background:var(--g200)}
  .pgf-url{margin-left:8px;flex:1;min-width:0;background:var(--white);border-radius:var(--pill);padding:4px 12px;font-size:12px;color:var(--g700);font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pgf-body{padding:18px 24px 20px;font-size:14.4px;line-height:1.65;color:var(--ink)}
  .pgf-body h1{font-size:24px;font-weight:800;letter-spacing:-.03em;line-height:1.15;margin:4px 0 10px}
  .pgf-body h2{font-size:16px;font-weight:800;letter-spacing:-.02em;margin:16px 0 4px}
  .pgf-body ul{margin:4px 0 4px 20px}
  .pgf-body li{margin-top:3px}
  .pgf-crumb{font-size:11.5px;color:var(--g600);font-weight:600}
  .pg-cta{margin-top:14px;font-weight:700}
  .pg-btn{display:inline-flex;margin-top:10px;background:#25D366;color:#fff;font-weight:800;font-size:13.5px;border-radius:var(--pill);padding:10px 18px}
  .pgf-upd{margin-top:14px;font-size:11.5px;color:var(--g600);font-weight:600}
  .pgtbl td{font-size:12.6px;vertical-align:top}
  .pgtbl td:nth-child(3),.pgtbl td:nth-child(4){min-width:190px}
  .faqi{border:var(--line);border-radius:14px;padding:14px 16px;margin-top:10px;background:var(--white)}
  .faqi h4{font-size:15px;font-weight:800;letter-spacing:-.02em}
  .faq-a{font-size:13.8px;color:var(--ink);margin-top:6px;line-height:1.55}
  .faq-none{color:var(--g600);font-style:italic}
  .faq-m{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px;margin-top:8px}
  .tgs{display:inline-flex;flex-wrap:wrap;gap:4px}
  .tg{font-size:10px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;padding:2px 8px;border-radius:var(--pill);background:var(--tint-lav);color:#7B00BE}
  .faq-w{font-size:12.4px;color:var(--g600);font-weight:600;flex:1;min-width:220px}
  .faq-p{font-size:12.4px;margin-top:6px;background:var(--tint-peach);color:#7a3a16;border-radius:9px;padding:6px 10px}
  .citl{margin:12px 0 0 22px;display:flex;flex-direction:column;gap:7px}
  .cq{display:inline;background:var(--tint-mint);color:#0A4A36;font-weight:600;font-size:13.6px;line-height:1.55;padding:1px 4px;border-radius:5px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
  .codeb{font-size:11.6px;line-height:1.5;max-height:520px;overflow:auto}
  ul.chk{list-style:none;margin-top:10px;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}
  @media(max-width:760px){ul.chk{grid-template-columns:1fr}}
  ul.chk li{position:relative;padding-left:26px;font-size:13.4px;color:var(--g700);line-height:1.45}
  ul.chk li::before{content:"✓";position:absolute;left:0;top:0;width:18px;height:18px;border-radius:50%;background:var(--tint-mint);color:#06724F;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center}
'''
rep('  .cta-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}',
    CSS + '  .cta-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}')

# =====================================================================
# 8. JS — navegação genérica entre abas com menu lateral
# =====================================================================
rep('''  function goSec(id){
    var el = document.getElementById(id); if(!el) return false;
    show('cont', true);''',
    '''  function panelOf(el){ var p = el && el.closest('.panel'); return p ? p.id.replace('p-','') : null; }
  function goSec(id){
    var el = document.getElementById(id); if(!el) return false;
    show(panelOf(el) || 'cont', true);''')
rep('''  function copyPrompt(btn){
    var t = document.getElementById('prompt-text').textContent;
    function ok(){ btn.textContent = 'Copiado ✓'; setTimeout(function(){ btn.textContent = 'Copiar o prompt'; }, 2200); }''',
    '''  function copyPrompt(btn){ copyBlock(btn, 'prompt-text', 'Copiar o prompt'); }
  function copyBlock(btn, id, label){
    var t = document.getElementById(id).textContent;
    function ok(){ btn.textContent = 'Copiado ✓'; setTimeout(function(){ btn.textContent = label; }, 2200); }''')
rep('''  (function(){
    var links = [].slice.call(document.querySelectorAll('.cm-i'));
    var secs = [].slice.call(document.querySelectorAll('.csec'));
    if(!('IntersectionObserver' in window) || !secs.length) return;
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        var id = e.target.id;
        links.forEach(function(l){ l.classList.toggle('on', l.getAttribute('href') === '#' + id); });
        // no celular o menu é uma faixa horizontal: traz o chip ativo para a vista
        var on = document.querySelector('.cm-i.on'), menu = document.querySelector('.cont-menu');
        if(on && menu && getComputedStyle(menu).flexDirection === 'row'){ menu.scrollTo({left: Math.max(0, on.offsetLeft - 12), behavior:'smooth'}); }
      });
    }, {rootMargin:'-25% 0px -65% 0px', threshold:0});
    secs.forEach(function(x){ io.observe(x); });
  })();''',
    '''  (function(){
    if(!('IntersectionObserver' in window)) return;
    // um observador por aba com menu lateral (Solusite e Conteúdo)
    [].slice.call(document.querySelectorAll('.cont-layout')).forEach(function(lay){
      var menu = lay.querySelector('.cont-menu');
      var links = [].slice.call(lay.querySelectorAll('.cm-i'));
      var secs = [].slice.call(lay.querySelectorAll('.csec'));
      if(!secs.length) return;
      var io = new IntersectionObserver(function(es){
        es.forEach(function(e){
          if(!e.isIntersecting) return;
          var id = e.target.id;
          links.forEach(function(l){ l.classList.toggle('on', l.getAttribute('href') === '#' + id); });
          // no celular o menu é uma faixa horizontal: traz o chip ativo para a vista
          var on = menu && menu.querySelector('.cm-i.on');
          if(on && getComputedStyle(menu).flexDirection === 'row'){ menu.scrollTo({left: Math.max(0, on.offsetLeft - 12), behavior:'smooth'}); }
        });
      }, {rootMargin:'-25% 0px -65% 0px', threshold:0});
      secs.forEach(function(x){ io.observe(x); });
    });
  })();''')
rep('''  else if(h.indexOf('c-') === 0 && document.getElementById(h)){
    show('cont', true);''',
    '''  else if(h && document.getElementById(h) && document.getElementById(h).classList.contains('csec')){
    show(panelOf(document.getElementById(h)) || 'cont', true);''')

# cabeçalho e rodapé
rep(' · rev. 11/09/2026</p>', ' · rev. 29/09/2026</p>')
rep('regras em <code>docs/descricao-empresa-3-0.md</code> e <code>docs/editorias-conteudo.md</code>',
    'regras em <code>docs/descricao-empresa-3-0.md</code>, <code>docs/editorias-conteudo.md</code> e <code>docs/solusite-padrao.md</code>')

open(P, 'w', encoding='utf-8').write(s)
print('ok · palavras do conteúdo único:', NWORDS, '· páginas:', len(PAGES))
for p in PAGES: print(f"  {p['url']:28} title {len(p['title']):>2} · meta {len(p['meta']):>3}")
print('  meta Solutudo:', len(NEW_META_T))
