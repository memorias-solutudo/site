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

Estes são os resultados que não ficam presos aos três parceiros: valem como
sistema, para qualquer empresa da base.

### 4.1 A data 12/05/1999

**Aparece idêntica nos três parceiros** — segmentos diferentes, cidades
diferentes. É valor-padrão de formulário, não fato.

Isso deixou de ser coincidência e virou **achado de sistema**: vale medir
quantos dos **28 milhões de perfis** carregam essa data. Enquanto não for
medido, nenhum campo de data do cadastro deve ser tratado como dado real.

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
