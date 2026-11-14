# Correlação e causalidade — AO1

## Associação observada

No conjunto de avaliação `casos-ams-60.csv` (60 casos, dos quais 20 têm
`falhou_depois = 1`), a temperatura medida e a ocorrência posterior de falha
apresentam associação positiva: correlação ponto-bisserial de Pearson
`r = 0,601` e correlação de Spearman `rho = 0,543`. A temperatura média foi
`71,81 °C` nos casos com falha posterior e `62,74 °C` nos demais.

Isso descreve uma associação neste conjunto; não demonstra que o aumento da
temperatura cause a falha.

## Duas explicações não causais plausíveis

1. **Confundimento:** tipo de máquina, carga ou regime de operação podem
   influenciar tanto a temperatura normal quanto a chance de falha. Sem
   controlar essas variáveis, parte da associação atribuída à temperatura
   pode vir dessas diferenças.
2. **Viés de seleção:** o arquivo é um conjunto de avaliação pequeno e não
   documenta uma amostragem aleatória de ordens reais. Se casos de alerta ou
   de falha foram incluídos com maior frequência, a associação pode ser mais
   forte do que seria na frota em produção.

## Limites

Os 60 casos não bastam para estabelecer causalidade nem para generalizar a
associação para a frota. A temperatura pode ser um sinal de uma falha
incipiente, mas isso também não prova a direção causal. Uma análise melhor
exigiria dados representativos, identificação da máquina, carga operacional
e validação temporal dos desfechos.
