# Métricas de produto e renovação — resposta dada em 28/09/2026

> Pergunta do usuário: *"Em termos de produto Solutudo, quais seriam métricas importantes de serem acompanhadas, como por exemplo, quantos clientes entraram e quantos clientes fizemos a entrega final (contendo todos os produtos do pacote adquirido)? e quais mais? E em termos de sucesso, estamos focando em renovação, o que poderia ser?"*
>
> Resposta registrada aqui porque não está em nenhum documento dos repositórios. São recomendações, ainda sem decisão do produto.

---

A pergunta certa não é quantos entraram e quantos entregamos. É quantos, da mesma coorte de entrada, receberam o pacote inteiro **no ar** dentro do prazo, e quantos desses viram um resultado que dá para apontar com o dedo. Entrega e publicação são coisas diferentes, e publicação e uso também.

Antes de qualquer número, falta uma definição de pronto por item do pacote. Sem isso, "entrega final completa" não fecha: cada CS conta de um jeito. Cada item do pacote precisa de um critério binário, por exemplo descrição aprovada e publicada, Solusite no ar com domínio apontado, perfil do Google completo, bio e cinco destaques e três fixados publicados, calendário de 24 temas entregue, tráfego configurado e gastando.

## O funil de entrega, sempre por coorte de mês

| Etapa | Métrica | Por que ela existe |
|---|---|---|
| Entrada | contratos ativados no mês, separando novo de renovado | é o denominador de tudo |
| Insumo | % com cadastro completo em até 7 dias | sem cadastro não há produção |
| Diagnóstico | % com reunião comercial registrada e transcrita | é onde aparecem as queixas que viram churn |
| Produção | % com todos os itens do pacote produzidos | a sua "entrega final" |
| Publicação | % com todos os itens **no ar** | produzido não é publicado |
| Ativação | % que publicou algo do calendário que entregamos | se o conteúdo fica na gaveta, não renova |
| Prova | % com pelo menos um lead rastreado | é o que sustenta a conversa de renovação |

Os tempos importam mais que os percentuais, e sempre em mediana, nunca em média:

| Tempo | O que responde |
|---|---|
| entrada até o primeiro item no ar | quanto o cliente espera para ver qualquer coisa |
| entrada até pacote completo no ar | o ciclo real da operação |
| % entregue em até 30, 60 e 90 dias | onde o SLA quebra |
| idade da pendência aberta mais velha | o que está travando, e há quanto tempo |

Pendência merece métrica própria, porque é o que trava esta operação. Na LAAE foram doze correções, foto de operação inexistente e autorização de depoimento pendente. Meça volume de pendências por entrega, tempo médio aberto, taxa de resolução e quantas foram causadas por nós contra quantas dependem do cliente.

## As métricas que só vocês têm

Estas são medíveis por consulta na base inteira e valem como termômetro do produto, não de um cliente:

| Achado | Métrica | Como medir |
|---|---|---|
| Data-padrão de fundação | % de perfis com 12/05/1999 no campo de ano | varredura do campo |
| Texto de tradutor colado | % de perfis com markup de tradução automática | busca por `font dir="auto"` |
| Palavra-chave digitada | % de perfis sem busca real capturada | os quatro sinais do teste de autenticidade |
| Sem matéria-prima visual | % de perfis sem foto própria da operação | inventário de imagens |
| Contato quebrado | % com telefone, WhatsApp e horário validados nos últimos 90 dias | checagem periódica |
| Fonte inalcançável | % de entregas com alguma fonte não lida | o inventário da PARTE 0 do prompt |

Do lado da qualidade da entrega, quatro números bastam: o score de 0 a 100 antes e depois com o delta médio, o percentual de entregas acima de 85, a taxa de retrabalho após revisão, e a taxa de queixa endereçada. Esta última é a mais subestimada: a reunião comercial registra em voz alta o que fez o cliente trocar de fornecedor. Na LAAE foram três, o site estacionado, o telefone que não aparece e o post genérico de São João. Medir quantas dessas queixas a entrega resolveu é medir a razão pela qual ele fica.

## Renovação: o que medir antes do vencimento

Renovação é métrica atrasada. Quando ela aparece, a decisão já foi tomada, provavelmente nos primeiros sessenta dias. O que dá para acompanhar em tempo de fazer algo:

| Marco | O que precisa estar verdadeiro |
|---|---|
| D+7 | cadastro completo e reunião feita |
| D+30 | primeiro item no ar, e o cliente sabe disso |
| D+60 | pacote completo publicado |
| D+90 | cliente publicando, primeiro lead rastreado, checkpoint com o CS |
| D+180 | constância de publicação e leads acumulados |
| D+300 | conversa de renovação aberta, nunca no vencimento |

Junte isso num índice de saúde por cliente, atualizado toda semana. Pesos que eu usaria como ponto de partida: pacote completo no ar vale 25, leads rastreados nos últimos 60 dias vale 25, cliente publicou nos últimos 30 dias vale 15, dados de contato validados vale 10, contato de CS respondido vale 10, orçamento de tráfego efetivamente investido vale 15. Pendência aberta há mais de 30 dias subtrai.

Os sinais de risco que merecem alerta automático:

- **Nenhum item no ar em 45 dias.** O cliente está pagando e não viu nada.
- **Pendência de foto ou autorização parada há mais de 30 dias.** Metade do calendário não sai sem ela.
- **Zero lead rastreado em 90 dias.** Ou o produto não está performando, ou não está instrumentado.
- **Orçamento de tráfego não gasto.** É dinheiro contratado que não virou entrega.
- **Dois contatos de CS sem resposta.** Cliente ausente é cliente que já decidiu.

E as métricas de renovação propriamente ditas: taxa bruta por coorte, retenção líquida de receita contando upgrade e downgrade, renovação aberta por pacote, por segmento, por CS e por cidade, e churn classificado por motivo declarado. O motivo precisa ser categoria fechada, não texto livre, senão ninguém consegue somar.

O cruzamento que vale mais que todos os outros é este: taxa de renovação contra completude da entrega, e contra tempo até o primeiro item no ar. Se quem recebeu o pacote completo em 30 dias renova muito mais, a operação é a alavanca e o investimento vai para produção. Se a diferença for pequena, o problema está no produto em si, e nenhum esforço de entrega resolve.

Três coisas precisam ser instrumentadas antes, porque hoje não dá para medir: link de WhatsApp rastreável por parceiro, para transformar "acho que não deu resultado" em número; registro de URL publicada por item entregue, para separar produzido de no ar; e status estruturado de pendência, com dono e data. O link de WhatsApp é o de maior retorno, porque é o único que produz a evidência que o cliente aceita na hora de renovar.

Se quiser, monto isso como painel de métricas com as definições, as fórmulas e as consultas, publicado junto às centrais de parceiro.