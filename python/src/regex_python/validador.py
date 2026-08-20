from __future__ import annotations

from datetime import date, time

from regex_python.modelos import OcorrenciaExtraida, OcorrenciaValidada, TipoEntidade


def validar_ocorrencias(
    ocorrencias: list[OcorrenciaExtraida],
) -> list[OcorrenciaValidada]:
    """Classifica ocorrências como válidas ou inválidas com regras iniciais."""
    validadas: list[OcorrenciaValidada] = []
    for ocorrencia in ocorrencias:
        valido, motivo, valor_normalizado = _validar_por_tipo(ocorrencia)
        validadas.append(
            OcorrenciaValidada(
                tipo=ocorrencia.tipo,
                valor=ocorrencia.valor,
                arquivo=ocorrencia.arquivo,
                linha=ocorrencia.linha,
                inicio=ocorrencia.inicio,
                fim=ocorrencia.fim,
                contexto=ocorrencia.contexto,
                valido=valido,
                motivo=motivo,
                valor_normalizado=valor_normalizado,
            )
        )
    return validadas


def _validar_por_tipo(ocorrencia: OcorrenciaExtraida) -> tuple[bool, str, str]:
    if ocorrencia.tipo == TipoEntidade.DATA:
        return _validar_data(ocorrencia.valor)
    if ocorrencia.tipo == TipoEntidade.HORA:
        return _validar_hora(ocorrencia.valor)
    if ocorrencia.tipo == TipoEntidade.DATA_HORA:
        return _validar_data_hora(ocorrencia.valor)

    return True, "", ocorrencia.valor


def _validar_data(valor: str) -> tuple[bool, str, str]:
    try:
        dia, mes, ano = (int(parte) for parte in valor.split("/"))
        if ano < 100:
            ano += 2000 if ano <= 50 else 1900
        data = date(ano, mes, dia)
        return True, "", data.isoformat()
    except (TypeError, ValueError):
        return False, "data invalida", valor


def _validar_hora(valor: str) -> tuple[bool, str, str]:
    partes = valor.split(":")
    if len(partes) == 2:
        partes.append("00")
    elif len(partes) != 3:
        return False, "hora invalida", valor
    try:
        hora, minuto, segundo = map(int, partes)
        horario = time(hora, minuto, segundo)
        return True, "", horario.strftime("%H:%M:%S")
    except (TypeError, ValueError):
        return False, "hora invalida", valor


def _validar_data_hora(valor: str) -> tuple[bool, str, str]:
    try:
        valor_data, valor_hora = valor.split(" ", maxsplit=1)
        data_valida, _, data_normalizada = _validar_data(valor_data)
        hora_valida, _, hora_normalizada = _validar_hora(valor_hora)
        if data_valida and hora_valida:
            return True, "", f"{data_normalizada} {hora_normalizada}"
    except ValueError:
        return False, "data_hora invalida", valor
    else:
        return False, "data_hora invalida", valor
