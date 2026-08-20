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
    inicio: int
    fim: int
    contexto: str


@dataclass(slots=True)  
class OcorrenciaValidada(OcorrenciaExtraida):
    valido: bool
    motivo: str = ""
    valor_normalizado: str = ""


@dataclass(slots=True)
class Estatisticas:
    total_ocorrencias: int = 0
    total_validas: int = 0
    total_invalidas: int = 0
    por_tipo: dict[TipoEntidade, int] = field(default_factory=dict[TipoEntidade, int])
    validas_por_tipo: dict[TipoEntidade, int] = field(
        default_factory=dict[TipoEntidade, int]
    )
    invalidas_por_tipo: dict[TipoEntidade, int] = field(
        default_factory=dict[TipoEntidade, int]
    )
    por_arquivo: dict[str, int] = field(default_factory=dict[str, int])
