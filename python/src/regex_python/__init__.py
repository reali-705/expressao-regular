from __future__ import annotations

from pathlib import Path

from regex_python.escritor import escrever_arquivo_saida
from regex_python.estatistica import gerar_estatisticas
from regex_python.extrator import extrair_ocorrencias
from regex_python.leitor import ler_arquivos
from regex_python.validador import validar_ocorrencias


def main() -> None:
    data_dir = Path(__file__).resolve().parents[3] / "data"
    output_dir = Path(__file__).resolve().parents[3] / "output" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)

    arquivos = ler_arquivos(data_dir)
    escrever_arquivo_saida(output_dir / "arquivos_lidos.json", arquivos)

    ocorrencias = extrair_ocorrencias(arquivos)
    escrever_arquivo_saida(output_dir / "ocorrencias_extraidas.json", ocorrencias)

    validadas = validar_ocorrencias(ocorrencias)
    escrever_arquivo_saida(output_dir / "ocorrencias_validadas.json", validadas)

    estatisticas = gerar_estatisticas(validadas)
    escrever_arquivo_saida(output_dir / "estatisticas.json", estatisticas)

    print(f"Arquivos lidos: {len(arquivos)}")
    print(f"Ocorrencias: {estatisticas.total_ocorrencias}")
    print(f"Validas: {estatisticas.total_validas}")
    print(f"Invalidas: {estatisticas.total_invalidas}")
    print("Ocorrencias por tipo:")
    for tipo, total in estatisticas.por_tipo.items():
        print(f"\t{tipo}: {total}")
    print("Ocorrencias validas por tipo:")
    for tipo, total in estatisticas.validas_por_tipo.items():
        print(f"\t{tipo}: {total}")
    print("Ocorrencias invalidas por tipo:")
    for tipo, total in estatisticas.invalidas_por_tipo.items():
        print(f"\t{tipo}: {total}")


if __name__ == "__main__":
    main()
