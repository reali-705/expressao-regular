from __future__ import annotations

from typing import TypeVar

from regex_python.modelos import Estatisticas, OcorrenciaValidada, TipoEntidade

Chave = TypeVar("Chave")


def gerar_estatisticas(ocorrencias: list[OcorrenciaValidada]) -> Estatisticas:
    """Agrega contagens totais, por tipo e por arquivo."""
    estatistica = Estatisticas()
    estatistica.total_ocorrencias = len(ocorrencias)

    for ocorrencia in ocorrencias:
        _incrementar(estatistica.por_tipo, ocorrencia.tipo)
        _incrementar(estatistica.por_arquivo, ocorrencia.arquivo)

        if ocorrencia.valido:
            estatistica.total_validas += 1
            _incrementar(estatistica.validas_por_tipo, ocorrencia.tipo)
        else:
            estatistica.total_invalidas += 1
            _incrementar(estatistica.invalidas_por_tipo, ocorrencia.tipo)

    for tipo in TipoEntidade:
        estatistica.por_tipo.setdefault(tipo, 0)
        estatistica.validas_por_tipo.setdefault(tipo, 0)
        estatistica.invalidas_por_tipo.setdefault(tipo, 0)

    return estatistica


def _incrementar(
    dados: dict[Chave, int],
    chave: Chave,
) -> None:
    dados[chave] = dados.get(chave, 0) + 1
