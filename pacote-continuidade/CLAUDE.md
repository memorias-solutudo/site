# A Fonte — manual de operação do Claude

> **Para o Claude que abre este arquivo.** Você está continuando o projeto **A Fonte**, da Solutudo, em
> uma conta nova. Este manual vale como instrução permanente. Os detalhes estão nos arquivos do pacote
> de continuidade (`00` a `07`) e nos documentos de regra do repositório `soluintel`, em `docs/`.
> Onde este resumo e um documento de regra discordarem, **vale o documento de regra**. Avise a pessoa
> da divergência.
>
> Para que toda sessão comece já com este contexto, este arquivo deve ficar na raiz do repositório
> `memorias-solutudo/soluintel`.

---

## 1. O projeto

A Solutudo é uma plataforma com cerca de **28 milhões de perfis de empresas**. **A Fonte** é a
inteligência de conteúdo dos parceiros pagantes. O **cadastro** que a empresa mantém na Solutudo é a
fonte da verdade. Dele, sem inventar nada, saem:

- a **descrição da página** de detalhes da empresa, a página de Destaque, pela regra da **Descrição 3.0**;
- o **FAQ** e o **catálogo**, em que cada produto vira uma página;
- o **Solusite**, o site do parceiro, com o mesmo conteúdo da página e páginas a mais;
- o **perfil do Google**;
- as peças do **Instagram**: bio, 5 destaques, 3 posts fixados e a assinatura de rodapé;
- as **6 editorias com 24 temas** de conteúdo;
- quando contratado, o **tráfego pago**.

Cada empresa ganha uma **central** publicada no GitHub Pages, que mostra:

- o que está no ar hoje e o que propomos, com **notas de 0 a 100** e a fonte de cada frase;
- o que os agentes derrubaram;
- as pendências, cada uma com dono.

## 2. Quem pede e como gosta de receber

- O usuário é da equipe Solutudo e escreve em português. **Responda em português do Brasil**, direto e
  sem enrolação.
- Quando ele diz **"como sempre faz"**, isso quer dizer:
  - **agentes na curadoria**;
  - **central publicada** com o link;
  - **notas antes × depois**;
  - **o que foi barrado**;
  - **pendências com dono**;
  - **fontes não lidas em evidência**, no topo.
- Quer resultado **visual e fácil de entender**, com link para conferir.
- Se houver um caminho melhor do que o que ele pediu, **diga, com a recomendação**.
- **Títulos úteis, nunca rótulos.** Nada de "Serviços", "Sobre", "Contato" ou "Perguntas frequentes"
  como título. O título diz o que a pessoa busca. O menu é curto, mas específico: "Construção e reforma"
  (Execon) ou "Análises" (LAAE), nunca "Serviços". Vale também para destaque do Instagram: "Obra e reforma",
  e não "Serviços".
- **Não refaça nem modifique as centrais antigas** (Pizza Frita Semião, Porto Certo, EA3 e Blocok). As
  regras novas valem da LAAE em diante. Correção pontual numa delas, como a de privacidade da pendência
  B6, só com o ok do usuário.

## 3. Onde está cada coisa

| O quê | Onde |
|---|---|
| Agentes (5) | `soluintel/.claude/agents/*.md` |
| Orquestrador do pipeline | `soluintel/.claude/skills/empresa-3-0/SKILL.md` |
| Regras de texto | `soluintel/docs/descricao-empresa-3-0.md` (envelope de fatos, selo, prompt 3.0, canais, gate) |
| Regras do site | `soluintel/docs/solusite-padrao.md`, que traz também a rubrica das notas (§4.1) |
| Regras de conteúdo | `soluintel/docs/editorias-conteudo.md`, com o prompt da §8.1 e a declaração de fontes da §1.1 |
| Entrada pela API | `soluintel/docs/processo-api-cadastro.md` |
| Telas e indexação | `soluintel/docs/orientacoes-telas-solutudo.md` |
| Tráfego pago | `soluintel/docs/gestao-trafego-operacao.md`. A §7 tem precedência sobre o resto do documento |
| Estado do projeto | `site/docs/estado-do-projeto.md`, o diário completo (§1 a §12), e este pacote. O `soluintel/docs/estado-do-projeto.md` está **defasado**: o cabeçalho é de 27/08/2026, ele cita o branch antigo e a tabela de parceiros não tem Blocok nem LAAE. Atualize-o (pendência A5) antes de confiar nele |
| Centrais publicadas | `soluintel/artefatos/parceiros/<slug>/index.html` |
| Hub | `soluintel/artefatos/parceiros/index.html`, com o bloco "Começar um parceiro" |
| Lista do seletor | `soluintel/artefatos/parceiros/parceiros.js`. Adicionar parceiro é acrescentar um objeto |
| Publicação | `.github/workflows/pages.yml`, que publica só a partir do `main` |
| Endereço público | `https://memorias-solutudo.github.io/soluintel/` |
| Scripts das centrais e dossiê da Execon | no pacote de continuidade: `ferramentas/` e `empresas/grupo-execon/dossie/`. Não estão em nenhum repositório |

## 4. Regras que nunca se quebram

O detalhe e a origem de cada uma estão em `02-REGRAS.md`.

1. **Nada é inventado.** Todo fato tem fonte, confiança e se é publicável (`PUB`) ou interno (`int`).
   Sem fonte, o fato não existe.
2. **Ausência não é fato.** "Não encontrei" quer dizer desconhecido. Não escreva "a empresa não tem X".
3. **Conflito sai do texto** e vira pendência com dono. Nunca escolha um lado.
4. **Google Maps e Places são proibidos** como fonte, por restrição contratual.
5. **O CNPJ é pista interna.** Os campos do **patrocinador** (nome, telefone, e-mail) nunca vão a texto
   publicado. Outros dados pessoais não entram só por estarem em base pública: titular do CNPJ, sócio,
   endereço residencial, e-mail nominal. Pessoa física só aparece com fato publicável específico, como o
   consultor que assina o texto do Porto Certo.
6. **A chave da API nunca vai para arquivo nem para o chat.** Ela fica na variável de ambiente
   `SOLUTUDO_API_KEY` ou no navegador de quem usa o gerador do hub.
7. **`12/05/1999` é valor-padrão do formulário,** e aparece em seis de seis parceiros. Não é fato nem
   conflito. "Desde [ano]" só entra com o ano confirmado por outra fonte.
8. **Texto com `<font dir="auto" style="vertical-align: inherit;">` passou por tradutor automático.**
   Ele está corrompido e não serve de fonte sem conferência.
9. **Declaração de acesso às fontes, em evidência.** Receber um link não é ter lido o link. Toda
   entrega abre com o inventário das fontes:
   - cada fonte com um status: **LIDO**, **COLADO**, **PARCIAL** ou **NÃO ACESSADO**;
   - o aviso do que não abriu vem **no topo** e se repete no fim;
   - nunca escreva "segundo o site" sobre uma fonte que não abriu.
10. **Cidade em peça fixa é tudo ou nada.** Peça fixa é destaque, fixado, bio ou assinatura.
    - Se a empresa atende várias cidades, ou aparece a lista inteira ou não aparece nenhuma.
    - No lugar da lista, entra "Sede em X" ou o alcance.
    - Nunca meia lista.
11. **Selo de procedência em toda descrição, depois do texto.**
    - **A:** a empresa confirmou.
    - **B:** a Solutudo montou o texto de fontes públicas, sem confirmação. O selo diz isso com todas as letras e com data.
12. **CTA sem link e sem setas** na descrição da Solutudo. O telefone e o WhatsApp vão por extenso.
13. **Setor regulado** (engenharia, saúde, consórcio etc.):
    - nenhuma promessa de resultado;
    - credencial sempre com a ressalva do escopo;
    - sem registro no conselho, o serviço não é anunciado. Exemplo: projeto arquitetônico sem CAU.
14. **Notas e contagens são medidas em código**, nunca estimadas. O Instagram conta caracteres em UTF-16.
15. **Ninguém assina o próprio trabalho.**
    - Quem descobre não verifica.
    - Quem escreve não usa a internet.
    - Quem audita mede.
    - O supervisor refaz buscas por amostragem.
    - Zero barrados e zero conflitos numa empresa de nome comum é sinal de verificação fraca: desconfie e
      anote para o supervisor.
    - Honestidade do pipeline vale mais que entrega bonita: o veredito "reprovado" aparece se for o caso.

## 5. Como uma empresa é feita

O passo a passo completo e os modelos de pedido para cada agente estão em `03-COMO-FAZER-UMA-EMPRESA.md`.

1. **Entrada.** O usuário manda a ID ou o JSON do `getData`. A entrada pode vir também com:
   - o texto atual da página;
   - o link da prévia do Solusite;
   - o site e as redes;
   - o pedido específico, por exemplo "incluir a atuação nos EUA".

   Com `api.solutudo.com` liberado e `SOLUTUDO_API_KEY` no ambiente, busque o cadastro você mesmo:

   ```bash
   curl -s "https://api.solutudo.com/ad_costumer_core/ad_costumer_core/getData?key=$SOLUTUDO_API_KEY&id=<ID>"
   ```

   Nunca imprima a chave.
2. **Dossiê** no espaço temporário: `dossie-<slug>/`, com os arquivos `00-alvo`, `01-fatos-fornecidos`
   e `02-textos-atuais`. Retire os campos do patrocinador.
3. **Fase 1 · Descoberta.** São 4 agentes `descobridor-empresa` em paralelo, um por ângulo: site
   oficial, redes e diretórios, bases oficiais, reputação e conteúdo. Saída: `10-descoberta-<angulo>.md`.
4. **Fase 2 · Verificação.** O `verificador-adversarial` gera `20-envelope.md`, com os fatos
   verificados, os barrados, os conflitos, as lacunas e as pré-condições.
5. **Fase 3 · Redação e pauta.** Os redatores trabalham **sem internet**:
   - o `redator-3-0` escreve a descrição e o FAQ em `30-textos.md`;
   - o `redator-3-0` escreve o catálogo como páginas em `31-catalogo.md`;
   - o planejador de pauta, pela §8 de `editorias-conteudo.md`, escreve `32-pauta.md`.
6. **Fase 4 · Auditoria.** O `auditor-indexacao` gera `40-auditoria.md`.
7. **Fase 5 · Supervisão.** O `supervisor-3-0` gera `50-supervisao.md`.
8. **Retrabalho.**
   - Pelo SKILL, o normal é reexecutar só a fase reprovada, com as ordens no pedido ao agente, e
     repassar pelo supervisor. O limite é de 2 ciclos.
   - Quando a ordem vem literal (antes → depois), ela pode ser aplicada por código. Confira que cada
     troca casou uma vez e registre em `35-retrabalho.md`.
   - Se não houver um novo passe do supervisor depois disso, diga na entrega. Foi o caso da Execon.
9. **Fonte única.** Um arquivo `<slug>_src.py` concentra:
   - o texto, o FAQ, o catálogo, as páginas do site e as editorias;
   - a rubrica de `04-RUBRICA-E-NOTAS.md`, que mede o hoje e a proposta.

   A central é gerada desse arquivo, nunca editada à mão. Os textos finais são exportados para `36-textos-finais.md`.
10. **Central com 5 abas:** Parceiro · Agentes · Destaque · Solusite · Conteúdo. Depois vêm o cartão
    no hub e a entrada no `parceiros.js`.
11. **Testes** em 390, 768 e 1400 px:
    - sem rolagem lateral;
    - sem erro de JS;
    - todas as fichas abrem;
    - os links com `#` funcionam;
    - as tags estão equilibradas.
12. **Publicar e registrar.**
    - Faça commit no `main` do `soluintel` e confira se a execução do workflow terminou em `success`.
    - Atualize os dois arquivos `estado-do-projeto.md`.
    - Atualize o "Aplicado em" de `editorias-conteudo.md`.

Agentes personalizados: quando a sessão não carrega os de `soluintel/.claude/agents/`, porque o
diretório principal é outro, rode cada um como `general-purpose`. No pedido, mande:

- "leia e siga `<caminho>/.claude/agents/<nome>.md`";
- os caminhos de entrada;
- o arquivo de saída.

Rode em segundo plano e entregue o dossiê por arquivo.

## 6. Como entregar

A resposta final ao usuário segue esta ordem. O modelo completo está em `03-COMO-FAZER-UMA-EMPRESA.md`, §10.

1. **Link da central**, já publicada, com o deploy conferido.
2. **Fontes que não foram lidas**, nomeadas e em destaque.
3. **Tabela de notas**, hoje × proposta: descrição, páginas do catálogo e Solusite.
4. **O pedido específico do usuário**, e o que a curadoria mudou nele.
5. **O que os agentes derrubaram**, com números concretos.
6. **Catálogo e Solusite**, com o que muda na ordem de publicação.
7. **Editorias**: os 6 nomes, o tema único, a série recorrente e a data mais próxima.
8. **O que depende do cliente**: as perguntas que mais destravam.

## 7. Publicação e ambiente

- **O GitHub Pages publica só o `main` do `soluintel`.** Push em outro branch não vai ao ar.
- **Para conferir a publicação**, veja a execução "Deploy to GitHub Pages" pelas ferramentas do GitHub.
  Não dá para abrir o site publicado: o `github.io` está bloqueado neste ambiente.
- **O repositório `site`** recebe só documentação, no branch indicado pela sessão.
- **Limites de rede vistos até 01/10/2026** (proxy de saída, 403):
  - **bloqueados:** `api.solutudo.com`, `solutudo.com.br`, `previa.solusite.com.br`, `github.io`, os
    sites dos parceiros e o Instagram;
  - **funcionam:** o WebSearch e o CDN de imagens S3.
  - Se a conta nova liberar domínios, confira de novo e diga o que mudou.
- **Ferramentas de teste:**
  - Playwright global em `/opt/node22/lib/node_modules/playwright`;
  - Chromium em `/opt/pw-browsers/chromium`;
  - servidor local com `python3 -m http.server 8765` na raiz do `soluintel`;
  - Python 3.11, que não aceita barra invertida dentro de f-string.
- **Repositórios e site são públicos.** Nada de chave, contato de patrocinador ou dossiê bruto em
  arquivo versionado.

## 8. Onde registrar o que muda

- **Regra nova:** vai para o documento certo em `soluintel/docs/`, com data e o caso que a originou.
  Depois entra uma linha no estado do projeto.
- **Central nova:** precisa de quatro registros:
  - o cartão no hub;
  - a entrada no `parceiros.js`;
  - uma seção nova em `site/docs/estado-do-projeto.md`;
  - uma linha na tabela de parceiros de `soluintel/docs/estado-do-projeto.md`.
- **Achado que vale para a base inteira:** entra em "achados de sistema", em `estado-do-projeto.md`.
  Exemplos: a data-padrão de fundação e o markup do tradutor automático.
