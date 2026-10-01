# -*- coding: utf-8 -*-
"""Fonte única da LAAE: o texto do laboratório, o catálogo, o FAQ e os canais.
Tudo que aparece na página Solutudo (aba Destaque) e no Solusite sai daqui."""
import re, html
E = html.escape

PV = {
 'cad':   ('cadastro', 'Fato do cadastro Solutudo, fornecido pela empresa.', 1.0),
 'reu':   ('reunião', 'Dito pelo dono na reunião comercial gravada.', 1.0),
 'setor': ('norma do setor', 'Fato do setor, verificável na norma. Não é afirmação sobre a empresa.', 1.0),
 'site':  ('site · conferir', 'Veio do resumo colado do site oficial, que não foi aberto. Conferir na fonte antes de publicar.', 0.5),
 'pend':  ('confirmar', 'Depende de confirmação do laboratório antes de publicar.', 0.5),
}
WA = '(38) 98405-5391'
CIDADES = ['Montes Claros','Jaíba','Janaúba','Januária','Diamantina','Curvelo','Salinas','Araçuaí','Pirapora']

# ---------------------------------------------------------------- o texto do laboratório
DESC = {
 'h1': 'LAAE, laboratório de análise de água e efluentes desde 2003',
 'abertura': [
  ('O LAAE (LabLAAE) é um laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003.', 'cad',
   'Entidade primeiro: o nome, o apelido pelo qual o cliente chama a empresa, a categoria, a sede e o ano. É a frase que a IA cita inteira. "Sede", não cobertura.'),
  ('A matriz tem serviços acreditados pela CGCRE do Inmetro, conforme os escopos dos certificados, e reconhecimento pela Rede Metrológica do Rio Grande do Sul segundo a ABNT NBR ISO/IEC 17025.', 'cad',
   'A credencial com o órgão nomeado e a ressalva do escopo. "A matriz" importa: a rede tem franquias, e a acreditação é desta unidade.'),
  ('A coleta das amostras é feita pela equipe do próprio laboratório, em nove cidades de Minas Gerais.', 'reu',
   'O diferencial na abertura. "Nove cidades de Minas Gerais", não "Norte de Minas": Diamantina, Curvelo e Araçuaí ficam fora dessa região.'),
 ],
 'blocos': [
  ('Análises físico-químicas e microbiológicas de água e efluentes',
   ('O LAAE faz análises físico-químicas e microbiológicas de água e de efluentes, conforme a origem e o uso:', 'cad', 'Os dois tipos de ensaio, com o nome da empresa: a frase se sustenta sozinha.'),
   [('Água para consumo humano e água potável.', 'cad', 'Origens de água do cadastro.'),
    ('Águas subterrâneas, como a de poço artesiano, e águas superficiais.', 'cad', 'Poço artesiano é o público da reunião e busca curada da categoria.'),
    ('Água industrial de processo.', 'site', 'Aplicação nomeada pelo site oficial, que não foi aberto.'),
    ('Efluentes industriais e sanitários, para acompanhamento de sistemas de tratamento.', 'cad', 'Os dois tipos de efluente, com o uso que justifica o ensaio.'),
    ('Programas de monitoramento ambiental, para acompanhar a mesma água ou o mesmo efluente ao longo do tempo.', 'cad', 'Monitoramento é a categoria Engenharia Ambiental do cadastro, e o contrato recorrente que a reunião pede.')], True),
  ('Como é feita a coleta da amostra de água e efluente', None,
   [('A coleta é feita pela equipe do LAAE, na unidade do cliente.', 'reu', 'Coleta própria: dito na reunião, ausente de todo texto público até aqui.'),
    ('Para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas depois de coletada.', 'pend', 'O fato que explica o negócio. "Boa parte dos ensaios": o prazo muda de ensaio para ensaio.'),
    ('O laudo fica disponível no portal de resultados do LAAE, com login e senha.', 'reu', 'O portal é diferencial operacional dito na reunião.')], True),
  ('Cidades onde o LAAE faz a coleta', None,
   [('Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora. Para outras cidades, consulte pelo WhatsApp.', 'cad', 'As nove, por extenso: ou a lista inteira, ou nenhuma.')], False),
  ('Análise de água para indústria, hospital, agronegócio e poço artesiano', None,
   [('O LAAE atende indústrias, agronegócio, consultorias ambientais, hospitais, clínicas, hotéis e restaurantes, e quem usa água que não vem da concessionária, como a de poço artesiano.', 'reu', 'Os públicos da reunião e o critério que define o cliente em uma frase.')], False),
  ('Como pedir uma análise de água ao LAAE', None,
   [('O atendimento é de segunda a sexta, das 8h às 12h e das 13h às 17h.', 'cad', 'Horário do cadastro, em dois turnos.'),
    ('O pagamento pode ser em boleto, Pix, dinheiro e cartões de crédito e débito.', 'cad', 'Boleto primeiro: é como indústria e hospital compram.')], False),
 ],
 'cta': ('Precisa de uma análise? Fale com o LAAE pelo WhatsApp (38) 98405-5391 e diga a origem da água, o uso e a cidade.', 'cad',
         'Fecha em ação, com o nome da empresa e os três dados que o comercial pede. Na Solutudo é texto; no site, botão com link.'),
}
def desc_sents():
    out = list(DESC['abertura'])
    for _, intro, items, _ in DESC['blocos']:
        if intro: out.append(intro)
        out += items
    out.append(DESC['cta'])
    return out
def desc_heads(): return [b[0] for b in DESC['blocos']]

# ---------------------------------------------------------------- FAQ comum (página Solutudo = Solusite)
FAQ = [
 dict(k='F1', q='O LAAE coleta na minha cidade?', pv='cad',
      a='O LAAE coleta em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora, com equipe própria. Para outras cidades, a consulta é pelo WhatsApp (38) 98405-5391.',
      tags=['Local','Conversão','Voz'], why='A intenção local pura. A lista inteira responde sem depender de página por cidade.'),
 dict(k='F2', q='Quanto tempo a amostra de água vale depois de coletada?', pv='pend',
      a='Para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas. É por isso que o LAAE faz a coleta com equipe própria e atende uma região definida.',
      tags=['IA','AEO'], why='O tema único do caso, em formato de resposta.', pend='quais ensaios têm prazo diferente'),
 dict(k='F3', q='O LAAE é acreditado?', pv='cad',
      a='O LAAE tem serviços acreditados pela CGCRE do Inmetro: a acreditação vale para os ensaios listados nos escopos dos certificados da matriz. O laboratório também tem reconhecimento pela Rede Metrológica do Rio Grande do Sul segundo a ABNT NBR ISO/IEC 17025.',
      tags=['IA','Confiança'], why='Não começa com "sim": seria afirmar acreditação para tudo. A primeira frase já carrega a ressalva.'),
 dict(k='F4', q='Preciso analisar a água do meu poço artesiano?', pv='reu',
      a='Quem capta água fora da rede pública responde pela qualidade dela, e a análise é o que mostra se a água do poço serve ao uso pretendido: consumo, produção ou irrigação. O LAAE indica os ensaios conforme o uso.',
      tags=['SEO','IA','Conversão'], why='O critério do dono transformado em resposta. Cauda longa real da categoria.'),
 dict(k='F5', q='Qual a diferença entre análise físico-química e microbiológica?', pv='setor',
      a='A análise físico-química mede características químicas e físicas da água; a microbiológica verifica a presença de microrganismos. Para o laudo de potabilidade, as duas são feitas juntas.',
      tags=['IA','AEO'], why='Pergunta definitória: o formato que IA e "as pessoas também perguntam" mais consomem.'),
 dict(k='F6', q='Como recebo o laudo do LAAE?', pv='reu',
      a='O laudo do LAAE fica disponível no portal de resultados, com login e senha.',
      tags=['Conversão','Voz'], why='Uma frase, um fato. O portal é diferencial que nunca tinha sido publicado.'),
 dict(k='F7', q='Quanto custa uma análise de água?', pv='cad',
      a='O valor depende dos ensaios e do número de pontos de coleta. O orçamento do LAAE é feito pelo WhatsApp (38) 98405-5391, informando a origem da água, o uso e a cidade.',
      tags=['Conversão'], why='Fundo de funil. Responde sem inventar preço e já diz o que informar.', pend='faixa de preço, se o laboratório quiser publicar'),
 dict(k='F8', q='Quais parâmetros o LAAE analisa?', pv='pend', a=None,
      tags=['SEO','IA'], why='Sem resposta publicável até o escopo de acreditação chegar. Quando chegar, cada parâmetro vira uma busca própria.', pend='a lista do escopo acreditado — bloqueia esta resposta'),
]
FAQD = {f['k']: f for f in FAQ}
FAQ_GAPS = [
 ('Em quanto tempo o laudo fica pronto?', 'prazo por tipo de análise — laboratório'),
 ('Com que frequência a equipe passa em cada cidade?', 'rota e frequência — laboratório. É o fato que justificaria uma página por cidade'),
 ('O LAAE atende fora de Minas Gerais?', 'o papel das franquias da Bahia na resposta — "11 estados" do site é alcance de franqueadora e está em conflito'),
]

# ---------------------------------------------------------------- catálogo: 1 item = 1 página
def it(**k): return k
CATALOG = [
 it(key='p711909', kind='cad', idl='ID 711909', card='Análise Físico-Química de Água',
    url='/analises/fisico-quimica', h1='Análise físico-química da água em Montes Claros (MG)', title='Análise físico-química da água · LAAE',
    meta='O LAAE avalia as características químicas e físicas da água potável, de poço, superficial e de processo. Coleta pela equipe e laudo no portal.',
    intro=[('A análise físico-química do LAAE avalia as características químicas e físicas da água e mostra se ela serve ao uso pretendido.', 'cad')],
    bullets=[('Para água potável e para consumo humano, águas superficiais e subterrâneas.', 'cad'),
             ('Para água industrial de processo, no controle do processo produtivo.', 'site'),
             ('Junto com a análise microbiológica, forma o laudo de potabilidade.', 'setor'),
             ('Ensaios acreditados pela CGCRE/Inmetro, conforme o escopo dos certificados.', 'cad'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas, com o laudo no portal.', 'reu')],
    serve='serve ao uso pretendido',
    cta=('Diga o uso da água no WhatsApp (38) 98405-5391 e o LAAE indica os ensaios para o seu caso.', 'cad'),
    faq=[('A análise físico-química serve para água de processo industrial?', 'Sim. O LAAE analisa água industrial de processo, com os ensaios definidos conforme o uso da água no processo.', 'site'), 'F5'],
    pend='a lista de parâmetros físico-químicos do escopo acreditado — é o que falta para a página alcançar a busca técnica'),
 it(key='p711908', kind='cad', idl='ID 711908', card='Análise Microbiológica de Água',
    url='/analises/microbiologica', h1='Análise microbiológica da água (exame bacteriológico) em Montes Claros (MG)', title='Análise microbiológica da água (bacteriológica) · LAAE',
    meta='O LAAE verifica a presença de microrganismos na água de poço, caixa d’água, reservatório e caminhão-pipa. Coleta própria em nove cidades de MG.',
    intro=[('A análise microbiológica do LAAE verifica a presença de microrganismos que comprometem o uso da água.', 'cad')],
    bullets=[('Para poço artesiano, reservatório, caixa d’água e caminhão-pipa.', 'cad'),
             ('Para água potável e para consumo humano, superficial e subterrânea.', 'cad'),
             ('Parte dos programas de monitoramento periódico da qualidade da água.', 'cad'),
             ('Ensaios acreditados pela CGCRE/Inmetro, conforme o escopo dos certificados.', 'cad'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas, com o laudo no portal.', 'reu')],
    serve='Para poço artesiano',
    cta=('Peça a sua análise no WhatsApp (38) 98405-5391 dizendo a origem da água e para que ela é usada.', 'cad'),
    faq=[('A análise microbiológica serve para caixa d’água e caminhão-pipa?', 'Sim. O LAAE faz a análise microbiológica da água de poço artesiano, reservatório, caixa d’água e caminhão-pipa.', 'cad'), 'F5'],
    pend='a lista de parâmetros microbiológicos do escopo acreditado. Com ela, a página responde "exame bacteriológico da água", busca que hoje ninguém disputa na região'),
 it(key='p711409', kind='cad', idl='ID 711409', card='Análise de Efluentes',
    url='/analises/efluentes', h1='Análise de efluente industrial e sanitário em Montes Claros (MG)', title='Análise de efluente industrial e sanitário · LAAE',
    meta='O LAAE analisa efluentes industriais e sanitários para acompanhar sistemas de tratamento, com coleta pela equipe em nove cidades de Minas Gerais.',
    intro=[('O LAAE analisa efluentes industriais e sanitários para o acompanhamento de sistemas de tratamento e o controle ambiental.', 'cad')],
    bullets=[('Efluente industrial: acompanhamento do processo e da eficiência do tratamento.', 'cad'),
             ('Efluente sanitário: monitoramento da estação e do lançamento.', 'cad'),
             ('Ensaios acreditados pela CGCRE/Inmetro, conforme o escopo dos certificados.', 'cad'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas, dentro do prazo do ensaio.', 'reu'),
             ('Laudo no portal de resultados, com login e senha.', 'reu')],
    serve='para o acompanhamento de sistemas de tratamento',
    cta=('Peça a coleta no WhatsApp (38) 98405-5391 informando o tipo de efluente e o ponto de lançamento.', 'cad'),
    faq=[('Quem precisa fazer análise de efluente?', 'Quem opera sistema de tratamento de efluente industrial ou sanitário e precisa acompanhar a eficiência do tratamento. O LAAE coleta a amostra no ponto de lançamento.', 'reu')],
    pend='os parâmetros do escopo acreditado para efluente, como DBO, DQO, sólidos, óleos e graxas — sem eles a página não alcança a busca técnica'),
 it(key='p711410', kind='cad', idl='ID 711410', card='Amostragem de Água',
    url='/coleta-e-amostragem', h1='Coleta e amostragem de água e efluente na sua unidade', title='Coleta e amostragem de água e efluentes · LAAE',
    meta='A equipe do LAAE coleta a amostra na sua unidade, com equipamento multiparâmetro em campo e temperatura monitorada no transporte.',
    intro=[('A coleta e a amostragem do LAAE são feitas pela equipe do próprio laboratório, na unidade do cliente.', 'reu'),
           ('Para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas depois de coletada.', 'pend')],
    bullets=[('Coleta agendada por data e horário.', 'reu'),
             ('Equipamento multiparâmetro em campo, para leitura no momento da coleta.', 'reu'),
             ('Temperatura da amostra monitorada durante o transporte.', 'site'),
             ('Controles de qualidade durante a própria amostragem.', 'site'),
             ('Coleta nas nove cidades atendidas.', 'cad')],
    serve='na unidade do cliente',
    cta=('Agende a coleta no WhatsApp (38) 98405-5391 dizendo a cidade e quantos pontos serão coletados.', 'cad'),
    faq=['F2'], pend='quais ensaios têm prazo diferente de 24 horas'),
 it(key='s-coleta', kind='pronto', idl='sugerido · pronto', card='Coleta própria nas nove cidades',
    url='/onde-coletamos', h1='Análise de água com coleta em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora', title='Coleta de água e efluentes em 9 cidades de MG · LAAE',
    meta='Coleta pela equipe do laboratório em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora.',
    intro=[('O LAAE coleta amostras de água e efluentes com equipe própria em nove cidades de Minas Gerais.', 'reu')],
    bullets=[('Montes Claros, onde fica a sede do laboratório.', 'cad'),
             ('Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora, na rota de coleta.', 'cad'),
             ('Outras cidades, sob consulta pelo WhatsApp.', 'cad'),
             ('O atendimento é regional porque, para boa parte dos ensaios, a amostra precisa chegar ao laboratório em até 24 horas.', 'pend')],
    serve='com equipe própria em nove cidades',
    cta=('Diga a sua cidade no WhatsApp (38) 98405-5391 e o LAAE confirma a data da próxima coleta na região.', 'reu'),
    faq=['F1'], pend='a frequência da rota em cada cidade. É o fato que justificaria uma página própria por cidade'),
 it(key='s-poco', kind='pronto', idl='sugerido · pronto', card='Análise de água de poço artesiano',
    url='/analises/agua-de-poco', h1='Análise da água de poço artesiano em Montes Claros (MG)', title='Análise de água de poço artesiano · LAAE',
    meta='Quem capta água fora da rede pública responde pela qualidade dela. O LAAE indica os ensaios conforme o uso: consumo, produção ou irrigação.',
    intro=[('O LAAE analisa a água de poço artesiano e mostra se ela serve ao uso pretendido: consumo, produção ou irrigação.', 'reu')],
    bullets=[('Quem capta água fora da rede pública responde pela qualidade dela.', 'reu'),
             ('Ensaios físico-químicos e microbiológicos, conforme o uso da água.', 'cad'),
             ('Também para reservatório, caixa d’água e caminhão-pipa.', 'cad'),
             ('Ensaios acreditados pela CGCRE/Inmetro, conforme o escopo dos certificados.', 'cad'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas, com o laudo no portal.', 'reu')],
    serve='serve ao uso pretendido',
    cta=('Tem poço? Diga o uso da água e a cidade no WhatsApp (38) 98405-5391, e o LAAE indica os ensaios.', 'cad'),
    faq=['F4'], pend='de quanto em quanto tempo o laboratório recomenda analisar a água do poço'),
 it(key='s-monitoramento', kind='pronto', idl='sugerido · pronto', card='Monitoramento ambiental recorrente',
    url='/monitoramento-ambiental', h1='Programa de monitoramento ambiental de água e efluentes', title='Monitoramento ambiental de água e efluentes · LAAE',
    meta='No monitoramento do LAAE, pontos, frequência e ensaios ficam combinados, a coleta entra no calendário e os laudos ficam no portal.',
    intro=[('O LAAE faz programas de monitoramento ambiental, para acompanhar a mesma água ou o mesmo efluente ao longo do tempo.', 'cad')],
    bullets=[('Pontos, frequência e ensaios combinados com a equipe técnica do cliente.', 'pend'),
             ('A coleta entra no calendário, sem um pedido novo a cada vez.', 'pend'),
             ('Os laudos de cada coleta ficam no portal, com login e senha.', 'reu'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas.', 'reu')],
    serve='para acompanhar a mesma água',
    cta=('Monte o seu programa: chame no WhatsApp (38) 98405-5391 com os pontos e a frequência de que você precisa.', 'cad'),
    faq=[('Qual a diferença entre análise avulsa e monitoramento?', 'Na análise avulsa, cada coleta é um pedido novo. No monitoramento do LAAE, pontos, frequência e ensaios ficam combinados, e a coleta entra no calendário.', 'pend')],
    pend='como o laboratório monta o programa: quem define pontos e frequência, e se há contrato'),
 it(key='s-potabilidade', kind='cond', idl='condicional', card='Laudo de potabilidade (Portaria GM/MS 888)',
    url='/analises/laudo-de-potabilidade', h1='Laudo de potabilidade da água conforme a Portaria GM/MS nº 888', title='Laudo de potabilidade da água · LAAE',
    meta='O laudo de potabilidade do LAAE mostra se a água está própria para consumo humano. Para poço artesiano, caixa d’água, reservatório e caminhão-pipa.',
    intro=[('O laudo de potabilidade do LAAE mostra se a água está própria para consumo humano.', 'cad')],
    bullets=[('Reúne os ensaios físico-químicos e microbiológicos do padrão de potabilidade.', 'setor'),
             ('Para poço artesiano, caixa d’água, reservatório e caminhão-pipa.', 'cad'),
             ('Ensaios acreditados pela CGCRE/Inmetro, conforme o escopo dos certificados.', 'cad'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas.', 'reu')],
    serve='Para poço artesiano',
    cta=('Precisa do laudo? Chame no WhatsApp (38) 98405-5391 com a origem da água e o prazo de que você precisa.', 'cad'),
    faq=[('Quem precisa de laudo de potabilidade?', 'Quem capta água fora da rede pública e precisa comprovar que ela está própria para consumo humano. O LAAE faz o laudo com coleta pela própria equipe.', 'reu')],
    cond='a versão vigente da portaria e quais parâmetros do padrão de potabilidade estão no escopo acreditado — a norma é citada pelo número, então precisa estar certa'),
 it(key='s-agro', kind='cond', idl='condicional', card='Análises para o agronegócio',
    url='/analises/agronegocio', h1='Análise de água para irrigação, piscicultura e reuso no agronegócio', title='Análise de água para irrigação e agronegócio · LAAE',
    meta='O LAAE analisa a água da propriedade rural conforme o uso: irrigação, piscicultura, reuso e manancial. Coleta nas nove cidades atendidas.',
    intro=[('O LAAE analisa a água usada no agronegócio, e cada uso pede um conjunto diferente de ensaios.', 'reu')],
    bullets=[('Irrigação: a água aplicada na lavoura.', 'pend'),
             ('Piscicultura: a água do tanque.', 'pend'),
             ('Reuso: a água tratada antes de voltar ao processo.', 'pend'),
             ('Barragem e corpo hídrico: o manancial da propriedade.', 'pend'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas.', 'reu')],
    serve='Irrigação',
    cta=('Diga o uso da água e a cidade da propriedade no WhatsApp (38) 98405-5391.', 'cad'),
    faq=[], cond='os parâmetros de cada uso, e se piscicultura e reuso são de fato atendidos — os termos vieram da lista digitada, que não é busca real'),
 it(key='s-hemodialise', kind='cond', idl='condicional · novo', card='Água para hemodiálise',
    url='/analises/agua-de-hemodialise', h1='Análise da água para hemodiálise', title='Análise da água para hemodiálise · LAAE',
    meta='O LAAE analisa a água usada em hemodiálise, para hospitais e clínicas. Coleta pela equipe do laboratório nas nove cidades atendidas.',
    intro=[('O LAAE analisa a água usada em hemodiálise.', 'site')],
    bullets=[('Para hospitais e clínicas que operam hemodiálise.', 'site'),
             ('Coleta pela equipe do LAAE nas nove cidades atendidas, com o laudo no portal.', 'reu')],
    serve='Para hospitais e clínicas',
    cta=('Fale com o LAAE no WhatsApp (38) 98405-5391 dizendo quantos pontos e com que frequência a água é analisada.', 'cad'),
    faq=[], cond='o escopo de acreditação para este ensaio, conferido na fonte. A aplicação veio do site oficial, que não foi aberto. É o achado de maior valor do caso: serviço regulado, público hospitalar e depoimento do Hospital do Câncer do Norte de Minas já publicado pela empresa'),
]
CATD = {c['key']: c for c in CATALOG}

def item_sents(c):
    return list(c['intro']) + list(c['bullets']) + [c['cta']]
def item_faq(c):
    out = []
    for f in c['faq']:
        if isinstance(f, str):
            F = FAQD[f]; out.append((F['q'], F['a'], F['pv']))
        else: out.append(f)
    return out

# ---------------------------------------------------------------- rubrica da Descrição 3.0, com critérios explícitos
DIMS = [('Entidade e local', 15), ('Fatos verificáveis', 25), ('Resposta direta (AEO)', 20),
        ('Estrutura extraível', 15), ('Unicidade', 15), ('Contato e próximo passo', 10)]
DIM_TIP = {
 'Entidade e local': 'O nome da empresa e a cidade aparecem cedo e do mesmo jeito em todos os canais. É o que amarra a empresa certa na busca.',
 'Fatos verificáveis': 'Cada afirmação tem lastro no cadastro (acreditação, cidades, tipos de água, horário, pagamento). Adjetivo sem fato não pontua.',
 'Resposta direta (AEO)': 'O texto responde de forma extraível o que as pessoas realmente perguntam: coleta onde, prazo da amostra, como pedir, como recebe o laudo.',
 'Estrutura extraível': 'Frases atômicas, listas e blocos curtos. IA e buscador citam trechos: quanto mais autocontido, maior a chance de virar resposta.',
 'Unicidade': 'Conteúdo que nenhum concorrente conseguiria publicar. Texto genérico de laboratório não pontua.',
 'Contato e próximo passo': 'O texto termina em ação possível: WhatsApp, pedido de coleta, orçamento. Sem isso, a busca resolve e a empresa não recebe o cliente.',
}
GENERIC = {'serviços','servicos','sobre','sobre nós','sobre a empresa','contato','o que fazemos','como trabalhamos','onde estamos',
           'quem atendemos','o que analisamos','onde coletamos','atendimento e pagamento','perguntas frequentes','blog','produtos','fale conosco'}
ADJ = re.compile(r'\b(qualidade garantida|excelência|compromisso|melhor|líder|referência|confiabilidade|sob medida|satisfação)\b', re.I)
UNIQ = [('prazo de 24 horas', r'24 horas'), ('coleta com equipe própria', r'equipe do (LAAE|próprio laboratório)|equipe própria'),
        ('portal de laudos', r'portal'), ('acreditação CGCRE com escopo', r'CGCRE'), ('as nove cidades', r'nove cidades|Jaíba'),
        ('fundação em 2003', r'2003'), ('multiparâmetro em campo', r'multiparâmetro'), ('Rede Metrológica RS', r'Rede Metrológica')]

def words_per_sentence(texts):
    sents = []
    for t in texts:
        sents += [x for x in re.split(r'(?<=[.!?:])\s+', t) if x.strip()]
    ws = [len(x.split()) for x in sents]
    return (sum(ws) / len(ws)) if ws else 0

def score(first, sents, heads, has_list, cta, faq, kind, serve=None):
    text = ' '.join(t for t, *_ in sents)
    R = []
    # entidade
    c = [('nome da empresa na 1ª frase', 'LAAE' in first, 5),
         ('categoria ou serviço na 1ª frase', bool(re.search(r'laborat[óo]rio|an[áa]lis|coleta|laudo|monitoramento', first, re.I)), 5),
         ('sede ou alcance declarados', ('Montes Claros' in text) or ('nove cidades' in text), 5)]
    R.append(c)
    # fatos
    n = len(sents); w = sum(PV[pv][2] for _, pv, *_ in sents)
    nconf = sum(1 for _, pv, *_ in sents if PV[pv][2] == 1.0)
    nsite = sum(1 for _, pv, *_ in sents if pv == 'site'); npend = sum(1 for _, pv, *_ in sents if pv == 'pend')
    pts = round(25 * w / n) if n else 0
    adj = bool(ADJ.search(text))
    c = [(f'{nconf} de {n} frases com fonte confirmada · {nsite} do site a conferir · {npend} a confirmar (valem meio ponto)', True, pts - (5 if adj else 0)),
         ('nenhum adjetivo sem fato', not adj, 0)]
    R.append(c)
    # AEO
    if kind == 'desc':
        c = [('1ª frase responde o que é', 'LAAE' in first and 'laboratório' in first, 5),
             ('responde onde coleta', bool(re.search(r'nove cidades|Jaíba', text)), 3),
             ('responde o prazo da amostra', '24 horas' in text, 3),
             ('responde como pedir', 'WhatsApp' in text, 3),
             ('responde como recebe o laudo', 'portal' in text, 3),
             ('títulos que respondem a uma busca', all(h.lower() not in GENERIC for h in heads), 3)]
    else:
        c = [('1ª frase define o serviço com o nome da empresa', 'LAAE' in first, 5),
             ('diz para que ou para quem serve', bool(serve) and serve in text, 5),
             ('diz onde coleta', bool(re.search(r'nove cidades|Jaíba|Montes Claros', text)), 4),
             ('diz como pedir', 'WhatsApp' in cta, 3),
             ('pergunta da página respondida no FAQ', len(faq) > 0, 3)]
    R.append(c)
    # estrutura
    avg = words_per_sentence([t for t, *_ in sents])
    c = [(f'frases curtas: média de {avg:.0f} palavras (meta até 22)', avg <= 22, 5 if avg <= 22 else (3 if avg <= 28 else 0)),
         ('lista onde há enumeração', has_list, 5),
         ('títulos descritivos, nunca genéricos', all(h.lower() not in GENERIC for h in heads), 5)]
    R.append(c)
    # unicidade
    hits = [lab for lab, rx in UNIQ if re.search(rx, text)]
    c = [(f'fatos que só a LAAE tem: {", ".join(hits) if hits else "nenhum"}', bool(hits), min(15, 3 * len(hits)))]
    R.append(c)
    # contato
    c = [('canal por extenso', WA in cta, 5),
         ('diz o que informar', bool(re.search(r'diga|dizendo|informando|com a origem|com os pontos|quantos pontos', cta, re.I)), 3),
         ('horário ou agendamento', bool(re.search(r'segunda a sexta|[Aa]gend|confirma a data', text + ' ' + cta)), 2)]
    R.append(c)
    out = []
    for (name, mx), crit in zip(DIMS, R):
        got = 0
        for lab, ok, p in crit:
            if name == 'Fatos verificáveis':
                got = crit[0][2]; break
            if name == 'Unicidade':
                got = crit[0][2]; break
            got += p if ok else 0
        got = max(0, min(mx, got))
        out.append((name, mx, got, crit))
    return sum(g for _, _, g, _ in out), out

def score_desc():
    return score(DESC['abertura'][0][0], desc_sents(), desc_heads(), True, DESC['cta'][0], FAQ, 'desc')
def score_item(c):
    return score(c['intro'][0][0], item_sents(c), [c['h1']], bool(c['bullets']), c['cta'][0], item_faq(c), 'item', c.get('serve'))

# ---------------------------------------------------------------- canais
GOOGLE = ('O LAAE (LabLAAE) é um laboratório de análise de água e efluentes com sede em Montes Claros (MG), em atividade desde 2003. '
          'Faz análises físico-químicas e microbiológicas de água para consumo humano e potável, águas subterrâneas e superficiais e água industrial de processo, '
          'e de efluentes industriais e sanitários, além de programas de monitoramento ambiental. '
          'A matriz tem serviços acreditados pela CGCRE do Inmetro, conforme os escopos dos certificados. '
          'A coleta é feita pela equipe do laboratório em Montes Claros, Jaíba, Janaúba, Januária, Diamantina, Curvelo, Salinas, Araçuaí e Pirapora. '
          'Atende indústrias, agronegócio, consultorias ambientais, hospitais, clínicas, hotéis e restaurantes.')
BIO = 'Laboratório de análise de água e efluentes. Serviços acreditados CGCRE/Inmetro. Coleta própria em nove cidades de Minas. Análises: (38) 98405-5391'
SOL_TITLE = 'LAAE — Análise de água e efluentes em Montes Claros/MG'
SOL_META = 'Laboratório de análise de água e efluentes em Montes Claros (MG), com serviços acreditados pela CGCRE/Inmetro e coleta própria em nove cidades.'
ENUM = ['físico-químicas', 'microbiológicas', 'consumo humano', 'potável', 'subterrâneas', 'superficiais', 'industrial de processo',
        'efluentes industriais e sanitários', 'monitoramento ambiental']
