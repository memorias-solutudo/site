# -*- coding: utf-8 -*-
"""Rubrica da Descrição 3.0 aplicada à Execon, com critérios explícitos, e o texto publicado hoje
marcado frase a frase. Mesma régua da LAAE (seis dimensões, 100 pontos), com os critérios de AEO
trocados para o que se pergunta a uma construtora."""
import re, html
E = html.escape

PV = {
 'cad':   ('cadastro', 'Fato do cadastro Solutudo, fornecido pela empresa.', 1.0),
 'cs':    ('Solutudo · CS', 'Declarado pela Solutudo no pedido de 30/09/2026 e no banner do Solusite de 28/09/2026. É fonte única: vale como declaração do cliente via CS.', 1.0),
 'pub':   ('fonte pública', 'Fonte pública com amarra na empresa (telefone ou e-mail iguais), lida por trecho de busca. Conferir na fonte antes de publicar.', 0.5),
 'setor': ('regra do setor', 'Fato do setor, não afirmação sobre a empresa.', 1.0),
 'pend':  ('confirmar', 'Depende de confirmação da empresa antes de publicar.', 0.5),
 'conf':  ('em conflito', 'Número que diverge entre os canais da própria empresa: 9, 10 ou 12 anos; 70 casas ou "centenas de obras"; 20.000 ou 30.000 m².', 0.0),
 'barr':  ('barrado', 'Afirmação que o verificador barrou: promessa, superlativo ou serviço regulado sem o registro que o sustente.', 0.0),
 'vazio': ('sem fato', 'Frase sem fato verificável: adjetivo, promessa ou slogan que qualquer construtora assinaria.', 0.0),
}

DIMS = [('Entidade e local', 15), ('Fatos verificáveis', 25), ('Resposta direta (AEO)', 20),
        ('Estrutura extraível', 15), ('Unicidade', 15), ('Contato e próximo passo', 10)]
DIM_TIP = {
 'Entidade e local': 'O nome da empresa, a categoria e a sede ou o alcance aparecem na primeira frase. É o que amarra a empresa certa na busca e na resposta da IA.',
 'Fatos verificáveis': 'Proporção de frases com fonte. Frase de fonte pública lida por trecho, ou a confirmar, vale meio ponto; frase sem fato ou com número em conflito vale zero; adjetivo sem fato tira 5.',
 'Resposta direta (AEO)': 'O texto responde o que se pergunta a uma construtora: o que é, onde atua (sede e alcance), o que faz, como a obra é acompanhada e como pedir orçamento, com títulos que são buscas. Frase que espera confirmação, como a dos EUA, não dá ponto.',
 'Estrutura extraível': 'Frases de até 22 palavras em média, lista onde há enumeração e títulos descritivos. IA e buscador citam trechos autocontidos.',
 'Unicidade': 'Fatos que só a Execon tem, 3 pontos por fato, até 5. Só conta fato em frase com fonte e que não espera confirmação: a expansão para os EUA não conta até a pré-condição 4.',
 'Contato e próximo passo': 'Termina em ação possível: o WhatsApp por extenso, o que informar e quando falar.',
}
GENERIC_RX = re.compile(r'^(hist[óo]ria|servi[çc]os|diferenciais|valores|sobre|contato|quem somos|miss[ãa]o|o que fazemos|produtos|perguntas frequentes|descri[çc][ãa]o|informa[çc][õo]es t[ée]cnicas|venha conhecer)', re.I)
ADJ = re.compile(r'\b(excel[êe]ncia|de ponta|incr[íi]ve(l|is)|impec[áa]ve(l|is)|perfei[çc][ãa]o|perfeit[oa]|ideal|sonho|sonhos|refer[êe]ncia|sob medida|altamente|a mais alta|m[áa]xima qualidade|superam|al[ée]m das expectativas|vibrante|impressionante|inovador(a|es)?|inova[çc][ãa]o)\b', re.I)

def words_per_sentence(texts):
    sents = []
    for t in texts:
        sents += [x for x in re.split(r'(?<=[.!?:])\s+', t) if x.strip()]
    ws = [len(x.split()) for x in sents]
    return (sum(ws) / len(ws)) if ws else 0

def score(first, sents, heads, has_list, cta, kind, wa, uniq, faq=(), serve=None):
    """sents: [(texto, pv, ...)]. heads: títulos. kind: 'desc' ou 'item'."""
    text = ' '.join(t for t, *_ in sents)
    R = []
    R.append([('nome da empresa na 1ª frase', 'Execon' in first, 5),
              ('categoria ou serviço na 1ª frase', bool(re.search(r'construtora|constru[çc][ãa]o|obra|projeto|engenharia|arquitet|pergolado|el[ée]tric|lazer', first, re.I)), 5),
              ('sede ou alcance declarados', bool(re.search(r'S[ãa]o Paulo', text)), 5)])
    n = len(sents); w = sum(PV[pv][2] for _, pv, *_ in sents)
    nfull = sum(1 for _, pv, *_ in sents if PV[pv][2] == 1.0)
    nhalf = sum(1 for _, pv, *_ in sents if PV[pv][2] == 0.5)
    nzero = n - nfull - nhalf
    pts = round(25 * w / n) if n else 0
    adj = bool(ADJ.search(text))
    R.append([(f'{nfull} de {n} frases com fonte confirmada · {nhalf} a conferir ou confirmar (meio ponto) · {nzero} sem fato ou em conflito', True, pts - (5 if adj else 0)),
              ('nenhum adjetivo sem fato', not adj, 0)])
    generic = [h for h in heads if GENERIC_RX.search(h.strip())]
    if kind == 'desc':
        R.append([('1ª frase responde o que é', 'Execon' in first and bool(re.search(r'construtora', first, re.I)), 5),
                  ('responde onde atua: sede e alcance', bool(re.search(r'S[ãa]o Paulo', text)) and bool(re.search(r'interior|litoral|Grande S[ãa]o Paulo', text)), 3),
                  ('responde o que a empresa faz, em lista', has_list, 3),
                  ('responde como o cliente acompanha a obra', bool(re.search(r'relat[óo]rio', text, re.I)), 3),
                  ('responde como pedir orçamento', 'WhatsApp' in text, 3),
                  ('títulos que respondem a uma busca', not generic, 3)])
    else:
        R.append([('1ª frase define o serviço com o nome da empresa', 'Execon' in first, 5),
                  ('diz para que ou para quem serve', bool(serve) and bool(re.search(serve, text, re.I)), 5),
                  ('diz onde atua', bool(re.search(r'S[ãa]o Paulo|Estados Unidos|condom[íi]nio', text)), 4),
                  ('diz como pedir', 'WhatsApp' in cta, 3),
                  ('pergunta da página respondida no FAQ', len(faq) > 0, 3)])
    avg = words_per_sentence([t for t, *_ in sents])
    R.append([(f'frases curtas: média de {avg:.0f} palavras (meta até 22)', avg <= 22, 5 if avg <= 22 else (3 if avg <= 28 else 0)),
              ('lista onde há enumeração', has_list, 5),
              ('títulos descritivos, nunca genéricos' + (f' · genéricos: {", ".join(generic)}' if generic else ''), not generic, 5)])
    # só conta fato próprio que está numa frase com fonte e que não espera confirmação
    utext = ' '.join(t for t, pv, *_ in sents if PV[pv][2] > 0 and pv != 'pend')
    hits = [lab for lab, rx in uniq if re.search(rx, utext, re.I)]
    R.append([(f'fatos que só a Execon tem, em frase com fonte e sem pendência: {", ".join(hits) if hits else "nenhum"}', bool(hits), min(15, 3 * len(hits)))])
    R.append([('canal por extenso', wa in cta, 5),
              ('diz o que informar', bool(re.search(r'\b(diga|informe|informando|dizendo|conte|envie)\b', cta, re.I)), 3),
              ('horário ou agendamento', bool(re.search(r'todos os dias|agend|visita|das 8h', text + ' ' + cta, re.I)), 2)])
    out = []
    for (name, mx), crit in zip(DIMS, R):
        if name in ('Fatos verificáveis', 'Unicidade'):
            got = crit[0][2]
        else:
            got = sum(p for lab, ok, p in crit if ok)
        out.append((name, mx, max(0, min(mx, got)), crit))
    return sum(g for _, _, g, _ in out), out

# ------------------------------------------------------------------ o texto publicado hoje, frase a frase
# (texto, pv, dica). Títulos à parte. É a íntegra do campo Descrição do cadastro, de 13/10/2022.
NOW_HEADS = ['Execução de Projetos Inovadores e de Alta Qualidade com a Execon Engenharia e Construção – São Paulo/SP',
             'História da Execon Engenharia e Construção', 'Serviços Oferecidos pela Execon Engenharia e Construção',
             'Diferenciais da Execon Engenharia e Construção', 'Valores da Execon Engenharia e Construção',
             'Construtora Especializada em São Paulo – Transforme Seu Projeto com a Execon']
NOW_P = [
 ('Execução de Projetos Inovadores e de Alta Qualidade com a Execon Engenharia e Construção – São Paulo/SP', 'h',
  'O título é o primeiro texto que a IA lê, e ele gasta "inovadores" e "alta qualidade" antes de dizer o que a empresa é. Não diz construtora, não diz casa, não diz alto padrão.'),
 [('Localizada na vibrante Avenida Paulista, um dos maiores centros financeiros e culturais de São Paulo, a Execon Engenharia e Construção se consolidou como uma construtora de excelência, especializada em transformar sonhos em realidade.', 'vazio',
   'A primeira frase tem o nome, a categoria e a cidade, e é por isso que a entidade pontua cheio. Mas gasta 34 palavras e termina em "transformar sonhos em realidade". "Vibrante" e "centros financeiros e culturais" falam da avenida, não da empresa.'),
  ('Com mais de 9 anos de experiência, a empresa acumula um portfólio impressionante de 70 residências de alto padrão e mais de 20.000 m² de áreas construídas que refletem o compromisso com qualidade, inovação e precisão em cada detalhe.', 'conf',
   'Os três números da empresa estão aqui, e os três estão em conflito. "9 anos" foi escrito em outubro de 2022 e envelheceu quatro anos. Outros canais da Execon dizem 10 e 12 anos, "centenas de obras" e 30.000 m².'),
  ('Se você está buscando uma construtora em São Paulo que combine experiência, confiança e eficiência, a Execon é a sua escolha ideal.', 'vazio',
   'Frase de venda sem fato: qualquer construtora de São Paulo publica igual.')],
 ('História da Execon Engenharia e Construção', 'h', 'Rótulo, não busca. E a seção não conta história nenhuma: não há ano, lugar de origem nem obra.'),
 [('A trajetória da Execon Engenharia e Construção começou com a visão de oferecer soluções construtivas que aliem modernidade, tecnologia e sustentabilidade.', 'vazio', 'Três abstrações e nenhum fato.'),
  ('Ao longo desses 9 anos, a empresa se tornou referência em construção civil em São Paulo, destacando-se pela realização de projetos arquitetônicos sofisticados, construção de casas e projetos comerciais com a mais alta qualidade.', 'conf',
   '"Referência" sem prova e "9 anos" de novo, o mesmo número que já envelheceu.'),
  ('Com uma equipe altamente qualificada, a Execon consegue transformar espaços e garantir que cada cliente tenha a experiência de um imóvel dos seus sonhos, atendendo de forma personalizada e exclusiva.', 'vazio',
   '"Equipe altamente qualificada" sem nenhum registro profissional citado. Num setor regulado, o número do CREA prova mais que qualquer adjetivo.')],
 ('Serviços Oferecidos pela Execon Engenharia e Construção', 'h', 'O rótulo que a regra 10 do padrão proíbe. O título útil diz o serviço: "Construção de casas de alto padrão, projeto e gestão de obra".'),
 [('A Execon Engenharia e Construção é especializada em diversos segmentos da construção civil, oferecendo uma gama de serviços que atendem tanto clientes residenciais quanto comerciais.', 'cad',
   'Diz residencial e comercial, o que o catálogo confirma. É a única frase introdutória com fato.'),
  ('Entre os principais serviços que a empresa oferece estão:', 'vazio', 'Frase de passagem.')],
 ('LISTA', None, None),
 [('Projetos Arquitetônicos: Criamos projetos arquitetônicos inovadores que refletem o estilo e as necessidades dos nossos clientes, com soluções criativas e práticas.', 'barr', 'O primeiro serviço da lista é o que não pode ser anunciado: nenhum registro no CAU foi encontrado. Até o cliente mostrar arquiteto com CAU, o texto não fala em projeto.'),
  ('Gerenciamento de Obras: Acompanhamento rigoroso e detalhado das obras, garantindo a entrega dentro do prazo e do orçamento, com a qualidade que só a Execon oferece.', 'cad', 'O serviço é real, em três fontes. Mas "garantindo a entrega dentro do prazo e do orçamento" e "a qualidade que só a Execon oferece" são promessas que o verificador barrou.'),
  ('Construção de Casas: Para aqueles que buscam realizar o sonho da casa própria, a Execon se destaca como uma construtora de casas em São Paulo, proporcionando excelência em cada fase da obra.', 'cad',
   '"O sonho da casa própria" é a linguagem do programa habitacional, o oposto do alto padrão. O banner novo, de 28/09, já fala em "casa de alto padrão".'),
  ('Projeto de Áreas de Lazer: Idealizamos e executamos projetos de áreas de lazer incríveis para sua residência ou empreendimento comercial, trazendo conforto e sofisticação.', 'cad', 'Serviço real. Não nomeia piscina, área gourmet nem pergolado, que o catálogo tem.'),
  ('Elétrica e Hidráulica em Geral: Realizamos instalações de elétrica e hidráulica de alta qualidade, sempre respeitando as normas de segurança e eficiência.', 'cad', 'A elétrica é serviço real, do produto 547883. Hidráulica aparece só aqui, sem produto próprio, e "respeitando as normas de segurança" é promessa que o setor regulado barra.')],
 [('Além desses, a Execon também se especializa na construção de pergolados e outros elementos arquitetônicos que agregam valor e funcionalidade aos projetos, seja para residências, comércios, ou áreas de lazer.', 'cad', 'Pergolado é fato do catálogo, com materiais nomeados no produto 547873.')],
 ('Diferenciais da Execon Engenharia e Construção', 'h', 'Rótulo. E nenhum dos quatro "diferenciais" abaixo é diferente do que qualquer construtora escreve.'),
 [('O que realmente diferencia a Execon Engenharia e Construção no mercado de construtoras em São Paulo é a nossa busca constante pela inovação, pelo compromisso com a qualidade e pelo atendimento personalizado.', 'vazio', 'Inovação, qualidade e atendimento personalizado: os três diferenciais mais comuns do setor.'),
  ('Cada projeto é tratado de forma única, com atenção aos detalhes, e com uma gestão eficaz de todos os processos, da concepção até a entrega final.', 'vazio', 'Sem fato.'),
  ('Com a Execon, você tem a certeza de contar com:', 'vazio', 'Frase de passagem.')],
 ('LISTA', None, None),
 [('Equipe experiente e qualificada: Profissionais altamente treinados em todas as áreas da construção civil.', 'vazio', 'Sem registro, sem número.'),
  ('Tecnologia de ponta: Utilizamos as melhores ferramentas e técnicas para garantir a qualidade e a segurança em cada projeto.', 'vazio', 'O produto 547879 diz mais: acompanhamento da obra em tempo real. Esse fato, se confirmado, é o diferencial, e ele não aparece aqui.'),
  ('Entrega no prazo e dentro do orçamento: Transparência em cada etapa do processo, com uma gestão eficiente de custos e prazos.', 'vazio', 'Promessa. O fato que a sustentaria, os relatórios periódicos citados nos produtos, não aparece.'),
  ('Atendimento personalizado: Cada cliente é único, e os projetos são desenvolvidos de acordo com suas necessidades e desejos específicos.', 'vazio', 'Sem fato.')],
 ('Valores da Execon Engenharia e Construção', 'h', 'Seção inteira sem um fato. Valores não respondem a nenhuma busca.'),
 [('Na Execon Engenharia e Construção, nossos valores são a base de tudo o que fazemos.', 'vazio', 'Sem fato.'),
  ('Trabalhamos com honestidade, responsabilidade e comprometimento para entregar sempre o melhor.', 'vazio', 'Sem fato.'),
  ('Acreditamos que a qualidade, a transparência e o respeito aos prazos são essenciais para construir uma relação de confiança com nossos clientes.', 'vazio', 'Sem fato.'),
  ('A ética é um pilar fundamental em nosso trabalho, e nos orgulhamos de oferecer soluções de construção sustentáveis e responsáveis, respeitando o meio ambiente e as normas de segurança.', 'vazio', '"Sustentáveis" sem nenhuma prática nomeada. O produto 547874 cita energia solar e reúso de água da chuva, e isso não chegou aqui.')],
 ('Construtora Especializada em São Paulo – Transforme Seu Projeto com a Execon', 'h', 'O melhor título do texto, porque tem categoria e cidade. Mas vem no fim.'),
 [('Se você está em busca de uma construtora em São Paulo/SP que seja referência em projetos arquitetônicos, gerenciamento de obras e construção de imóveis de alto padrão, a Execon Engenharia e Construção é a escolha certa.', 'barr',
   'A única frase que junta construtora, São Paulo e alto padrão, e ela está no último parágrafo: a ideia deveria abrir o texto. Mas diz "referência" e "a escolha certa", que o verificador barrou, e "projetos arquitetônicos", que espera o CAU.'),
  ('Com anos de experiência, mais de 70 residências entregues e projetos comerciais bem-sucedidos, nossa missão é transformar seus sonhos em realidade com qualidade, segurança e inovação.', 'conf', 'O número em conflito, de novo, e "sonhos em realidade" pela segunda vez.')],
 [('Venha conhecer nossos projetos e descubra como a Execon pode realizar o seu sonho!', 'vazio',
   'O fim não tem telefone nem WhatsApp. Não diz como pedir orçamento nem o que informar, e o convite "venha conhecer" não leva a lugar nenhum.')],
]
MISSING = [
 ('os Estados Unidos', 'O banner novo do Solusite diz "com atual expansão no EUA". O texto não diz uma palavra.'),
 ('o foco em alto padrão', 'Aparece uma vez, no último parágrafo, e o texto usa "o sonho da casa própria", linguagem do programa habitacional.'),
 ('o WhatsApp', 'Três números no cadastro, e nenhum no texto.'),
 ('os condomínios', 'Ninho Verde, Riviera de Santa Cristina e Águas de Santa Bárbara estão na outra página da empresa na Solutudo, e não aqui.'),
 ('o acompanhamento da obra', 'Relatórios periódicos e acompanhamento em tempo real estão nos produtos, e não na descrição.'),
 ('o registro profissional', 'Nenhum CREA ou CAU citado, num setor regulado.'),
]
def now_sents():
    out = []
    for blk in NOW_P:
        if isinstance(blk, tuple):
            continue
        out += blk
    return out
NOW_WA = '(11) 98454-5681'

# fatos que só a Execon tem — a mesma lista mede o texto de hoje e o proposto
UNIQ = [('expansão para os Estados Unidos', r'Estados Unidos'),
        ('condomínios nomeados', r'Ninho Verde|Riviera de Santa Cristina|[ÁA]guas de Santa B[áa]rbara'),
        ('projeto e obra na mesma empresa', r'projetos? arquitet[ôo]nicos?[^.]{0,160}(obra|constru)|projetos e execu[çc][ãa]o de obras|arquitetura e engenharia'),
        ('relatórios periódicos da obra', r'relat[óo]rio'),
        ('registro no CREA-SP', r'CREA'),
        ('sede na Avenida Paulista', r'Avenida Paulista|Av\. Paulista'),
        ('atendimento pelo WhatsApp todos os dias', r'todos os dias')]

# ------------------------------------------------------------------ os 9 produtos publicados hoje, classificados por código
PV['trad'] = ('tradução corrompida', 'A frase voltou quebrada do tradutor automático do navegador, como "canto de obras" no lugar de canteiro. Não carrega fato utilizável.', 0.0)
TRAD = re.compile(r'canto de obras|Cust[óo]dia|instala[çc][õo]es poss[íi]veis|projeto atualizado|licen[çc]as permitidas|cont[íi]nuo com compet[êe]ncia|interruptores, tomadas e interruptores|Controle rigorosamente', re.I)
CONCRETE = re.compile(r'piscina|churrasqueira|pergolad|madeira|alum[íi]nio|ferro\b|policarbonato|vegeta|jardi|paisag|ilumina|varanda|gourmet|lojas|escrit[óo]rio|restaurante|ind[úu]stri|el[ée]tric|hidr[áa]ulic|rede de dados|climatiza|acessibilidade|automa[çc]|NBR|tomadas|manuten[çc]|licen|regulariza|estrutur|funda[çc]|acabamento|cronograma|or[çc]amento aprovado|fornecedores|subcontrat|relat[óo]rio|layout|fluxo de pessoas|energia solar|chuva|inspe[çc]|apartamentos|condom[íi]nio|terra[çc]o|reforma|aprova[çc]|[óo]rg[ãa]os|alto padr[ãa]o|tempo real', re.I)
def classify(t):
    if re.search(r'9 anos', t): return 'conf'
    if TRAD.search(t): return 'trad'
    if CONCRETE.search(t): return 'cad'
    return 'vazio'
def parse_items(path):
    txt = open(path, encoding='utf-8').read().split('## PRODUTOS', 1)[1]
    items = []
    for blk in re.split(r'\n### ', txt)[1:]:
        head, body = blk.split('\n', 1)
        pid, title = head.split(' · ', 1)
        title = re.sub(r'\s*\[.*$', '', title).strip()
        flags = re.findall(r'\[([^\]]+)\]', head)
        sec = dict(re.findall(r'^(Descrição|Serviços|Diferenciais|CTA): (.*)$', body, re.M))
        sents = []
        for part in ('Descrição', 'Serviços', 'Diferenciais', 'CTA'):
            raw = sec.get(part, '').replace('**', '')
            pieces = raw.split(' · ') if part in ('Serviços', 'Diferenciais') else re.split(r'(?<=[.!?])\s+', raw)
            for x in pieces:
                x = x.strip()
                if x: sents.append((x, classify(x), part))
        items.append(dict(id=pid.strip(), title=title, flags=flags, sents=sents,
                          trad='markup de tradutor' in head, cta=sents[-1][0]))
    return items

def now_stats():
    ns = now_sents()
    words = sum(len(t.split()) for t, *_ in ns) + sum(len(h.split()) for h in NOW_HEADS)
    zero = sum(1 for _, pv, *_ in ns if PV[pv][2] == 0)
    return dict(words=words, n=len(ns), zero=zero)
