from __future__ import annotations

from pathlib import Path

from regex_python.modelos import ArquivoLido


def ler_arquivos(diretorio_data: str | Path) -> dict[str, ArquivoLido]:
    """Lê arquivos do diretório e retorna o conteúdo indexado por nome de arquivo."""
    base = Path(diretorio_data)
    if not base.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {base}")

    arquivos_lidos: dict[str, ArquivoLido] = {}
    for arquivo in sorted(base.iterdir()):
        if not arquivo.is_file():
            continue

        conteudo = arquivo.read_text(encoding="utf-8", errors="replace")
        arquivos_lidos[arquivo.name] = ArquivoLido(
            caminho=str(arquivo),
            linhas=conteudo.splitlines(),
        )

    return arquivos_lidos
