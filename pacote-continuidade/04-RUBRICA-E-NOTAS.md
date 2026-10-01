# 04 · A rubrica: como as notas de 0 a 100 são calculadas

Toda comparação "como está hoje × como deveria ser" usa **a mesma régua**:

- a descrição da página;
- cada página do catálogo;
- o Solusite.

As notas são **medidas por código**, nunca estimadas. Os critérios aparecem junto com a nota: na central,
cada barra tem a dica com ✓ e ✗.

A base é a §4.1 de `solusite-padrao.md`, a rubrica da Descrição 3.0. A versão implementada está em
`ferramentas/central-execon/execon_rubric.py`, função `score()`. A LAAE usou a mesma régua, em
`laae_src.py`.

---

## 1. As seis dimensões

| Dimensão | Pontos | Critérios (descrição da empresa) |
|---|---|---|
| **Entidade e local** | 15 | nome da empresa na 1ª frase (5) · categoria ou serviço na 1ª frase (5) · sede ou alcance declarados (5) |
| **Fatos verificáveis** | 25 | `round(25 × soma dos pesos das frases ÷ nº de frases)`, menos 5 se houver adjetivo sem fato (lista abaixo) |
| **Resposta direta (AEO)** | 20 | 1ª frase responde o que é (5) · onde atua, com sede e alcance (3) · o que faz, em lista (3) · uma pergunta própria do segmento (3) · como pedir (3) · títulos que respondem a uma busca, nenhum genérico (3) |
| **Estrutura extraível** | 15 | média de até 22 palavras por frase (5; vale 3 se até 28) · lista onde há enumeração (5) · títulos descritivos, nunca genéricos (5) |
| **Unicidade** | 15 | 3 pontos por fato que só a empresa tem, até 5 fatos. **Só conta fato em frase com peso maior que 0 e que não seja `pend`** |
| **Contato e próximo passo** | 10 | canal por extenso, com o WhatsApp no CTA (5) · diz o que informar (3) · horário ou agendamento (2) |

**Nas páginas do catálogo**, a dimensão de AEO troca os critérios:

| Critério | Pontos |
|---|---|
| 1ª frase define o serviço com o nome da empresa | 5 |
| diz para que ou para quem serve (o campo `serve` da ficha) | 5 |
| diz onde atua | 4 |
| diz como pedir | 3 |
| a pergunta da página está respondida no FAQ | 3 |

**O critério do segmento muda de empresa para empresa.** Na construtora, a pergunta própria foi "como o
cliente acompanha a obra", que é responder relatórios. No laboratório, foi o prazo e a coleta. Escolha
a pergunta que todo cliente do segmento faz e **escreva-a nos critérios**, à vista.

## 2. O peso de cada frase, pelo tipo de fonte

| Código | Tipo | Peso | Quando usar |
|---|---|---|---|
| `cad` | cadastro | 1 | fato do cadastro Solutudo, fornecido pela empresa |
| `cs` | Solutudo · CS | 1 | declarado pela Solutudo, no pedido ou no banner. Vale como declaração do cliente via CS, **mas é fonte única** |
| `setor` | regra do setor | 1 | fato do setor, não afirmação sobre a empresa. Exemplo: o que é análise microbiológica |
| `pub` | fonte pública | 0,5 | fonte pública com amarra (telefone ou e-mail iguais), lida só por trecho: "conferir na fonte" |
| `pend` | a confirmar | 0,5 | depende de confirmação da empresa. Vale meio ponto em fatos, mas **não conta em unicidade** |
| `conf` | em conflito | 0 | número que diverge entre canais da própria empresa |
| `barr` | barrado | 0 | o verificador barrou: promessa, superlativo, serviço regulado sem registro |
| `vazio` | sem fato | 0 | adjetivo, promessa ou slogan que qualquer concorrente assinaria |
| `trad` | tradução corrompida | 0 | voltou quebrada do tradutor automático |

## 3. Como medir o "hoje"

1. Transcreva a íntegra do texto publicado. Na central da Execon, essa íntegra é a `NOW_P` de `execon_rubric.py`.
2. Marque **cada frase** com o tipo de fonte e uma dica que explica a marca. A dica aparece no hover
   da central.
3. Os títulos entram à parte (`NOW_HEADS`) e são testados contra a lista de títulos genéricos.
4. Rode a mesma `score()` da proposta. **Nunca dê nota "no olho"**, nem para o texto de hoje.

**Títulos genéricos** (`GENERIC_RX`): os que começam com história, serviços, diferenciais, valores,
sobre, contato, quem somos, missão, o que fazemos, produtos, perguntas frequentes, descrição,
informações técnicas ou venha conhecer.

**Adjetivos sem fato** (`ADJ`): excelência, de ponta, incrível, impecável, perfeição, perfeito, ideal,
sonho(s), referência, sob medida, altamente, a mais alta, máxima qualidade, superam, além das
expectativas, vibrante, impressionante, inovador(a), inovação.

## 4. Lições que viraram regra da régua

1. **A régua não pode premiar fato pendente.** O critério de AEO dizia "onde atua, incluindo os
   Estados Unidos" e dava 3 pontos à frase que ainda espera confirmação. Ele virou "sede e alcance".
   - Na unicidade, frase `pend` deixou de contar.
   - Efeito medido na época: 81 com a frase dos EUA e 82 sem ela. Depois das 31 trocas do supervisor,
     a descrição mede 81 com ou sem a frase.
   - *(01/10/2026)*
2. **Fato único se procura com regex estreita.** "paulista" contava como "sede na Avenida Paulista".
   A regex virou `Avenida Paulista|Av\. Paulista`.
3. **Rubrica explícita pega erro antigo.** Na LAAE, a ficha de efluentes tinha 15 de 15 em "entidade e
   local" sem citar o nome LAAE. Com os critérios escritos, o erro apareceu. *(29/09/2026)*
4. **A mesma régua para as três peças.** Descrição, páginas do catálogo e Solusite usam a mesma
   régua. A nota do Solusite é a média do texto e das páginas.

## 5. Limites por canal (conferidos na mesma entrega)

| Peça | Limite | Observação |
|---|---|---|
| Descrição (detalhes da empresa) | 80–250 palavras | proporcional ao envelope, nunca esticada |
| `seo.title` | 50–60 caracteres | entidade primeiro. O Google pode reescrever |
| `seo.meta` | 140–160 caracteres; no Solusite, até ~155 | termina no fato |
| Perfil da Empresa no Google | até 750 caracteres | o essencial nos ~250 primeiros. Sem URL nem preço |
| Bio do Instagram | até 150 caracteres | contada em **UTF-16**: `len(s.encode('utf-16-le'))//2` |
| Assinatura de rodapé | até ~70 caracteres | uma linha, legível no celular |
| Título de destaque | até ~11 caracteres | o que cabe no círculo |
| Texto na imagem do fixado | até 6 palavras + 2 linhas de apoio | — |

## 6. As notas de cada empresa

| Empresa | Descrição (hoje → proposta) | Outras notas |
|---|---|---|
| Pizza Frita Semião | 40 → 92 | — |
| Porto Certo Consórcio | 44 → 91 | — |
| EA3 Engenharia | 31 → 92 | — |
| Blocok O Original | 13 → 91 | — |
| LAAE Laboratório | 47 → 94 | Solusite com a rubrica explícita (29/09/2026) |
| Grupo Execon | 33 → 81 (716 → 212 palavras) | catálogo: de 35–46 para 79–82 · Solusite: de 36 para 81 |

Por que a Execon fecha em 81, e não em 90 e tantos:

- a régua ficou mais rígida, e unicidade só conta em frase com fonte e sem pendência;
- o setor é regulado, e o envelope é enxuto: 29 afirmações barradas;
- as fontes públicas só puderam ser lidas por trecho, e valem meio ponto.

As primeiras centrais usaram as mesmas seis dimensões, mas antes de duas mudanças: os critérios
explícitos, de 29/09/2026, e a unicidade mais rígida, de 01/10/2026. **Não compare números entre
empresas: compare o hoje com a proposta da mesma empresa.**
