from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class TipoEntidade(str, Enum):
    EMAIL = "email"
    TELEFONE = "telefone"
    CPF = "cpf"
    DATA = "data"
    HORA = "hora"
    DATA_HORA = "data_hora"
    URL = "url"
    MOEDA_BRL = "moeda_brl"
    NOME_PROPRIO = "nome_proprio"


def _mapa_tipos_zerado() -> dict[TipoEntidade, int]:
    return {tipo: 0 for tipo in TipoEntidade}


@dataclass(slots=True)
class ArquivoLido:
    caminho: str
    linhas: list[str]


@dataclass(slots=True)
class OcorrenciaExtraida:
    tipo: TipoEntidade
    valor: str
    arquivo: str
    linha: int


@dataclass(slots=True)
class OcorrenciaValidada(OcorrenciaExtraida):
    valido: bool


@dataclass(slots=True)
class Estatisticas:
    total_ocorrencias: int = 0
    total_validas: int = 0
    total_invalidas: int = 0
    por_tipo: dict[TipoEntidade, int] = field(default_factory=_mapa_tipos_zerado)
    validas_por_tipo: dict[TipoEntidade, int] = field(
        default_factory=_mapa_tipos_zerado
    )
    invalidas_por_tipo: dict[TipoEntidade, int] = field(
        default_factory=_mapa_tipos_zerado
    )
    por_arquivo: dict[str, int] = field(default_factory=dict[str, int])
    tempo_leitura: float = 0.0
    tempo_extracao: float = 0.0
    tempo_validacao: float = 0.0
    tempo_estatisticas: float = 0.0
    tempo_escrita: float = 0.0
    tempo_total: float = 0.0
