from __future__ import annotations

import re

from regex_python.modelos import ArquivoLido, OcorrenciaExtraida
from regex_python.padroes import PADROES_EXTRACAO as PADROES


def extrair_ocorrencias(arquivos: dict[str, ArquivoLido]) -> list[OcorrenciaExtraida]:
    """Extrai ocorrências por regex e retorna uma lista plana para validação posterior."""
    return [
        OcorrenciaExtraida(
            tipo=tipo,
            valor=match.group(0),
            arquivo=nome_arquivo,
            linha=numero_linha,
            inicio=match.start(),
            fim=match.end(),
            contexto=linha,
        )
        for nome_arquivo, arquivo in arquivos.items()
        for numero_linha, linha in enumerate(arquivo.linhas, start=1)
        for tipo, padrao in PADROES.items()
        for match in re.finditer(padrao, linha)
    ]
