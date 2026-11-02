# Resultado — D2 Laboratório 06

- **Tipo de agente:** agente baseado em modelo, com estado interno. O ambiente é parcialmente observável: `falhou_depois` só é revelado depois da decisão; por isso, o agente guarda as falhas recentes por família de máquina.
- **Métrica primária:** acerto da decisão (casos com decisão igual à rotulada, sobre o total).
- **Valor:** 25/30 = 0,8333.
- **Conjunto:** `dados/meus_casos.csv`, 30 casos rotulados — 16 `seguir_operando`, 8 `parar_para_manutencao` e 6 `inspecionar_antes_de_operar`.
- **Casos com erro:** C07, C08, C16, C17 e C24.

O agente erra em C07 e C08 porque as leituras estão abaixo dos limites e o desfecho de cada falha só é incorporado ao estado depois da decisão, então ele ainda não acumulou duas falhas observadas para recomendar inspeção. Em C16, C17 e C24, a contagem de falhas recentes por família generaliza o risco entre máquinas da mesma família e provoca inspeções que os rótulos desses casos não recomendam.

-------------------------------------

(.venv) luciano (D02) D2-06-agente-baseline $ python medir.py 
Métrica primária: acerto da decisão (casos com decisão igual à rotulada, sobre o total)
Valor: 25/30 = 0.8333
Conjunto: dados/meus_casos.csv — 30 casos rotulados {'seguir_operando': 16, 'parar_para_manutencao': 8, 'inspecionar_antes_de_operar': 6}
Onde erra (o rótulo que o agente não deu):
  caso C07: decidiu seguir_operando, correto era inspecionar_antes_de_operar
  caso C08: decidiu seguir_operando, correto era inspecionar_antes_de_operar
  caso C16: decidiu inspecionar_antes_de_operar, correto era seguir_operando
  caso C17: decidiu inspecionar_antes_de_operar, correto era seguir_operando
  caso C24: decidiu inspecionar_antes_de_operar, correto era seguir_operando
  
  
  (.venv) luciano (D02) D2-06-agente-baseline $ python -m pytest teste.py -q
..........                                                                                                    [100%]
