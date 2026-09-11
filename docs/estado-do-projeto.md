# Estado do projeto — fim da etapa 1

> **Para que serve este documento.** É o ponto de partida da etapa 2. Ao abrir a
> próxima sessão, peça para ler este arquivo: ele devolve o contexto inteiro sem
> precisar colar nada no chat.
>
> Última atualização: 28/08/2026 · Fecha a etapa 1.

---

## 1. Ambiente

O trabalho da etapa 1 aconteceu no repositório **`memorias-solutudo/soluintel`**,
branch **`claude/intelligent-gates-av5c7o`**, publicando por GitHub Pages.
(Este resumo está guardado em `memorias-solutudo/site` apenas como documento de
passagem entre etapas — o código e os artefatos continuam no `soluintel`.)

### Limites de rede confirmados

Três limites foram testados na prática e valem ser carregados para a próxima
sessão, para não se gastar tempo redescobrindo:

| Limite | Sintoma | Contorno usado |
|---|---|---|
| **`api.solutudo.com` está bloqueada** | 403 no CONNECT | Todo payload foi colado manualmente no chat |
| **`github.io` está bloqueada para leitura** | Publica, mas não abre o que foi publicado | Validação feita antes de publicar, não depois |
| **CDN de imagens trava o headless** | Screenshot pendura | `imagesEnabled=false` |

---

## 2. O que existe hoje

### 2.1 Infraestrutura de agentes

- **5 agentes** em `.claude/agents/`, mais o orquestrador **`empresa-3-0`**.
- **8 execuções por empresa.**
- A **régua de score de 6 dimensões (0–100)** governa toda comparação
  "como está × como deveria". É ela que produz os números de antes/depois da
  tabela de parceiros.

### 2.2 Documentação

**Sete documentos** em `docs/`. Os dois que mais mudaram na etapa 1:

- **`editorias-conteudo.md`** — os 6 slots fixos de editoria.
- **`gestao-trafego-operacao.md`** — atenção: a **§7 tem precedência** sobre
  qualquer referência de mercado citada antes dela no mesmo documento. Em caso
  de conflito, vale a §7.

### 2.3 Artefatos publicados

- **`sobre-empresa-new-rock`** — o artefato principal, 5 abas, incluindo a aba
  de Agentes.
- **Hub de parceiros** — com 3 centrais.
- **Proposta da EA3** — 3 abas.

### 2.4 Parceiros trabalhados

| Parceiro | Score (antes → depois) | Catálogo | Abas |
|---|---|---|---|
| Pizza Frita Semião | 40 → 92 | 6 itens | 6 |
| Porto Certo Consórcio (segmento regulado) | 44 → 91 | 7 itens | 6 |
| **EA3 Engenharia** | **31 → 92** | **29 itens** | **7** |

### 2.5 Cobertura da EA3 — corrige o roteiro

**O roteiro hoje diz “Avaré e região”. Isso cobre menos da metade do que a
empresa atende e precisa ser corrigido na etapa 2.**

A EA3 atende **8 municípios**, distribuídos em **dois eixos que não se tocam**:

| Eixo | Municípios |
|---|---|
| Campinas–Sorocaba | Vinhedo, Indaiatuba, Boituva |
| Avaré | Avaré, Arandu, Itaí, Paranapanema, Águas de Santa Bárbara |

Dentro do eixo de Avaré, a presença é por **condomínio nomeado**, não por
cidade — são **5 condomínios Momentum**:

| Condomínio | Cidade |
|---|---|
| Riviera de Santa Cristina I | Arandu, SP |
| Riviera de Santa Cristina IV | Arandu, SP |
| Riviera de Santa Cristina II | Itaí, SP |
| Riviera de Santa Cristina XIII | Paranapanema, SP |
| Santa Bárbara Resort Residence | Águas de Santa Bárbara, SP |

Ou seja: quatro cidades de atuação declarada (Vinhedo, Indaiatuba, Boituva,
Avaré) mais quatro cidades alcançadas pelos condomínios (Arandu, Itaí,
Paranapanema, Águas de Santa Bárbara).

#### Por que isso muda a campanha, não só o texto

1. **“Avaré e região” apaga o eixo mais forte.** Vinhedo, Indaiatuba e Boituva
   ficam de fora — e estão em outro eixo econômico do estado, com ticket e
   perfil de obra diferentes dos condomínios.
2. **Não existe raio único.** São duas manchas separadas no mapa: raio a partir
   de Avaré não alcança Vinhedo, e raio a partir de Vinhedo não alcança nenhum
   dos condomínios. A segmentação de Google e Meta tem que ser **por lista de
   cidades**, ou dois conjuntos de campanha, nunca um raio só.
3. **Os 5 condomínios são nome próprio — e nome próprio é termo de busca.**
   Liga direto no achado 4.2: quem vai construir ali procura
   “Riviera de Santa Cristina”, não “engenheiro em Arandu”. Os nomes dos
   condomínios devem entrar como grupo de anúncio próprio, do mesmo jeito que
   as 43 buscas reais viraram os outros 5 grupos.

---

## 3. Gestão de Tráfego como produto

Deixou de ser serviço sob medida e passou a ter preço fechado.

| Item | Preço |
|---|---|
| Google | R$ 600 |
| Meta | R$ 800 |
| Os dois | R$ 1.200 |
| Plano de entrada | R$ 400 + R$ 400 |

**Setup é cortesia** em todos os planos.

Regras comerciais que acompanham o preço:

- **Taxa de 10%** acima do teto.
- **Gestão e mídia nunca são somadas** — são linhas separadas, sempre.
- **Contrato mínimo de 3 meses.**

---

## 4. Os três achados que valem além dos casos

Estes são os resultados que não ficam presos aos casos: valem como sistema,
para qualquer empresa da base.

### 4.1 A data 12/05/1999

**Aparece idêntica nos cinco parceiros** — segmentos diferentes, cidades
diferentes. É valor-padrão de formulário, não fato.

Isso deixou de ser coincidência e virou **achado de sistema**: vale medir
quantos dos **28 milhões de perfis** carregam essa data. Enquanto não for
medido, nenhum campo de data do cadastro deve ser tratado como dado real.

**Quarta ocorrência, na Blocok (§7) — e ela mostra o mecanismo.** A pergunta do
formulário é *“Em que ano a empresa foi fundada?”*, e o que ficou gravado é uma
**data completa**, não um ano. O campo é um seletor de data respondendo a uma
pergunta de ano, e o que sobra é o valor-padrão do seletor. Quatro em quatro
parceiros — a taxa na base inteira provavelmente é alta.

**Quinta ocorrência, no LAAE (§10) — e a primeira com o valor certo à vista.**
Até aqui dava para dizer que o campo estava errado, não qual era o valor certo.
No LAAE a empresa se contradiz dentro do próprio cadastro: o campo do contrato
diz `12/05/1999`, a descrição publicada diz **"Fundado em 2003, em Montes
Claros/MG"** e a transcrição da reunião confirma ("2003 o nascimento da
empresa"). Duas fontes independentes contra o valor-padrão. **Cinco em cinco.**

### 4.2 As palavras-chave particulares são o ativo mais subestimado do cadastro

Na EA3, **43 buscas reais viraram 5 grupos de anúncio sem uma única suposição**.
Entre elas, `eletrecista` — com erro de grafia — que é clique barato e que
concorrente nenhum disputa.

É exatamente o que uma agência leva **três meses de teste pago** para descobrir,
e que já está no cadastro, de graça, desde o primeiro dia.

### 4.3 O cadastro responde 13 das 35 perguntas de briefing de campanha

Essa é **a vantagem estrutural da Solutudo sobre agência**, e agora está
formalizada como sistema fixo, aplicável a qualquer segmento — não como
observação sobre um caso.

---

## 5. Pendências (6)

### Dependem do especialista

1. **Os 10% incidem sobre o excedente ou sobre o total?**
   Adotei **sobre o excedente**. Se a resposta for "sobre o total", os números
   das propostas já emitidas mudam.
2. **O que é a API do Dani.** Segue sem definição.

### Dependem de decisão sua

3. **Salvar ou não o prompt expandido de editorias** em
   `docs/editorias-conteudo.md`.
4. ~~**Remover ou não o branch do gatilho do `pages.yml`.**~~
   **Corrigido em 31/08/2026 — o diagnóstico da etapa 1 estava errado.**
   Não é "inofensivo até divergirem", e não é uma corrida: o gatilho do branch
   **nunca funcionou**. Ver §9.

### Registradas nos documentos do `soluintel`

5. e 6. Duas pendências de **CS** e **comercial**. Ficaram registradas nos
   documentos do repositório; o detalhe delas não foi transcrito neste resumo —
   consultar `docs/` do `soluintel` na etapa 2.

---

## 6. Como retomar na etapa 2

1. Ler este arquivo.
2. Abrir `docs/gestao-trafego-operacao.md` no `soluintel` — lembrando da
   precedência da §7.
3. Resolver as pendências 1 e 2 com o especialista antes de emitir nova
   proposta com preço.
4. Decidir 3 e 4 (são de uma linha cada).
5. Recuperar o conteúdo das pendências 5 e 6 nos documentos do `soluintel`.
6. **Corrigir o roteiro da EA3**, que hoje diz “Avaré e região”, usando a
   cobertura real da §2.5 — e refazer a segmentação geográfica em cima dela.
7. **Resolver a nota “Não pode utilizar IA” da Blocok (§7)** antes de gerar
   qualquer conteúdo para ela — e responder as três confirmações abertas:
   Itatinga, pedras ornamentais e o posicionamento em Sorocaba.

---

## 7. Blocok O Original — quarta empresa

> **Atualizado em 31/08/2026: a central foi produzida e publicada.**
> `artefatos/parceiros/blocok-o-original/` no `soluintel`, no mesmo formato das
> outras — 6 abas, descrição **13 → 91** (o maior salto da série), catálogo de 7
> itens e 24 temas. A nota interna abaixo **não foi revogada**: a central saiu
> por decisão explícita do responsável, e o alcance da restrição continua
> pendente de confirmação com o CS antes de qualquer texto ir aos canais do
> cliente. O diagnóstico que segue é o que orientou a produção.

### ⚠️ A nota interna “Não pode utilizar IA”

O cadastro carrega uma **anotação interna prioritária** (tag `Prioridade`,
`Nota prioritária: true`), criada em **10/08/2026 por João Pedro Cavassini**,
com o texto: **“Não pode utilizar IA”**.

Isso colide de frente com o pipeline `empresa-3-0`, cuja saída é justamente
conteúdo gerado. A restrição foi levantada duas vezes e o responsável decidiu
seguir — a central existe. **A pendência que sobra é de publicação, não de
produção:** nenhum texto da central deve ir para o perfil, o site ou as redes do
cliente até o alcance da nota estar esclarecido.

Precisa ser respondido antes de seguir: a restrição vale para **publicar
conteúdo gerado no perfil do cliente**, ou para **usar IA em qualquer etapa**,
inclusive análise interna? São coisas diferentes e mudam o que dá para entregar.

### 7.1 Ficha

| Campo | Valor |
|---|---|
| ID | 27112782 |
| Nome | Blocok O Original *(assina “Franquia Riviera”)* |
| Produto Solutudo | Força Digital Essencial |
| **Avaliação do perfil** | **13** — o mais baixo dos quatro parceiros |
| Funcionários | 1 – 5 |
| Patrocinador | Fábio *(telefone e e-mail do patrocinador em branco)* |
| Catálogo | 3 produtos cadastrados → **7 itens** na central |
| Categorias | 4 — Materiais para Construção *(padrão)*, Blocos de Cimento, Concretos, Tijolos Ecológicos |
| Palavras-chave particulares | **104** |

Para comparação: a EA3 partiu de 31 com 29 itens de catálogo. A Blocok parte de
**13 com 3 itens** — é o pior ponto de partida da série, e o de maior espaço.
A descrição fechou em **91**, ganho de 78 pontos.

A nota 13 não vinha de texto mal escrito. Vinha de **texto de franqueadora
publicado como se fosse da franquia**: sem território, sem contato e sem
operação. A primeira frase do texto publicado é escrita na voz de quem
*descobriu* o produto, não de quem o vende.

### Três decisões que a central tomou e valem como regra

1. **O Google vira empresa de área de atendimento, com endereço oculto.**
   Publicar o apartamento é contra a política do Google, expõe a casa do
   franqueado e ancora o perfil em Sorocaba — o mercado mais disputado e onde a
   franquia não tem vantagem.
2. **Nada de “desde 1999”** — a data do contrato é valor-padrão (§4.1).
3. **Nada de “todos os dias”** — horário de sete dias mais feriado, para
   fornecedor de material de construção, é valor não verificado. A central
   publica só a faixa de horas.

### Uma contradição técnica que trava conteúdo

O produto 698701 chama de **“alta resistência estrutural”** um bloco que o
próprio texto descreve como **“de vedação”**. Bloco de vedação não sustenta
carga. Enquanto a franqueadora não confirmar se existe uma linha estrutural
separada, nenhuma afirmação sobre carga entra em canal nenhum — e duas perguntas
do FAQ ficam declaradamente sem resposta, por falta da medida nominal do bloco.

### 7.2 Cobertura

| Eixo | Municípios |
|---|---|
| Sorocaba | Sorocaba |
| Interior (Botucatu–Avaré) | Pardinho, Avaré, Paranapanema |

| Condomínio Momentum | Cidade |
|---|---|
| Ninho Verde II Eco Residence | Pardinho, SP |
| Riviera de Santa Cristina XIII | Paranapanema, SP |

**Riviera de Santa Cristina XIII é o mesmo condomínio da EA3.** Duas empresas da
carteira atendendo o mesmo condomínio, em ramos complementares (bloco e
engenharia) — vale checar se isso é oportunidade de venda casada ou conflito de
exclusividade de franquia.

### 7.3 O cadastro está posicionado na cidade errada

Este é o achado central da empresa. O cadastro inteiro aponta para **Sorocaba**:

- **Cidade na página de busca:** Sorocaba
- **Endereço:** Avenida Ipanema, 5381 — complemento **“BLOCO B; APT 14”**,
  Jardim Planalto, Sorocaba. É **endereço residencial**, apartamento.
- **Descrição:** cita Sorocaba três vezes (“Construção Inteligente em
  Sorocaba”), e o resto vira “toda a região”.
- **Banners do Solusite** (desktop e mobile): “transformar sua obra em sorocaba”.

Mas a identidade da empresa aponta para o **condomínio**:

- Nome da franquia: **“Blocok O Original Franquia Riviera”**
- E-mail: **blocok.riviera@gmail.com**
- Instagram: **@blocok.riviera**
- Os **3 produtos** descrevem, todos, **Ninho Verde II Eco Residence**

Ou seja: o endereço é onde o franqueado mora, e o cadastro tomou isso como o
mercado. Sorocaba é o **mais disputado dos quatro** — cidade grande, cheia de
depósito de material de construção — e é exatamente onde a Blocok não tem
vantagem nenhuma. Nos condomínios ela tem presença de fato.

> **Padrão que se repete.** Na EA3 o texto dizia “Avaré e região” e apagava o
> eixo Campinas–Sorocaba (§2.5). Na Blocok o cadastro diz “Sorocaba” e apaga o
> eixo do interior. Nos dois casos o material nomeia **um eixo só, e é o eixo
> errado** — o que tem menos vantagem competitiva. Vale virar item de checagem
> fixo da régua: *a cidade declarada é onde a empresa vende, ou onde o dono
> mora?*

### 7.4 O que as 104 palavras-chave particulares entregam

| Grupo | Termos | O que fazer |
|---|---|---|
| Nome de condomínio | **11** | Grupo de anúncio próprio — é o ativo de maior intenção |
| Cidade nomeada | 8 | Confirmam Pardinho, Paranapanema e Avaré na prática |
| **Pedras ornamentais** | **10** | Linha inteira **sem nenhum produto no catálogo** |
| Marca de terceiro | 6 | Revisar política de marca antes de subir |
| Pergunta (intenção informativa) | 9 | Pauta de conteúdo, não anúncio |
| Superlativo (“top…”, “melhor…”) | 11 | Suspeitos — ver 7.5 |

**Os 11 termos de condomínio** repetem o achado 4.2 num segundo segmento:
`onde comprar blocos de cimento no ninho verde ii eco residence`,
`blocos de concreto riviera de santa cristina`,
`contratar fornecimento de cimento ninho verde`. Quem constrói ali procura pelo
nome do condomínio — não por “bloco de concreto em Pardinho”.

**Itatinga aparece nas palavras-chave e não na sua lista.** Dois termos:
`loja de blocos em itatinga sp` e `loja de pedras ornamentais itatinga sp`.
Ou é cidade atendida que ficou de fora da lista, ou é termo que não deveria
estar no cadastro. **Confirmar.**

**Pedras ornamentais é o buraco comercial.** Dez termos pedindo pedra ornamental,
decorativa e de revestimento — e os três produtos cadastrados são todos bloco e
sistema construtivo. Ou a empresa vende pedra e não cadastrou, ou não vende e os
termos vão queimar verba. **Confirmar antes de subir campanha.**

**Intenção trocada:** `franquia blocok em sao paulo interior` não é cliente
procurando bloco — é alguém querendo **comprar a franquia**. Outra campanha,
outra landing, outro funil. Não pode ficar no mesmo grupo.

**As 9 perguntas são pauta, não anúncio:** `quanto custa um bloco de cimento
39x19x14`, `quantos blocos de cimento para construir um quarto`, `como assentar
blocos de concreto corretamente`, `blocos de concreto sao melhores que tijolos`,
`evitar infiltracao em muros de blocos de concreto`. Alimentam direto os 6 slots
fixos de `editorias-conteudo.md`.

### 7.5 A lista mistura dois registros — triar antes de gastar

Diferente da EA3, onde as 43 buscas eram todas reais, aqui convivem dois tipos:

- **Parecem busca real:** `quanto custa um bloco de cimento 39x19x14` (medida
  padrão de bloco), `blocos concrelagos`, `blocos tupan`, os termos de
  condomínio, os de cidade.
- **Parecem redigidos:** `top empresa de blocos de cimento`, `top fornecedor de
  blocos de cimento em sp`, `melhor fabrica de blocos em sp`, `empresa
  referencia em blocos de cimento`, `top pedras ornamentais interior paulista`.
  Ninguém digita “top fornecedor de”.

São **11 termos** nesse segundo grupo. E isso tem uma implicação incômoda: se
parte da lista foi redigida por IA, **já existe conteúdo gerado no cadastro de
uma empresa marcada como “não pode utilizar IA”**. Vale verificar a origem antes
de qualquer coisa.

### 7.6 Higiene do cadastro — o que derruba a nota para 13

| Campo | Estado |
|---|---|
| `Palavras-chave` | `[""]` — **vazia** |
| `Palavras-chave estendidas` | `[""]` — **vazia** |
| Nome fantasia | vazio |
| Vídeo | vazio |
| Campo `Logo` | `null` — **embora exista logo em Fotos** |
| Preço dos 3 produtos | `null` nos três |
| Menu / Ofertas / Eventos | todos `false` |
| Horário | 08:00–18:00 **sete dias por semana, feriado incluído** |
| Ano de fundação | `12/05/1999` — ver §4.1 |

As duas listas de palavras-chave vazias, com **104 particulares preenchidas**, é
a contradição mais fácil de corrigir. O `Logo: null` com logo presente em Fotos
é provável falha de vínculo, não ausência de arquivo. E horário comercial de
domingo e feriado, para fornecedor de material de construção, é quase certamente
valor não verificado — mesma família de problema da data de fundação.

---

## 8. Seletor de parceiros — bloco novo para o hub

Arquivo: **`docs/seletor-parceiros.html`** (neste repositório, pronto para portar).

Substitui a grade de 3 cards do hub
(`artefatos/parceiros/` no `soluintel`), que não escala. Resolve os três
pedidos de uma vez:

1. **A Blocok entra na lista** — e entra com estado próprio, `Bloqueada`, não
   como “central completa”, porque ela não tem central.
2. **Header persistente.** Barra fixa no topo com todos os parceiros, visível
   também dentro de uma central. Ponto verde = central completa, ponto vermelho
   = bloqueada.
3. **Voltar.** Botão “← Todos os parceiros” dentro da central, e o histórico do
   navegador funciona porque a rota é por hash (`#/ea3`).

### Por que virou lista e não card

Card tem ~350 px de altura. Com 3 parceiros cabe numa linha; com 10 vira parede
de rolagem. A lista mantém uma linha por parceiro com logo, nome, estado,
segmento, cidade, ID, o salto de score e as etiquetas — e ganha **busca** (nome,
segmento, cidade ou ID) e **filtro por estado**.

### Como adicionar o parceiro seguinte

Um objeto no array `PARCEIROS`, no topo do `<script>`. Nada mais. Os campos:

| Campo | Para que serve |
|---|---|
| `slug` | vira a rota `#/slug` |
| `curto` | nome curto que aparece no header |
| `sigla`, `cor` | o quadrado colorido no lugar do logo |
| `estado` | `completa` ou `bloqueada` — define pill, ponto e filtro |
| `antes`, `depois` | o salto de score; `depois: null` desenha “sem central” |
| `href` | **URL da central real** — hoje vazio, ver abaixo |
| `stats`, `resumo`, `tags` | o que aparece na linha e no dossiê |

### Status: superado pelo porte real

Este arquivo foi um plano B, escrito quando esta sessão ainda não alcançava o
`soluintel`. O acesso foi liberado depois, e **a mudança foi feita direto no hub
real** (`artefatos/parceiros/`), respeitando o design system que já existia lá —
DM Sans, os tokens de marca, os estados `.pcard.wait` e `.st.wait` que o CSS já
previa. O que foi ao ar:

- `artefatos/parceiros/parceiros.js` — seletor compartilhado, fonte única da
  lista. Adicionar parceiro = um objeto no array `PARCEIROS`.
- `artefatos/parceiros/blocok-o-original/` — página de diagnóstico, sem
  conteúdo gerado, por causa da nota da §7.
- Hub com busca, filtro por estado com contagem, o card da Blocok e grade mais
  densa.
- Voltar explícito e seletor no topo nas quatro páginas.

`docs/seletor-parceiros.html` fica como referência da alternativa considerada.

---

## 9. O gatilho do `pages.yml` no branch nunca publicou

Corrige a pendência 4, que a etapa 1 registrou como risco latente. Não é
latente: **é uma falha permanente, e ela esconde trabalho publicado.**

### O que o histórico mostra

Nas 98 execuções do workflow no branch `claude/intelligent-gates-av5c7o`,
**nenhuma terminou em sucesso** — todas são `cancelled` ou `failure`. No `main`,
todas as execuções do mesmo workflow terminam em `success`.

A execução do meu push (nº 222, commit `9474731`) **falhou em 1 segundo** —
começou 01:58:05 e terminou 01:58:06. Não é falha de build: nesse tempo o job
não chegou a fazer checkout. É rejeição no portão do ambiente.

### A causa

O `pages.yml` dispara em `main` **e** no branch, mas o ambiente `github-pages`
só aceita deploy do branch padrão. Todo push no branch falha imediatamente na
etapa de ambiente, antes de rodar qualquer coisa.

O `cancel-in-progress` do grupo `pages` explica o resto: quando os dois branches
recebiam o mesmo commit, uma execução cancelava a outra — daí a alternância
entre `cancelled` e `failure`.

### A consequência que importa

**O site publicado sempre refletiu apenas o `main`.** Todo commit que chegou ao
ar foi empurrado para `main` direto. Enquanto branch e `main` carregavam o mesmo
commit, isso passou despercebido.

Agora eles divergiram: `main` está em `fd08baa` e o branch em `9474731`. **O
trabalho do seletor de parceiros está commitado e pushado, mas não está no ar.**

### Resolvido em 31/08/2026

1. **Publicado.** `4645af3` foi para o `main`; execução nº 223 terminou em
   `success`. O hub novo está no ar.
2. **Gatilho corrigido.** `claude/intelligent-gates-av5c7o` saiu da lista de
   `branches` do `pages.yml`. O deploy passa a rodar só no `main`, que é o
   único que funciona.

Se um dia a intenção for pré-visualizar branch, o caminho é outro — ambiente
separado ou deploy de preview —, nunca o mesmo ambiente `github-pages`.

---

## 10. LAAE Laboratório — quinta empresa

Publicado em `artefatos/parceiros/laae-laboratorio/` no `soluintel`. Descrição
**47 → 94**. Catálogo de 9 itens, 24 temas, 12 correções de cadastro.

O cadastro não traz nota calculada (`Avaliação do perfil: null`) — a de 47 foi
apurada pela régua de 6 dimensões. **É a melhor base factual da série** e ainda
assim zera na dimensão de contato: não há um telefone, um WhatsApp ou um "como
pedir" em parágrafo nenhum do texto publicado.

### 10.1 O que este parceiro tem e nenhum outro tinha

A **análise da transcrição da reunião comercial** anexada ao cadastro. Ela
responde perguntas de briefing que normalmente ficam em aberto e muda a
prioridade do conteúdo:

| Fato | Consequência |
|---|---|
| **99% do negócio é água e efluente**; solo é 1% | Nenhum tema de solo entra no calendário |
| **130 tipos de exame** | Sustenta a série recorrente por mais de dez anos |
| **A amostra vale 24 horas** | Explica o raio de ~600 km, a coleta própria e os 80–90% de mercado regional |
| Contrato de 20–30% do faturamento **deve cair em ~6 meses** | O conteúdo ataca aquisição, não marca |
| **"Meu público não está no Instagram"** (literal) | O calendário sai do feed — ver 10.4 |
| Perfil do Google com reclamações antigas, e a empresa **mudou de sede e telefonia** | Responder as avaliações com o fato novo é ação de reputação, não desculpa |

### 10.2 Achado novo, e mensurável na base inteira

**Três dos quatro produtos têm texto colado de tradutor automático.** O corpo
inteiro vem envolvido em `<font dir="auto" style="vertical-align: inherit;">`,
em pares aninhados — o markup que o tradutor do navegador injeta no DOM. Alguém
traduziu, copiou da tela e colou de volta no cadastro.

O português voltou quebrado, e os erros são os que só a ida e volta produz:

- *"Vantagens da **pesquisa** especializada"* — no produto de **amostragem**
- *"empresas que **detectam** resultados confiáveis"* — por "buscam"
- *"**Monitorização** das condições da água"* — português europeu
- *"projetos de monitoramento que **desativam** avaliação de parâmetros"* — a
  frase publicada não tem sentido
- espaços de largura zero (`U+200B`) no meio das frases

**Por que vale como achado de sistema:** a assinatura é detectável por código.
Uma varredura por `font dir="auto"` e `vertical-align: inherit` nos campos de
descrição diz, em uma consulta, **quantos dos 28 milhões de perfis têm texto
colado de tradutor**. Mesma família do achado da data: um defeito invisível no
caso a caso que aparece na medição.

O produto 711409 é o único limpo — serve de controle: o problema não é o
redator, é o caminho pelo qual o texto entrou.

### 10.3 Segundo padrão: listas que parecem busca real e não são

As **16 "palavras-chave particulares"** do LAAE estão em **ordem alfabética
perfeita**, **14 das 16 terminam com ponto final**, e os erros são de digitação
(`psicultura`, `pocos artesiano`), não de busca. Não são buscas capturadas: é
lista digitada.

Somando com a Blocok (§7), onde 11 dos 104 termos eram superlativos redigidos,
já são **dois de cinco parceiros com o campo contaminado**. O campo mais valioso
do cadastro — o que sustenta o achado 4.2 — também é o mais fácil de preencher à
mão sem ninguém notar. **Vale a mesma medição:** quantos perfis têm listas
alfabetadas ou com pontuação de item.

Neste caso o slot F foi montado pela substituição prevista na §6 do padrão de
editorias — `curated_keywords` da categoria e dúvidas clássicas do setor — e a
lacuna ficou registrada na própria central.

### 10.4 Uma decisão que contraria o manual e está certa

O dono disse, com todas as letras: *"Meu público não está no Instagram. Meu
público é muito direcionado."* Quem compra análise de água é responsável técnico
de indústria, engenheiro ambiental, gestor de hospital — procura no Google
quando precisa, não descobre laboratório rolando feed.

Então os 24 temas foram produzidos uma vez e **redistribuídos por peso**: blog
do site e perfil do Google como destino principal, FAQ em seguida, Instagram e
Facebook em manutenção. **A arquitetura das 6 editorias não muda; a distribuição
é que segue o público** — o que a §7 do padrão já previa ao listar destino
múltiplo por editoria.

### 10.5 Outros achados

- **Três depoimentos nomeados** — SEAM Engenharia (cliente há 15 anos), Hospital
  do Câncer do Norte de Minas e Tânia Botelho — guardados no campo
  **"[Solusite] Ícones"**. Prova social real, invisível.
- **`Solusite: false`** com **seis imagens de Solusite** cadastradas, com
  legendas escritas. Ou foi montado e não marcado, ou cancelado com os ativos
  sobrando.
- **Duas categorias marcadas como padrão** e uma terceira ("Tratamento de Água")
  classificando os produtos. Três classificações para a mesma empresa.
- **11 imagens e nenhuma da operação** — nem bancada, nem coleta, nem equipe,
  nem fachada. É o cadastro com menos imagens da série, e para um laboratório
  acreditado é a lacuna mais cara.
- **A janela de 24 horas** explica o negócio inteiro e não estava em texto
  nenhum. Virou o **tema único** do calendário e o bloco 2 do site.
- **Nenhum parâmetro de ensaio publicado** — 130 exames e nem pH, nem coliformes,
  nem DBO aparecem. É a pendência número 1 para o CS: pedir o **escopo de
  acreditação**. Sem ele, nada pode ser nomeado, porque publicar ensaio fora do
  escopo é problema regulatório.
- **O horário é o primeiro verossímil da série:** seg–sex, 8h–12h e 13h–17h,
  fim de semana fechado. Serve de contraste com os "sete dias mais feriado" dos
  outros parceiros.

---

## 11. Instrução permanente — editorias e temas

**Definida em 08/09/2026. Vale para todas as empresas daqui em diante.**

As editorias e seus temas passam a receber **atenção especial** em toda central,
não tratamento de rodapé. Na prática, o que a aba Conteúdo precisa entregar:

1. **Declarar o lastro antes dos temas.** Uma tabela por slot com os fatos do
   cadastro que sustentam cada eixo e a contagem. Editoria com menos de 2 fatos
   não existe — vira pendência de CS, e isso fica escrito.
2. **Marcar o tema único e a série recorrente** explicitamente, com a
   justificativa de por que aquele tema é impublicável por um concorrente.
3. **Mostrar o que os quatro filtros descartaram**, não só o que passou. No LAAE
   isso eliminou todo tema de solo (1% do negócio) e os três termos fora do
   escopo declarado.
4. **Registrar a substituição quando não há buscas reais**, com a ordem da §6 do
   padrão e a lacuna nomeada como achado.
5. **Distribuir por canal segundo o público**, não por hábito. Quando o cadastro
   ou a reunião disser onde o público está, a distribuição segue — a arquitetura
   dos 6 slots não muda.
6. **Cruzar datas comemorativas com o negócio, quando fizerem sentido para o
   segmento.** Formalizado em 08/09/2026 na §4.1 de `docs/editorias-conteudo.md`.
   A regra: *a data não é o assunto, a data é o gancho*. **Revisada em
   10/09/2026:** não há teto — toda data que cruzar com um fato entra, e o que
   existe é piso (havendo alguma que cruze, ela precisa aparecer). Procura-se em
   cinco frentes: segmento, área de atuação, público, profissões e ciclo do
   setor, e a própria empresa (aniversário e marcos redondos de 10, 15, 20, 25
   anos, só com o ano de fundação confirmado por outra fonte). As datas não
   ocupam editoria exclusiva: entram como abordagem eventual, por padrão no
   slot D, no E quando a data é do lugar e no A quando é da própria empresa. As
   demais viram **âncora de publicação** de temas já existentes, sem criar o
   tema 25. Data sem fato para cruzar não entra; data não verificável entra
   como "confirmar com o parceiro"; e as descartadas ficam listadas com o
   motivo. Formato de entrega de cada editoria: Nome · Objetivo · CONTEÚDOS ·
   ESSA EDITORIA RESPONDE (§4.2), tirado dos casos EA3 e Blocok.

7. **Cruzar o site oficial do parceiro com o dossiê**, dando funções
   diferentes a cada fonte. O **dossiê manda na estratégia** — público, dor com
   prazo, o que entra e o que não entra, território, prioridade, lógica das
   datas. O **site manda no detalhe técnico** — como o processo é feito,
   aplicações nomeadas, certificações, provas de autoridade. Quando as duas
   discordam, vale a regra da casa: **conflito sai do texto e vira pendência
   humana**, nunca escolha de lado.

   No LAAE isso rendeu o achado de maior valor do caso — **água de hemodiálise**,
   que não estava no cadastro nem na reunião — e resolveu uma pendência aberta:
   os termos de alimentos, ar e resíduos que eu havia marcado como fora do
   escopo são serviços reais do portfólio, só não são o foco comercial.
   Também barrou "atuação em 11 estados", que é alcance de franqueadora e não
   da unidade.

   **Requisito de operação que isso expõe:** o pipeline precisa alcançar o site
   do parceiro. Metade do detalhe técnico mora lá e não no cadastro, e hoje
   `lablaae.com.br` não é alcançável deste ambiente — os fatos entraram por
   leitura manual, com a procedência registrada na própria central.

   No LAAE o segmento é dono de três datas — 22/03 (Água), 05/06 (Meio Ambiente)
   e 19/11 (saneamento) —, e a justificativa veio do próprio cliente: ele já
   tinha reclamado do fornecedor atual querendo postar conteúdo de São João,
   *"para São João em Minas, São João em outros estados, isso aqui não tem
   nada"*.

8. **Nome de editoria não pode contradizer os próprios temas.** O slot E leva o
   nome do lugar só quando o território é um lugar só. Quando há rota, região
   multi-cidade ou rede em expansão, ele leva o **nome do alcance**. No LAAE,
   "Norte de Minas é aqui" brigava com o tema das franquias na Bahia e virou
   **"Onde a gente chega"**. O teste é direto: *se um dos 4 temas contradiz o
   nome da editoria, o nome está errado.*

**Acrescentados em 10/09/2026, a partir do LAAE e valendo para os próximos:**

9. **As três peças fixas do perfil saem junto com as editorias**, dos mesmos
   fatos, e vão ao ar antes do primeiro tema do calendário. São: os **5
   destaques do Instagram** (Sobre · Oferta · Diferencial · Prova social ·
   Contato, reordenados se o segmento pedir — em venda técnica o Sobre vem
   primeiro, em loja de consumo a oferta vem primeiro), cada um com título de
   até ~11 caracteres, o que vai dentro, a capa e o porquê, mais as alternativas
   descartadas; os **3 posts fixados** (1 a empresa · 2 o que oferece, com até 4
   itens · 3 uma frase curta de CTA, descrição breve e os contatos principais),
   cada um com **legenda, sugestão de imagem e texto na imagem** — e, quando a
   foto não existe no cadastro, o caminho honesto enquanto não chega; e **uma
   assinatura de rodapé** para toda imagem publicada, definida **em um único
   lugar** e nunca repetida nas peças: frase no tom da empresa · WhatsApp
   principal (dois só com duas linhas de atendimento) · terceiro elemento por
   regra ("Cidade e Região" quando a empresa vai até o cliente; endereço só com
   uma loja física; site só se atual e destino da conversão). Método na §4.3 de
   `docs/editorias-conteudo.md`; no LAAE ficou *Fale com o laboratório ·
   (38) 98405-5391 · Montes Claros e Região*, sem site (estacionado, palavra do
   dono) e sem endereço (B2B, a coleta vai até o cliente).
10. **A aba Conteúdo de cada central passa a ter menu lateral** com oito seções
    numeradas: fontes e regra · editorias e temas · datas comemorativas ·
    destaques · posts fixados · assinatura · filtros e como usar · o prompt. Os
    fixados saem da aba Redes, que fica com a decisão de canal, a bio e um
    ponteiro para o Conteúdo — para não existirem duas versões da mesma peça.
11. **O prompt vigente (§8.1) fica colado na íntegra no fim da aba Conteúdo**,
    com botão de copiar, gerado a partir do arquivo-fonte para que seja sempre o
    mesmo texto. Quando o padrão mudar, a página é regenerada; não se edita o
    prompt na página à mão.
12. **Cidade em peça fixa é tudo ou nada** (definido em 11/09/2026). Empresa que
    atende mais de uma cidade **nunca aparece presa a uma delas** nos destaques,
    nos posts fixados, na bio ou na assinatura: ou a lista completa aparece (na
    legenda do fixado 1, no fixado 3, no destaque de território, na área de
    atendimento do Google), ou **nenhuma cidade aparece** e entra a sede
    ("Sede em X", quando o endereço importa para o cliente) ou o alcance sem nome
    de lugar. Atendimento nacional não cita cidade. Destacar uma praça continua
    permitido **em tema de post** — é o que a série do slot E faz —, nunca em
    peça fixa. O erro que a regra elimina: escolher "as duas ou três principais"
    para caber num espaço curto, o que comunica que o resto não é atendido. Isso
    **não vale** para a página de busca da Solutudo nem para o perfil do Google,
    que são indexados por cidade. No LAAE a assinatura perdeu "Montes Claros e
    Região" e ficou com duas partes (*Fale com o laboratório · (38) 98405-5391*),
    a bio passou a dizer "coleta própria em nove cidades", o fixado 1 saiu de
    "em Montes Claros" para "desde 2003, com coleta em nove cidades" e o fixado 3
    ganhou a sede por extenso mais as nove cidades da rota.

13. **Declaração de acesso às fontes, em evidência** (definida em 11/09/2026,
    §1.1 de `docs/editorias-conteudo.md`). **Receber um link não é ter lido o
    link.** Toda entrega abre com o inventário de tudo que foi enviado e de tudo
    que o payload aponta — site, redes, catálogos, arquivos —, cada fonte com um
    status: **LIDO**, **COLADO** (veio pela pessoa), **PARCIAL** ou **NÃO
    ACESSADO**. Havendo qualquer não acessada, o aviso vem **em destaque, antes
    das editorias**, nomeando cada fonte e dizendo o que isso muda, e se repete
    no fim junto às pendências. Com fonte não lida é proibido escrever "segundo
    o site", deduzir conteúdo pela URL ou descrever o estado atual de um perfil
    que não foi visto — e é proibido ficar calado: o trabalho segue, com cada
    peça dependente marcada como "depende de fonte não lida". Quando tudo foi
    lido, o inventário aparece igual, todas em LIDO.

    No LAAE isso expôs duas fontes que ninguém tinha declarado com esse peso:
    `lablaae.com.br` (403 neste ambiente; o detalhe técnico veio de resumo
    colado) e `instagram.com/lablaae` (nunca aberto — os 5 destaques são
    recomendação a partir do cadastro, não reforma do que está no ar). As 11
    imagens entraram como parciais: foram lidos os rótulos, não os arquivos.

As centrais anteriores (Pizza Frita Semião, Porto Certo, EA3, Blocok) não são
refeitas por causa dos itens 9 a 13 — a regra vale da LAAE em diante.

Referência: `docs/editorias-conteudo.md`. Primeiro caso aplicado com esse rigor:
a central do LAAE.
