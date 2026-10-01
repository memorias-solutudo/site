# 06 · Pendências abertas (01/10/2026)

Cada pendência tem um dono. Quando uma for resolvida, registre a resposta no lugar certo:

- na fonte única da empresa, se muda texto;
- no documento de regra, se muda regra;
- no `estado-do-projeto.md`, sempre.

---

## A. Para a conta nova funcionar

| # | Pendência | Dono | Como resolver |
|---|---|---|---|
| A1 | Acesso aos repositórios `memorias-solutudo/soluintel` e `memorias-solutudo/site` | usuário | conectar o GitHub em https://claude.ai/connect-github, instalar o app do Claude na organização se for pedido, e criar a sessão com os dois repositórios |
| A2 | Liberar `api.solutudo.com` na rede do ambiente | usuário | menu do ambiente → Editar → Acesso à rede. Se possível, liberar também `solutudo.com.br`, `previa.solusite.com.br` e `memorias-solutudo.github.io` |
| A3 | Chave da API como segredo | usuário e TI da Solutudo | variável `SOLUTUDO_API_KEY` no ambiente, nunca no chat. **Gerar uma chave nova**: a atual circulou em conversa |
| A4 | Pôr este `CLAUDE.md` na raiz do `soluintel` | Claude, com o "ok" do usuário | assim toda sessão nova começa já sabendo as regras |
| A5 | Atualizar o `soluintel/docs/estado-do-projeto.md` | Claude, com o "ok" do usuário | ele está defasado: o cabeçalho é de 27/08/2026, ele cita o branch antigo e a tabela de parceiros não tem Blocok nem LAAE. O pacote e o diário do `site` estão certos |

## B. Do projeto (valem para todas as empresas)

| # | Pendência | Dono |
|---|---|---|
| B1 | Tráfego: os **10%** incidem sobre o que excede o teto (leitura adotada) ou sobre o total? Se for sobre o total, mudam as propostas já emitidas | especialista |
| B2 | O que é a **"API do Dani"**, como o aceite do plano é registrado e o que ele dispara | especialista |
| B3 | Medir na base inteira: `12/05/1999`; o markup do tradutor (`dir="auto" style="vertical-align: inherit;"`); listas de palavras-chave digitadas (ordem alfabética e ponto final); HTML de chat de IA (`agent-turn`) | produto e dados |
| B4 | O editor de produto deveria **limpar o markup do tradutor ao salvar** | produto |
| B5 | API: uma versão **sem os dados do patrocinador**, uma foto datada do cadastro a cada rodada e uma **fila por lista de IDs** | produto e engenharia |
| B6 | **Privacidade nas centrais publicadas.** Há dados do patrocinador num site público, embora marcados "uso interno, nunca publicar": a **Pizza Frita Semião** mostra nome, telefone e e-mail (o e-mail é também o da empresa); a **LAAE**, nome e telefone; a **EA3**, nome, telefone e e-mail; a **Blocok**, o nome; o **Porto Certo**, o e-mail pessoal do consultor, que é o e-mail cadastrado da empresa. Decidir se remove. A LAAE não é central antiga. Nas antigas, seria uma correção pontual à regra de não modificá-las | usuário |
| B7 | Sugestões ainda sem decisão sobre métricas de produto: link de WhatsApp rastreável por parceiro, URL publicada por item entregue e status estruturado de pendência. Ver `referencia/metricas-de-produto-e-renovacao.md` | produto |
| B8 | Validar se o salto de preço entre os planos de tráfego afasta o cliente do plano maior | comercial |

## C. Por empresa

### Grupo Execon (ID 23008544): a mais recente

**Condições do veredito do supervisor:**

- **C09:** resolver a **página duplicada ID 23064979**, que tem os mesmos telefones e e-mail.
  Consolidar com redirecionamento, ou alinhar o texto e tirar "CREA-SP nº" do título. Pelo gate,
  nada vai ao ar antes. *(Solutudo)*
- **PC4a:** a **confirmação escrita do cliente** para a frase dos EUA, válida até 31/12/2026. Sem ela,
  a frase sai, e a descrição continua com 81. *(cliente)*
- **Opcional, pelo SKILL:** uma 2ª passada do supervisor sobre o 36, o 32 e a central. O veredito formal
  da 1ª passada foi REPROVADO, com a condição de virar APROVADO COM RESSALVAS depois das 31 trocas.
  Elas foram aplicadas, e todas casaram uma vez, mas ninguém conferiu depois. *(nós)*

**As 12 perguntas ao cliente:**

1. Em que ano a Execon começou a atuar? Se a conta inclui o responsável técnico antes do CNPJ de 2020,
   a frase fala dele.
2. Quantas casas foram entregues, quantos m², e com que data?
3. Qual é o endereço de hoje? Ele recebe cliente? Os dois endereços da Paulista ficam em prédio de
   escritório compartilhado.
4. Qual é o site oficial? São três domínios, e o Solusite seria o quarto.
5. Estados Unidos: onde, com que empresa e com que licença? (PC4: estado e cidade, empresa americana,
   licença estadual de construtor, tipo de serviço e desde quando.)
6. Quem é o responsável técnico? Há arquiteto com CAU? O CREA 5070683298 tem formato de registro de
   profissional.
7. Como funciona a contratação: administração ou preço fechado, visita técnica, como sai o orçamento?
8. Como o cliente acompanha a obra: com que frequência e em que formato chegam os relatórios?
9. A Execon ainda faz obra de médio padrão?
10. Qual é o horário de resposta no WhatsApp?
11. A Execon faz reforma de casa, além da comercial? Se sim, a página de reforma sobe de 79 para 81.
12. O perfil `/execonengconstrucao/` é da Execon e está ativo? Mande prints da bio e dos destaques.

**As 13 tarefas de cadastro:**

| Campo | Correção |
|---|---|
| Nome fantasia | hoje tem o nome de uma pessoa física: trocar por "Execon Engenharia e Construção" |
| Fundação | apagar o `12/05/1999` |
| WhatsApp 2 | "(149) 9120-9697" → (14) 99120-9697, se tiver WhatsApp |
| Bairro | "Centro" → Bela Vista, que é o bairro do CEP 01310-000 |
| Exibir endereço | desligar se não houver atendimento presencial |
| Página duplicada | resolver a 23064979 |
| Categoria Arquitetura | em revisão até o CAU |
| Atributo Solusite | hoje `false`: acertar ao publicar |
| Texto dos 6 produtos com tradutor | substituir pelas fichas novas |
| Legendas das 63 fotos | serviço, local e ano de cada uma |
| Banner do Solusite | "expansão no EUA" → "nos Estados Unidos", só com a confirmação |
| Horário | "todos os dias 8h–20h" → o horário real do WhatsApp |
| Palavras-chave da empresa | hoje vazias: preencher |

**Ordem de publicação:** cadastro novo → Solusite. Ao contrário, o site nasce com o texto de 2022.

**Calendário:** 17/10, Dia do Eletricista, e o aniversário de Pardinho, a confirmar.

**Quando as respostas chegarem:**

1. Atualize a fonte única: `ferramentas/central-execon/execon_src.py` e `execon_parc.py`.
2. Rode de novo a rubrica, o build, o export e os testes.
3. Republique e registre.

Com as quatro primeiras respostas, a descrição ganha o "desde", o número de obras e o endereço.

### LAAE Laboratório (ID 32069845)

| Pendência | Dono | Efeito |
|---|---|---|
| **O Solusite existe?** O campo está `false`, mas há 6 imagens | CS | bloqueia tudo |
| **Qual domínio?** O Solusite substitui lablaae.com.br ou convive com ele? | produto + cliente | bloqueia tudo |
| Um nome só: LAAE ou LabLAAE | cliente | ajusta os títulos |
| Escopo de acreditação: a lista de parâmetros | laboratório | limita 4 páginas |
| Quais ensaios fogem das 24 horas | laboratório | ajusta 3 frases |
| Conferir os fatos do site atual: água industrial de processo, temperatura, controles e hemodiálise | nós | "conferir na fonte" |
| URL do portal e número da acreditação | cliente + laboratório | bloqueia 2 recomendações |
| Fotos da operação | cliente | limita a home |
| Autorização dos 3 depoimentos | cliente | bloqueia 1 bloco |
| Robôs de IA na CDN e velocidade antes e depois | técnico / nós | antes de publicar |

### Blocok O Original (ID 27112782)

- **Alcance da nota "Não pode utilizar IA"**: ela vale para publicar ou para qualquer uso? Isso
  **bloqueia a publicação** de todo o conteúdo da central. *(CS)*
- Itatinga é cidade atendida? Ela aparece em 2 buscas e não na lista.
- A empresa vende **pedras ornamentais**? São 10 buscas sem nenhum produto no catálogo.
- O posicionamento em Sorocaba.
- A linha estrutural existe, ou o bloco é só de vedação? Qual é a medida nominal?
- A origem dos 11 superlativos nas palavras-chave.

### EA3 Engenharia (ID 21651088)

- **Corrigir o roteiro "Avaré e região"** para a cobertura real, com dois eixos e 8 municípios, e refazer
  a segmentação por lista de cidades.
- As 12 correções de cadastro: as 5 primeiras levam 10 minutos e valem mais que qualquer texto.
- O DDD 11 do WhatsApp e o celular de 12 dígitos.
- A URL estável do perfil do Google: a cadastrada é um link curto `share.google`.
- **Definir a oferta da campanha.** Sem oferta, não há criativo no Meta, e o Meta já está fora nesta
  fase porque não dá para compartilhar o acesso.
- O prazo de entrega de laudo.

### Porto Certo Consórcio (ID 27460312)

- A marca: Porto Bank ou Porto Seguro? Qual está no contrato de representação?
- A datação: 1999 no contrato, 1995 no texto, "36 anos" no fechamento.
- As redes sociais: o contrato diz "redes ativas" e nenhuma está cadastrada.
- Fotos do escritório e do atendimento. A foto do consultor está guardada como logotipo.
- "Sanches" ou "Sanchez" no campo do patrocinador.
- A validação jurídica das expressões usadas em material de consórcio.

### Pizza Frita Semião (ID 1737)

- **Confirmar o ano de fundação** antes de usar "desde 1999". A central é de 12/08/2026 e tirou o ano
  do campo do contrato, que é o valor-padrão.
- As 5 correções de cadastro: WhatsApp, campo "Blog", palavras-chave, legendas das fotos e markup.

---

## D. Próximos passos sugeridos, em ordem

1. **Montar a conta nova:** A1 a A4.
2. **Execon:** levar ao CS e ao cliente as 12 perguntas e as 13 tarefas. Resolver a C09 e a PC4a. Com
   as respostas, aplicar na fonte única e republicar.
3. **Próxima empresa pelo processo da API.** Se a rede estiver liberada, a entrada é só a ID.
4. **Automação:** a fila por lista de IDs. Cada parceiro entra no hub como `diagnostico` e sobe para
   `completa`.
5. **Varreduras na base (B3)**: elas transformam os achados de caso em números do produto.
