# -*- coding: utf-8 -*-
"""Fonte única da Execon: o texto, o FAQ, o catálogo, as páginas do site e as editorias.
Tudo que aparece na aba Destaque, no Solusite e no Conteúdo sai daqui. Transcrito dos arquivos
30-textos.md, 31-catalogo.md e 32-pauta.md do dossiê, escritos pelos agentes a partir do envelope."""
import re, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad')
import execon_rubric as R
from execon_rubric import PV
WA = '(11) 98454-5681'

# ------------------------------------------------------------------ o texto (30-textos.md §1)
# (frase, fonte, dica, ids do envelope)
DESC = {
 'h1': 'Execon Engenharia e Construção: construtora de casas de alto padrão em São Paulo (SP)',
 'abertura': [
  ('A Execon Engenharia e Construção é uma construtora de São Paulo (SP) com foco em casas de alto padrão.', 'cs',
   'Entidade primeiro: a marca, a categoria, a cidade e o foco pedido pela Solutudo, na forma travada pelo verificador. Sem "exclusivamente" e sem "referência".',
   'fact.name.001 · fact.category.001 · fact.city.001 · fact.positioning.001'),
  ('A Execon Engenharia e Construção faz a gestão e o acompanhamento de obras.', 'cad',
   'O segundo serviço da empresa, em três fontes que concordam: dois produtos, o banner e o site.', 'fact.service.002'),
 ],
 'blocos': [
  ('Construção de casas de alto padrão, gestão de obras e reformas',
   ('Os serviços da Execon Engenharia e Construção são:', 'cad', 'Introduz a lista, com o nome da empresa para a frase se sustentar sozinha.', '—'),
   [('construção de casas de alto padrão;', 'cs', 'O serviço principal, no topo da lista.', 'fact.service.001'),
    ('gestão e acompanhamento de obras;', 'cad', 'Produtos 547879 e 547870, agora numa linha só.', 'fact.service.002'),
    ('reforma residencial e comercial;', 'pub', 'A reforma comercial está no produto 547876; a residencial só aparece em quatro canais públicos (Facebook, dois sites e Bendito Guia).', 'fact.service.003'),
    ('construção e reforma de lojas, escritórios e restaurantes;', 'cad', 'Produto 547876. "Indústrias" ficou de fora: só um produto cita.', 'fact.service.004'),
    ('áreas de lazer residenciais;', 'cad', 'Produto 547881.', 'fact.service.005'),
    ('pergolados;', 'cad', 'Produto 547873.', 'fact.service.006'),
    ('instalações elétricas residenciais e comerciais e manutenção elétrica.', 'cad', 'Produto 547883, sem a promessa de "conformidade com NBR".', 'fact.service.007')], True),
  ('Área de lazer com piscina, área gourmet e pergolado',
   ('A Execon Engenharia e Construção faz áreas de lazer residenciais com:', 'cad', 'O que a casa de alto padrão pede, nomeado item a item.', 'fact.service.005'),
   [('piscina;', 'cad', 'Produto 547881.', 'fact.service.005'),
    ('churrasqueira e área gourmet;', 'cad', 'Produto 547881.', 'fact.service.005'),
    ('varanda;', 'cad', 'Produto 547881.', 'fact.service.005'),
    ('paisagismo;', 'cad', 'Produto 547881.', 'fact.service.005'),
    ('iluminação externa.', 'cad', 'Produto 547881.', 'fact.service.005')], True,
   [('A Execon Engenharia e Construção constrói pergolados de madeira, alumínio ou ferro, com cobertura de policarbonato ou vegetal.', 'cad', 'Materiais e coberturas do produto 547873: o fato concreto que sustenta a página do pergolado.', 'fact.service.006')]),
  ('Construtora na Grande São Paulo, no interior e no litoral paulista', None,
   [('A Execon Engenharia e Construção atende a capital e a Grande São Paulo, o interior e o litoral paulista.', 'pub',
     'Alcance, e não lista de cidades: o site diz "Grande São Paulo, litoral e interior", e os DDDs 13 e 14 do cadastro batem. O CS confirma a lista.', 'fact.service_area.001'),
    ('A Execon Engenharia e Construção atende obras em condomínios do interior paulista, como Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII.', 'pub',
     'Forma segura travada pelo verificador: sem o nome da loteadora, sem "parceira" e sem número de casas. Veio da outra página da empresa na Solutudo, com o mesmo telefone.', 'fact.service_area.002'),
    ('A Execon Engenharia e Construção está em expansão para os Estados Unidos.', 'pend',
     'O pedido da Solutudo, na única forma que o envelope permite: uma frase, fora da abertura, do title e da meta. Sobe de nível com estado, empresa e licença. Reverificar até 31/12/2026.', 'fact.expansion.001')], False),
  ('Como pedir orçamento à Execon Engenharia e Construção', None, [], False),
 ],
 'cta': ('Para pedir orçamento, fale com a Execon Engenharia e Construção pelo WhatsApp (11) 98454-5681. Na mensagem, informe a cidade ou o condomínio da obra e o tipo de serviço.', 'cad',
         'Fecha em ação, com o canal por extenso e o que informar. Na Solutudo é texto; no site, botão com link.', 'fact.phone.001 · fact.channel.001'),
 'cta_extra': ('A Execon Engenharia e Construção também atende pelo WhatsApp (13) 98191-2794 e pelo e-mail contato@execoneng.com.br.', 'cad',
               'O segundo WhatsApp e o e-mail do cadastro. O (14) fica no bloco de contato: não se sabe se tem WhatsApp.', 'fact.phone.002 · fact.email.001'),
}
def desc_sents():
    out = list(DESC['abertura'])
    for b in DESC['blocos']:
        _, intro, items, _ = b[:4]
        if intro: out.append(intro)
        out += items
        if len(b) > 4: out += b[4]
    out.append(DESC['cta']); out.append(DESC['cta_extra'])
    return out
def desc_heads(): return [DESC['h1']] + [b[0] for b in DESC['blocos']]
NW = sum(len(t.split()) for t, *_ in desc_sents())
PV_USED = ['cad', 'cs', 'pub', 'pend']

SELO = ('variante B · sem confirmação da empresa',
        'Resumo elaborado pela Solutudo a partir do cadastro e de informações públicas, sem confirmação da empresa (30/09/2026). Endereço de atendimento, horário e tempo de atuação aguardam confirmação. Confirme preços e condições com a empresa. É o responsável? Confirme ou corrija.')
SOL_TITLE = 'Execon Engenharia e Construção: casas de alto padrão em SP'
SOL_META = 'A Execon Engenharia e Construção é uma construtora de São Paulo (SP) com foco em casas de alto padrão. Faz gestão de obras, reformas e obras comerciais.'
NAO_FAZ = ('Não escreve "há mais de 9 anos": o número foi escrito em 2022, envelheceu, e três canais dão três números. '
           'Não cita a Avenida Paulista nem bairro: são três endereços, dois em prédios de escritório compartilhado. '
           'Não diz "projetos arquitetônicos" nem "equipe de engenheiros": sem CAU e sem o registro do CREA conferido, a regra do setor regulado barra. '
           'E não coloca os Estados Unidos no título nem na primeira frase: a única fonte é a própria Solutudo, e o verificador travou uma frase só. '
           '<b>Selo B, e não A</b>: nada deste texto foi confirmado pela empresa. Com a aprovação escrita do cliente, as duas vitrines passam para o selo A, e essa aprovação também libera a frase dos EUA.')

def score_desc():
    return R.score(DESC['abertura'][0][0], desc_sents(), desc_heads(), True, DESC['cta'][0], 'desc', WA, R.UNIQ)

# ------------------------------------------------------------------ FAQ comum (30-textos.md §4)
FAQ = [
 dict(k='F1', q='A Execon Engenharia e Construção atende em condomínio fechado?', pv='pub',
      a='Sim: a Execon Engenharia e Construção atende obras em condomínios do interior paulista, como Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII.',
      tags=['Local', 'SEO', 'AEO', 'Conversão', 'Voz'], why='Quem vai construir em loteamento de lazer procura a construtora pelo nome do condomínio.',
      pend='se a Execon cuida da aprovação do projeto no condomínio, e a lista completa de condomínios'),
 dict(k='F2', q='A Execon Engenharia e Construção atende no interior e no litoral de São Paulo?', pv='pub',
      a='Sim: a Execon Engenharia e Construção atende a capital e a Grande São Paulo, o interior e o litoral paulista.',
      tags=['Local', 'SEO', 'Voz', 'AEO'], why='Quem tem casa de campo ou de praia pergunta se uma construtora da capital vai até a obra.',
      pend='a lista de cidades, confirmada com o cliente'),
 dict(k='F3', q='A Execon Engenharia e Construção faz área de lazer com piscina e pergolado?', pv='cad',
      a='Sim: a Execon Engenharia e Construção faz áreas de lazer residenciais com piscina, churrasqueira, área gourmet, varanda, paisagismo e iluminação externa. A Execon Engenharia e Construção também constrói pergolados de madeira, alumínio ou ferro, com cobertura de policarbonato ou vegetal.',
      tags=['SEO', 'AEO', 'Conversão'], why='Área de lazer em casa de condomínio é tema forte do nicho e corresponde a dois produtos do cadastro.'),
 dict(k='F4', q='Quanto custa construir uma casa de alto padrão com a Execon Engenharia e Construção?', pv='cad',
      a='O preço de uma casa de alto padrão com a Execon Engenharia e Construção não está publicado nesta página: o valor é pedido em orçamento. Para o orçamento, fale com a Execon Engenharia e Construção pelo WhatsApp (11) 98454-5681 e informe a cidade ou o condomínio da obra e o tipo de serviço.',
      tags=['SEO', 'Voz', 'AEO', 'Conversão'], why='É a pergunta dominante do nicho em 2026. Responder sem número evita preço inventado e leva ao orçamento.',
      pend='faixa de preço e o que ela inclui, se o cliente quiser publicar'),
 dict(k='F5', q='Como pedir orçamento à Execon Engenharia e Construção?', pv='cad',
      a='Para pedir orçamento à Execon Engenharia e Construção, envie mensagem pelo WhatsApp (11) 98454-5681. A Execon Engenharia e Construção também atende pelo WhatsApp (13) 98191-2794, pelo telefone (14) 99120-9697 e pelo e-mail contato@execoneng.com.br. Na mensagem, informe a cidade ou o condomínio da obra e o tipo de serviço.',
      tags=['Conversão', 'Voz', 'AEO', 'Local'], why='É o próximo passo de quem leu. Canal por extenso é citável por voz e por IA.',
      pend='se há visita técnica, o prazo de resposta e o horário do WhatsApp'),
 dict(k='F6', q='A Execon Engenharia e Construção constrói nos Estados Unidos?', pv='pend',
      a=None,
      tags=['IA', 'Confiança', 'AEO'], why='A pergunta é provável, e a resposta publicada repetiria a frase travada, que o verificador permite uma vez só, no texto da empresa. Ela volta quando o cliente confirmar estado, empresa e licença.',
      pend='a pré-condição 4: estado e cidade, empresa americana, licença estadual de construtor e tipo de serviço. Até lá, a frase "está em expansão para os Estados Unidos" aparece só no texto da empresa'),
 dict(k='F7', q='A Execon Engenharia e Construção é registrada no CREA-SP?', pv='pend', a=None,
      tags=['Confiança', 'IA', 'AEO'], why='Registro no CREA e no CAU é o primeiro critério de quem escolhe construtora para construir em condomínio.',
      pend='a consulta pública do CREA-SP 5070683298 (profissional ou empresa, ativo, título) e a certidão de registro da empresa. Quando chegar, a resposta é "tem responsável técnico registrado no CREA-SP", sem nome'),
 dict(k='F8', q='A Execon Engenharia e Construção trabalha por administração de obra ou por preço fechado?', pv='pend', a=None,
      tags=['Conversão', 'SEO', 'AEO'], why='Decide a escolha de quem compara construtoras de alto padrão.',
      pend='a forma de contratação: administração, com preço de custo mais taxa, ou empreitada com preço fechado'),
]
FAQD = {f['k']: f for f in FAQ}
FAQ_HEAD = '8 perguntas: 5 respondidas e 3 que esperam o cliente — as mesmas do site'
FAQ_GAPS = [
 ('Há quanto tempo a Execon atua?', 'o ano de início, e se conta a trajetória do responsável técnico — cliente'),
 ('A Execon mostra obras concluídas?', 'lista de obras com condomínio, ano e foto, com autorização — cliente'),
 ('Como acompanho a obra se não moro na cidade?', 'como funcionam os relatórios: frequência, formato e canal — cliente'),
 ('A Execon dá garantia da obra?', 'a política de garantia — cliente'),
]

# ------------------------------------------------------------------ catálogo: 1 item = 1 página (31-catalogo.md, dados de gen_catalogo.py)
_src = open('/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/gen_catalogo.py', encoding='utf-8').read()
_ns = {}; exec(_src[:_src.find('\nBANNED = ')], _ns)
_RAW = {it['key']: it for it in _ns['items']}
def _pv(ids):
    ids = ' '.join(ids)
    if 'expansion' in ids: return 'pend'
    if 'service_area' in ids: return 'pub'
    if 'positioning' in ids: return 'cs'
    return 'cad'
ORDER = ['p547877', 'p547879', 's-condominios-interior', 's-reforma', 'p547881', 'p547873', 'p547876', 'p547883', 'p547874', 'p547871', 's-eua', 'p547870']
TAGLINE = {'s-condominios-interior': 'fato próprio, nenhum item', 's-reforma': '4 canais, nenhum item', 'p547874': 'espera o CAU', 'p547871': 'espera o CREA',
           's-eua': 'espera a confirmação', 'p547870': 'fundir no 547879'}
PREV_SUG = {'s-condominios-interior': 'Não existe no catálogo. O fato vem da outra página da empresa na Solutudo, com o mesmo telefone.',
            's-reforma': 'Não existe no catálogo. A reforma aparece no Facebook, nos dois sites e dentro do produto comercial.',
            's-eua': 'Não existe no catálogo. A única menção é o banner do Solusite, de 28/09.'}
_NOWI = {('p' + it['id']): it for it in R.parse_items('/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/dossie-grupo-execon/02-textos-atuais.md')}
CATALOG = []
for k in ORDER:
    r = _RAW[k]
    c = dict(key=k, kind=r['kind'], card=r['card'], url=r['url'].split(' ')[0], nota_atual=r.get('nota_atual', ''),
             idl=('ID ' + k[1:]) if k.startswith('p') else '', tagline=TAGLINE.get(k, ''))
    if k in _NOWI:
        t0 = _NOWI[k]['sents'][0][0]
        c['prev'] = (t0[:118] + '…') if len(t0) > 120 else t0
    else:
        c['prev_sug'] = PREV_SUG.get(k, '')
    if r['kind'] in ('cad', 'pronto'):
        c.update(h1=r['h1'], title=r['title'], meta=r['meta'],
                 intro=[(r['intro'][0], _pv(r['intro'][1]))],
                 bullets=[(t, _pv(ids)) for t, ids in r['bullets']],
                 serve=re.escape(r['serve']), cta=(r['cta'][0], _pv(r['cta'][1])),
                 faq=[(q, a, _pv(ids)) for q, a, ids in r['faq']], pend=r.get('pend', ''), links=r.get('links', ''))
    elif r['kind'] == 'cond':
        c.update(reservado=True, h1=r.get('h1', 'Página reservada'), title=r.get('title', ''), meta=r.get('meta') or '',
                 cond=r['cond'], pend=r.get('pend', ''), enquanto=r.get('enquanto', ''), ja_pode=r.get('ja_pode', ''), perguntas=r.get('perguntas', ''))
    else:
        c.update(into='547879', fundir_why=r['motivo'], volta_se=r['volta_se'])
    CATALOG.append(c)
CATD = {c['key']: c for c in CATALOG}
# depois do R2, a página da casa diz "executa obras", e não mais "desenvolve projetos": a nota da ficha reservada acompanha
CATD['p547874']['enquanto'] = ('Tirar o item 547874 do ar nas duas vitrines agora: ele afirma arquitetura sem CAU. A categoria "Arquitetura" fica em revisão. '
                               'Reescrevê-lo no nível "projetos e execução de obras" criaria uma segunda página para a busca da casa de alto padrão, e a auditoria tirou essa expressão até da lista de serviços.')
# supervisão: reforma residencial só tem fonte pública (fact.service.003; o produto 547876 é comercial)
CATD['s-reforma']['intro'] = [(t, 'pub') for t, _ in CATD['s-reforma']['intro']]
CATD['s-reforma']['faq'] = [(q, a, 'pub') for q, a, _ in CATD['s-reforma']['faq']]

# retrabalho pedido pelo auditor (40-auditoria.md), aplicado literalmente e registrado em 35-retrabalho.md
for _c in CATALOG:
    if 'cta' in _c:   # ressalva 5: o CTA vira duas frases
        _c['cta'] = (_c['cta'][0].replace(' 98454-5681 e informe ', ' 98454-5681. Informe '), _c['cta'][1])
CATD['p547877']['intro'] = [('A Execon Engenharia e Construção é uma construtora de São Paulo (SP) que executa obras para quem quer construir uma casa de alto padrão.', 'cs')]  # R2
CATD['p547877']['meta'] = 'A Execon Engenharia e Construção constrói casas de alto padrão e faz a gestão da obra na capital, na Grande SP, no interior e no litoral paulista.'  # R2
_sc = CATD['s-condominios-interior']   # R3: só a forma segura travada
_sc['bullets'] = [b for b in _sc['bullets'] if 'Ninho Verde I,' not in b[0]]
_sc['faq'] = [(q, ('A Execon Engenharia e Construção atende obras em condomínios do interior paulista, como Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII.' if 'Em quais condomínios' in q else a), pv) for q, a, pv in _sc['faq']]
_sc['h1'] = 'Obras em condomínios do interior de SP: Ninho Verde II e Riviera de Santa Cristina XIII'
_sc['title'] = 'Obras no Ninho Verde II e na Riviera de Santa Cristina XIII'
CATD['p547879']['bullets'] = [b for b in CATD['p547879']['bullets'] if 'administração de obras' not in b[0]]   # ressalva 3
# R9: a pergunta que cada página responde
QPAGE = {'p547877': 'Quem constrói casa de alto padrão em São Paulo e no interior?',
         'p547879': 'Quem faz o gerenciamento da obra da minha casa em São Paulo?',
         's-condominios-interior': 'Que construtora atende obra no Ninho Verde II ou na Riviera de Santa Cristina XIII?',
         's-reforma': 'Quem faz reforma de casa em São Paulo?',
         'p547881': 'Quem constrói área de lazer com piscina e área gourmet em São Paulo?',
         'p547873': 'Quem faz pergolado de madeira, alumínio ou ferro em São Paulo?',
         'p547876': 'Quem constrói e reforma loja, escritório ou restaurante em São Paulo?',
         'p547883': 'Quem faz instalação e manutenção elétrica em São Paulo?'}
for _k, _q in QPAGE.items(): CATD[_k]['q'] = _q
JSONLD_ITEM = 'WebPage (dateModified) + Service, com provider = o nó GeneralContractor e areaServed = capital, Grande SP, interior e litoral paulista + BreadcrumbList · sem FAQPage (só na página de perguntas) · sem aggregateRating'
def item_sents(c): return list(c['intro']) + list(c['bullets']) + [c['cta']]
def item_faq(c): return c.get('faq', [])
def scorable(c): return c['kind'] in ('cad', 'pronto')
def score_item(c):
    return R.score(c['intro'][0][0], item_sents(c), [c['h1']], True, c['cta'][0], 'item', WA, R.UNIQ, item_faq(c), c['serve'])
def now_items():
    out, det = {}, {}
    for k, it in _NOWI.items():
        s = it['sents']
        t, d = R.score(s[0][0], s, [it['title']], True, it['cta'], 'item', R.NOW_WA, R.UNIQ, (), SERVE_NOW[k])
        from collections import Counter
        cn = Counter(pv for _, pv, _ in s)
        mix = ' · '.join(f'{n} {R.PV[pv][0]}' for pv, n in cn.most_common())
        out[k] = t; det[k] = dict(title=it['title'], dims=d, mix=mix, trad=it['trad'])
    return out, det
SERVE_NOW = {'p547870': r'fiscaliza|acompanh', 'p547871': r'residencia|comercia|industria', 'p547873': r'jardi|lazer|terra', 'p547876': r'lojas|escrit',
             'p547877': r'resid|casa', 'p547879': r'prazo|obra', 'p547881': r'resid|condom', 'p547883': r'resid|comerc', 'p547874': r'resid|escrit'}
N_PUB = sum(1 for c in CATALOG if scorable(c))
CAT_HEAD = f'12 fichas: {N_PUB} páginas publicáveis, 3 reservadas até o cliente confirmar e 1 que sai do catálogo'
CAT_SUB = ('Os nove produtos de hoje viram <b>seis páginas</b>: o "Construtora Especializada" vira a página do produto principal, a casa de alto padrão; '
           'o acompanhamento de obra é fundido no gerenciamento, porque os dois disputam a mesma busca; e o projeto arquitetônico e o projeto estrutural '
           '<b>saem do ar</b> até o registro no CAU e no CREA ser conferido. Entram <b>dois itens novos</b> que o envelope sustenta e o catálogo não tinha: '
           'obras em condomínios do interior e reforma de casa. A página dos Estados Unidos fica reservada.')
CAT_NOTE = ('<b>Por que reservar em vez de reescrever:</b> o projeto arquitetônico e o projeto estrutural não têm texto seguro hoje. O máximo seria "projetos e execução de obras", e a auditoria tirou '
            'até isso da lista de serviços, porque o leitor entende projeto arquitetônico. Reescrevê-los nesse nível criaria uma segunda e uma terceira página disputando a busca da casa de alto padrão. '
            'Com o CAU e o CREA confirmados, os dois voltam com fatos novos. <b>A ordem segue a jornada</b> de quem constrói uma casa de alto padrão: construir, gerenciar, '
            'onde, reformar, completar a área externa; depois o público comercial e o serviço de apoio.')
ENUM_NOTE = ('A lista de serviços é a mesma na descrição, nas metas e no catálogo: construção de casas de alto padrão · gestão e acompanhamento de obras · '
             'reforma residencial e comercial · obras comerciais (lojas, escritórios e restaurantes) · áreas de lazer residenciais · pergolados · instalações '
             'e manutenção elétrica. Nenhum canal lista "projetos arquitetônicos", "projeto estrutural", "licenciamento", "hidráulica" ou "automação".')

# ------------------------------------------------------------------ Solusite: páginas de entrada
def pg(**k): return k
HUB = [
 pg(menu='Início', url='/', h1='Execon Engenharia e Construção: casas de alto padrão, gestão de obras e reformas',
    title='Execon Engenharia e Construção: construtora em São Paulo, SP',
    meta='A Execon Engenharia e Construção constrói casas de alto padrão e faz gestão de obras e reformas na Grande SP, no interior e no litoral paulista.',
    q='construtora de casas de alto padrão em São Paulo', st='ok', stl='pronta', ld='WebSite + WebPage + GeneralContractor + BreadcrumbList'),
 pg(menu='A Execon', url='/sobre', h1=DESC['h1'], title='Quem é a Execon Engenharia e Construção, construtora de SP',
    meta='Construtora de São Paulo (SP) com foco em casas de alto padrão. Faz gestão de obras e reformas e atende a Grande SP, o interior e o litoral paulista.',
    q='quem é a Execon Engenharia e Construção?', st='ok', stl='pronta · o texto da empresa', ld='WebPage (about = GeneralContractor) + BreadcrumbList'),
 pg(menu='Construção e reforma', url='/construcao-e-reforma', h1='Construção, gestão de obras e reforma com a Execon Engenharia e Construção',
    title='Construção, gestão de obras e reforma em SP | Execon',
    meta='Construção de casas de alto padrão, gestão de obras, reforma, obras comerciais, área de lazer, pergolado e instalações elétricas em São Paulo (SP).',
    q='o que a Execon faz?', st='ok', stl='pronta · leva às 8 páginas', ld='WebPage + ItemList das 8 páginas + BreadcrumbList'),
 pg(menu='Capital, interior e litoral', url='/onde-a-execon-atende', h1='Onde a Execon Engenharia e Construção atende: capital, Grande SP, interior e litoral paulista',
    title='Onde a Execon atende: Grande SP, interior e litoral paulista',
    meta='A Execon Engenharia e Construção atende a capital, a Grande São Paulo, o interior e o litoral paulista, inclusive obras em condomínios do interior.',
    q='a Execon atende no interior e no litoral?', st='ok', stl='pronta · uma página com todo o alcance', ld='WebPage + GeneralContractor com areaServed + BreadcrumbList'),
 pg(menu='Dúvidas sobre obra', url='/perguntas-sobre-construcao-de-casa', h1='Perguntas sobre obra com a Execon: condomínio, região, área de lazer e orçamento',
    title='Perguntas sobre a Execon: condomínio, região e orçamento',
    meta='A Execon Engenharia e Construção responde se atende em condomínio, no interior e no litoral de SP, se faz área de lazer e como pedir orçamento.',
    q='dúvidas antes de contratar construtora de alto padrão', st='ok', stl='pronta · 5 de 8 respondidas', ld='WebPage + FAQPage (só as 5 respondidas) + BreadcrumbList'),
 pg(menu='Pedir orçamento', url='/pedir-orcamento', h1='Como pedir orçamento à Execon Engenharia e Construção',
    title='Como pedir orçamento à Execon Engenharia e Construção',
    meta='Orçamento da Execon Engenharia e Construção pelo WhatsApp (11) 98454-5681: informe a cidade ou o condomínio e o tipo de obra. Ou (13) 98191-2794.',
    q='como pedir orçamento de obra à Execon?', st='pa', stl='parcial · falta o processo', ld='WebPage + ContactPoint do GeneralContractor + BreadcrumbList'),
 pg(menu='fora do menu até existir', url='/obras', h1='Obras da Execon Engenharia e Construção, por condomínio e cidade',
    title='Obras da Execon Engenharia e Construção por condomínio',
    meta='As obras da Execon Engenharia e Construção com o condomínio ou a cidade, o tipo de obra e o ano, em fotos com legenda, publicadas com autorização.',
    q='a Execon mostra obras feitas?', st='no', stl='espera legendas e autorização', ld='WebPage + ImageGallery com legenda por obra + BreadcrumbList'),
 pg(menu='Como construir · quando existir', url='/guia', h1='Guia da Execon para construir casa de alto padrão em São Paulo e em condomínio',
    title='Guia para construir casa de alto padrão em SP · Execon',
    meta='Guia da Execon Engenharia e Construção para quem vai construir casa de alto padrão em SP: construir em condomínio, reformar e fazer área de lazer.',
    q='como construir casa de alto padrão em condomínio?', st='pa', stl='a produzir', ld='WebPage + Article em cada post + BreadcrumbList'),
 pg(menu='English · quando existir', url='/en', h1='Execon Engenharia e Construção: high-end home builder in São Paulo, Brazil',
    title='Execon · High-end home builder in São Paulo, Brazil',
    meta='Execon Engenharia e Construção builds high-end homes and manages construction projects in São Paulo, Brazil: the capital, the countryside and the coast.',
    q='Brazilian home builder expanding to the United States', st='no', stl='reservada · pré-condição 4 inteira', ld='WebPage (inLanguage en-US) + GeneralContractor + hreflang'),
]
BANNER_NEW = ('Frase: <i>"Construção de casas de alto padrão, com gestão da obra"</i> · apoio: <i>"Execon Engenharia e Construção · capital, Grande SP, interior e litoral paulista"</i> · '
              'botões <i>"Pedir orçamento no WhatsApp"</i> e <i>"Ver o que a Execon faz"</i>. A frase dos EUA sai do banner até a pré-condição 4.')
LACUNAS = [
 ('Ano de início da atuação', 'sem ele, nada de "desde" no texto e nenhum marco no calendário', 'cliente'),
 ('Obras com data e método', 'a unicidade fica baixa e a página de casas entregues não sai', 'cliente'),
 ('Endereço e atendimento presencial', 'endereço fora do texto e do JSON-LD', 'cliente'),
 ('Registro no CREA-SP e no CAU', 'duas páginas reservadas e uma pergunta sem resposta', 'cliente + nós'),
 ('Como o cliente acompanha a obra', 'o critério de AEO que falta à nota', 'cliente'),
 ('Horário do WhatsApp', 'o ponto que falta no contato', 'cliente'),
 ('EUA: estado, empresa e licença', 'frase travada e página em inglês reservada', 'cliente'),
 ('Forma de contratação e garantia', 'duas perguntas do FAQ sem resposta', 'cliente'),
 ('Site oficial entre três domínios', 'canonical e redirecionamentos', 'cliente'),
 ('Página duplicada 23064979', 'o gate de publicação falha até resolver', 'Solutudo'),
]
CLAIMS = [
 ('"Mais de 9 anos de experiência"', 'escrito em 2022, e em conflito com 10 e 12 anos em outros canais'),
 ('"70 residências" e "20.000 m²"', 'três canais, três números diferentes'),
 ('"Localizada na vibrante Avenida Paulista"', 'três endereços, dois em prédio de escritório compartilhado'),
 ('"Construtora de excelência", "referência", "escolha ideal"', 'superlativo sem prova'),
 ('"Entrega no prazo e dentro do orçamento", "conformidade com NBR"', 'promessa de resultado em setor regulado'),
 ('"Projetos arquitetônicos", "equipe de arquitetos e engenheiros"', 'sem CAU e sem registro conferido'),
 ('"Tecnologia de ponta", "acompanhamento em tempo real"', 'nenhuma ferramenta identificada'),
 ('"Soluções sustentáveis", energia solar, água da chuva', 'alegação ambiental sem evidência'),
 ('"Parceira da Momentum"', 'da outra página; sem vínculo comprovado com a loteadora'),
 ('"Atua nos Estados Unidos"', 'sem amarra pública; o texto diz "em expansão"'),
]
CIT = ['A Execon Engenharia e Construção é uma construtora de São Paulo (SP) com foco em casas de alto padrão.',
       'A Execon Engenharia e Construção faz a gestão e o acompanhamento de obras.',
       'A Execon Engenharia e Construção atende a capital e a Grande São Paulo, o interior e o litoral paulista.',
       'A Execon Engenharia e Construção atende obras em condomínios do interior paulista, como Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII.',
       'A Execon Engenharia e Construção faz áreas de lazer residenciais com piscina, churrasqueira, área gourmet, varanda, paisagismo e iluminação externa.',
       'A Execon Engenharia e Construção constrói pergolados de madeira, alumínio ou ferro, com cobertura de policarbonato ou vegetal.',
       'A Execon Engenharia e Construção faz reforma residencial e comercial.',
       'O orçamento da Execon Engenharia e Construção é pedido pelo WhatsApp (11) 98454-5681.']
REVIEW = ('Setor regulado: nenhuma frase pode sugerir registro ou projeto arquitetônico até a conferência. A frase dos Estados Unidos depende da confirmação escrita do cliente. '
          'A área atendida e os condomínios vieram de fonte pública lida por trecho. E a página duplicada na Solutudo reprova o gate de publicação até ser resolvida.')
BLOCOS = [
 ('Banner, desktop e mobile', BANNER_NEW, 'pa', 'só no site · ajustar', 'O banner de 28/09 é o melhor texto do cadastro. Só perde a frase dos EUA até a confirmação.'),
 ('Ícones', '<b>Casas de alto padrão</b> · <b>Gestão e acompanhamento da obra</b> · <b>Reforma e área de lazer</b> · <b>Capital, interior e litoral de SP</b>', 'ok', 'só no site', 'Quatro fatos do envelope. "Responsável técnico com CREA" entra quando for conferido.'),
 ('A Execon', 'O texto 3.0 inteiro em <code>/sobre</code>, com resumo de duas frases na home', 'ok', 'replica o Destaque', 'Idêntico aos detalhes da empresa.'),
 ('Construção e reforma', 'Um cartão por página publicável, cada um levando à sua página', 'ok', 'replica o Destaque', 'As oito páginas da seção 3.'),
 ('Condomínios do interior', 'Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII, com link para a página', 'ok', 'replica o Destaque', 'O fato mais próprio da Execon.'),
 ('Casas entregues', 'Galeria com legenda por obra: serviço, condomínio ou bairro, ano', 'no', 'só no site · falta legenda', '63 fotos sem legenda útil. Sem ela, não há portfólio.'),
 ('Perguntas', 'As três primeiras do FAQ na home; as oito na página de perguntas; as de cada página nas páginas', 'ok', 'replica o Destaque + só no site', ''),
 ('Expansão para os Estados Unidos', 'Fora da home até a pré-condição 4. A frase aparece uma vez só no site, no texto da empresa', 'no', 'só no site · depois da PC4', 'Um bloco na home seria a segunda ocorrência da frase travada, e o verificador permite uma.'),
 ('Depoimentos', 'Nome e condomínio ou cidade, com autorização', 'no', 'só no site · nenhum no cadastro', 'Compra de alto padrão é por indicação.'),
 ('Avaliações', 'Só as nativas desta página', 'pa', 'replica o Destaque', 'A nota 5,0 que aparece na busca é da outra página, e não entra.'),
 ('Como pedir orçamento', 'WhatsApp (11) e (13), telefone (14), e-mail, área atendida e "Atualizado em"', 'pa', 'replica o Destaque', 'Horário e endereço entram quando o cliente confirmar.'),
 ('Pagamento', 'Pix, dinheiro e cartões', 'pa', 'replica o Destaque · pouco útil', 'Verdadeiro, mas não decide uma obra.'),
]
EUA_SENT = ('A Execon Engenharia e Construção está em expansão para os Estados Unidos.', 'pend', 'Frase travada pelo verificador. Sobe de nível com a pré-condição 4. Reverificar até 31/12/2026.')
PC4 = ['confirmação escrita do cliente para a frase', 'estado e cidade', 'empresa americana (LLC ou Inc.) registrada na Secretaria de Estado',
       'licença estadual de construtor, com estado, classe e número conferível', 'tipo de serviço: obra própria, gestão para brasileiros ou parceria com construtor local',
       'desde quando', 'obra concluída ou em andamento', 'seguros exigidos, se executar a obra']
EN_PAGE = dict(url='/en', h1=HUB[-1]['h1'], title=HUB[-1]['title'],
               why=('Quem busca em inglês, americano ou brasileiro que já mora lá, encontra a página em inglês, e não a em português. Ela traduz os mesmos fatos, sem '
                    'acrescentar nenhum. Uma página em inglês fala com o público dos EUA, então ela só sobe com a pré-condição 4 inteira, e não só com a confirmação escrita.'),
               blocks=['O texto da empresa em inglês, com os mesmos fatos, e a frase "Execon is expanding to the United States."',
                       'Os mesmos sete serviços, em inglês',
                       'O WhatsApp com o código do país: +55 11 98454-5681',
                       'Com a licença: o estado, o número e o link de conferência no órgão estadual',
                       'hreflang en-US e pt-BR, com x-default para a home em português'])
ALEM = [
 ('Casas entregues, com ficha', 'Uma página com as obras: condomínio ou bairro, tipo de obra, ano e fotos com legenda.', 'Quem contrata alto padrão confere obra entregue antes de chamar. É a prova que o texto não pode dar hoje, porque os números estão em conflito.', 'legendas das 63 fotos e autorização', 'cliente', 'ok', 'alta'),
 ('Pedido de orçamento guiado', 'Um formulário curto (tipo de obra, cidade ou condomínio, terreno, se já tem projeto) que abre o WhatsApp com a mensagem pronta.', 'São os dados que o CTA já pede. Encurta a conversa, e cada pedido passa a ser contado.', 'nada além do WhatsApp', 'nós', 'ok', 'alta'),
 ('Registro profissional com prova', 'O responsável técnico com o CREA-SP e, se houver, o arquiteto com CAU, com link para a consulta pública.', 'Em setor regulado, registro conferível vale mais que qualquer adjetivo. E destrava as duas páginas reservadas.', 'a conferência do CREA e do CAU', 'cliente + nós', 'pa', 'alta'),
 ('Página em inglês', 'A versão en-US com os mesmos fatos e hreflang.', 'É por onde a expansão para os EUA aparece para quem busca em inglês.', 'confirmação escrita e a pré-condição 4', 'cliente', 'pa', 'alta quando confirmar'),
 ('Link de WhatsApp rastreável', 'Um link diferente por origem: site, página Solutudo e perfil do Google.', 'Transforma contato em número, que é a evidência que o cliente aceita na renovação.', 'configuração', 'nós', 'ok', 'alta'),
 ('Um domínio só', 'Os três domínios da empresa e o Solusite apontando para um endereço oficial, com redirecionamento 301.', 'Quatro endereços com o mesmo conteúdo dividem a busca e confundem a IA sobre qual é a empresa.', 'decisão do cliente', 'cliente', 'ok', 'alta'),
 ('Guia de construção em condomínio', 'O blog das editorias, começando pelas perguntas de quem constrói em condomínio de lazer.', 'Captura as buscas de cauda longa, e cada post leva à página certa.', 'produção dos textos', 'nós', 'ok', 'média'),
 ('Diário de obra do cliente', 'Uma área com os relatórios da obra, se a Execon já produz relatórios periódicos.', 'Responde "como acompanho a obra se não moro na cidade", a pergunta de quem constrói casa de campo.', 'saber como são os relatórios', 'cliente', 'pa', 'média'),
 ('Depoimentos com nome', 'Clientes com nome e condomínio, com autorização.', 'Compra de alto padrão é por indicação.', 'autorização', 'cliente', 'pa', 'média'),
 ('Página por condomínio', 'Uma página para cada condomínio atendido.', 'Só com fato próprio: obra entregue ali, com foto e ano. Sem isso, seria página que só troca o nome.', 'lista de obras por condomínio', 'cliente', 'no', 'depois'),
]
KNOWS = ['construção de casas de alto padrão', 'gestão de obras', 'acompanhamento de obras', 'reforma residencial', 'obras comerciais', 'área de lazer', 'pergolado', 'instalações elétricas']
GATE = [
 ('Página duplicada na Solutudo', 'A página 23064979 tem os mesmos telefones e o mesmo e-mail. Consolidar com redirecionamento, ou alinhar o texto e tirar "CREA-SP nº" do título.', 'Solutudo', 'no', 'bloqueia tudo'),
 ('Qual domínio', 'Três domínios da empresa, e o Solusite seria o quarto. Um oficial, os outros redirecionando.', 'cliente + produto', 'no', 'bloqueia tudo'),
 ('O cadastro antes do site', 'A descrição e os produtos novos entram no cadastro antes de o Solusite ir ao ar. Ao contrário, o site nasce com o texto de 2022 e com os erros de tradução.', 'Solutudo', 'no', 'bloqueia tudo'),
 ('Aprovação escrita do cliente', 'Aprova o texto, passa o selo para A e libera a frase dos EUA.', 'cliente', 'pa', 'ajusta selo e EUA'),
 ('CREA e CAU', 'Consulta pública do CREA-SP 5070683298 e registro no CAU, se houver arquiteto.', 'cliente + nós', 'pa', 'limita 2 páginas'),
 ('Endereço e atendimento presencial', 'Se houver, o endereço entra com bairro Bela Vista; se não, fica a área atendida.', 'cliente', 'pa', 'ajusta contato e JSON-LD'),
 ('Horário do WhatsApp', 'O cadastro diz 8h às 20h todos os dias; os diretórios, outra coisa.', 'cliente', 'pa', 'ajusta o contato'),
 ('Legendas das fotos', 'Serviço, condomínio ou bairro e ano de cada obra.', 'cliente', 'pa', 'limita o portfólio'),
 ('Atributo Solusite', 'Está false no cadastro, com o site em montagem.', 'Solutudo', 'pa', 'acertar ao publicar'),
 ('Robôs de IA na CDN', 'Conferir se a hospedagem bloqueia robôs de IA por padrão.', 'técnico', 'pa', 'antes de publicar'),
 ('Velocidade, antes e depois', 'Medir o Solusite com os mesmos critérios desde o primeiro dia.', 'nós', 'ok', 'recomendado'),
]

# ------------------------------------------------------------------ fases 3 a 5 e aba Conteúdo
from execon_review import AGENTES_EXTRA, VERDICT_HTML, AUDIT_HTML
from execon_pauta import *
