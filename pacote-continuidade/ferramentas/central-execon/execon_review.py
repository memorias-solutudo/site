# -*- coding: utf-8 -*-
"""Fases 3 a 5 na aba Agentes: redação, pauta, auditoria e supervisão."""
import os, re, html
from execon_agt import AG
E = html.escape
D = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/dossie-grupo-execon/'

AGENTES_EXTRA = [
 AG(6, 'Redator · texto e perguntas', 'redator-3-0', 'Redação',
    'só o envelope, sem internet', '30-textos.md',
    [('205 palavras', 'ok'), ('8 perguntas', ''), ('5 publicadas após a auditoria', 'ok'), ('selo B', 'pa')],
    'Escreveu a descrição com fonte em cada frase e escolheu o <b>selo B</b>, porque nada foi confirmado pela empresa. A pergunta sobre os EUA responde sem "sim" e sem "não": só a frase travada.'),
 AG(7, 'Redator · catálogo como páginas', 'redator-3-0', 'Redação',
    'só o envelope, sem internet', '31-catalogo.md',
    [('12 fichas', ''), ('8 publicáveis', 'ok'), ('3 reservadas', 'pa'), ('1 fundida', 'no')],
    'Fundiu o acompanhamento no gerenciamento, que disputavam a mesma busca, e <b>reservou</b> o projeto arquitetônico e o estrutural até o CAU e o CREA. Criou duas páginas que o catálogo não tinha: condomínios do interior e reforma.'),
]
VERDICT_HTML = ''
AUDIT_HTML = ''

def _read(name):
    p = D + name
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''

AGENTES_EXTRA.append(
 AG(8, 'Planejador de pauta', 'planejador de pauta (§8)', 'Pauta',
    'só o envelope e as perguntas do público, sem internet', '32-pauta.md',
    [('6 editorias', ''), ('24 temas', 'ok'), ('6 datas', ''), ('13 descartadas', 'pa')],
    'Trocou o destaque de prova social por <b>"Onde atende"</b>, porque não há depoimento autorizado e destaque vazio é pior que ausência. O tema único são os condomínios do interior, na forma segura; a série é "Execon perto da sua obra".'))
AGENTES_EXTRA.append(
 AG(9, 'Auditor de indexação', 'auditor-indexacao', 'Auditoria',
    'o envelope, os textos, o catálogo e as páginas do site', '40-auditoria.md',
    [('189 textos varridos', ''), ('20 aprovados', 'ok'), ('9 reprovados', 'no'), ('14 ressalvas', 'pa')],
    'Reprovou com <b>9 correções de texto</b>, todas aplicadas: a frase dos EUA repetida no FAQ e em duas metas, os condomínios fora da forma segura, a lista de serviços diferente entre canais e "Execon" sozinho em 12 frases, que um homônimo poderia herdar.'))

AUDIT = [
 ('R1', 'EUA além da frase única: a pergunta do FAQ repetia a frase, e as metas de /perguntas e de /en citavam os EUA', 'pergunta sem resposta publicada até a pré-condição 4; metas reescritas'),
 ('R2', 'Enumeração divergente: a descrição listava "projetos e execução de obras", que o catálogo não tem', 'uma lista só, de 7 serviços, na mesma ordem em todos os canais'),
 ('R3', 'Condomínios fora da forma segura: a página listava cinco, e o title só o nome de família', 'só Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII, como o verificador travou'),
 ('R4', '"Execon" sozinho em 12 frases: há homônimos em outros estados', 'nome completo em toda frase que pode ser citada sozinha'),
 ('R5', 'Home, /sobre e a página da casa disputavam a mesma busca', 'titles novos; "casa de alto padrão" fica na página do serviço'),
 ('R6', 'Title de /pedir-orcamento com 61 caracteres', '53'),
 ('R7', 'Menu com rótulos: "Perguntas", "Guia", "Área atendida"', '"Dúvidas sobre obra", "Como construir", "Capital, interior e litoral"'),
 ('R8', 'Metas com jargão interno, como "editorias"', 'reescritas e terminando em fato'),
 ('R9', 'Faltavam a pergunta e o JSON-LD de cada página', 'as 17 páginas ganharam os dois'),
]
AUDIT_HTML = ('''    <div class="card">
      <span class="badge warn">Auditoria · reprovada com 9 correções, todas aplicadas</span>
      <h3>O que o auditor pegou, e como ficou</h3>
      <p class="sub">A auditoria não achou nenhuma frase sem fonte, nenhum barrado e nenhum campo em conflito no texto. O que ela reprovou foi <b>forma</b>: as travas do verificador escapando pelas bordas, em metas, títulos e perguntas. As correções foram aplicadas literalmente, com o texto que o próprio auditor escreveu, e registradas no dossiê.</p>
      <div class="scroller"><table><tr><th></th><th>Reprovado</th><th>Como ficou</th></tr>'''
  + ''.join(f'<tr><td><b>{a}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in AUDIT)
  + '''</table></div>
      <div class="note">Achado do orquestrador no retrabalho: a frase do pergolado do bloco de área de lazer tinha ficado fora da transcrição para a fonte única. Entrou. <b>Com a régua mais rígida</b>, que só conta unicidade em frase com fonte e sem pendência, a descrição mede 81, e o texto de hoje, 33.</div>
    </div>''')
VERDICT_HTML = '''    <div class="verdict pa"><b>Em andamento</b><span>Descoberta, verificação, redação, pauta e auditoria concluídas. O supervisor ainda está conferindo: o veredito final sai na próxima atualização.</span></div>'''

AGENTES_EXTRA.append(
 AG(10, 'Supervisor', 'supervisor-3-0', 'Supervisão',
    'todos os arquivos do dossiê e a central publicada', '50-supervisao.md',
    [('3 contraprovas', ''), ('6 contagens refeitas', 'ok'), ('fase 3 reprovada', 'no'), ('31 trocas', 'pa')],
    'Aprovou descoberta, verificação e auditoria, e reprovou a primeira passada da redação. A pauta ainda trazia "projetos e execução de obras", o destaque "Serviços" que o cliente vetou e a frase dos EUA com o nome curto. A nota da reforma estava inflada: o cadastro só tem a reforma comercial.'))

FASES = [
 ('1 · Descoberta', 'ok', 'aprovada', '4 ângulos no formato, 81 fatos com fonte, nenhum dado de Google Maps, lacuna declarada como lacuna. A contraprova do supervisor em "execonobras" confere.'),
 ('2 · Verificação', 'ok', 'aprovada', 'Adversarial de fato: 12 contraprovas, 29 barrados com motivo e 11 conflitos convertidos em omissão. As três buscas do supervisor não acharam contaminação.'),
 ('3 · Redação e pauta', 'pa', 'reprovada e corrigida', 'O texto publicado estava limpo frase a frase. A pauta, escrita em paralelo com a auditoria, repetia o que a auditoria tinha corrigido. As 31 trocas do supervisor foram aplicadas por código, literalmente.'),
 ('4 · Auditoria', 'ok', 'aprovada', 'Contagens medidas, das quais o supervisor recontou seis, e todas batem. Os quatro blocos do checklist têm evidência e cada reprovação vem com a regra citada.'),
]
PEND_SUP = [
 ('A página duplicada na Solutudo', 'ID 23064979: consolidar com redirecionamento ou alinhar. Pelo gate, nada vai ao ar antes.', 'Solutudo'),
 ('A frase dos Estados Unidos', 'confirmação escrita do cliente, válida até 31/12/2026. Sem ela, a frase sai; a descrição mede 81 com ou sem.', 'cliente'),
 ('CREA, CAU e atos técnicos', 'a consulta pública do CREA-SP 5070683298, o CAU, se houver, e quais atos a Execon assina com ART.', 'Solutudo + cliente'),
 ('Reforma residencial', 'hoje só fontes públicas; com a confirmação, a página de reforma sobe de 79 para 81.', 'CS'),
 ('Endereço, horário e o (14)', 'onde há atendimento presencial, o horário do WhatsApp e se o (14) tem WhatsApp.', 'cliente'),
 ('Ano, obras e condomínios', 'o ano de início, a lista de obras com data e foto, e a lista inteira de condomínios.', 'cliente'),
 ('O perfil do Instagram', 'confirmar que é da Execon e mandar prints antes de aplicar destaques, fixados e bio.', 'Solutudo + cliente'),
 ('O calendário', '17/10, Dia do Eletricista, está a 16 dias; e o aniversário de Pardinho.', 'parceiro'),
]
VERDICT_HTML = ('''    <div class="verdict ok"><b>Aprovado com ressalvas</b><span>Na primeira passada, o supervisor reprovou a redação e a pauta com 31 trocas literais, que ele mesmo testou numa cópia. Com elas aplicadas, o veredito dele é este, condicionado a duas coisas: resolver a página duplicada na Solutudo e ter a confirmação escrita do cliente para a frase dos EUA.</span></div>

    <div class="card">
      <span class="badge">Supervisão · fase a fase</span>
      <div class="scroller"><table><tr><th>Fase</th><th></th><th>O que o supervisor conferiu</th></tr>'''
  + ''.join(f'<tr><td><b>{E(a)}</b></td><td><span class="stt {k}">{E(l)}</span></td><td>{E(w)}</td></tr>' for a, k, l, w in FASES)
  + '''</table></div>
      <h4 style="margin-top:14px">Pendências humanas consolidadas pelo supervisor</h4>
      <div class="scroller"><table><tr><th>Pendência</th><th>O que é</th><th>Dono</th></tr>'''
  + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in PEND_SUP)
  + '''</table></div>
    </div>''')
