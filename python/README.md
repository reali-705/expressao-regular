# Regex Python Module

Implementacao em Python do pipeline de extracao e validacao com expressoes regulares.

Este README cobre apenas o escopo do modulo Python. A visao geral do projeto
multi-linguagem esta no [README](../README.md) da raiz.

## Objetivo

- Servir como base de referencia funcional do pipeline em Python.
- Processar dados ruidosos e extrair entidades padronizadas.
- Gerar saidas consistentes para futura comparacao com a implementacao em Go.

## Requisitos

- Python 3.12+
- UV instalado no ambiente

## Setup rapido

1. Entrar na pasta do modulo:

    ```bash
    cd python
    ```

2. Sincronizar ambiente e dependencias:

    ```bash
    uv sync
    ```

3. Executar o comando registrado no projeto:

    ```bash
    uv run regex-python
    ```

No estado atual, o comando imprime uma mensagem inicial de bootstrap.

## Estrutura atual

- `pyproject.toml`: metadados do pacote e comando de entrada.
- `src/regex_python/__init__.py`: funcao main inicial.
- `uv.lock`: lockfile do ambiente.

## Proximos passos

1. Criar modulo de leitura de arquivos em data.
2. Implementar extratores regex por entidade (email, telefone, cpf, data, url, moeda, nome).
3. Adicionar validacao estrutural de cada padrao.
4. Escrever saidas em JSON e CSV dentro de output/python.
5. Cobrir regras com testes automatizados.

## Comandos uteis

- Rodar app:

  ```bash
  uv run regex-python
  ```

- Adicionar dependencia:

  ```bash
  uv add nome-da-biblioteca
  ```

- Atualizar lockfile apos mudancas:

  ```bash
  uv lock
  ```
