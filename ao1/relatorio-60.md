# O meu dado, com rigor — relatório do Laboratório 03

Conjunto: `casos-ams-60.csv` · 60 linhas · 9 variáveis

Medidas geradas pelo `medidas.py`: desvio padrão amostral (ddof=1),
quartis por interpolação linear, extremos pela regra da amplitude
interquartil — fora de 1,5 × a caixa (slide 24). As medidas são do
programa; as decisões são SUAS. Preencha todos os blocos `R:` e
confira com `python teste.py`.

## Medidas por variável

| variável | tipo | n | faltantes | média | mediana | desvio | Q1 | Q3 | AIQ | mín | máx |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| id_caso | categórica (60 valores; moda: C37) | 60 | 0 | — | — | — | — | — | — | — | — |
| data | categórica (30 valores; moda: 2026-03-27) | 60 | 0 | — | — | — | — | — | — | — | — |
| tipo_maquina | categórica (4 valores; moda: PRENSA) | 60 | 0 | — | — | — | — | — | — | — | — |
| idade_meses | numérica | 60 | 0 | 52.1833 | 53.0000 | 28.3067 | 36.0000 | 64.0000 | 28.0000 | 3.0000 | 216.0000 |
| temperatura_c | numérica | 60 | 0 | 65.7617 | 63.0000 | 7.1741 | 61.0000 | 66.6250 | 5.6250 | 58.0000 | 83.0000 |
| vibracao_mm_s | numérica | 60 | 0 | 4.3892 | 3.6500 | 1.9195 | 3.0000 | 5.5750 | 2.5750 | 2.0000 | 8.6000 |
| horas_desde_manutencao | numérica | 60 | 0 | 118.9667 | 107.5000 | 51.7399 | 85.0000 | 152.5000 | 67.5000 | 20.0000 | 230.0000 |
| acao_correta | categórica (3 valores; moda: seguir_operando) | 60 | 0 | — | — | — | — | — | — | — | — |
| falhou_depois | numérica | 60 | 0 | 0.3333 | 0.0000 | 0.4754 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 |

## Extremos marcados (fora de 1,5 × a caixa — slide 24)

### Extremos de `idade_meses` — 1 valor(es), limites [-6.0000; 106.0000]

| linha | valor |
|---:|---:|
| 12 | 216.0000 |

Decisão sobre ESTES extremos — manter ou remover, caso a caso,
com o motivo (slide 25: quem remove sem dizer, mente por omissão):

R:
Manter provisoriamente o valor de 216 meses da linha 12. É uma idade alta (18 anos), mas pode ser real; confirmar no cadastro da máquina e verificar a unidade antes de qualquer correção. Sem evidência de erro, não remover.

### Extremos de `temperatura_c` — 10 valor(es), limites [52.5625; 75.0625]

| linha | valor |
|---:|---:|
| 2 | 81.5000 |
| 6 | 77.5000 |
| 13 | 79.2000 |
| 17 | 76.0000 |
| 21 | 80.0000 |
| 27 | 82.5000 |
| 34 | 79.5000 |
| 41 | 83.0000 |
| 43 | 79.0000 |
| 53 | 81.0000 |

Decisão sobre ESTES extremos — manter ou remover, caso a caso,
com o motivo (slide 25: quem remove sem dizer, mente por omissão):

R:
Manter provisoriamente as dez temperaturas das linhas 2, 6, 13, 17, 21, 27, 34, 41, 43 e 53. Temperaturas altas podem representar condições operacionais ou eventos relevantes, não necessariamente erro. Conferir os registros e a calibração do sensor; só corrigir ou excluir se a fonte confirmar problema de medição.


## Faltantes (os três mecanismos do slide 26)

Nenhuma variável tem valores faltantes.

## As quatro perguntas do slide 29

**1. Média e mediana se separam em alguma variável? Em qual?**

R: Sim. A diferença aparece em temperatura (média 65,76 °C; mediana 63 °C), vibração (4,39 mm/s; 3,65 mm/s) e horas desde a manutenção (118,97 h; 107,5 h), sugerindo caudas de valores altos. Em idade, média 52,18 meses e mediana 53 meses são próximas. `falhou_depois` é binária: a média 0,333 representa a proporção de falhas e a mediana 0 indica que a maioria dos casos não falhou.

**2. Quantos extremos foram marcados, e quantos você decidiu manter?**

R: Foram marcados 11 extremos: 1 em `idade_meses` e 10 em `temperatura_c`. Decidi manter os 11 provisoriamente e sinalizá-los para conferência; a regra do AIQ identifica valores atípicos, mas não prova que sejam erros.

**3. Algum faltante parece do terceiro mecanismo?**

R: Não há valores faltantes nas 60 linhas e 9 variáveis. Portanto, não há faltantes para classificar como perdidos por causa do próprio valor (nem para atribuir a outro mecanismo).

**4. O que a análise da D1 não tinha visto?**

R: A exploração inicial já indicava diferenças entre médias e medianas e sinalizava extremos. Este relatório deixa mais explícitos os quartis, a amplitude interquartil e os limites usados para marcar os 11 casos, além de documentar a decisão de mantê-los provisoriamente. Também confirma que não há células faltantes; não surgiu evidência para tratar esses extremos como erros.

## Comparação com a análise exploratória da D1

O que mudou de lá para cá — o que a análise de lá não tinha visto,
e o que estas decisões escritas mudam no conjunto que a D5 vai usar:

R:
Em relação à exploração da D1, este relatório formaliza as distribuições com quartis e AIQ, lista os 11 extremos e registra a decisão de preservá-los enquanto são conferidos; confirma também que não há faltantes. Assim, os 60 registros seguem sem remoção, correção ou imputação para a D5. Os extremos devem permanecer identificados e ser verificados com os registros de origem antes de qualquer pré-processamento.
