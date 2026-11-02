"""Baseline de manutenção industrial e medição sobre os casos rotulados."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import date
from pathlib import Path

CAMINHO_DOS_CASOS = (
    Path(__file__).resolve().parents[2]
    / "D2-06-agente-baseline"
    / "dados"
    / "meus_casos.csv"
)

LIMITE_VIBRACAO = 7.0
LIMITE_TEMPERATURA = 78.0
FALHAS_PARA_INSPECAO = 2
JANELA_DIAS = 7


class EstadoDaFrota:
    """Falhas observadas por família de máquina dentro da janela recente."""

    def __init__(self, janela_dias: int = JANELA_DIAS) -> None:
        self._janela = janela_dias
        self._falhas: list[tuple[str, date]] = []
        self._ultima_data: date | None = None

    def falhas_recentes(self, familia: str) -> int:
        if self._ultima_data is None:
            return 0
        limite = self._ultima_data.toordinal() - self._janela
        return sum(
            1
            for familia_vista, dia in self._falhas
            if familia_vista == familia and dia.toordinal() >= limite
        )

    def registrar_desfecho(self, registro: dict) -> None:
        self._ultima_data = date.fromisoformat(registro["data"])
        if int(registro.get("falhou_depois", 0)) == 1:
            self._falhas.append((registro["tipo_maquina"], self._ultima_data))


def decidir(registro: dict, estado: EstadoDaFrota) -> str:
    """Aplica as regras reativa e baseada no histórico recente da frota."""
    if (
        registro["vibracao_mm_s"] > LIMITE_VIBRACAO
        or registro["temperatura_c"] > LIMITE_TEMPERATURA
    ):
        return "parar_para_manutencao"
    if estado.falhas_recentes(registro["tipo_maquina"]) >= FALHAS_PARA_INSPECAO:
        return "inspecionar_antes_de_operar"
    return "seguir_operando"


def carregar_casos(caminho: str | Path) -> list[dict]:
    """Lê casos rotulados em ordem cronológica e converte as colunas numéricas."""
    with Path(caminho).open(encoding="utf-8-sig", newline="") as arquivo:
        casos = list(csv.DictReader(arquivo))
    casos.sort(key=lambda registro: registro["data"])
    for registro in casos:
        registro["idade_meses"] = int(registro["idade_meses"])
        registro["temperatura_c"] = float(registro["temperatura_c"])
        registro["vibracao_mm_s"] = float(registro["vibracao_mm_s"])
        registro["horas_desde_manutencao"] = float(
            registro["horas_desde_manutencao"]
        )
        registro["falhou_depois"] = int(registro["falhou_depois"])
    return casos


def medir(caminho: str | Path = CAMINHO_DOS_CASOS) -> dict:
    """Executa o agente em sequência e devolve acertos, conjunto e erros."""
    casos = carregar_casos(caminho)
    estado = EstadoDaFrota()
    acertos = 0
    erros = []
    for registro in casos:
        decisao = decidir(registro, estado)
        correta = registro["acao_correta"]
        if decisao == correta:
            acertos += 1
        else:
            erros.append(
                {
                    "id_caso": registro["id_caso"],
                    "decidiu": decisao,
                    "correta": correta,
                }
            )
        estado.registrar_desfecho(registro)

    total = len(casos)
    rotulos = Counter(registro["acao_correta"] for registro in casos)
    return {
        "caminho": str(caminho),
        "total": total,
        "acertos": acertos,
        "valor": acertos / total if total else 0.0,
        "distribuicao": dict(rotulos),
        "erros": erros,
    }


def imprimir(resultado: dict) -> None:
    print("Métrica primária: acerto da decisão "
          "(casos com decisão igual à rotulada, sobre o total)")
    print(
        f"Valor: {resultado['acertos']}/{resultado['total']} = "
        f"{round(resultado['valor'], 4)}"
    )
    print(
        f"Conjunto: {resultado['caminho']} — {resultado['total']} casos "
        f"rotulados {resultado['distribuicao']}"
    )
    if resultado["erros"]:
        print("Onde erra (o rótulo que o agente não deu):")
        for erro in resultado["erros"]:
            print(
                f"  caso {erro['id_caso']}: decidiu {erro['decidiu']}, "
                f"correto era {erro['correta']}"
            )
    else:
        print("Onde erra: em nenhum dos casos.")


if __name__ == "__main__":
    imprimir(medir())
