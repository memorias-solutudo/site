# 02 · As regras, consolidadas

As regras estão agrupadas por assunto, e cada uma diz de onde veio. O texto integral está nos
documentos de `docs/soluintel/`. Se este resumo e o documento discordarem, **vale o documento**.

Legenda da origem:

| Sigla | Documento |
|---|---|
| 3.0 | `descricao-empresa-3-0.md` |
| ED | `editorias-conteudo.md` |
| SS | `solusite-padrao.md` |
| API | `processo-api-cadastro.md` |
| EP | `site/docs/estado-do-projeto.md` |
| AG | os arquivos dos agentes |

---

## A. Verdade e fontes

1. **Nada é inventado.** Fato sem fonte não existe. O que não tem lastro vira lacuna declarada ou
   pergunta para o CS. *(3.0, ED §1)*
2. **Todo fato carrega proveniência:** `[fato] | fonte | confiança | PUB ou int`.
   - Confiança **alta** só vale para canal próprio da empresa ou base oficial.
   - Trecho de resultado de busca vale no máximo **média**.
   - Perfil que só teve a existência confirmada não teve o conteúdo lido.
   - Texto atual da página Solutudo lido só por trecho de busca é "provável espelho, não íntegra
     confirmada". *(AG descobridor)*
3. **Ausência nunca é fato.** "Não encontrei" quer dizer desconhecido. Nunca escreva "a empresa não tem
   X", nem use a ausência em abordagem comercial. *(3.0 §4; o erro do Porto Certo: a foto existia)*
4. **Conflito sai do texto.**
   - Dois valores para o mesmo campo: o campo fica fora do texto e recebe a marca `needs_human_review`.
   - Abra uma tarefa de correção de cadastro.
   - Nunca escolha um lado. *(3.0, AG verificador)*
5. **Google Maps e Places são proibidos** como fonte, por restrição contratual dos termos do Maps.
   *(3.0 §1.3 e §9)*
6. **O CNPJ é pista interna.**
   - CNAE não prova o serviço atual.
   - Data de abertura não é a data de fundação.
   - Endereço fiscal não é local de atendimento. *(3.0 §2)*
7. **403 não quer dizer site fora do ar.** Registre "não acessível nesta sessão". *(AG descobridor)*
8. **Homônimos.**
   - Todo agente tem o dever de declarar os suspeitos.
   - Amarras aceitas: cidade e UF, DDD e CEP ou endereço, coerentes entre si.
   - Uma amarra só, como o mesmo nome, não sustenta fato.
   - **Todo endereço é conferido na base oficial de CEP.** Bairro errado no cadastro é achado
     recorrente: na Execon, "Centro" era Bela Vista. *(AG verificador)*
9. **`12/05/1999` é valor-padrão** do formulário, e aparece em seis de seis parceiros. Não é fato nem
   conflito. Marco redondo e "desde [ano]" só entram com o ano confirmado por outra fonte. *(EP §4.1, API §4)*
10. **Texto com `<font dir="auto" style="vertical-align: inherit;">` está corrompido** por tradutor
    automático. Não serve de fonte sem conferência. Diga quais produtos estão afetados. *(ED §8.1, teste 4)*
11. **Teste das palavras-chave particulares.** São sinais de que foram digitadas, e não capturadas de buscas reais:
    - ordem alfabética;
    - ponto final;
    - erro de digitação no lugar de erro de busca;
    - superlativo redigido.

    Se forem digitadas, valem as substituições da §6 de ED, e a lacuna é declarada. *(ED §8.1, teste 3)*
12. **Declaração de acesso às fontes, em evidência** *(11/09/2026, ED §1.1)*.
    - **Receber um link não é ter lido o link.**
    - Toda entrega **abre** com o inventário do que foi enviado e do que o cadastro aponta: site,
      redes, Solusite, arquivos.
    - Cada fonte recebe um status: **LIDO**, **COLADO**, **PARCIAL** ou **NÃO ACESSADO**.
    - Se alguma fonte não abriu, o aviso vem em destaque no topo e se repete no fim.
    - Com fonte não lida, é proibido escrever "segundo o site", deduzir conteúdo pela URL ou descrever
      um perfil que não foi visto.
    - Também é proibido ficar calado: o trabalho segue, com cada peça marcada "depende de fonte não lida".
13. **Fato de fonte pública lido só por trecho** entra marcado "conferir na fonte" e vale meio ponto na
    nota. *(SS §4, rubrica)*
14. **Quando há cadastro, site e reunião, cada um tem uma função.** *(EP §11, item 7)*
    - O dossiê e a reunião mandam na **estratégia**.
    - O site manda no **detalhe técnico**.
    - Se discordam, o dado em conflito vira pendência.
15. **O pedido do cliente ou do CS também é fonte, e é uma fonte só.** *(caso Execon, 30/09/2026)*
    - O que só ele sustenta entra **numa frase só**, fora do título, da abertura e da meta, até chegar a
      pré-condição.
    - Exemplo: "está em expansão para os Estados Unidos". A frase sobe de nível quando chegam estado,
      empresa americana, licença e serviço.
    - "Alto padrão" entra sem "exclusivamente" e sem "referência" quando outro canal diz "médio e alto".

## B. Dados pessoais, segurança e privacidade

16. **Os dados do patrocinador são internos.** O nome, o telefone e o e-mail nunca vão a texto
    publicado, a destaque nem a contato. *(API §4, ED §4.3)*
17. **LGPD.** Dado pessoal não entra em texto só por estar em base pública. *(3.0 §3 e §5, regra 6; Execon B16)*
    - Ficam fora: sócios e titular do CNPJ, endereço residencial e e-mail nominal.
    - Pessoa física só aparece com fato publicável específico, como o consultor que assina o texto do
      Porto Certo.
    - Os campos do patrocinador nunca entram, em caso nenhum (regra 16).
18. **A chave da API nunca vai para arquivo nem para o chat.** Os repositórios e o site são públicos. A
    chave fica na variável `SOLUTUDO_API_KEY` do ambiente ou no navegador, pelo gerador do hub. Ao migrar,
    gere uma chave nova. *(API §1 e §3)*
19. **O dossiê bruto não vai para repositório público.** Ele traz CNPJ e fatos barrados.
20. **Nota interna prioritária no cadastro é portão.** *(ED §8.1, parte 1; caso Blocok)*
    - Se a anotação tem `Nota prioritária: true` e restringe geração de conteúdo ou uso de IA, **pare**.
    - Relate a nota ao pé da letra e pergunte o alcance da restrição.
    - Exemplo: a Blocok tem a nota "Não pode utilizar IA". A central saiu por decisão do responsável,
      e a publicação nos canais depende do CS.

## C. Texto: a Descrição 3.0

21. **Entidade primeiro.** A 1ª frase diz o nome, a categoria e a cidade/UF, ou o escopo real.
22. **Frases atômicas**, um fato por frase, com sujeito explícito. **Use o nome completo da empresa** em
    toda frase que pode ser citada sozinha: abertura, resposta de FAQ e primeira linha de cada serviço.
    Um nome curto, como "Execon", seria herdado por homônimos. *(SS §4; auditoria Execon R4)*
23. **A frase termina no fato.**
    - Sem cauda genérica, como "soluções sob medida" ou "qualidade e compromisso".
    - Sem superlativo nem comparação.
    - Sem datação relativa, como "há mais de 9 anos": use "desde [ano]".
24. **A mesma lista de serviços em todos os canais**, na mesma ordem. *(3.0; auditoria Execon R2)*
25. **Módulo sem fato fica de fora.** Poucos fatos pedem texto curto. Nunca estique.
26. **Só entra fato aprovado.** O fato precisa estar confirmado, ter direito de publicação
    (`publication_allowed`) e escopo compatível com a unidade (`location_scope`). *(3.0 §3 e §5, regra 1)*
    - Campo volátil, como horário, preço e entrega, leva data própria (`valid_until`) e prazo de
      reverificação.
    - Emoji, só na bio do Instagram.
27. **Selo de procedência, depois do texto, com data.** *(3.0 §4)*
    - **A:** "Informações fornecidas pela empresa · atualizadas em DD/MM/AAAA".
    - **B:** "Resumo elaborado pela Solutudo a partir de informações públicas, sem confirmação da
      empresa (DD/MM/AAAA)…", com o convite à correção.
28. **CTA sem link e sem setas** na descrição da Solutudo.
    - Telefone e WhatsApp por extenso.
    - Diga o que a pessoa deve informar.
    - Inclua horário ou agendamento, quando houver.
29. **Canal não confirmado não recebe texto publicado.** Exemplo: Instagram que não aparece em busca.
    Recomendação sim, publicação não.
30. **Limites, contados em código:**

    | Peça | Limite |
    |---|---|
    | title | 50–60 caracteres |
    | meta | 140–160 caracteres (no Solusite, até ~155) |
    | Google | até 750 caracteres, com o essencial nos ~250 primeiros |
    | bio | até 150, contados em UTF-16 |
    | descrição | tipicamente 80–250 palavras |
31. **O JSON-LD é feito pela aplicação, nunca pelo redator.**
    - Use o `@type` mais específico.
    - Sem `PostalAddress` inventado: sem endereço público, use `areaServed`.
    - Sem `aggregateRating` de si mesmo no Solusite.
    - `FAQPage` só na página de perguntas, espelhando o texto visível. *(3.0 §6, SS §5)*
32. **Gate de publicação da página, o mesmo para grátis e pago.** *(3.0 §8)*
    - **Condições duras:**
      - entidade e unidade sem duplicidade;
      - status operacional conhecido;
      - direito de publicar os dados essenciais;
      - URL canônica estável, com HTTP 200;
      - contato público válido;
      - endereço ou área representados corretamente;
      - nada sensível nem claim proibido;
      - HTML coerente com o JSON-LD.
    - **Utilidade decisória:** oferta específica, escopo local, como e quando obter atendimento, e pelo
      menos 1 informação própria verificável além do cadastro.
    - **Se falhar:** `noindex` e pedido de dados, consolidação com 301, 404 ou 410, ou a URL não é
      criada. Pagar não indexa página fina.

## D. Solusite

33. **Um conteúdo, duas vitrines** *(29/09/2026)*. O texto do site é o mesmo da página de detalhes na
    Solutudo. Muda só o contato: na página é texto, no site é botão. O site é sempre **maior** que a
    página, e cada domínio aponta o canonical para si.
34. **Um item do catálogo é uma página do site, e vice-versa.** Um item condicionado sobe nas duas
    vitrines ao mesmo tempo.
35. **O FAQ é igual nas duas vitrines.** Cada página tem ainda de 1 a 3 perguntas próprias, só com fato.
36. **Títulos úteis, nunca rótulos.** *(pedido do usuário em 29/09/2026, SS §4, regra 10)*
    - Proibido em H1 ou H2: "Serviços", "Sobre", "Contato", "O que fazemos" e "Perguntas frequentes".
    - O título diz o que a pessoa busca ou responde a uma pergunta.
    - O menu pode ser curto, mas específico: "Construção e reforma" (Execon), "Análises" (LAAE).
    - Vale também para título de destaque do Instagram: "Obra e reforma", e não "Serviços".
37. **Página por cidade só com fato próprio da cidade.** Sem isso, ela vira página que só troca o nome,
    o alvo das atualizações de spam do Google.
38. **Para cada página, entregue:**
    - URL, H1, title e meta, com os caracteres contados;
    - a pergunta que ela responde e o conteúdo;
    - as perguntas da página e os links internos;
    - o JSON-LD esperado;
    - a nota, com os critérios.
39. **O cadastro vai antes do site.** O Solusite puxa o conteúdo do cadastro. Se o site sair antes, nasce
    com o texto velho. *(Execon)*
40. **Gate de publicação.** O site só vai ao ar com:
    - domínio definido;
    - o mesmo contato em todos os canais;
    - nenhum endereço inventado;
    - nenhuma afirmação sem fonte;
    - pendências com dono;
    - fontes não acessadas declaradas;
    - camada técnica cumprida;
    - a duplicidade de página resolvida (3.0 §8).
41. **Camada técnica, que é da aplicação e o gate confere.** *(SS §5)*
    - Todo conteúdo essencial vai no HTML servido: robôs de IA não executam JavaScript.
    - Telefone e WhatsApp clicáveis (`tel:`, `wa.me`) e visíveis sem clique.
    - O `robots.txt` libera Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot e PerplexityBot.
      Confira se a CDN ou o firewall bloqueiam robôs de IA.
    - Core Web Vitals no percentil 75: LCP até 2,5 s, INP até 200 ms, CLS até 0,1.
    - "Atualizado em DD/MM/AAAA" visível, `dateModified` e IndexNow para o Bing.

## E. Editorias e peças fixas do perfil

42. **Editoria é um eixo com pelo menos 2 fatos.** Sem isso, vira pendência de CS.
    - São **6 slots fixos**:

      | Slot | Função |
      |---|---|
      | A | processo e origem |
      | B | oferta |
      | C | conversão |
      | D | público |
      | E | território |
      | F | dúvidas |

    - O nome tem de 2 a 4 palavras, na linguagem do negócio.
    - O slot E leva o nome do lugar quando a empresa atende um lugar só, e o do **alcance** quando
      atende vários.
    - Teste: se um tema contradiz o nome da editoria, o nome está errado. *(ED §2–3)*
43. **24 temas, 4 por editoria**, do mais fácil ao mais trabalhoso. Marque **1 tema único**, que nenhum
    concorrente publicaria, e **1 série recorrente**. O padrão da série é "<Marca> perto da sua <coisa>". *(ED §4 e §4.2)*
44. **Formato de entrega:** Nome · Objetivo · CONTEÚDOS · ESSA EDITORIA RESPONDE. O que depende de
    confirmação entra com a condição escrita. *(ED §4.2)*
45. **Datas comemorativas: a data não é o assunto, é o gancho.** *(ED §4.1, 08/09 e revisão de 10/09)*
    - Procure em cinco frentes: segmento, área de atuação, público, profissões e ciclo, e a própria empresa.
    - Não há teto, mas há piso: se alguma data cruza com um fato, ela entra.
    - Data não ocupa editoria exclusiva. Vai no slot D por padrão, no E quando é do lugar e no A quando é
      da empresa.
    - Data não verificada entra como "confirmar com o parceiro".
    - As descartadas ficam listadas, com o motivo.
46. **Quatro filtros.** O que cai em cada um é relatado. *(ED §5)*
    - Tem lastro?
    - Termina em ação? Vale para o slot C.
    - É replicável por qualquer concorrente?
    - Em setor regulado, é tema sem promessa?
47. **Peças fixas, entregues junto com as editorias** e publicadas antes do 1º tema. *(ED §4.3, 10/09/2026)*
    - **5 destaques:** Sobre · Oferta · Diferencial · Prova social · Contato.
      - Reordene conforme o segmento e diga o motivo.
      - Título de até ~11 caracteres.
      - De 3 a 6 stories que já existam. Destaque vazio é pior que ausência.
      - O 5º sempre termina em contato.
      - Liste as alternativas descartadas.
    - **3 posts fixados:** a empresa · o que oferece, com até 4 itens · a chamada para contato.
      - Cada um leva legenda, sugestão de imagem e texto na imagem.
      - Fixe na ordem 3 → 2 → 1.
    - **Assinatura de rodapé:** frase · WhatsApp · terceiro elemento, escolhido por regra.
      - Até ~70 caracteres.
      - Definida em um lugar só.
    - **Bio:** até 150 caracteres.
48. **Cidade em peça fixa é tudo ou nada.** *(pedido do usuário em 11/09/2026, ED §4.3)*
    - Quem atende várias cidades nunca aparece preso a uma delas nos destaques, nos fixados, na bio ou na
      assinatura.
    - Ou entra a lista inteira, ou nenhuma cidade. No lugar, entra "Sede em X" ou o alcance.
    - Destacar uma praça é permitido em **tema de post**.
    - Não vale para a página de busca da Solutudo nem para o perfil do Google, que são indexados por cidade.
49. **A distribuição por canal segue o público, não o hábito.** Na LAAE, o dono disse: "meu público não
    está no Instagram". Os 6 slots não mudam, muda o peso de cada canal. *(EP §10.4)*
50. **O prompt vigente (§8.1) fica colado na aba Conteúdo** de cada central. Ele é gerado do arquivo-fonte
    e nunca editado à mão.

## F. Setor regulado

Engenharia, arquitetura, saúde, consórcio, laboratório acreditado e afins.

51. **Revisão humana sempre** (`needs_human_review`). Nenhuma promessa de resultado, prazo, orçamento,
    segurança ou norma.
    - Credencial sempre com a ressalva do escopo.
    - Confira o conselho de classe: CREA, CAU, CRC, OAB.
    - **Sem registro confirmado, o serviço não é anunciado.** Na Execon, "projeto arquitetônico" ficou
      reservado até o CAU.

## G. Processo, qualidade e entrega

52. **Ninguém assina o próprio trabalho.**
    - Quem descobre não verifica.
    - O redator não usa a internet.
    - O auditor mede.
    - O supervisor refaz buscas por amostragem.
    - Zero barrados e zero conflitos numa empresa de nome comum é sinal de verificação fraca: desconfie
      e anote para o supervisor.
    - Retrabalho: reexecute só a fase reprovada, com as ordens no pedido, e repasse pelo supervisor.
      No máximo 2 ciclos.
    - Se o veredito for REPROVADO, ele aparece. **Honestidade do pipeline vale mais que entrega bonita.**
    *(SKILL)*
53. **Notas medidas em código**, com a mesma régua para o hoje e para a proposta e os critérios à vista.
    *(04-RUBRICA)*
54. **Correção literal (antes → depois) pode ser aplicada por código.** Confira que cada troca casou
    uma vez e registre no dossiê, em `35-retrabalho.md`. Se não houver um novo passe do supervisor
    depois disso, diga na entrega. Foi o caso da Execon.
55. **As centrais antigas não são refeitas:** Pizza Frita Semião, Porto Certo, EA3 e Blocok. As regras
    novas valem da LAAE em diante. Correção pontual numa delas, como a de privacidade da pendência B6,
    só com o ok do usuário. *(EP §11)*
56. **Teste antes de publicar.** Publicar é push no `main`. Confira a execução do workflow.
57. **Registre o que muda:**
    - regra nova vai para o documento certo e para o estado do projeto;
    - central nova vai para o hub, o `parceiros.js`, o estado do projeto e o "Aplicado em" de ED.
58. **Toda entrega fecha com as pendências com dono**, em forma de perguntas de um toque para o CS ou o
    cliente, e repete o aviso das fontes não lidas.

## H. Como o usuário gosta de trabalhar

59. **Português, direto, visual**, com o **link para conferir**.
    - Mostre as **notas**: "mostre os scores, etc, como sempre faz".
    - Coloque **os agentes na curadoria**.
60. **Se houver sugestão melhor, diga.** Exemplo: no processo da API, as cinco melhorias em ordem de ganho.
61. **Padrão novo começa por uma empresa só** e depois é replicado. Exemplo: "FAÇA EM APENAS 1 PRA
    COMEÇAR, LABLAAE".
62. **Seja concentrado nas melhorias** que o projeto busca: SEO, AEO e GEO; ser encontrado por pessoas,
    buscadores e IAs; nada inventado.
63. **Quando o limite de uso cai no meio do trabalho**, o usuário volta com "continue de onde parou".
    Retome do ponto exato e relance o agente que caiu, sem refazer o que já terminou.
