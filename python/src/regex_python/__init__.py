from __future__ import annotations

from pathlib import Path
from time import perf_counter

from regex_python.escritor import escrever_arquivo_saida
from regex_python.estatistica import gerar_estatisticas
from regex_python.extrator import extrair_ocorrencias
from regex_python.leitor import ler_arquivos
from regex_python.modelos import Estatisticas
from regex_python.validador import validar_ocorrencias


def main() -> None:
    inicio = perf_counter()

    data_dir = Path(__file__).resolve().parents[3] / "data"
    output_dir = Path(__file__).resolve().parents[3] / "output" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)
    estatistica = Estatisticas()

    inicio_leitura = perf_counter()
    arquivos = ler_arquivos(data_dir)
    fim_leitura = perf_counter()
    estatistica.tempo_leitura = fim_leitura - inicio_leitura

    inicio_extracao = perf_counter()
    ocorrencias = extrair_ocorrencias(arquivos)
    fim_extracao = perf_counter()
    estatistica.tempo_extracao = fim_extracao - inicio_extracao

    inicio_validacao = perf_counter()
    validadas = validar_ocorrencias(ocorrencias)
    fim_validacao = perf_counter()
    estatistica.tempo_validacao = fim_validacao - inicio_validacao

    inicio_estatisticas = perf_counter()
    estatisticas = gerar_estatisticas(estatistica, validadas)
    fim_estatisticas = perf_counter()
    estatistica.tempo_estatisticas = fim_estatisticas - inicio_estatisticas

    inicio_escrita = perf_counter()
    escrever_arquivo_saida(output_dir / "arquivos_lidos.json", arquivos)
    escrever_arquivo_saida(output_dir / "ocorrencias_validadas.json", validadas)
    fim_escrita = perf_counter()
    estatistica.tempo_escrita = fim_escrita - inicio_escrita

    fim = perf_counter()
    estatistica.tempo_total = fim - inicio

    escrever_arquivo_saida(output_dir / "estatisticas.json", estatisticas)

    print(f"Arquivos lidos: {len(arquivos)}")
    print(f"Ocorrencias: {estatisticas.total_ocorrencias}")
    print(f"Validas: {estatisticas.total_validas}")
    print(f"Invalidas: {estatisticas.total_invalidas}")
    print("Ocorrencias por tipo:")
    for tipo, total in estatisticas.por_tipo.items():
        print(f"\t{tipo.value}: {total}")
    print("Ocorrencias validas por tipo:")
    for tipo, total in estatisticas.validas_por_tipo.items():
        print(f"\t{tipo.value}: {total}")
    print("Ocorrencias invalidas por tipo:")
    for tipo, total in estatisticas.invalidas_por_tipo.items():
        print(f"\t{tipo.value}: {total}")
    print(f"Tempo de leitura: {estatistica.tempo_leitura:.4f} segundos")
    print(f"Tempo de extração: {estatistica.tempo_extracao:.4f} segundos")
    print(f"Tempo de validação: {estatistica.tempo_validacao:.4f} segundos")
    print(
        f"Tempo de geração de estatísticas: {estatistica.tempo_estatisticas:.4f} segundos"
    )
    print(f"Tempo de escrita: {estatistica.tempo_escrita:.4f} segundos")
    print(f"Tempo total: {estatistica.tempo_total:.4f} segundos")


if __name__ == "__main__":
    main()
