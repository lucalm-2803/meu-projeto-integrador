"""Arquivo de apoio parcial para a AO1 da D3: compara a linha de base (A) com a sua variante B.

Fica na pasta ao1/, junto com o arquivo de casos. Rode com o .venv ativo:
    cd ao1
    python ao1.py
"""
import csv
import sys
import time
from pathlib import Path

# Do próprio projeto, src/ams/baseline.py:
# decidir() é a variante A; EstadoDaFrota guarda as falhas recentes; carregar_casos() lê o CSV.
# Seus 60 casos rotulados (ou o casos-ams-60.csv do pacote do E2).
PASTA = Path(__file__).resolve().parent
ARQUIVO_DE_CASOS = PASTA / "casos-ams-60.csv"
RAIZ = PASTA.parent
sys.path.insert(0, str(RAIZ / "src"))

import numpy as np  # noqa: E402

from ams.baseline import EstadoDaFrota, carregar_casos, decidir  # noqa: E402

# --- Variante B ---------------------------------------------------------------
# Um agente parecido com a variante A (decidir() de src/ams/baseline.py), com uma
# regra nova ou bem diferente. Tem que mudar o comportamento: ajustar um limite
# em poucos décimos não conta. Abaixo está a A, como ponto de partida.
#
# A mudança da B: acrescentar uma inspeção preventiva quando já passaram
# mais de 180 horas desde a manutenção. Esse limite é uma hipótese de teste,
# não uma política operacional validada.

def decidir_b(caso, estado):
    vibracao = caso["vibracao_mm_s"]
    temperatura = caso["temperatura_c"]

    if vibracao > 7.0 or temperatura > 78:
        return "parar_para_manutencao"
    if caso["horas_desde_manutencao"] > 180:
        return "inspecionar_antes_de_operar"
    if estado.falhas_recentes(caso["tipo_maquina"]) >= 2:
        return "inspecionar_antes_de_operar"
    return "seguir_operando"


# --- Acertos de A e B nos mesmos casos (item 1 do enunciado) -------------------
# 1 = acertou a ação, 0 = errou. Grava o acertos.csv que os labs 05 e 06 leem.

def contar_acertos(casos, funcao_de_decisao):
    estado = EstadoDaFrota()
    acertos = []
    for caso in casos:
        decisao = funcao_de_decisao(caso, estado)
        if decisao == caso["acao_correta"]:
            acertos.append(1)
        else:
            acertos.append(0)
        estado.registrar_desfecho(caso)   # o agente fica sabendo se a máquina falhou
    return acertos


casos = carregar_casos(ARQUIVO_DE_CASOS)
acertos_a = contar_acertos(casos, decidir)
acertos_b = contar_acertos(casos, decidir_b)

with (PASTA / "acertos.csv").open("w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["linha_de_base", "variante_b"])
    for i in range(len(casos)):
        escritor.writerow([acertos_a[i], acertos_b[i]])

print(len(casos), "casos")
print("A acertou", sum(acertos_a), "· B acertou", sum(acertos_b))
for i in range(len(casos)):
    if acertos_a[i] != acertos_b[i]:
        print("discordam no", casos[i]["id_caso"], "· A:", acertos_a[i], "· B:", acertos_b[i])

if acertos_a == acertos_b:
    print("A e B acertaram os mesmos casos; confira se a regra nova da B foi aplicada.")


# --- Latência da linha de base, p50 e p95 (item 2 do enunciado) ----------------
# Cronometra cada decisão, passando 50 vezes pelos casos.

variantes = (("A", decidir), ("B", decidir_b))
tempos_por_variante = {nome: [] for nome, _ in variantes}

for _, funcao in variantes:
    estado = EstadoDaFrota()
    for caso in casos:
        funcao(caso, estado)
        estado.registrar_desfecho(caso)

for rodada in range(50):
    ordem = variantes if rodada % 2 == 0 else variantes[::-1]
    for nome, funcao in ordem:
        estado = EstadoDaFrota()
        for caso in casos:
            inicio = time.perf_counter()
            funcao(caso, estado)
            tempos_por_variante[nome].append(
                (time.perf_counter() - inicio) * 1_000_000)
            estado.registrar_desfecho(caso)

for nome, _ in variantes:
    tempos = np.array(tempos_por_variante[nome])
    print(f"latência da variante {nome} (µs) em {len(tempos)} decisões: "
          f"p50 {np.percentile(tempos, 50):.1f} · "
          f"p95 {np.percentile(tempos, 95):.1f} · "
          f"média {np.mean(tempos):.1f} · máximo {np.max(tempos):.1f}")


# O intervalo de confiança e o tamanho de amostra ficam no notebook
# (depois do E3, entregues com a N2).
