# 07 · Prompts prontos para colar

## Versão A: primeira mensagem no Claude Code (com os repositórios)

Anexe o zip `A-Fonte_pacote-de-continuidade.zip` e cole:

```text
Este zip é o pacote de continuidade do projeto A Fonte (Solutudo), que eu tocava em outra conta do
Claude. Quero continuar exatamente de onde parou.

1. Descompacte o zip no espaço temporário desta sessão, fora dos repositórios: eles são públicos.
2. Leia, nesta ordem: 00-LEIA-PRIMEIRO.md, CLAUDE.md, 01-PROJETO-A-FONTE.md, 02-REGRAS.md,
   03-COMO-FAZER-UMA-EMPRESA.md, 04-RUBRICA-E-NOTAS.md, 05-EMPRESAS-ANALISADAS.md, 06-PENDENCIAS.md
   e MANIFESTO.md. Os documentos de regra completos estão no repositório soluintel, em docs/.
3. Confira o ambiente:
   - os repositórios memorias-solutudo/soluintel e memorias-solutudo/site estão aqui, e em que branch?
   - o último commit do soluintel é o 819d438 ou posterior? O do site é o eb72658 ou posterior?
   - a rede alcança api.solutudo.com, solutudo.com.br e previa.solusite.com.br?
   - existe a variável SOLUTUDO_API_KEY? Não imprima a chave.
4. Proponha copiar o CLAUDE.md do pacote para a raiz do soluintel, com commit no main. Só faça com o
   meu ok. Os scripts de ferramentas/ e o dossiê da Execon ficam no espaço temporário, e nunca vão
   para os repositórios públicos.
5. Responda com:
   (a) o projeto em 10 linhas;
   (b) uma tabela com as 6 empresas: notas, estado e o que trava cada uma;
   (c) o que falta no ambiente;
   (d) a sua recomendação de próximo passo.

A partir de agora, siga o CLAUDE.md como instrução permanente.
```

## Versão B: primeira conversa num Projeto do Claude.ai (sem repositório)

Com o `INSTRUCOES-DO-PROJETO.txt` colado nas instruções e os arquivos no conhecimento, cole:

```text
Este projeto continua o trabalho "A Fonte" da Solutudo, que eu tocava em outra conta. Leia os
arquivos do conhecimento: comece por 00-LEIA-PRIMEIRO, CLAUDE.md e 01 a 06. Aqui não há
repositório nem publicação. Quando eu pedir a central de uma empresa, entregue o conteúdo em texto:

- declaração de fontes;
- descrição 3.0 com notas;
- FAQ;
- catálogo como páginas;
- Solusite;
- editorias e peças fixas;
- pendências.

Siga as mesmas regras e marque o que precisa ser publicado pela conta com Claude Code. Para começar,
responda com:
(a) o projeto em 10 linhas;
(b) uma tabela com as 6 empresas;
(c) as pendências que travam;
(d) a sua recomendação de próximo passo.
```

## Modelo para pedir a próxima empresa

É como o usuário costuma pedir, com as palavras dele no caso da Execon:

```text
Empresa nova: <nome>, ID <ID> na Solutudo.
<Se a API estiver liberada: "busque o cadastro pela API". Se não: cole o JSON do getData aqui.>
Texto atual da página de detalhes: <colar, se tiver>.
Solusite atual: <link da prévia, se houver>.
Pedido específico: <ex.: incluir a atuação nos EUA; foco em alto padrão>.

Considerando apenas a descrição 3.0, o conteúdo atual da página de detalhes e como ele deveria ser,
o conteúdo atual do Solusite × como poderia ser, e as editorias: seja bem concentrado nas melhorias
que buscamos com os projetos e coloque os agentes para trabalhar na curadoria desses conteúdos.
Mostre os scores, etc., como sempre faz.
```

## Modelo para aplicar as respostas do cliente (Execon)

```text
Chegaram as respostas do cliente da Execon: <colar>.
Aplique na fonte única da central (ferramentas/central-execon do pacote): atualize os fatos, tire as
pendências resolvidas, recalcule as notas pela mesma régua, refaça os testes, republique e registre no
estado do projeto. Diga o que mudou na nota e o que ainda falta.
```
