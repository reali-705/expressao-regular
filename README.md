# Multi-Language Regex Engine & Data Extractor

Projeto pessoal de estudo e engenharia prática de **Expressões Regulares (Regex)**, com implementação paralela em **Python** e **Go**.

---

## 🎯 Objetivo do Projeto

Este repositório foi criado com dois objetivos principais:

1. Colocar em prática expressões regulares em cenários realistas de dados ruidosos.
2. Implementar o mesmo pipeline em Python e, depois, em Go para comparar desempenho e ergonomia entre as linguagens.

Em resumo: a ideia é manter **paridade funcional** entre as duas versões e medir diferenças de execução de forma justa.

---

## 🎓 Contexto Acadêmico

> **Origem / Inspiração:**  
> Projeto concebido a partir da especificação prática da disciplina de *Linguagens Formais e Autômatos / Teoria da Computação* da **Universidade Federal do Pará (UFPA)**, com proposta didática formulada pelo Prof. Reginaldo Santos.

---

## ✅ Requisitos Principais do Pipeline

1. **Inspeção de Arquivos:** análise estrutural, contagem de linhas e amostragem de dados brutos.
2. **Extração de Padrões:** reconhecimento de e-mails, telefones, CPFs, datas/horários, URLs, valores monetários (BRL) e nomes próprios.
3. **Validação Estrutural:** classificação em tempo de execução de entradas sintaticamente válidas vs. inválidas/mal formatadas.
4. **Exportação e Estatísticas:** agregação quantitativa e geração de datasets consolidados em JSON e CSV.

---

## 🧱 Organização do Repositório

- `python/`: implementação Python do pipeline.
- `go/`: implementação Go do pipeline.
- `data/`: entradas brutas para testes e validação.
- `output/`: saídas geradas por linguagem.
- `docs/`: documentação complementar e anotações de benchmark.

---

## ⚙️ Estratégia de Ambientes e Execução

### Recomendação adotada

Usar cada linguagem com seu fluxo nativo e, opcionalmente, uma camada de orquestração na raiz:

- **Python:** gerenciado com **UV** (dependências, ambiente e execução).
- **Go:** gerenciado com **Go Modules** (`go.mod`).

Essa abordagem preserva boas práticas de cada ecossistema e facilita comparação entre as implementações.

---

## 📊 Plano de Comparação de Desempenho (Python vs Go)

Para comparação justa, as duas versões devem manter os mesmos critérios:

1. Mesmo conjunto de arquivos de entrada.
2. Mesmas regras de extração e validação.
3. Mesmo formato de saída para conferência de paridade.
4. Múltiplas execuções por cenário para reduzir variação.

Métricas sugeridas:

- Tempo total de execução.
- Throughput (linhas/seg ou MB/seg).
- Consumo de memória.
- Taxa de sucesso na extração/validação (consistência funcional).

---

## 🚀 Próximos Passos

1. Implementar primeiro pipeline funcional em Python (base de referência).
2. Reproduzir as mesmas regras em Go.
3. Criar rotina de benchmark padronizada.
4. Publicar resultados comparativos em `docs/`.
