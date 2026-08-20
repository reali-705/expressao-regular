from __future__ import annotations

from regex_python.modelos import TipoEntidade

PADROES_EXTRACAO: dict[TipoEntidade, str] = {
    TipoEntidade.EMAIL: r"\b[\w.%+\-]+@[a-zA-Z\d.\-]+\.[a-zA-Z]{2,}\b",
    TipoEntidade.TELEFONE: r"\b(?:\(?\d{2}\)? ?)?(?:9?\d{4})(-| )?\d{4}\b",
    TipoEntidade.CPF: r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
    TipoEntidade.DATA: r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    TipoEntidade.HORA: r"\b\d{1,2}:\d{2}(?::\d{2})?\b",
    TipoEntidade.DATA_HORA: r"\b\d{1,2}/\d{1,2}/\d{2,4}\s+(?:[01]?\d|2[0-3]):[0-5]\d\b",
    TipoEntidade.URL: r"\bhttps?://[^\s]+\b",
    TipoEntidade.MOEDA_BRL: r"\bR\$\s?\d{1,3}(?:\.?\d{3})*(?:,\d{2})?\b",
    TipoEntidade.NOME_PROPRIO: r"\b(?:[A-Z][a-z]{2,}\s?)+\b",
}