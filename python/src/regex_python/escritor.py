from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Any, cast


def escrever_arquivo_saida(
    arquivo_saida: str | Path,
    data: Any,
    *,
    formato: str = "auto",
    indent: int = 2,
) -> None:
    """Escreve texto ou JSON no arquivo de saída.

    Em `formato="auto"`, usa JSON quando o sufixo é `.json`;
    caso contrário, converte para texto.
    """
    caminho_saida = (
        Path(arquivo_saida) if isinstance(arquivo_saida, str) else arquivo_saida
    )
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    formato_normalizado = formato.lower()
    if formato_normalizado not in {"auto", "json", "texto"}:
        raise ValueError("formato deve ser 'auto', 'json' ou 'texto'")

    if formato_normalizado == "auto":
        formato_normalizado = (
            "json" if caminho_saida.suffix.lower() == ".json" else "texto"
        )

    if formato_normalizado == "json":
        conteudo = json.dumps(
            _normalizar_para_json(data),
            ensure_ascii=False,
            indent=indent,
        )
    else:
        conteudo = data if isinstance(data, str) else str(data)

    caminho_saida.write_text(conteudo, encoding="utf-8", errors="replace")


def _normalizar_para_json(valor: Any) -> Any:
    if is_dataclass(valor) and not isinstance(valor, type):
        return _normalizar_para_json(asdict(valor))
    if isinstance(valor, Enum):
        return valor.value
    if isinstance(valor, Path):
        return str(valor)
    if isinstance(valor, dict):
        valor_dict = cast(dict[Any, Any], valor)
        return {
            _normalizar_chave_json(chave): _normalizar_para_json(item)
            for chave, item in valor_dict.items()
        }
    if isinstance(valor, (list, tuple, set)):
        valor_iteravel = cast(list[Any] | tuple[Any, ...] | set[Any], valor)
        return [_normalizar_para_json(item) for item in valor_iteravel]
    return valor


def _normalizar_chave_json(chave: Any) -> str:
    if isinstance(chave, Enum):
        return str(chave.value)
    return str(chave)
