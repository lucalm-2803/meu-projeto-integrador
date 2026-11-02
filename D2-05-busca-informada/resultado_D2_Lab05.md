# Lab-04
(.venv) luciano (D02) D2-04-busca-nao-informada $ python esqueleto.py 
Formulação: problemas.diagnostico_ams:MAIOR

| Busca | Custo | Ações | Nós expandidos | Nós gerados | Prof. máx. | Segundos |
|---|---:|---:|---:|---:|---:|---:|
| largura | 2138.8 | 11 | 234781 | 243222 | 12 | 1.0531 |
| custo_uniforme | 2138.8 | 11 | 245527 | 245725 | 15 | 1.5774 |
| profundidade_limitada(limite=32) | 2186.8 | 15 | 16 | 15 | 15 | 0.0001 |
| aprofundamento_iterativo(limite=32) | 2138.8 | 11 | 132308 | 861124 | 11 | 2.2701 |

Custo e segundos arredondados. Forma: `comum.busca.comparar()` em 4.9278 s.

Lembre a ressalva de contagem (slide 20): a profundidade limitada é recursiva e não tem fronteira — nela, `nos_expandidos` conta entradas na recursão, sem repetidos. Parte da vantagem aparente dela é diferença de contagem. Registre isso na análise.

Próximo passo: cole a tabela na entrega e responda — alguma busca achou caminho mais barato que a largura? Em problemas.diagnostico_ams, por quê?

-----------------------------------------
## Resposta lab-04:
Não. Largura, custo uniforme e aprofundamento iterativo encontraram o mesmo custo: 2.138,8. A busca limitada em profundidade encontrou um caminho mais caro: 2.186,8, uma diferença de 48.

Em diagnostico_ams, o objetivo exige fazer todas as 11 verificações marcadas como essenciais (diagnostico_ams.py:113). Esse é o menor caminho possível: 11 ações. A largura minimiza o número de ações; neste caso, esse caminho também custa menos porque as 11 essenciais são obrigatórias e as verificações extras têm custo positivo. O custo uniforme, que minimiza o custo total, chega ao mesmo resultado.

A busca limitada em profundidade parou no primeiro objetivo que encontrou, com 15 ações, incluindo as quatro verificações não essenciais. Elas somam justamente 48; por isso seu caminho ficou mais caro. Isso é próprio desta instância, não uma garantia de que largura e custo uniforme sempre empatem.

-----------------------------------------

# Lab-05
(.venv) luciano (D02) D2-05-busca-informada $ python esqueleto.py 
Formulação: problemas.diagnostico_ams:MAIOR

| Busca | Custo | Ações | Nós expandidos | Nós gerados | Prof. máx. | Segundos |
|---|---:|---:|---:|---:|---:|---:|
| gulosa[admissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0013 |
| a_estrela[admissivel] | 2138.8 | 11 | 784 | 2903 | 11 | 0.0312 |
| gulosa[inadmissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0012 |
| a_estrela[inadmissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0011 |

Como ler (slide 36):
  - A estrela expandindo MAIS que o custo uniforme do lab-04? Heurística fraca.
  - A estrela com custo PIOR que o custo uniforme? A heurística superestima.
  - Antes de qualquer outra verificação: h vale zero em todo estado objetivo?
  - O item que vale nota: o parágrafo da dominância, comparando as duas
    colunas de expandidos — a evidência são os números, a explicação é sua.
    
    -----------------------------------------
## Resposta lab-05:

A primeira verificação é se `h` vale zero nos estados objetivo. Na heurística admissível, isso acontece: quando o objetivo é atingido, todas as verificações essenciais já foram feitas, então não falta custo essencial. Na inadmissível, não: em um objetivo, a fórmula fica `-2 × custo já gasto`, portanto é negativa e diferente de zero. Além disso, ela pode superestimar o custo restante em outros estados; assim, o A* com ela não tem garantia de encontrar o caminho ótimo.

Nesta execução, o A* com a heurística admissível encontrou o mesmo custo do custo uniforme do Lab-04 (2.138,8), mas expandiu muito menos nós: 784 contra 245.527. A heurística é informativa o bastante para reduzir a busca sem perder a garantia de otimalidade. O A* com a inadmissível também encontrou custo 2.138,8 neste caso, mas isso foi circunstancial: uma heurística inadmissível pode levar a uma solução mais cara em outras instâncias. A busca gulosa também encontrou esse custo aqui, sem garantia geral de otimalidade.

Quanto à dominância, os números mostram que, nesta execução, o A* com a inadmissível expandiu menos nós que com a admissível: 12 contra 784. Isso é uma comparação empírica, não uma dominância teórica. A dominância formal é comparada entre heurísticas admissíveis, verificando se uma estima pelo menos tanto quanto a outra em todo estado. A heurística inadmissível não atende a essa condição: sua estimativa `3 × custo essencial que falta - 2 × custo já gasto` pode ficar acima ou abaixo da admissível conforme o estado. Portanto, os 12 nós expandidos não significam que ela seja melhor em geral nem que preserve a solução ótima.
