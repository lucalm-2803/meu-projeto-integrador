# Anotações — Laboratório 02, a descida à mão

> O critério do slide 11: as quatro perguntas respondidas por escrito, com o
> número que sustenta cada resposta. Preencha a tabela rodando o esqueleto
> com as três taxas do slide 12 e copiando a última linha de cada execução.

## A última linha de cada taxa

| Taxa | Última linha da saída (perda, w, b) |
|---|---|
| 0,001 | passo  200 perda 22462.1 w 215.016 b -17.7381 |
| 0,1 | passo  200 perda 0.752176 w 300.008 b 4.91185 |
| 1,5 | passo  200 perda inf w -3.12216e+190 b 4.826e+189 |

## As quatro perguntas do slide 11

**1. A perda está caindo a cada passo, ou oscilando?**

R: 
python esqueleto.py --taxa 0.001
passo  200 perda 22462.1 w 215.016 b -17.7381
A perda foi caindo lentamente até o último passo.

python esqueleto.py
passo  200 perda 0.752176 w 300.008 b 4.91185
A perda começou caindo até chegar em seu valor mínimo e então ficou estabilizada.

python esqueleto.py --taxa 1.5
passo  200 perda inf w -3.12216e+190 b 4.826e+189
Neste caso a perda ficou oscilando desde os primeiros passos.

**2. Ela estabiliza, ou continua descendo até o fim?**

R: 
taxa 0,001: A perda continuou caindo até o último passo. Se houvessem mais poassos ela continuaria caindo.

taxa 0,1: Ela caiu até o passo 52, depois se estabilizou em seu valor mínimo.

taxa: 1,5: A perda não se estabilizou, ela ficou variando bastante.

**3. Os pesos encontrados batem com os que geraram os dados?**

R:
- Taxa 0,1: sim, aproximadamente — w=300.008 e b=4.91185, perto dos valores verdadeiros (300 e 5).
- Taxa 0,001: ainda não — w=215.016 e b=-17.7381 após 200 passos; a taxa baixa não deu tempo de convergir.
- Taxa 1,5: não — w=-3.12216e190 e b=4.826e189, valores divergentes.

**4. Se algo divergiu, qual foi o primeiro passo estranho?**

R:
- Taxa 0,1: nenhum; a perda caiu e estabilizou perto de 0.752176.
- Taxa 0,001: nenhum aumento ou oscilação; a perda continuou caindo, mas lentamente.
- Taxa 1,5: no passo 2, a perda subiu de 284802 (passo 1) para 2.14358e7. Continuou crescendo até virar `inf` no passo 161.
