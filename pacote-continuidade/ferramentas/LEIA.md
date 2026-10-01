# Ferramentas: os scripts que montam as centrais

Estes scripts estavam **só no espaço temporário da sessão antiga**. Não estão em nenhum repositório. São
o modelo para montar a próxima central e para atualizar a da Execon quando chegarem as respostas do
cliente.

> **Os caminhos estão fixos no código.** A constante `SP` e as menções a
> `/tmp/claude-0/-home-user-site/ca93b4a4-…/scratchpad` apontam para o espaço temporário antigo. O
> `OUT`, o `DOC` e o `HUB` apontam para `/home/user/soluintel/…`. Ao usar numa sessão nova:
>
> 1. copie esta pasta e o dossiê para o novo espaço temporário;
> 2. troque esses caminhos com um `sed` ou à mão, conferindo com `grep -rn "scratchpad\|/home/user" *.py`;
> 3. nunca suba estes arquivos para os repositórios públicos, porque alguns leem o dossiê.

## `central-execon/`: a central do Grupo Execon, que é o modelo atual

A ordem em que rodam:

| # | Script | O que faz |
|---|---|---|
| 1 | `gen_catalogo.py` | lê `20-envelope.md` e grava `31-catalogo.md`, com o catálogo como páginas. Os dados das 12 fichas ficam aqui, e a fonte única importa o `CATALOG` daqui |
| 2 | `execon_rubric.py` | a **rubrica**, com as dimensões, os pesos por tipo de fonte (`PV`), `score()`, `GENERIC_RX`, `ADJ` e `UNIQ`. Também guarda o **texto de hoje marcado frase a frase** (`NOW_P`, `NOW_HEADS`) e classifica os 9 produtos atuais (`TRAD`, `CONCRETE`, `classify`) |
| 3 | `execon_src.py` | **a fonte única**. Reúne `DESC` (descrição em blocos, com frase · fonte · dica · ids), `FAQ`, `SELO`, `SOL_TITLE`, `SOL_META`, `NAO_FAZ`, `CATALOG` com as correções, `HUB` (as páginas de entrada do Solusite), `BANNER_NEW`, `LACUNAS`, `CLAIMS`, `CIT`, `REVIEW`, `BLOCOS`, `EUA_SENT`, `PC4`, `EN_PAGE`, `ALEM`, `KNOWS`, `GATE` e as funções `score_desc()` e `score_item()`. Importa `execon_review` e `execon_pauta` |
| 4 | `execon_review.py` | a aba Agentes, fases 3 a 5: os cartões dos agentes de 6 a 10, a tabela da auditoria (R1–R9), as fases e as pendências do supervisor, e o veredito |
| 5 | `execon_pauta.py` | lê `32-pauta.md`, do planejador, e devolve as estruturas da aba Conteúdo. **Depende da estrutura exata do 32** (§5 de `03-COMO-FAZER-UMA-EMPRESA.md`) |
| 6 | `execon_frame.py` | a moldura: cabeçalho, abas e o CSS e o JS da LAAE. Lê `laae_style.css` e `laae_script.js` da pasta `SP`; neste pacote eles estão em `../central-laae/` |
| 7 | `execon_parc.py` | a aba Parceiro: fontes, linha do tempo, tradutor, números em conflito, `CORRECOES` (13) e `PERGUNTAS` (12) |
| 8 | `execon_agt.py` | a aba Agentes, fases 1 e 2 (classe `AG`) |
| 9 | `execon_dest.py` | a aba Destaque: hoje × proposta, as notas e as fichas do catálogo na gaveta |
| 10 | `execon_site.py` | a aba Solusite, com as 10 seções: `s-atual`, `s-conteudo`, `s-paginas`, `s-faq`, `s-blocos`, `s-eua`, `s-alem`, `s-mapa`, `s-tecnica`, `s-gate` |
| 11 | `execon_cont.py` | a aba Conteúdo, com as 8 seções: `c-fontes`, `c-editorias`, `c-datas`, `c-destaques`, `c-fixados`, `c-assinatura`, `c-uso`, `c-prompt`. A função `hum()` traduz os códigos internos para texto |
| 12 | `execon_build.py` | **monta a central** e grava `soluintel/artefatos/parceiros/grupo-execon/index.html`. Lê a §7 de `solusite-padrao.md` e a §8.1 de `editorias-conteudo.md` na hora, para colar o texto vigente |
| 13 | `execon_export.py` | exporta os textos finais para `36-textos-finais.md`, com as notas medidas |
| 14 | `execon_hub.py` | cria ou atualiza o cartão no hub e a entrada no `parceiros.js` |
| — | `audit_execon_parse.py` | extrai os textos do dossiê para a auditoria. Só lê |

**Conferido em 01/10/2026.** Copiei estes scripts e o dossiê para uma pasta nova, troquei os
caminhos e rodei o `execon_build.py`. A central que saiu é **idêntica, byte a byte**, à publicada:
435.746 caracteres (445.631 bytes), descrição 33 → 81, páginas de 79 a 82. O pacote está completo para refazer e atualizar
a Execon.

Para montar a central:

```bash
python3 execon_build.py
python3 execon_export.py
python3 execon_hub.py
```

O `src` importa a `rubric`, o `review` e a `pauta`.

**Para uma empresa nova:**

1. Copie `execon_*.py` para `<slug>_*.py` e troque os imports.
2. Substitua os dados: textos, catálogo, pendências e perguntas.
3. Adapte a rubrica:
   - o critério de AEO próprio do segmento;
   - `UNIQ`, com os fatos que só ela tem;
   - `NOW_P`, com o texto de hoje marcado.
4. Mantenha a estrutura e as abas.

## `central-laae/`: a central da LAAE

| Arquivo | O que faz |
|---|---|
| `laae_src.py` | fonte única da LAAE: texto, catálogo, FAQ e canais |
| `build_site.py` | 1ª versão da aba Solusite (29/09) |
| `build_site_v3.py` | aba Solusite revisada (29/09): métricas, catálogo como páginas e FAQ único |
| `build_v3.py` | métricas da 3.0 na aba Destaque |
| `laae_style.css` e `laae_script.js` | o CSS e o JS da central, reaproveitados na moldura da Execon |

## `testes/`

| Arquivo | O que testa |
|---|---|
| `vhtml.py <arquivo.html>` | tags equilibradas e ids duplicados. Tem de dar `errors 0` |
| `tex.mjs` | as 5 abas em 1400, 768 e 390 px: visíveis, sem rolagem lateral, sem erro de JS e com todas as gavetas abrindo. Tem também um link com `#` |
| `thash.mjs` | os links diretos por hash (`#s-eua`, `#c-fixados`…) |
| `tshots.mjs`, `shot.mjs` | capturas de tela para conferir |
| `thub.mjs`, `thub2.mjs` | o hub e o bloco "Começar um parceiro" |
| `tsite.mjs`, `tv3.mjs`, `tdest.mjs` | testes da LAAE: Solusite, métricas e Destaque |
| `tree.py` | a árvore de tags, para depurar |

Para rodar:

1. Suba um servidor em segundo plano, na raiz do `soluintel`: `python3 -m http.server 8765`.
2. Rode `node tex.mjs`.

Os `.mjs` usam o Playwright global em `/opt/node22/lib/node_modules/playwright` e o Chromium em
`/opt/pw-browsers/chromium`. As fontes do Google são bloqueadas no teste, para ele não travar.

## `html2md.py`

Converte uma central publicada em texto legível, preservando as dicas de fonte de cada frase como
`⟨nota: …⟩`. Foi assim que se geraram os arquivos `empresas/*/central-em-texto.md`.

```bash
python3 html2md.py entrada.html saida.md
```
