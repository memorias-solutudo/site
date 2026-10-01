# A Fonte — pacote de continuidade

**Gerado em 01/10/2026**, a partir da sessão do Claude Code "A Fonte™/API (2): Agentes / Check / FAQ / Descrições".

Este pacote leva o projeto A Fonte para outra conta do Claude sem perder nada. Ele reúne:

- o que está configurado;
- as regras que você definiu ao longo do trabalho;
- o passo a passo de cada empresa;
- as seis empresas já analisadas;
- as pendências abertas;
- o material que só existia no espaço temporário da sessão antiga: o dossiê dos agentes e os scripts que montam as centrais.

---

## O projeto em um minuto

| | |
|---|---|
| **O que é** | A inteligência de conteúdo da Solutudo. O cadastro da empresa na Solutudo é a fonte da verdade. Dele saem a descrição da página (Descrição 3.0), o FAQ, o catálogo, o Solusite, o perfil do Google, as peças do Instagram e as editorias. Tudo passa pela curadoria de agentes que não inventam nada |
| **Onde mora** | Dois repositórios no GitHub. `memorias-solutudo/soluintel` tem os agentes, as regras e as centrais publicadas. `memorias-solutudo/site` tem o diário do projeto |
| **Onde se vê** | https://memorias-solutudo.github.io/soluintel/artefatos/parceiros/ (hub com as seis centrais) |
| **Como uma empresa entra** | ID do cliente → link da API → JSON colado na conversa → 10 execuções de agentes → central publicada |
| **O que já está pronto** | 6 centrais: Pizza Frita Semião, Porto Certo, EA3, Blocok, LAAE e Grupo Execon |
| **O que vem a seguir** | A próxima empresa pelo processo da API, as respostas do cliente às pendências da Execon e a automação da entrada |

---

## Como usar em outra conta

### Caminho A — Claude Code na web (recomendado, continuidade completa)

É o mesmo ambiente desta sessão: lê os repositórios, roda os agentes em paralelo, testa e publica no GitHub Pages.

1. **Conecte o GitHub da nova conta** em https://claude.ai/connect-github. Se for pedido, instale o app do Claude GitHub na organização `memorias-solutudo`, ou peça a quem é dono dela.
2. **Crie a sessão com os dois repositórios selecionados**: `memorias-solutudo/soluintel` e `memorias-solutudo/site`. Os repositórios de uma sessão são escolhidos na hora de criar.
3. **Ajuste o ambiente** pelo menu do ambiente na barra de título da sessão, em **Editar**:
   - **Acesso à rede:** libere `api.solutudo.com`. Com isso o Claude busca o cadastro sozinho, só com a ID. Se der, libere também `solutudo.com.br`, `previa.solusite.com.br` e `memorias-solutudo.github.io`. Hoje esses domínios dão 403, e por isso a prévia do Solusite e a página publicada nunca foram lidas.
   - **Variável de ambiente `SOLUTUDO_API_KEY`:** coloque a chave da API aqui, nunca no chat. Vale gerar uma chave nova, porque a atual já circulou em conversa.
4. **Primeira mensagem:** anexe este zip e cole a **versão A** de `07-PROMPT-INICIAL.md`.
5. O Claude vai descompactar o pacote e ler os arquivos na ordem abaixo. Depois ele propõe copiar o `CLAUDE.md` para a raiz do `soluintel`, para que toda sessão nova já comece sabendo das regras, e responde com o estado do projeto.

### Caminho B — Projeto no Claude.ai (sem código)

Serve para conversar, gerar textos e editorias e revisar conteúdo. Ele **não** roda agentes em paralelo, não publica centrais e não acessa os repositórios.

1. Crie um Projeto chamado **A Fonte**.
2. Em **Instruções do projeto**, cole o conteúdo de `INSTRUCOES-DO-PROJETO.txt`.
3. Em **Conhecimento**, envie estes arquivos:
   - `00-LEIA-PRIMEIRO.md` e `CLAUDE.md`;
   - os documentos de 01 a 07 deste pacote;
   - `docs/soluintel/descricao-empresa-3-0.md`, `editorias-conteudo.md`, `solusite-padrao.md` e `processo-api-cadastro.md`;
   - os `empresas/*/FICHA.md`.
   - O resto é consulta: anexe na conversa quando precisar.
4. Na primeira conversa, cole a **versão B** de `07-PROMPT-INICIAL.md`.

---

## Ordem de leitura

| # | Arquivo | Para quê |
|---|---|---|
| 1 | `00-LEIA-PRIMEIRO.md` | este guia |
| 2 | `CLAUDE.md` | o manual de operação do Claude: quem ele é aqui, o que nunca pode fazer, onde está cada coisa |
| 3 | `01-PROJETO-A-FONTE.md` | tudo o que está configurado: repositórios, publicação, agentes, documentos, centrais, convenções, achados e linha do tempo |
| 4 | `02-REGRAS.md` | as regras e as suas preferências, consolidadas e com a data em que cada uma foi definida |
| 5 | `03-COMO-FAZER-UMA-EMPRESA.md` | o passo a passo, da ID à central publicada, com os modelos de pedido para cada agente |
| 6 | `04-RUBRICA-E-NOTAS.md` | como as notas de 0 a 100 são calculadas, para medir "hoje × proposta" sempre igual |
| 7 | `05-EMPRESAS-ANALISADAS.md` | as seis empresas: notas, achados, decisões e pendências |
| 8 | `06-PENDENCIAS.md` | tudo o que está aberto, com dono |
| 9 | `07-PROMPT-INICIAL.md` | o texto para colar na primeira mensagem da conta nova |
| — | `MANIFESTO.md` | o índice de todos os arquivos do pacote |

---

## O que fica fora do pacote, de propósito

- **A chave da API.** Os repositórios e o site são públicos, e a API devolve o nome, o telefone e o e-mail do patrocinador. A chave vai na variável `SOLUTUDO_API_KEY` do ambiente, ou fica guardada só no navegador, pelo gerador do hub.
- **Os dados do patrocinador.** São campos internos e nunca vão a texto publicado.
  - Nas cópias em texto das centrais, foram retirados o telefone, o e-mail e o nome do patrocinador.
  - Ficou o contato que é **também** o contato público da empresa no cadastro. Exemplos: o WhatsApp e o
    e-mail da Execon, e o e-mail da Pizza Frita Semião.
  - No Porto Certo, ficou o nome do patrocinador: ele é o consultor que assina o texto público da empresa.
  - As cópias dos documentos dos repositórios, em `docs/`, estão iguais ao original.
- **As capturas de tela dos testes.** Elas são refeitas a cada central.

## Atenção antes de compartilhar este zip

O pacote é para uso interno. O dossiê da Execon (`empresas/grupo-execon/dossie/`) traz dados de trabalho que nunca vão a público, como o número do CNPJ e os fatos barrados. Não suba o zip inteiro em repositório público.
