# O meu dado, com rigor — relatório do Laboratório 03

Conjunto: `/home/luciano/CEDAGI/meu-projeto-integrador/data/dataset.csv` · 60 linhas · 5 variáveis

Medidas geradas pelo `medidas.py`: desvio padrão amostral (ddof=1),
quartis por interpolação linear, extremos pela regra da amplitude
interquartil — fora de 1,5 × a caixa (slide 24). As medidas são do
programa; as decisões são SUAS. Preencha todos os blocos `R:` e
confira com `python teste.py`.

## Medidas por variável

| variável | tipo | n | faltantes | média | mediana | desvio | Q1 | Q3 | AIQ | mín | máx |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| id_dia | categórica (60 valores; moda: d14) | 60 | 0 | — | — | — | — | — | — | — | — |
| temperatura_c | numérica | 56 | 4 | 63.0839 | 62.4500 | 5.0535 | 61.7750 | 63.1250 | 1.3500 | 60.2000 | 99.5000 |
| vibracao_mm_s | numérica | 60 | 0 | 5.1100 | 5.1000 | 0.3887 | 4.8000 | 5.4000 | 0.6000 | 4.3000 | 6.0000 |
| horas_desde_manutencao | numérica | 60 | 0 | 748.0000 | 290.0000 | 1474.7548 | 123.7500 | 580.0000 | 456.2500 | 35.0000 | 7800.0000 |
| chamados_no_mes | numérica | 60 | 0 | 2.0167 | 1.0000 | 6.0155 | 0.0000 | 2.0000 | 2.0000 | 0.0000 | 47.0000 |

## Extremos marcados (fora de 1,5 × a caixa — slide 24)

### Extremos de `temperatura_c` — 1 valor(es), limites [59.7500; 65.1500]

| linha | valor |
|---:|---:|
| 35 | 99.5000 |

Decisão sobre ESTES extremos — manter ou remover, caso a caso,
com o motivo (slide 25: quem remove sem dizer, mente por omissão):

R: Manter provisoriamente o 99.5 da linha 35 e conferir o registro com a fonte/sensor. Pode ser um superaquecimento real ou um erro de medição; removê-lo sem essa verificação poderia esconder um evento importante. Só corrigir ou excluir se a fonte confirmar o erro, registrando o motivo.

### Extremos de `horas_desde_manutencao` — 6 valor(es), limites [-560.6250; 1264.3750]

| linha | valor |
|---:|---:|
| 25 | 1450.0000 |
| 31 | 2100.0000 |
| 34 | 3400.0000 |
| 36 | 5100.0000 |
| 38 | 6800.0000 |
| 58 | 7800.0000 |

Decisão sobre ESTES extremos — manter ou remover, caso a caso,
com o motivo (slide 25: quem remove sem dizer, mente por omissão):

R: Manter provisoriamente os seis valores (linhas 25, 31, 34, 36, 38 e 58). Intervalos longos desde a manutenção podem representar atraso real e relevante para a operação. Conferir unidades e histórico de manutenção antes de qualquer correção ou exclusão.

### Extremos de `chamados_no_mes` — 1 valor(es), limites [-3.0000; 5.0000]

| linha | valor |
|---:|---:|
| 32 | 47.0000 |

Decisão sobre ESTES extremos — manter ou remover, caso a caso,
com o motivo (slide 25: quem remove sem dizer, mente por omissão):

R: Manter provisoriamente o 47 da linha 32 e conferir a contagem na fonte. Pode ser um mês com muitos chamados ou um erro de digitação; não há evidência suficiente para decidir pela exclusão.


## Faltantes (os três mecanismos do slide 26)

### Faltantes de `temperatura_c` — 4 (6.7% das linhas)

Mecanismo provável — marque UM com um `x` dentro do colchete:

- [ ] perdido ao acaso — a falta não depende de nada
- [x] perdido condicionalmente — depende de outra variável observada
- [ ] perdido por causa do próprio valor — falta porque o valor era o que era

Por quê:

R:
As temperaturas faltam em d21, d22 e d23, três registros consecutivos, e também em d49. Isso sugere, como hipótese, uma falha de medição em um período ou condição de coleta, não que o valor da temperatura tenha causado a falta. O CSV não registra a condição do sensor, então é preciso confirmar essa hipótese nos registros de coleta.

## As quatro perguntas do slide 29

**1. Média e mediana se separam em alguma variável? Em qual?**

R: Sim. A separação é mais forte em horas desde a manutenção (média 748, mediana 290) e chamados no mês (2.0167 e 1), e também aparece em temperatura (63.0839 e 62.45). Os extremos altos puxam as médias para cima. Em vibração, média 5.11 e mediana 5.10 são praticamente iguais.

**2. Quantos extremos foram marcados, e quantos você decidiu manter?**

R: Foram marcados 8 extremos: 1 em temperatura, 6 em horas desde a manutenção e 1 em chamados. Decidi manter os 8 provisoriamente, sinalizados para conferência, porque o critério estatístico sozinho não prova erro e alguns podem representar eventos reais.

**3. Algum faltante parece do terceiro mecanismo?**

R: Não há evidência de que algum valor esteja faltando por causa da própria temperatura. O agrupamento de três faltas consecutivas sugere investigar uma condição de coleta, mas não permite concluir que a temperatura ausente causou a falta.

**4. O que a análise da D1 não tinha visto?**

R: Esta análise tornou explícitos 4 faltantes de temperatura (6.7%), 8 extremos e a assimetria de algumas variáveis. Por exemplo, a média de horas desde a manutenção (748) é bem maior que a mediana (290), e 47 chamados destoa dos demais valores. Esses pontos precisam ser considerados antes de usar médias ou treinar um modelo.

## Comparação com a análise exploratória da D1

O que mudou de lá para cá — o que a análise de lá não tinha visto,
e o que estas decisões escritas mudam no conjunto que a D5 vai usar:

R:
Na D1, esses problemas não estavam registrados com medidas por variável e decisões caso a caso. Agora identifiquei as faltas e os extremos; por enquanto, não removi nem alterei valores. Para a D5, os 60 registros ficam preservados, mas será necessário tratar explicitamente as temperaturas ausentes e validar os oito extremos com as fontes antes de decidir se algum valor deve ser corrigido ou excluído.
