# Regex Python Module

Implementacao em Python do pipeline de extracao e validacao com expressoes
regulares.

Este README cobre apenas o escopo do modulo Python. A visao geral do projeto
multi-linguagem esta no [README](../README.md) da raiz.

## Objetivo

- Extrair entidades de dados textuais com regex.
- Validar regras semanticas apos a extracao.
- Gerar arquivos de saida em JSON para analise posterior.
- Medir tempo total e por etapa do pipeline.

## Requisitos

- Python 3.12+
- UV instalado no ambiente

## Execucao rapida

1. Entrar na pasta do modulo:

    ```bash
    cd python
    ```

2. Sincronizar ambiente e dependencias:

    ```bash
    uv sync
    ```

3. Executar o pipeline:

    ```bash
    uv run regex-python
    ```

As saidas sao geradas em `../output/python`:

- `arquivos_lidos.json`
- `ocorrencias_validadas.json`
- `estatisticas.json`

## Estrutura de diretorios e modulos

```text
python/
├─ pyproject.toml
├─ uv.lock
├─ README.md
└─ src/
    └─ regex_python/
        ├─ __init__.py
        ├─ modelos.py
        ├─ leitor.py
        ├─ extrator.py
        ├─ padroes.py
        ├─ validador.py
        ├─ estatistica.py
        └─ escritor.py
```

Resumo de cada modulo:

- `__init__.py`: ponto de entrada do pipeline; orquestra leitura, extracao,
  validacao, estatisticas, escrita de saidas e cronometra tempos por etapa.
- `modelos.py`: modelos de dados (`dataclass`) e tipos centrais do dominio,
  como `TipoEntidade`, ocorrencias e estatisticas.
- `leitor.py`: leitura dos arquivos de entrada do diretorio de dados.
- `extrator.py`: aplicacao dos padroes regex para gerar ocorrencias extraidas.
- `padroes.py`: dicionario central de regex genericas usadas na extracao.
- `validador.py`: regras semanticas por tipo (ex.: data, hora, data_hora, CPF).
- `estatistica.py`: agregacao de contagens totais, por tipo, por arquivo e
  campos de tempo acumulados.
- `escritor.py`: escrita de saida em texto/JSON com normalizacao de tipos
  Python para serializacao.

## Fluxo do pipeline

1. Le os arquivos de `../data`.
2. Extrai ocorrencias com regex generica.
3. Valida ocorrencias com regras especificas.
4. Agrega estatisticas de qualidade e volume.
5. Persiste resultados em JSON no diretorio de saida.
6. Exibe resumo e tempos no terminal.
