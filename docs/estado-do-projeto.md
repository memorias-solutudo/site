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

**Aparece idêntica nos quatro parceiros** — segmentos diferentes, cidades
diferentes. É valor-padrão de formulário, não fato.

Isso deixou de ser coincidência e virou **achado de sistema**: vale medir
quantos dos **28 milhões de perfis** carregam essa data. Enquanto não for
medido, nenhum campo de data do cadastro deve ser tratado como dado real.

**Quarta ocorrência, na Blocok (§7) — e ela mostra o mecanismo.** A pergunta do
formulário é *“Em que ano a empresa foi fundada?”*, e o que ficou gravado é uma
**data completa**, não um ano. O campo é um seletor de data respondendo a uma
pergunta de ano, e o que sobra é o valor-padrão do seletor. Quatro em quatro
parceiros — a taxa na base inteira provavelmente é alta.

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
4. **Remover ou não o branch do gatilho do `pages.yml`.**
   Hoje ele dispara em `main` **e** no branch, com o mesmo grupo de
   concorrência. É inofensivo enquanto os dois carregarem o mesmo commit — e
   vira corrida no momento em que divergirem.

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

## 7. Blocok O Original — quarta empresa, entrada da etapa 2

### ⚠️ Bloqueio antes de qualquer coisa: nota interna “Não pode utilizar IA”

O cadastro carrega uma **anotação interna prioritária** (tag `Prioridade`,
`Nota prioritária: true`), criada em **10/08/2026 por João Pedro Cavassini**,
com o texto: **“Não pode utilizar IA”**.

Isso colide de frente com o pipeline `empresa-3-0`, cuja saída é justamente
conteúdo gerado. **Nada de descrição, editoria ou texto de anúncio deve ser
gerado para essa empresa até que essa nota seja esclarecida.** O que segue
abaixo é leitura do dado que já existe no cadastro — diagnóstico, não geração.

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
| Catálogo | 3 produtos |
| Categorias | 4 — Materiais para Construção *(padrão)*, Blocos de Cimento, Concretos, Tijolos Ecológicos |
| Palavras-chave particulares | **104** |

Para comparação: a EA3 partiu de 31 com 29 itens de catálogo. A Blocok parte de
**13 com 3 itens** — é o pior ponto de partida da série, e o de maior espaço.

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
