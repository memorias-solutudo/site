# -*- coding: utf-8 -*-
"""Aba Agentes: quem trabalhou, o que cada um achou, o que foi barrado e o veredito."""

def AG(n, nome, papel, fase, entrada, saida, kpis, achado):
    return dict(n=n, nome=nome, papel=papel, fase=fase, entrada=entrada, saida=saida, kpis=kpis, achado=achado)

AGENTES = [
 AG(1, 'Descobridor · site oficial', 'descobridor-empresa', 'Descoberta',
    'cadastro colado + o site do cadastro', '10-descoberta-site-oficial.md',
    [('19 buscas', ''), ('21 fatos', ''), ('6 publicáveis', 'ok'), ('3 domínios', 'pa')],
    'Achou um segundo site, <b>execonobras.com</b>, com o mesmo endereço e os mesmos telefones, e um terceiro domínio no e-mail. Os números não batem entre eles.'),
 AG(2, 'Descobridor · redes e diretórios', 'descobridor-empresa', 'Descoberta',
    'Instagram, Facebook, diretórios e a Solutudo', '10-descoberta-redes-diretorios.md',
    [('18 buscas', ''), ('33 fatos', ''), ('página duplicada', 'no')],
    'Provou pelos três telefones que a página <b>23064979</b> é da mesma empresa. É dela que vêm os condomínios: Ninho Verde e Riviera de Santa Cristina.'),
 AG(3, 'Descobridor · bases oficiais', 'descobridor-empresa', 'Descoberta',
    'CEP, CNPJ, CREA, CAU e registros dos EUA', '10-descoberta-bases-oficiais.md',
    [('18 buscas', ''), ('23 fatos', ''), ('setor regulado', 'pa')],
    'O bairro do CEP é <b>Bela Vista</b>, não Centro. O número do CREA tem formato de registro de profissional. Nenhum registro no CAU e nenhuma empresa americana ligada à Execon.'),
 AG(4, 'Descobridor · reputação e conteúdo', 'descobridor-empresa', 'Descoberta',
    'Reclame Aqui, processos, notícias e o que o público pergunta', '10-descoberta-reputacao-conteudo.md',
    [('17 buscas', ''), ('pauta do nicho', 'ok'), ('homônimos', 'pa')],
    'Separou os processos de uma "Execon … Ltda" do Rio Grande do Sul, que é outra empresa. Trouxe as perguntas reais de quem constrói em condomínio e de quem quer construir nos EUA.'),
 AG(5, 'Verificador adversarial', 'verificador-adversarial', 'Verificação',
    'os 4 arquivos de descoberta + o cadastro', '20-envelope.md',
    [('12 buscas', ''), ('23 publicáveis', 'ok'), ('29 barrados', 'no'), ('11 conflitos', 'pa')],
    'Tentou derrubar cada fato. Achou o endereço fiscal já mudado para a Paulista 2202 e travou a frase dos Estados Unidos: uma só, fora do título e da abertura.'),
]

BARRADOS = [
 ('Datas e números', '"12/05/1999" é o valor-padrão do formulário · "mais de 9 anos", escrito em 2022 · "10" e "12 anos", sem data · "desde 1995", que é de um homônimo de Minas · 70 casas, 20.000 m², 30.000 m² e "centenas de obras", que divergem entre si', 'B01–B05'),
 ('Terceiros', 'qualquer menção à Momentum, dona dos loteamentos: não há vínculo comprovado, e a loteadora é alvo de ação do Procon-SP', 'B06'),
 ('Estados Unidos', '"atua", "constrói" ou "atende nos EUA", estado, cidade e "licenciada": não há amarra pública', 'B07'),
 ('Setor regulado', 'o número do CREA no texto · "empresa registrada no CREA" · "equipe de arquitetos e engenheiros" · "projetos arquitetônicos" sem CAU', 'B08–B10'),
 ('Promessas', '"referência em São Paulo", "construtora de excelência", "a escolha ideal", "tecnologia de ponta", "entrega no prazo e no orçamento", "conformidade com NBR", "acompanhamento em tempo real", "soluções sustentáveis"', 'B11, B27, B28'),
 ('Endereço', '"vibrante Avenida Paulista" e qualquer rua, número ou bairro no texto · "Centro" e "Consolação", que são bairros errados · o endereço fiscal', 'B12–B15'),
 ('Dados pessoais', 'titular do CNPJ, patrocinador, campo "Nome fantasia", e-mails nominais', 'B16'),
 ('Homônimos', 'processos de uma "Execon … Ltda" no Rio Grande do Sul · @execon.eng de Fortaleza · Execon de Florianópolis, Londrina, Patos de Minas · empresas da Romênia, Dinamarca, Polônia e Argentina', 'B17–B20'),
 ('Reputação e horário', '"sem reclamações", porque não achar a página não é prova · a nota 5,0 da outra página · "WhatsApp sempre disponível" e o horário de 8h às 20h todos os dias', 'B21–B25'),
 ('Nome', '"Grupo" no sentido de grupo de empresas: é empresário individual', 'B26'),
]

def render(extra_agents, verdict_html, audit_html):
    ags = AGENTES + extra_agents
    cards = ''
    for a in ags:
        k = ''.join(f'<span class="{c}">{t}</span>' for t, c in a['kpis'])
        cards += f'''          <div class="ag">
            <div class="ag-h"><span class="ag-n">{a["n"]}</span><span class="ag-t">{a["nome"]}<small>{a["fase"]} · <code>{a["papel"]}</code></small></span></div>
            <p><b>Recebeu:</b> {a["entrada"]}<br><b>Entregou:</b> <code>{a["saida"]}</code></p>
            <div class="ag-k">{k}</div>
            <p>{a["achado"]}</p>
          </div>
'''
    bar = ''.join(f'<tr><td><b>{g}</b></td><td>{w}</td><td><code>{i}</code></td></tr>' for g, w, i in BARRADOS)
    return f'''  <section id="p-agt" class="panel">

    <div class="sec first">
      <span class="eyebrow">Curadoria · {len(ags)} execuções de agentes</span>
      <h2>Quem trabalhou neste conteúdo, e o que cada um derrubou</h2>
      <p class="secsub">É o pipeline da Descrição 3.0, com cinco papéis e uma regra que atravessa todos: <b>ninguém assina o próprio trabalho</b>. Quem descobre não verifica, e quem escreve não usa a internet. Assim, nenhum fato que o verificador não aprovou chega ao texto. Quem audita mede em código, e o supervisor refaz buscas por amostragem para conferir os outros.</p>
      <div class="phase" aria-label="Fases"><span>1 · Descoberta, em 4 ângulos</span><i>→</i><span>2 · Verificação adversarial</span><i>→</i><span>3 · Redação e pauta, sem internet</span><i>→</i><span>4 · Auditoria de indexação</span><i>→</i><span>5 · Supervisão</span></div>
    </div>

    {verdict_html}

    <div class="card">
      <span class="badge">As execuções</span>
      <h3>O que cada agente recebeu, entregou e achou</h3>
      <div class="ag-grid">
{cards}      </div>
      <div class="note">Todo fato carrega fonte, confiança e se é publicável ou interno. Os arquivos ficam no dossiê da empresa, e o envelope de fatos é a única fonte que os redatores podem ler.</div>
    </div>

    <div class="card" style="border-color:rgba(196,43,34,.3)">
      <span class="badge" style="background:#FFE4E0;color:#A3200F">O que o verificador barrou · 29 itens</span>
      <h3>O material que prova o valor da curadoria</h3>
      <p class="sub">Tudo isto estava publicado ou disponível em algum canal da empresa, e sairia no texto novo se ninguém conferisse.</p>
      <div class="scroller"><table><tr><th>Grupo</th><th>O que caiu</th><th>Itens</th></tr>{bar}</table></div>
    </div>

    {audit_html}

  </section>'''
