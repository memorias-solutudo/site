# -*- coding: utf-8 -*-
"""Aba Parceiro da central da Execon — sai do envelope (20-envelope.md) e do cadastro colado."""

def stt(k, lab): return f'<span class="stt {k}">{lab}</span>'

FONTES = [
 ('Cadastro Solutudo', 'getData?id=23008544, colado na conversa em 30/09', 'ok', 'colado', 'Base de tudo, íntegra: descrição, 9 produtos, 63 fotos, contatos, horário e pesquisa do contrato'),
 ('Prévia do Solusite', 'previa.solusite.com.br/site/grupo_execon', 'no', 'não acessado', '<b>Não abri a prévia.</b> O proxy desta sessão bloqueia o domínio. O "Solusite atual" desta central foi <b>reconstituído a partir do cadastro</b>, que é de onde o Solusite puxa o conteúdo: o banner, o logotipo, a descrição, os produtos e as fotos. Layout, menu e ordem dos blocos não foram vistos'),
 ('obrasexecon.com.br', 'o site do cadastro', 'no', 'não acessado', 'Só trechos de busca. O título indexado cita "Ninho Verde II Eco Residence/SP"'),
 ('execonobras.com', 'fora do cadastro', 'no', 'não acessado', 'Um segundo site com o mesmo endereço e os mesmos telefones, achado pelos agentes. Fala em "médio e alto padrão", 12 anos e 30.000 m²'),
 ('execoneng.com.br', 'domínio do e-mail', 'no', 'não acessado', 'Erro de DNS nesta sessão. Não concluir que está fora do ar'),
 ('Instagram /execonengconstrucao/', 'declarado no cadastro', 'no', 'não acessado', '<b>Não vi o perfil, e ele nem aparece nos buscadores.</b> Os destaques, os fixados e a bio da aba Conteúdo são recomendação a partir do cadastro'),
 ('Facebook /execonengconstrucao/', 'declarado no cadastro', 'pa', 'parcial', 'Só o trecho de busca: "Projetos, Construção e Reforma"'),
 ('Segunda página na Solutudo', 'ID 23064979, "… CREA-SP 5070683298 em Riviera de Santa Cristina XIII"', 'pa', 'parcial', 'Só trechos de busca. Tem os mesmos três telefones e o mesmo e-mail: é a mesma empresa, com outra página'),
 ('Bases oficiais', 'CREA-SP, CAU, Receita, Correios, Sunbiz', 'no', 'não acessado', 'Consulta direta bloqueada. O que se sabe veio de espelhos lidos por trecho: bairro do CEP, formato do número do CREA, abertura do CNPJ'),
 ('Imagens do cadastro', '63 fotos + banner, logotipo e capas', 'pa', 'parcial', 'Abri o banner e o logotipo. As 63 fotos do álbum não foram abertas; a conclusão de que nenhuma tem legenda útil vem do campo de legenda'),
 ('Perfil do Google', 'link no cadastro', 'pa', 'fora do escopo', 'Não consultado por regra do projeto: dado de Google Maps e Places não entra'),
]

TIMELINE = [
 ('16/09/2022', 'A página é criada na Solutudo', 'O ID do cadastro carrega a data.'),
 ('13/10/2022', 'Entram a descrição, os 9 produtos e as primeiras 30 fotos', 'É daqui o "mais de 9 anos", o "sonho da casa própria" e o texto que passou pelo tradutor.'),
 ('27/03/2024', 'Sete imagens "[Solusite] Outras"', 'Primeiro sinal de site. O atributo Solusite continua false até hoje.'),
 ('28/09/2026', 'Banner, logotipo e favicon do Solusite', 'O banner diz: <i>"Construção de casas de alto padrão e projetos completos de gestão de obras"</i> e <i>"…em São Paulo, SP e com atual expansão no EUA"</i>.'),
 ('29/09/2026', '33 fotos novas e as imagens dos 9 produtos trocadas', 'O time está montando o Solusite agora. As legendas das fotos novas dizem só "Grupo Execon".'),
]

TRAD = [
 ('547870 · Acompanhamento de Obra', '"atividades no <b>canto de obras</b>"', 'canteiro de obras'),
 ('547870 · Acompanhamento de Obra', '"<b>Gerenciamento de Custódia</b>: controle de orçamento"', 'gerenciamento de custos'),
 ('547870 · Acompanhamento de Obra', '"<b>Controle rigorosamente dos prazos</b>"', 'controle rigoroso dos prazos'),
 ('547871 · Projeto de Construção', '"em conformidade com o <b>projeto atualizado</b>"', 'projeto aprovado'),
 ('547871 · Projeto de Construção', '"obtenção de todas as <b>licenças permitidas</b>"', 'licenças necessárias'),
 ('547876 · Projeto Comercial', '"execução das <b>instalações possíveis</b>"', 'instalações necessárias'),
 ('547879 · Gerenciamento de Obras', '"que seu projeto <b>seja contínuo com competência</b>"', 'seja conduzido com competência'),
 ('547883 · Elétrica em Geral', '"<b>conectores, interruptores, tomadas e interruptores</b>"', 'a mesma palavra duas vezes na lista'),
 ('547874 · Projetos Arquitetônicos', '"cada <b>projeto atualizado</b>"', 'projeto aprovado'),
]

NUMEROS = [
 ('Tempo de atuação', '"mais de 9 anos"', 'texto de 13/10/2022, com 4 anos de atraso', '"mais de 10 anos" e "12 anos"', 'CNPJ aberto em 2020; 12/05/1999 é o valor-padrão do formulário'),
 ('Obras', '"70 residências de alto padrão"', '', '"centenas de obras concluídas"', ''),
 ('Área construída', '"mais de 20.000 m²"', '', '"30.000 m²"', ''),
 ('Posicionamento', '"alto padrão"', 'banner de 28/09 e pedido da Solutudo', '"médio e alto padrão"', 'o segundo site e a segunda página'),
]

CORRECOES = [
 ('Campo "Nome fantasia"', 'nome de uma pessoa física, o mesmo do patrocinador', '"Execon Engenharia e Construção"', 'Solutudo'),
 ('Fundação', '12/05/1999, o valor-padrão do formulário', 'apagar; preencher com o ano que o cliente confirmar', 'Solutudo + cliente'),
 ('WhatsApp 2', '"(149) 9120-9697", formato inválido', '(14) 99120-9697, se o cliente confirmar que tem WhatsApp', 'cliente'),
 ('Bairro', '"Centro"', 'Bela Vista, que é o bairro do CEP 01310-000, se o endereço for mantido', 'Solutudo'),
 ('Endereço exibido', 'Paulista 302–306, com "Exibir endereço" ligado', 'confirmar se há atendimento presencial; se não houver, desligar a exibição e usar área de atendimento', 'cliente'),
 ('Página duplicada', 'ID 23064979, com os mesmos telefones e e-mail', 'consolidar nesta página com redirecionamento, ou manter com texto coerente; tirar "CREA-SP nº" do título', 'Solutudo'),
 ('Categoria Arquitetura', 'ativa, sem registro no CAU encontrado', 'em revisão até o cliente mostrar arquiteto(a) com CAU, próprio ou parceiro', 'cliente'),
 ('Atributo Solusite', 'false, com banner, logotipo e prévia em produção', 'acertar quando o site entrar no ar', 'Solutudo'),
 ('Texto dos 6 produtos', 'markup do tradutor automático e erros de tradução', 'substituir pelas fichas da aba Destaque', 'Solutudo'),
 ('Legendas das 63 fotos', '"Execon Engenharia e Construção" ou "Grupo Execon" em todas', 'serviço, condomínio ou bairro e ano de cada obra', 'cliente'),
 ('Banner do Solusite', '"expansão no EUA"', '"nos Estados Unidos", e só depois de o cliente confirmar por escrito', 'Solutudo'),
 ('Horário', 'todos os dias, das 8h às 20h, inclusive feriados', 'o horário real de resposta no WhatsApp; diretórios dizem seg–sex 9h–18h e sáb 9h–13h', 'cliente'),
 ('Palavras-chave da empresa', 'vazias', 'preencher com os serviços e os condomínios atendidos', 'Solutudo'),
]

PERGUNTAS = [
 ('Em que ano a Execon começou a atuar?', 'Sem o ano, o texto não diz "desde". Se a contagem inclui a trajetória do responsável técnico antes do CNPJ de 2020, a frase fala dele, não da empresa.'),
 ('Quantas casas foram entregues, e quantos m², com data?', 'Os canais da própria empresa dão três números diferentes. Com data e método, o número volta ao texto.'),
 ('Qual é o endereço de hoje, e ele recebe cliente?', 'Os dois endereços da Paulista ficam em prédios de escritórios compartilhados. Sem atendimento presencial, o certo é mostrar a área atendida, e não o endereço.'),
 ('Qual é o site oficial?', 'São três domínios, e o Solusite vai ser o quarto. Os outros devem redirecionar para um só.'),
 ('Estados Unidos: onde, com que empresa e com que licença?', 'Estado e cidade, a empresa americana, a licença estadual de construtor, o tipo de serviço e desde quando. Sem isso, o texto diz só "em expansão para os Estados Unidos".'),
 ('Quem é o responsável técnico, e há arquiteto com CAU?', 'O CREA 5070683298 tem formato de registro de profissional. Sem CAU, "projeto arquitetônico" não pode ser anunciado.'),
 ('Como funciona a contratação?', 'Administração de obra ou preço fechado, se há visita técnica e como sai o orçamento. É a pergunta que todo cliente de alto padrão faz, e hoje não há resposta.'),
 ('Como o cliente acompanha a obra?', 'Os produtos falam em relatórios periódicos. Com a frequência e o formato, isso vira o diferencial do texto.'),
 ('A Execon ainda faz obra de médio padrão?', 'O pedido é destacar o alto padrão, mas dois canais dizem "médio e alto". A resposta decide se os outros canais mudam.'),
 ('Qual é o horário de resposta no WhatsApp?', 'O cadastro diz todos os dias, das 8h às 20h. Os diretórios dizem outra coisa.'),
 ('A Execon faz reforma de casa, além da comercial?', 'O cadastro só tem a reforma comercial; a residencial vem de fontes públicas. Com a confirmação, a página de reforma sobe de 79 para 81.'),
 ('O perfil /execonengconstrucao/ é da Execon e está ativo?', 'Ele não aparece em nenhum buscador. Destaques, fixados e bio da aba Conteúdo só valem depois de confirmar o perfil: mande prints da bio e dos destaques.'),
]

def render(desc_before, desc_after, n_items, n_fotos=63):
    fontes = ''.join(f'<tr><td><b>{a}</b><br><small>{b}</small></td><td>{stt(k, lab)}</td><td>{w}</td></tr>' for a, b, k, lab, w in FONTES)
    tl = ''.join(f'<tr><td><b>{d}</b></td><td><b>{t}</b><br><small>{w}</small></td></tr>' for d, t, w in TIMELINE)
    trad = ''.join(f'<tr><td>{p}</td><td>{a}</td><td>{b}</td></tr>' for p, a, b in TRAD)
    nums = ''.join(f'<tr><td><b>{a}</b></td><td>{b}<br><small>{c}</small></td><td>{d}<br><small>{e}</small></td></tr>' for a, b, c, d, e in NUMEROS)
    corr = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in CORRECOES)
    perg = ''.join(f'<li><b>{q}</b> {w}</li>' for q, w in PERGUNTAS)
    return f'''  <section id="p-parc" class="panel on">

    <div class="sec first">
      <span class="eyebrow">Como esta central funciona</span>
      <h2>O banner de 28/09 já conta a Execon de hoje. O texto da página ainda é o de 2022.</h2>
      <p class="secsub">Esta é a primeira central que nasce do <b>processo da API</b>: o cadastro colado na conversa, dez execuções de agentes na curadoria e a central publicada. O pedido era melhorar a descrição, <b>incluir a expansão para os Estados Unidos</b> e o <b>foco em alto padrão</b>, comparar o Solusite atual com o proposto e montar as editorias.</p>
      <p class="secsub">A curadoria mudou o tamanho da resposta. O cadastro diz muita coisa, e os agentes derrubaram <b>29 afirmações</b> e acharam <b>11 conflitos</b>: anos de atuação, números de obras, endereço, registro profissional e os próprios Estados Unidos. O texto novo é mais curto e diz menos, mas <b>tudo o que ele diz tem fonte</b>. O que falta está na lista de perguntas ao cliente, no fim desta aba.</p>
    </div>

    <div class="alert">
      <span class="atop"><i aria-hidden="true">!</i> Declaração de acesso às fontes · leia antes de tudo</span>
      <h3>Não consegui abrir a prévia do Solusite, nenhum dos três sites da empresa e nem o Instagram</h3>
      <p><b>Receber um link não é ter lido o link.</b> O proxy desta sessão bloqueia <code>previa.solusite.com.br</code>, <code>obrasexecon.com.br</code>, <code>solutudo.com.br</code> e <code>api.solutudo.com</code> (403 no CONNECT). Tudo o que veio de fora chegou por <b>trecho de resultado de busca</b>, e por isso a confiança máxima de qualquer fato externo é média. O cadastro, que é a base, chegou colado e inteiro.</p>
      <div class="scroller"><table>
        <tr><th>Fonte</th><th>Status</th><th>O que isso muda</th></tr>
        {fontes}
      </table></div>
    </div>

    <div class="card">
      <span class="badge">Os números da central</span>
      <div class="chips" style="margin-top:6px">
        <span class="chip lav">Descrição {desc_before} → {desc_after}</span>
        <span class="chip lav">Catálogo: 9 produtos → {n_items} páginas publicáveis</span>
        <span class="chip">{len(CORRECOES)} correções de cadastro</span>
        <span class="chip">{len(PERGUNTAS)} perguntas ao cliente</span>
        <span class="chip">{n_fotos} fotos sem legenda útil</span>
        <span class="chip peach">29 afirmações barradas · 11 conflitos</span>
      </div>
    </div>

    <div class="card" style="border-color:rgba(196,43,34,.3);background:linear-gradient(180deg,#FFF6F4 0%,var(--white) 60%)">
      <span class="badge" style="background:#FFE4E0;color:#A3200F">Achado principal · duas histórias no mesmo cadastro</span>
      <h3>O cadastro tem uma camada de 2022 e outra desta semana, e elas contam empresas diferentes</h3>
      <p class="sub">Os IDs dos arquivos da Solutudo carregam a data em que cada coisa foi criada. Lidos em ordem, mostram por que o texto não combina com o pedido: <b>ele foi escrito quatro anos antes do banner</b>. O texto fala em "sonho da casa própria", não cita os Estados Unidos e diz "9 anos". O banner, montado em 28/09, fala em "casa de alto padrão" e em "expansão no EUA".</p>
      <div class="scroller"><table><tr><th>Data</th><th>O que entrou</th></tr>{tl}</table></div>
      <div class="note"><b>Consequência:</b> o Solusite em montagem vai puxar o texto de 2022 para dentro de um site de 2026. Trocar a descrição e os produtos <b>antes</b> de o site ir ao ar evita publicar a versão velha em mais um domínio.</div>
    </div>

    <div class="card">
      <span class="badge warn">Achado recorrente · segundo parceiro com o mesmo defeito</span>
      <h3>Seis dos nove produtos passaram pelo tradutor automático e voltaram quebrados</h3>
      <p class="sub">Os produtos 547870, 547871, 547874, 547876, 547879 e 547883 têm o texto inteiro envolvido em <code>&lt;font dir="auto" style="vertical-align: inherit;"&gt;</code>, o código que o tradutor do navegador injeta na página. Alguém traduziu, copiou da tela e colou de volta. <b>No LAAE foram três de quatro produtos.</b> Dois parceiros em seis é padrão, não acidente: o editor de produto da Solutudo devia remover esse código ao salvar.</p>
      <div class="scroller"><table><tr><th>Produto</th><th>Publicado hoje</th><th>O que era para dizer</th></tr>{trad}</table></div>
    </div>

    <div class="card">
      <span class="badge">Os números não fecham em lugar nenhum</span>
      <h3>Anos, obras e metros quadrados: cada canal da empresa diz uma coisa</h3>
      <div class="scroller"><table><tr><th>Dado</th><th>Página Solutudo e obrasexecon.com.br</th><th>Segundo site e segunda página</th></tr>{nums}</table></div>
      <div class="note"><b>Decisão da curadoria:</b> nenhum ano e nenhum número entram no texto até o cliente confirmar, com data e método. É o que a regra manda quando o conflito é da própria empresa: omitir e perguntar, nunca escolher um lado. O "alto padrão" entra, porque está em todos os canais, mas sem "exclusivamente" e sem "referência".</div>
    </div>

    <div class="grid2">
      <div class="card" style="margin-top:0">
        <span class="badge warn">Setor regulado</span>
        <h3>O registro profissional trava três produtos</h3>
        <p class="sub">O número <b>CREA-SP 5070683298</b> aparece no título da segunda página da empresa na Solutudo. O formato é de registro de <b>profissional</b>, não de empresa, e a situação não pôde ser consultada. Nenhum registro no <b>CAU</b> foi encontrado, apesar da categoria Arquitetura.</p>
        <p class="sub">Por isso, <b>"projeto arquitetônico" não pode ser anunciado</b> até o cliente mostrar arquiteto com CAU, próprio ou parceiro. Projeto estrutural, licenciamento e aprovação na prefeitura esperam a confirmação do CREA. O texto novo não fala em projeto: diz construção e gestão de obras, que o cadastro sustenta sem registro a conferir.</p>
      </div>
      <div class="card" style="margin-top:0">
        <span class="badge warn">Onde a Execon está</span>
        <h3>Três endereços, dois em prédios de escritórios compartilhados</h3>
        <p class="sub">O cadastro diz Paulista 302–306, com o bairro errado: é Bela Vista, não Centro. A segunda página diz Paulista 2202, e o CNPJ já teve endereço na Av. Jardim Japão. Os dois endereços da Paulista ficam em prédios que oferecem escritório compartilhado.</p>
        <p class="sub">O texto novo diz só <b>"São Paulo (SP)"</b> e a área atendida: capital e Grande São Paulo, interior e litoral paulista, e condomínios do interior como <b>Ninho Verde II</b> (Pardinho) e <b>Riviera de Santa Cristina XIII</b>. A Momentum, dona dos loteamentos, não é citada: não há vínculo comprovado.</p>
      </div>
    </div>

    <div class="card" style="border-color:rgba(11,127,171,.3)">
      <span class="badge" style="background:var(--tint-cyan);color:#065F73">Estados Unidos · o que dá para dizer hoje</span>
      <h3>Uma frase: "em expansão para os Estados Unidos". Nada além, por enquanto.</h3>
      <p class="sub">Os quatro agentes de descoberta e o verificador procuraram em sites, redes, diretórios e registros estaduais americanos, e <b>nenhuma fonte pública liga a Execon aos Estados Unidos</b>. A única fonte é a da própria Solutudo: o pedido de hoje e o banner montado dois dias antes. Isso basta para uma frase honesta, mas não para "construímos nos EUA".</p>
      <p class="sub">A frase fica fora da abertura, do title e da meta, que são as partes que o buscador mostra. Ela sobe de nível quando o cliente disser, por escrito: <b>o estado e a cidade, a empresa americana, a licença estadual de construtor, o tipo de serviço</b> (obra própria, gestão para brasileiros ou parceria com construtor local) <b>e desde quando</b>. A página em inglês do Solusite está pronta para receber isso (aba Solusite).</p>
    </div>

    <div class="card">
      <span class="badge">Correções de cadastro</span>
      <h3>{len(CORRECOES)} tarefas antes de publicar qualquer texto</h3>
      <div class="scroller"><table><tr><th>Campo</th><th>Hoje</th><th>Correção</th><th>Dono</th></tr>{corr}</table></div>
    </div>

    <div class="card" style="border-color:rgba(167,1,253,.28)">
      <span class="badge">Perguntas para o cliente · uma conversa resolve</span>
      <h3>{len(PERGUNTAS)} respostas que destravam o texto, o catálogo e o site</h3>
      <ul class="clean">{perg}</ul>
      <div class="note">Todas estão também nas abas onde fazem falta. Com as quatro primeiras respondidas, a descrição ganha o "desde", o número de obras e o endereço, e a nota sobe sem mudar uma palavra do resto.</div>
    </div>

  </section>'''
