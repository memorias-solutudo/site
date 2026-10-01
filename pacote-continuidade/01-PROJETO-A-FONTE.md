# 01 · O projeto A Fonte — tudo o que está configurado

Situação em **01/10/2026**. As fontes deste resumo são:

- os dois repositórios;
- os documentos de regra;
- as seis centrais publicadas;
- o dossiê da Execon;
- o histórico da sessão "A Fonte™/API (2): Agentes / Check / FAQ / Descrições", aberta em 28/08/2026.

---

## 1. O que é

A Solutudo publica perfis de empresas, e a base tem cerca de **28 milhões de perfis**. A Fonte é a
inteligência de conteúdo que atende os **parceiros pagantes**. O nome vem da ideia central: o
**cadastro da empresa é a fonte da verdade**. Ele vira uma base de fatos verificados, e dessa base
saem todos os produtos, com o mesmo conteúdo em cada canal:

| Produto | O que entregamos |
|---|---|
| **Destaque** (página de detalhes na Solutudo) | descrição pela regra da **Descrição 3.0**, FAQ e catálogo |
| **Solusite** (site do parceiro) | o **mesmo texto** da página, e o site é sempre maior que ela: uma página por produto, FAQ, contato, blog e camada técnica |
| **Google** (Perfil da Empresa) | descrição com até 750 caracteres, área de atendimento e correções |
| **Instagram e redes** | bio, 5 destaques, 3 posts fixados e uma assinatura de rodapé |
| **Conteúdo** | 6 editorias fixas, 24 temas por ano e datas comemorativas cruzadas com fatos da empresa |
| **Tráfego pago** (produto à parte) | Google e Meta, com preço fechado e grupos de anúncio tirados das buscas reais do cadastro |

Para cada empresa existe uma **central**: uma página publicada que reúne tudo isso. Ela mostra o que
está no ar hoje e o que propomos, frase a frase, com a fonte de cada frase e **notas de 0 a 100**.
Mostra também o que os agentes derrubaram e as pendências, cada uma com dono.

---

## 2. Repositórios, branches e endereços

| | `memorias-solutudo/soluintel` | `memorias-solutudo/site` |
|---|---|---|
| Papel | **o projeto**: agentes, regras, centrais, hub e ferramentas | **o diário**: o estado do projeto, para passar o trabalho de uma etapa a outra |
| Branch em uso | `main`, porque o Pages publica só dele | `claude/etapa-1-resumo-projeto-xbt35s` |
| Branch antigo | `claude/intelligent-gates-av5c7o`, da etapa 1. Não publica: o ambiente `github-pages` só aceita o `main` | — |
| Publicação | `.github/workflows/pages.yml` → GitHub Pages, o repositório inteiro, a cada push no `main` | não publica |
| Endereço | https://memorias-solutudo.github.io/soluintel/ | — |
| Últimos commits (01/10/2026) | `819d438` feat(execon): aba Conteudo, supervisao e correcoes finais da central | `eb72658` docs(estado): veredito da supervisao do caso Grupo Execon |

Os dois repositórios **são públicos**.

---

## 3. O ambiente da sessão antiga

| Item | Valor |
|---|---|
| Produto | Claude Code na web, em ambiente na nuvem da Anthropic ("Default — trusted network access") |
| Modelo e esforço | Opus 5.5, esforço "xhigh" (extra alto), modo de permissão automático |
| Diretório principal | `/home/user/site`. O `soluintel` fica em `/home/user/soluintel` |
| Ferramentas | Python 3.11 · Node 22 · Playwright global em `/opt/node22/lib/node_modules/playwright` · Chromium em `/opt/pw-browsers/chromium` |
| GitHub | pelas ferramentas do GitHub da sessão, sem a CLI `gh` |

### Limites de rede confirmados (proxy de saída)

| Domínio | Situação | Contorno usado |
|---|---|---|
| `api.solutudo.com` | 403 | o usuário cola o JSON na conversa |
| `solutudo.com.br`, `previa.solusite.com.br` | 403 | o Solusite atual é reconstituído a partir do cadastro, e isso é declarado como NÃO ACESSADO |
| sites dos parceiros, Instagram | 403 ou DNS | trechos do WebSearch, com confiança no máximo média e a marca "conferir na fonte" |
| `memorias-solutudo.github.io` | publica, mas não abre para leitura | validação local antes de publicar e conferência da execução do workflow |
| WebSearch | **funciona** | é por onde os agentes de descoberta trabalham |
| CDN S3 de imagens da Solutudo | funciona | nos testes headless, imagens desligadas para não travar |

**Ganho imediato numa conta nova:** liberar `api.solutudo.com` na rede do ambiente e guardar a chave
em `SOLUTUDO_API_KEY`. Com isso, a entrada vira só a ID. O detalhe está em
`docs/soluintel/processo-api-cadastro.md`, §3.

---

## 4. Mapa do repositório `soluintel`

```text
soluintel/
├── index.html                      ferramenta "Fixados": cadastra cliente, cola o conteúdo e organiza os 3 fixados (dados no navegador)
├── fixados/index.html              variação da mesma ferramenta, com "Gerar entrega" e "Salvar como Word"
├── checklist/                      app "Entrega PRO — Checklist Sem / Com Solutudo" (React), régua de entrega por bloco
├── assets/, favicon.svg            marca Solutudo
├── .github/workflows/pages.yml     publica o repositório inteiro a cada push no main
├── .claude/
│   ├── agents/                     descobridor-empresa · verificador-adversarial · redator-3-0 · auditor-indexacao · supervisor-3-0
│   └── skills/empresa-3-0/SKILL.md o orquestrador do pipeline
├── docs/                           as regras (ver §7)
└── artefatos/
    ├── sobre-empresa-new-rock/     artefato principal da Descrição 3.0, caso de referência New Rock Expresso, com 5 abas
    ├── propostas/ea3-gestao-trafego/  proposta de tráfego pago, com 3 abas
    ├── central-conteudo-parceiro/  redirecionamento antigo para a central da Pizza Frita Semião
    └── parceiros/
        ├── index.html              o HUB: "Começar um parceiro · API do cadastro", busca, filtro e os cartões
        ├── parceiros.js            a lista única do seletor de parceiros: adicionar parceiro é acrescentar um objeto
        ├── pizza-frita-semiao/     central (6 abas)
        ├── porto-certo-consorcio/  central (6 abas)
        ├── ea3-engenharia/         central (7 abas, com Tráfego pago e Briefing)
        ├── blocok-o-original/      central (6 abas)
        ├── laae-laboratorio/       central (6 abas): a primeira com o padrão novo de Conteúdo e Solusite
        └── grupo-execon/           central (5 abas): a primeira pelo processo da API e com a aba Agentes
```

## 5. O que está publicado

| Página | Endereço |
|---|---|
| Hub de parceiros | https://memorias-solutudo.github.io/soluintel/artefatos/parceiros/ |
| Começar um parceiro (gerador do link da API) | https://memorias-solutudo.github.io/soluintel/artefatos/parceiros/#comecar |
| Central Pizza Frita Semião | …/artefatos/parceiros/pizza-frita-semiao/ |
| Central Porto Certo Consórcio | …/artefatos/parceiros/porto-certo-consorcio/ |
| Central EA3 Engenharia | …/artefatos/parceiros/ea3-engenharia/ |
| Central Blocok O Original | …/artefatos/parceiros/blocok-o-original/ |
| Central LAAE Laboratório | …/artefatos/parceiros/laae-laboratorio/ |
| Central Grupo Execon | …/artefatos/parceiros/grupo-execon/ |
| Artefato da Descrição 3.0 (New Rock) | …/artefatos/sobre-empresa-new-rock/ |
| Proposta de tráfego da EA3 | …/artefatos/propostas/ea3-gestao-trafego/ |
| Checklist Sem / Com Solutudo | …/checklist/ |
| Ferramenta Fixados | …/ (raiz) e …/fixados/ |

A conta antiga também tem dois artefatos do Claude.ai: "Soluintel Etapa 1" e "Seletor de Parceiros",
de 31/08/2026. Eles ficam na conta antiga e não abrem em outra conta, a menos que sejam
compartilhados. O conteúdo deles já está no hub publicado.

---

## 6. Os agentes

O pipeline é o da **Descrição 3.0**: são cinco papéis, e cada um tem um arquivo em `.claude/agents/`.
As cópias estão em `config-claude/agents/` deste pacote.

| # | Agente | Papel | Ferramentas | Saída no dossiê |
|---|---|---|---|---|
| 1–4 | `descobridor-empresa` | um por ângulo: **site oficial**, **redes e diretórios**, **bases oficiais** (com o conselho de classe quando o setor é regulado) e **reputação e conteúdo**. Coleta fatos com proveniência e declara homônimos suspeitos e lacunas | WebSearch, WebFetch, Read, Grep, Bash | `10-descoberta-<ângulo>.md` |
| 5 | `verificador-adversarial` | tenta **derrubar** cada fato: caça homônimos, cruza cidade, DDD, CEP e endereço, rebaixa confiança e registra conflitos | WebSearch, WebFetch, Read, Grep, Bash | `20-envelope.md` |
| 6 | `redator-3-0` (descrição e FAQ) | escreve **só com o envelope**, sem internet | Read, Grep, Bash | `30-textos.md` |
| 7 | `redator-3-0` (catálogo como páginas) | cada produto vira uma página, com funde, reserva ou cria | Read, Grep, Bash | `31-catalogo.md` |
| 8 | planejador de pauta | segue a §8 de `editorias-conteudo.md`: 6 editorias, 24 temas, datas, destaques, fixados, assinatura e bio | Read, Grep, Bash | `32-pauta.md` |
| 9 | `auditor-indexacao` | limites de canal **medidos em código**, frases atômicas, coerência entre canais e acessibilidade | Read, Grep, Bash, WebSearch | `40-auditoria.md` |
| 10 | `supervisor-3-0` | confere as 4 fases com contraprova por amostragem e dá o veredito com ordens de retrabalho | Read, Grep, Bash, WebSearch, WebFetch | `50-supervisao.md` |

- **A regra que atravessa todos: ninguém assina o próprio trabalho.**
- O orquestrador, que é o Claude principal, segue `.claude/skills/empresa-3-0/SKILL.md`:
  - cria o dossiê `dossie-<slug>/` no espaço temporário;
  - salva cada fase em arquivo antes de chamar a seguinte;
  - aplica o retrabalho, no máximo em 2 ciclos;
  - entrega com o veredito à vista, mesmo quando é REPROVADO.

**Como os agentes rodaram na prática.** O diretório principal da sessão era o `site`, por isso os
agentes do `soluintel` não apareciam como tipos próprios. Cada um rodou como `general-purpose`, em
segundo plano. O pedido levava três coisas: "siga `/home/user/soluintel/.claude/agents/<nome>.md`",
os caminhos dos arquivos de entrada e o arquivo de saída. Os modelos estão em
`03-COMO-FAZER-UMA-EMPRESA.md`. Na Execon foram **10 execuções**: 4 descobridores, o verificador, 2
redatores, o planejador, o auditor e o supervisor.

**Arquivos do dossiê:**

| Arquivo | O que guarda |
|---|---|
| `00-alvo` | quem é a empresa-alvo |
| `01-fatos-fornecidos` | o cadastro, sem os dados do patrocinador |
| `02-textos-atuais` | os textos de hoje |
| `10-*` | a descoberta |
| `20-envelope` | os fatos verificados |
| `30`, `31`, `32` | a redação e a pauta |
| `35-retrabalho` | as correções aplicadas |
| `36-textos-finais` | exportado da fonte única |
| `40-auditoria` | a auditoria |
| `50-supervisao` | a supervisão, mais `50-supervisao-ordens.json` |

---

## 7. Os documentos de regra (`soluintel/docs/`)

| Documento | O que governa | Quando ler |
|---|---|---|
| `descricao-empresa-3-0.md` | **a regra vigente do texto**: envelope de fatos, arquétipos e módulos, selo A/B, CTA sem link, prompt gerador 3.0, saídas por canal, FAQ, gate de publicação, auditoria da spec 2.1 | sempre |
| `editorias-conteudo.md` | **conteúdo**: o princípio, a declaração de fontes (§1.1), os 6 slots, os nomes, os 24 temas, as datas comemorativas (§4.1), o formato de entrega (§4.2), as peças fixas e a regra das cidades (§4.3), os filtros, os prompts da §8 (com envelope) e da §8.1 (direto do JSON) | sempre |
| `solusite-padrao.md` | **o site**: um conteúdo em duas vitrines, as páginas, as 10 regras de conteúdo (a 10ª é "títulos úteis, nunca rótulos"), a rubrica, os blocos, o que vai além do Destaque, a camada técnica, o gate e a especificação de bolso (§7) | sempre |
| `processo-api-cadastro.md` | **a entrada**: o link `getData`, os 6 passos e o caminho da automação | sempre |
| `orientacoes-telas-solutudo.md` | as novas telas do site Solutudo: HTML servido, 3 camadas, JSON-LD, frescor, indexação | ao opinar sobre telas e SEO técnico |
| `inteligencia-solutudo.md` | o desenho do hub de inteligência e do schema geral, os cards da 2.0 e a conferência | contexto |
| `descricao-empresa-2-0.md` | a versão anterior, histórica, com o caso New Rock | contexto |
| `gestao-trafego-plano.md` | o resumo executivo do produto de tráfego, para o CEO | ao vender tráfego |
| `gestao-trafego-operacao.md` | a operação de tráfego. **A §7 tem precedência** sobre o resto do documento | ao operar tráfego |
| `estado-do-projeto.md` | o resumo do estado. **Está defasado:** o cabeçalho é de 27/08/2026, ele cita o branch antigo e a tabela de parceiros não tem Blocok nem LAAE. Por enquanto valem o diário do `site` e este pacote | depois de atualizado (pendência A5) |

E no repositório `site`: `docs/estado-do-projeto.md`, o diário completo com §1 a §12, a instrução
permanente das editorias (§11, itens 1 a 15) e o caso Execon (§12). Há também
`docs/seletor-parceiros.html`, uma referência antiga, já superada pelo hub real.

---

## 8. A central do parceiro (padrão atual)

O padrão atual vem da LAAE e da Execon.

| Aba | O que tem |
|---|---|
| **Parceiro** | a declaração de acesso às fontes, em evidência no topo, a ficha da empresa, a linha do tempo do cadastro, os números em conflito, as correções de cadastro com dono e as perguntas para o cliente |
| **Agentes** | o organograma das execuções, o que cada uma recebeu, entregou e achou, o que foi barrado, a auditoria e o veredito do supervisor, fase a fase, com as pendências consolidadas |
| **Destaque** | a página na Solutudo **hoje × proposta**, frase a frase, com marcações e dicas, as notas, o FAQ e o catálogo em fichas que abrem numa gaveta lateral |
| **Solusite** | menu lateral com o Solusite atual, o conteúdo, as páginas (URL, H1, title, meta contados, JSON-LD), as perguntas, os blocos SEO/AEO/GEO, os pedidos específicos (na Execon, os EUA), o que vai além do Destaque, o mapa do site, a camada técnica e o que falta para publicar (gate), além da especificação de bolso para copiar |
| **Conteúdo** | menu lateral com 8 seções: as fontes e a regra, as editorias e temas, as datas comemorativas, os destaques, os posts fixados, a assinatura, os filtros e como usar, e o prompt vigente (§8.1) colado na íntegra com botão de copiar |

As centrais antigas têm abas próprias: Google, Redes, e na EA3 também Tráfego pago e Briefing.
**Elas não são refeitas.**

**Marcações:** cada uma tem uma dica (`data-tip`) que explica o porquê, e a regra vira dica, nunca nota de rodapé.

| Classe | Cor | Significa |
|---|---|---|
| `m-bad` | laranja | enfraquece o texto |
| `m-fill` | roxo | fato a conferir ou confirmar |
| `m-good` | verde | fato verificado |

**Hub:** cada central tem um cartão com o logotipo, os rótulos, um resumo e quatro números: a nota da
descrição (antes→depois), o catálogo, as correções e as imagens. E tem uma entrada no `parceiros.js`
com `pasta`, `nome`, `meta` e `estado` (`completa` ou `diagnostico`).

---

## 9. Convenções de construção

- **Design system:**

  | Elemento | Valor |
  |---|---|
  | Fonte | DM Sans |
  | Roxo | `--brand-purple:#A701FD` |
  | Rosa | `--brand-pink:#FC0097` |
  | Laranja | `--brand-orange:#FF6849` |
  | Fundo | `--bg:#F5F4F8` |
  | Tons claros | lav, mint, peach, cyan, yellow |
  | CTA | `--grad-cta` |
  | Bordas | `--r-lg:20px` e `--pill:999px` |

  É o mesmo em todos os artefatos. As centrais novas reaproveitam o CSS e o JS da LAAE, em
  `ferramentas/central-laae/laae_style.css` e `laae_script.js`.
- **Fonte única → central gerada.**
  - Um `<slug>_src.py` reúne o texto, o FAQ, o catálogo, as páginas, as editorias e as notas.
  - Um módulo por aba gera o HTML.
  - Nada é editado à mão na página.
  - Os prompts e a especificação são lidos dos documentos de regra na hora de gerar, por isso são
    sempre o texto vigente.
  - O modelo está em `ferramentas/central-execon/`.
- **Gaveta lateral:** `.dw-back` e `.dw` são filhos diretos de `<body>`, e a gaveta fecha com Esc.
- **Testes antes de publicar:**
  - tags equilibradas e ids sem duplicata, com `vhtml.py`;
  - em 390, 768 e 1400 px: sem rolagem lateral, sem erro de JS, todas as fichas abrem e os links com
    `#` funcionam, com os scripts `.mjs` e um servidor local na porta 8765.
- **Publicar:** commit no `main` do `soluintel` e push. Depois, conferir a execução "Deploy to GitHub
  Pages", que tem de terminar em `success`. A última da sessão antiga foi a nº 241.
- **Screenshot sem Playwright:** `chromium --headless --blink-settings=imagesEnabled=false --virtual-time-budget=4000`.

---

## 10. Achados que valem para a base inteira

1. **`12/05/1999` em seis de seis parceiros.** É o valor-padrão do seletor de data, que responde à
   pergunta "Em que ano a empresa foi fundada?". Vale medir na base inteira.
2. **Texto colado de tradutor automático.**
   - Aparece como `<font dir="auto" style="vertical-align: inherit;">`, com erros como "canto de
     obras" no lugar de canteiro e "Gerenciamento de Custódia" no lugar de custos.
   - LAAE: 3 de 4 produtos. Execon: 6 de 9.
   - O editor de produto deveria limpar esse código ao salvar. Vale varrer a base.
3. **HTML de interface de chat de IA colado em produto.** Classes `agent-turn` e `markdown prose`, na EA3.
4. **Palavras-chave "particulares" digitadas, e não capturadas.**
   - Na LAAE: ordem alfabética, ponto final e erro de digitação.
   - Na Blocok: superlativos redigidos.
   - Onde são reais, são o ativo mais valioso do cadastro: na EA3, 43 buscas viraram 5 grupos de
     anúncio, inclusive "eletrecista".
5. **O cadastro responde 13 das 35 perguntas de briefing** de campanha. É a vantagem estrutural sobre
   agência.
6. **Cidade errada no cadastro.**
   - Pergunta de checagem fixa: a cidade declarada é onde a empresa vende ou onde o dono mora?
   - Na EA3, "Avaré e região" apagava o eixo Campinas–Sorocaba.
   - Na Blocok, o cadastro dizia Sorocaba, onde fica o apartamento do franqueado, mas a venda é nos condomínios.
7. **Os IDs de arquivo do cadastro carregam a data de criação em hexadecimal.** Exemplos: `634832bf`
   = 13/10/2022 e `6aba8196` = 28/09/2026. Foi isso que mostrou o texto de 2022 convivendo com o banner
   novo na Execon.
8. **Ausência presumida não é fato.** Uma vez se concluiu, pelo nome da categoria, que o Porto Certo
   não tinha foto real. Tinha.

---

## 11. Gestão de Tráfego, o produto

O detalhe está em `docs/soluintel/gestao-trafego-operacao.md`, §7.

| Plano | Gestão | Mídia coberta |
|---|---|---|
| Só Google | R$ 600/mês | até R$ 1.500/mês |
| Só Meta | R$ 800/mês | até R$ 1.500/mês |
| Google + Meta | R$ 1.200/mês | até R$ 3.000/mês |
| Entrada (só Google) | R$ 400 de setup + R$ 400/mês | até R$ 1.500/mês |

- Setup cortesia nos três primeiros planos.
- **10% sobre o que exceder o teto, por canal.** Pendente: confirmar se é sobre o excedente, que é a
  leitura adotada, ou sobre o total.
- Gestão e mídia nunca somadas.
- Contrato mínimo de 3 meses.
- **Meta:** sempre conversa no WhatsApp, e só com oferta concreta, que é pré-condição do cliente.
- **Google:** 1 campanha de Pesquisa, objetivo Leads, palavras específicas.
- Contas sempre no nome do cliente.
- O site captura o número do interessado antes de abrir a conversa.

---

## 12. Linha do tempo

| Data | O que aconteceu |
|---|---|
| até 22/07/2026 | Descrição 2.0 (caso New Rock) → auditoria da spec 2.1 → **Descrição 3.0 consolidada** (22/07) |
| 12/08/2026 | Centrais da **Pizza Frita Semião** e do **Porto Certo**; plano e operação de tráfego, com as regras internas da §7 |
| 27–28/08/2026 | Central da **EA3** (7 abas) e proposta de tráfego; fim da etapa 1 |
| 31/08/2026 | Central da **Blocok**; seletor de parceiros e `parceiros.js`; o `pages.yml` passa a publicar só do `main` |
| 08/09/2026 | Central da **LAAE**; instrução permanente das editorias; datas comemorativas (§4.1) |
| 10/09/2026 | Peças fixas do perfil (§4.3), menu lateral na aba Conteúdo e o prompt dentro da central |
| 11/09/2026 | **Cidade em peça fixa é tudo ou nada**; **declaração de acesso às fontes** (§1.1) |
| 28/09/2026 | Pergunta sobre métricas de produto e renovação (a resposta está em `referencia/`) |
| 29/09/2026 | **Padrão do Solusite** aplicado na LAAE, e revisado no mesmo dia: métricas da 3.0, catálogo como páginas, FAQ único e títulos úteis |
| 30/09/2026 | **Processo pela API** (hub "Começar um parceiro") e central do **Grupo Execon**, com 10 execuções de agentes |
| 01/10/2026 | Execon final, com o veredito "aprovado com ressalvas"; este pacote |
