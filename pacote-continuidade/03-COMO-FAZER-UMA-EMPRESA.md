# 03 · Como fazer uma empresa — da ID à central publicada

Este é o processo que produziu a central do **Grupo Execon** (30/09–01/10/2026), a primeira pelo
processo da API. Vale para toda empresa nova. As regras são as de `02-REGRAS.md`. Os pedidos reais
usados na Execon estão em `referencia/prompts-reais-dos-agentes-execon.md`.

```text
ID ──► link da API ──► JSON colado ──► dossiê 00–02 ──► 4 descobridores ──► verificador ──► 20-envelope
                                                                                              │
     central publicada ◄── testes ◄── build ◄── fonte única ◄── retrabalho ◄── 50 ◄── 40 ◄── 30 · 31 · 32
```

---

## 0. Antes de começar (5 minutos)

1. Leia `CLAUDE.md` e confira se os documentos de regra do `soluintel/docs/` mudaram desde a última
   central. Use `git log -5 -- docs/`.
2. Teste a rede uma vez: `curl -sI https://api.solutudo.com` e `curl -sI https://www.solutudo.com.br`.
   Anote o resultado: ele vai para a declaração de fontes.
3. Confira se `SOLUTUDO_API_KEY` existe no ambiente com `test -n "$SOLUTUDO_API_KEY"`. **Nunca
   imprima a chave.**

## 1. Entrada

| O usuário manda | O que fazer |
|---|---|
| **Só a ID** e a API está liberada | `curl -s "https://api.solutudo.com/ad_costumer_core/ad_costumer_core/getData?key=$SOLUTUDO_API_KEY&id=<ID>" > <dossiê>/cadastro.json`. Guarde fora de qualquer repositório |
| **O JSON colado** | trate como fonte **COLADO**, que vale como íntegra. Confira se veio inteiro: o da Execon tinha cerca de 70 mil caracteres |
| O texto atual da página, o link da prévia do Solusite, site, redes | são fontes a declarar: **LIDO**, **PARCIAL** ou **NÃO ACESSADO** |
| Um pedido específico ("incluir os EUA", "foco em alto padrão") | registre o pedido em `00-alvo.md`. Ele é fonte (**cs**), mas fonte única: a curadoria decide o nível publicável |

O hub tem um gerador de link por ID: https://memorias-solutudo.github.io/soluintel/artefatos/parceiros/#comecar.
A chave fica só no navegador de quem usa.

## 2. O dossiê inicial

O dossiê fica no espaço temporário da sessão, **nunca no repositório**. Crie
`<espaço temporário>/dossie-<slug>/`.

| Arquivo | Conteúdo |
|---|---|
| `00-alvo.md` | o nome na Solutudo e o nome usado nos textos, ID, UUID, cidade, segmento e categorias, DDD esperado, se o setor é regulado (qual conselho), os canais declarados, o Solusite e o **pedido do usuário** em itens |
| `01-fatos-fornecidos.md` | os fatos do cadastro no formato `[fato] \| fonte \| confiança \| PUB/int`, por bloco: identidade, local e contato, horário, pagamento, oferta, história, fotos, palavras-chave, pesquisa do contrato. **Retire o patrocinador** e marque os erros de cadastro |
| `02-textos-atuais.md` | a íntegra da descrição atual e dos produtos, com ID, título, categoria e a marca `[markup de tradutor]` onde houver |

Verificações que entram já no `01`. As cinco primeiras são as da parte 1 da §8.1 de
`editorias-conteudo.md`. A sexta veio do caso Execon:

1. **Nota interna prioritária.** Se ela restringe IA ou conteúdo, **pare e pergunte**.
2. **Data de fundação.** `12/05/1999` é valor-padrão.
3. **Autenticidade das palavras-chave particulares.**
4. **Markup de tradutor automático** nos produtos.
5. **Conflitos** entre os campos.
6. **Data de criação dos arquivos.** Os IDs de imagem carregam a data em hexadecimal: os 8 primeiros
   dígitos são o horário Unix. Exemplo: `6aba8196` = 28/09/2026. Isso data banners e textos.

## 3. Fase 1 · Descoberta: 4 agentes em paralelo

Lance os quatro **numa mesma mensagem**, em segundo plano. Use o tipo `general-purpose` se os agentes
do `soluintel` não aparecerem como tipos próprios. Os ângulos são: `site-oficial`, `redes-diretorios`,
`bases-oficiais` (avise se o setor é regulado: CREA, CAU, CRC, OAB…) e `reputacao-conteudo`.

```text
Você é o agente `descobridor-empresa` do pipeline Descrição 3.0 da Solutudo. Suas instruções completas
estão em <SOLUINTEL>/.claude/agents/descobridor-empresa.md — leia com Read e siga à risca (formato de
retorno, proveniência, ausência não é fato, nada de Google Maps/Places, homônimos). Regra vigente geral:
<SOLUINTEL>/docs/descricao-empresa-3-0.md (leia só o que precisar).

EMPRESA-ALVO: leia <DOSSIE>/00-alvo.md e 01-fatos-fornecidos.md (orientam; não repita o que já está lá,
confirme ou derrube).

SEU ÂNGULO: <ângulo> — <o que procurar neste ângulo, incluindo o pedido específico do usuário>.

AMBIENTE: o WebFetch e o curl podem ser bloqueados pelo proxy de saída (403). Tente uma vez; se
bloquear, registre em NAO_ACESSIVEL como "não acessível nesta sessão (egress)" e trabalhe com WebSearch
(trechos), marcando confiança média e "conteúdo não lido, só trecho". Carregue as ferramentas com
ToolSearch (select:WebSearch,WebFetch) se não estiverem disponíveis. Orçamento: 10 a 20 buscas.

SAÍDA: escreva o retorno completo, no formato do seu arquivo de instruções, em
<DOSSIE>/10-descoberta-<ângulo>.md (use Write). Na resposta final, devolva só um resumo de no máximo 12
linhas: nº de fatos, os 5 fatos mais importantes, suspeitos e o que não foi acessível. Não publique nada
em lugar nenhum; não escreva nome de pessoa física (patrocinador, titular do CNPJ, sócio).
```

## 4. Fase 2 · Verificação adversarial

Um agente, depois que os quatro terminarem. **O que mais vale no pedido é a lista de pontos que
exigem decisão explícita.** Escreva essa lista a partir do 01 e da descoberta. Na Execon foram 12
pontos: fundação, números de obras, alto padrão, EUA, endereços, página duplicada, condomínios, CREA e
CAU, três domínios, horário, WhatsApp malformado e o nome fantasia de pessoa física.

```text
Você é o agente `verificador-adversarial` do pipeline Descrição 3.0 da Solutudo. Instruções completas:
<SOLUINTEL>/.claude/agents/verificador-adversarial.md — leia e siga à risca. Regra vigente:
<SOLUINTEL>/docs/descricao-empresa-3-0.md (seções 3 e 8).

Dossiê (leia todos), pasta <DOSSIE>/: 00-alvo.md, 01-fatos-fornecidos.md (cadastro COLADO — a base mais
forte), 02-textos-atuais.md e os quatro 10-descoberta-*.md.

Pontos que exigem decisão explícita sua (cada um vira fato, barrado ou conflito, com motivo):
1. <ponto> … N. <ponto>

Faça buscas de contraprova próprias (telefone isolado, nome + outra cidade, nome + CNPJ). Orçamento:
até 12 buscas.

SAÍDA: grave o envelope completo em <DOSSIE>/20-envelope.md, com ids estáveis: fact.* (publicáveis),
int.* (internos), B01… (barrados), C01… (conflitos), PC1… (pré-condições), formulações travadas. Na
resposta final, só o RESUMO (contagens) e os 5 barrados ou conflitos mais importantes, em até 12
linhas. Nunca escreva nome de pessoa física.
```

## 5. Fase 3 · Redação e pauta: três agentes em paralelo, sem internet

| Agente | Lê | Grava |
|---|---|---|
| `redator-3-0` · descrição e FAQ | 3.0, `solusite-padrao` (§2, §4, §4.1), 20, 02 e a pauta do nicho em 10-reputação | `30-textos.md` |
| `redator-3-0` · catálogo como páginas | `solusite-padrao` (§3, §4, §4.1), 3.0, 20, os produtos do 02 e a pauta do nicho | `31-catalogo.md` |
| planejador de pauta (§8 de `editorias-conteudo.md`) | o documento de editorias inteiro, 20, 30, 31 e a pauta do nicho | `32-pauta.md` |

Os três pedidos precisam dizer:

- **"Você NÃO usa internet: não chame WebSearch nem WebFetch."**
- O envelope é a única fonte de fatos. Respeite os barrados, os conflitos e as pré-condições, pelos ids.
- O pedido específico do usuário, no nível que o envelope permite. Exemplo: "EUA: uma frase travada,
  fora da abertura, do title e da meta".
- **Formato transcrevível:** cada frase numa linha, como `frase | [ids]`, e rótulos fixos de seção.
  O orquestrador transcreve por código para a fonte única.
- **Títulos úteis, nunca rótulos**, inclusive nos destaques. Na Execon, "Serviços" virou "Obra e reforma".
- **Contagens com python3**, e a bio em UTF-16.

O que cada um entrega:

- **Descrição e FAQ:**
  - H1 útil e abertura de 2 a 3 frases, com entidade primeiro.
  - De 3 a 5 blocos com H2 que são buscas reais, frases atômicas e o nome completo da empresa.
  - CTA com o WhatsApp por extenso e o que informar.
  - Texto de 150 a 230 palavras, mas proporcional ao envelope.
  - Selo, title e meta da página e do `/sobre`.
  - FAQ de 6 a 8 perguntas com a primeira frase respondendo. Pergunta sem fato fica "Sem resposta
    publicável hoje", com o que falta e de quem.
  - Relatório, claims evitados e essência.
- **Catálogo:**
  - para cada produto: `key`, `kind` (cad, pronto, cond ou fundir), `card`, `url`, `h1`, `title`
    (até 60), `meta` (até 155), `intro`, `bullets`, `serve`, `cta`, `faq` (de 0 a 3), `pend`, `cond` e `nota_atual`;
  - as decisões explícitas de fundir, reservar ou criar;
  - a ordem do catálogo e a tabela item → URL.
- **Pauta**, com a estrutura exata:
  - `## 0. Fontes`;
  - `## 1. Editorias`, com `### E<n> · nome` e as linhas slot, objetivo, pergunta, fatos, conteudos e
    temas (`título :: descrição :: marcas`);
  - `## 2. Datas`, `## 3. Destaques`, `## 4. Fixados`, `## 5. Assinatura`, `## 6. Bio`;
  - `## 7. Filtros` e `## 8. Pendências`.

  Essa estrutura é lida pelo `execon_pauta.py`.

## 6. Fase 4 · Auditoria de indexação

Um agente, sobre 20, 30, 31 e as páginas de entrada do Solusite, como a lista `HUB` da fonte única.

Peça, além do checklist do agente:

1. pente-fino frase a frase contra o envelope;
2. o pedido sensível só onde é permitido, conferido em **todos** os titles e metas;
3. a mesma lista de serviços em todos os canais;
4. títulos úteis em H1, H2 e no menu;
5. canibalização entre páginas;
6. leitura por leigo;
7. nome da entidade e `alternateName`.

As reprovações vêm com **a correção literal** e a regra que a fundamenta. A saída é `40-auditoria.md`.

## 7. Retrabalho

- **Pelo SKILL**, o normal é reexecutar só a fase reprovada, com as ordens de retrabalho no pedido ao
  agente, e repassar pelo supervisor. O limite é de 2 ciclos.
- **Quando a correção vem literal** (antes → depois), ela pode ser aplicada por código na fonte única.
  Nada de reescrever por conta própria.
- Registre o antes e o depois em `35-retrabalho.md`.
- Se a régua precisar de ajuste, registre também e meça o efeito. Na Execon, a régua premiava a frase
  dos EUA, que ainda espera confirmação, e foi corrigida.
- Exporte os textos finais para `36-textos-finais.md` com o `<slug>_export.py`.

## 8. Fase 5 · Supervisão

Um agente, **com escopo enxuto**: leia cada arquivo uma vez, use só Grep no HTML da central e faça no
máximo 3 buscas. Uma execução caiu por limite de uso. Ele confere:

- as fases 1 e 2, com 2 ou 3 contraprovas próprias;
- o 36 frase a frase, o selo e as notas;
- a pauta contra as decisões da auditoria. A pauta é escrita em paralelo e tende a repetir o que a
  auditoria corrigiu;
- a cobertura da auditoria;
- se a declaração de fontes está em evidência nas abas.

**As ordens de retrabalho vêm literais** (arquivo · campo · texto antes → texto depois), mais um JSON
com as ordens. Aplique por código, confira que cada troca casou exatamente uma vez e registre no 35.
O veredito final é publicado como está: aprovado, aprovado com ressalvas ou reprovado.

Se o veredito depende de trocas que foram aplicadas sem um novo passe do supervisor, diga isso na
entrega. Foi o caso da Execon: REPROVADO na 1ª passada, com a condição escrita de virar APROVADO COM
RESSALVAS depois das 31 trocas. Elas foram aplicadas e reexportadas, sem conferência posterior.

## 9. Fonte única, build, testes e publicação

O modelo está em `ferramentas/central-execon/`. Leia antes o `ferramentas/LEIA.md`.

1. **`<slug>_rubric.py`**
   - A rubrica de `04-RUBRICA-E-NOTAS.md`.
   - O texto publicado hoje, marcado frase a frase com o tipo de fonte e a dica (`NOW_P`).
   - Os fatos únicos (`UNIQ`).
2. **`<slug>_src.py`**, a fonte única. Reúne:
   - a descrição (`DESC`) e o FAQ;
   - o selo, o title e a meta;
   - o catálogo (`CATALOG`) e as páginas de entrada (`HUB`);
   - os blocos e o "além do Destaque";
   - o gate;
   - as funções de nota.
3. **Um módulo por aba:** `frame` (moldura, CSS e JS da LAAE), `parc`, `agt` + `review`, `dest`, `site`,
   `cont` + `pauta`. Depois o **`<slug>_build.py`** grava
   `soluintel/artefatos/parceiros/<slug>/index.html`.
4. **`<slug>_hub.py`** coloca o cartão no hub e a entrada no `parceiros.js`, com `estado: "completa"`.
5. **Testes** em `ferramentas/testes/`:
   - `python3 vhtml.py <central>`: precisa dar 0 erros;
   - servidor `python3 -m http.server 8765` na raiz do `soluintel`, em segundo plano;
   - `node tex.mjs`: as 5 abas nas 3 larguras, sem rolagem lateral, sem erro de JS e com todas as
     gavetas abrindo;
   - `node thash.mjs`: os links com `#`;
   - `node tshots.mjs`: as capturas, para olhar;
   - `node thub2.mjs`: o hub.
6. **Publicar:**
   - `git add` só nos arquivos do parceiro, do hub e dos docs;
   - commit `feat(<slug>): …` e `git push origin main`;
   - acompanhe a execução "Deploy to GitHub Pages" até `success`.
7. **Registrar:**
   - no `site/docs/estado-do-projeto.md`, uma seção nova com o pedido, o que a curadoria mudou, o
     resultado, a supervisão e os achados;
   - no `soluintel/docs/estado-do-projeto.md`, uma linha na tabela de parceiros e os achados de sistema;
   - no `editorias-conteudo.md`, o "Aplicado em";
   - commit no `site`, no branch da sessão.

## 10. A mensagem final ao usuário (modelo)

```text
A central do <Empresa> está publicada com as cinco abas completas, e o deploy terminou com sucesso.
O veredito do supervisor é **<veredito>**, <condições>.

<link da central>

**Fontes que não consegui abrir:** <lista>. <o que foi lido inteiro>. <o que veio só por trecho>.

| | Hoje | Proposta |
|---|---|---|
| Descrição da empresa | <nota>, com <n> palavras | <nota>, com <n> palavras |
| Páginas do catálogo | <faixa> | <faixa> |
| Solusite, média de texto e páginas | <nota> | <nota> |

**<O pedido específico>.** <o que a curadoria decidiu e por quê; o que falta para ir além>.

**O que os agentes derrubaram.** <n execuções>, <n> afirmações caíram: <exemplos concretos>. <o que
o auditor e o supervisor reprovaram>.

**Catálogo e Solusite.** <defeitos do cadastro>; o catálogo ficou: <n publicáveis>; <n reservadas>;
<n fundidas>. <o ponto de ordem de publicação>.

**Editorias.** <as 6, em lista>. Tema único: <…>. Série recorrente: <…>. Data mais próxima: <…>.

**O que depende do cliente.** <as perguntas que mais destravam>.
```

## 11. Atalho: só editorias, sem pipeline

Para quem tem só o JSON e precisa só de editorias e peças fixas, use o prompt da **§8.1** de
`editorias-conteudo.md`. Ele recebe o JSON cru e pula a verificação adversarial. Para editoria
costuma bastar, mas para descrição pública não basta.
