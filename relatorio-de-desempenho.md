# Relatório de desempenho da linha de base

**Projeto:** AMS — Assistente de Manutenção Segura · **Data da medição:** 02/11/2026

## 1. A métrica primária

Acerto da decisão: número de casos em que a ação decidida pelo agente coincide com a ação rotulada, dividido pelo total de casos rotulados.

## 2. O valor

**25/30 = 0,8333 (83,33%)**.

## 3. O conjunto

Arquivo `D2-06-agente-baseline/dados/meus_casos.csv`: 30 casos rotulados, com datas de 01/04/2026 a 16/04/2026. A distribuição é: 16 `seguir_operando`, 8 `parar_para_manutencao` e 6 `inspecionar_antes_de_operar`. São casos de avaliação rotulados, não 30 ordens reais nem o conjunto de 200 ordens mencionado como meta de desempenho no `agent-spec.md`.

## 4. Onde o agente erra

```text
caso C07: decidiu seguir_operando, correto era inspecionar_antes_de_operar
caso C08: decidiu seguir_operando, correto era inspecionar_antes_de_operar
caso C16: decidiu inspecionar_antes_de_operar, correto era seguir_operando
caso C17: decidiu inspecionar_antes_de_operar, correto era seguir_operando
caso C24: decidiu inspecionar_antes_de_operar, correto era seguir_operando
```

Os erros formam dois padrões. Em C07 e C08, as leituras atuais não ultrapassam os limites e a regra de inspeção depende de duas falhas recentes já observadas na família da máquina. Como o desfecho de cada caso só é revelado depois da decisão, o agente ainda não tinha acumulado as duas observações necessárias. Em C16, C17 e C24, o histórico da família aciona a inspeção em máquinas cujos rótulos indicam que poderiam seguir operando.

A linha de base não incorpora o desfecho futuro antes de decidir, como é correto nesse ciclo, mas usa o histórico da família como aproximação do risco de cada máquina. Isso explica tanto os dois casos em que a evidência ainda não estava disponível quanto os três falsos alarmes por generalização entre máquinas. O conjunto é pequeno e rotulado; portanto, o resultado é uma referência inicial, não uma estimativa de desempenho em produção.

## 5. Tabela comparativa de busca

| Busca | Custo | Ações | Nós expandidos | Nós gerados | Prof. máx. | Segundos |
|---|---:|---:|---:|---:|---:|---:|
| largura | 2138.8 | 11 | 234781 | 243222 | 12 | 1.0531 |
| custo_uniforme | 2138.8 | 11 | 245527 | 245725 | 15 | 1.5774 |
| profundidade_limitada(limite=32) | 2186.8 | 15 | 16 | 15 | 15 | 0.0001 |
| aprofundamento_iterativo(limite=32) | 2138.8 | 11 | 132308 | 861124 | 11 | 2.2701 |
| gulosa[admissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0013 |
| a_estrela[admissivel] | 2138.8 | 11 | 784 | 2903 | 11 | 0.0312 |
| gulosa[inadmissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0012 |
| a_estrela[inadmissivel] | 2138.8 | 11 | 12 | 110 | 11 | 0.0011 |

O A* com a heurística admissível manteve o custo ótimo de 2.138,8, igual ao custo uniforme, e expandiu 784 nós em vez de 245.527: **244.743 a menos (cerca de 99,68%)**. A heurística soma o custo das verificações essenciais ainda não feitas; como elas são obrigatórias e a estimativa não supera o custo restante, o A* pode priorizar estados promissores sem perder a garantia de custo ótimo. A busca limitada em profundidade encontrou um caminho de custo 2.186,8, mas sua contagem recursiva não mantém uma fronteira nem contabiliza repetidos como as demais; seus 16 nós expandidos não são diretamente comparáveis.

## 6. Conferindo o conteúdo para a entrega

(.venv) luciano (D02) D2-08-fechar-a-n2 $ python conferir-entrega.py 
Conferindo a entrega final em /home/luciano/CEDAGI/meu-projeto-integrador

  1. agent-spec.md          ✅  `agent-spec.md` com 7 das 7 seções (agent-spec.md)
  2. baseline.py            ✅  `baseline.py` encontrado e compilando (src/ams/baseline.py)
     o baseline mora em um pacote: chame com `python -m ams.baseline`
  3. relatório de desempenho ✅  relatório de desempenho preenchido (relatorio-de-desempenho.md)
  4. tabela de busca        ✅  tabela de busca com 8 linhas (relatorio-de-desempenho.md)
  5. análise escrita        ✅  análise escrita encontrada (analise.md)
  6. pytest do repositório  ✅  pytest: -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

Cinco itens de pé e testes verdes.
Entregue pelo Moodle até a véspera da primeira sexta da D3, às 23h59.
A data exata desta turma está na tarefa do Moodle.

