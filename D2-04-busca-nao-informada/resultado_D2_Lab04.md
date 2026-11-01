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

Não. Largura, custo uniforme e aprofundamento iterativo encontraram o mesmo custo: 2.138,8. A busca limitada em profundidade encontrou um caminho mais caro: 2.186,8, uma diferença de 48.

Em diagnostico_ams, o objetivo exige fazer todas as 11 verificações marcadas como essenciais (diagnostico_ams.py:113). Esse é o menor caminho possível: 11 ações. A largura minimiza o número de ações; neste caso, esse caminho também custa menos porque as 11 essenciais são obrigatórias e as verificações extras têm custo positivo. O custo uniforme, que minimiza o custo total, chega ao mesmo resultado.

A busca limitada em profundidade parou no primeiro objetivo que encontrou, com 15 ações, incluindo as quatro verificações não essenciais. Elas somam justamente 48; por isso seu caminho ficou mais caro. Isso é próprio desta instância, não uma garantia de que largura e custo uniforme sempre empatem.
