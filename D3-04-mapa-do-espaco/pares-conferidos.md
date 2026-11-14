# O mapa do meu domínio — conferência (Laboratório 04)

Conjunto: manutencao · 384 dimensões antes da redução
Escolha registrada (slide 55): normalizado · semente da vizinhança: 20260901
Mapas: mapa-do-espaco.png (componentes principais à esquerda, vizinhança à direita) · pontos: mapa-pontos.csv

## Passo 4 — os três pares que você escolheu no mapa (slide 52)

Comando usado: `python esqueleto.py manutencao --pares 60,65 105,167 26,187`

| par | cosseno original | a vizinhança visual |
|---|---:|---|
| (60, 65) | +0.1901 | NÃO confirma |
| (105, 167) | +0.5892 | confirma |
| (26, 187) | +0.7164 | confirma |

## As quatro perguntas do slide 53

1. Os dois métodos produzem os mesmos agrupamentos?
R: Não. A PCA espalha os pontos de forma mais global e determinística; o t-SNE enfatiza vizinhanças locais e forma grupos compactos diferentes. Por exemplo, (60, 65) fica próximo na PCA, mas separado no t-SNE.

2. Há grupo que só aparece em um deles?
R: Sim. No t-SNE aparecem pequenos agrupamentos locais mais compactos que não ficam tão definidos na PCA. Esses grupos devem ser interpretados como vizinhanças locais; a distância entre grupos no t-SNE não representa necessariamente semelhança.

3. Os vizinhos visuais confirmam no cosseno original?
R: Dois dos três pares confirmam pelo critério do laboratório (cosseno >= 0.5): (105, 167) deu 0.5892 e (26, 187) deu 0.7164. O par (60, 65) não confirmou: 0.1901.

4. O que aconteceria com um vetor novo, fora do conjunto?
R: Na PCA, aplicaria ao vetor novo a mesma transformação fixa: subtrair o centro aprendido e multiplicar pelas componentes. No t-SNE deste laboratório não há projeção direta para novos vetores; seria preciso refazer a redução incluindo o novo ponto.

## O caso em que o mapa enganou (critério do slide 52)

Par e o que a figura sugeria, e o que o cosseno original disse:

R: O par (60, 65) parece próximo na PCA (distância 2D 0.2332), mas as frases tratam de componentes diferentes: soldagem dos contatos de um contator e atraso de resposta de uma válvula solenoide. O cosseno original é apenas 0.1901, portanto a proximidade visual da PCA não se confirma. No t-SNE, os pontos ficam bem mais separados.
