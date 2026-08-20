from __future__ import annotations

from datetime import date, time

from regex_python.modelos import OcorrenciaExtraida, OcorrenciaValidada, TipoEntidade


def validar_ocorrencias(
    ocorrencias: list[OcorrenciaExtraida],
) -> list[OcorrenciaValidada]:
    """Classifica ocorrências como válidas ou inválidas com regras iniciais."""
    return [
        OcorrenciaValidada(
            tipo=ocorrencia.tipo,
            valor=ocorrencia.valor,
            arquivo=ocorrencia.arquivo,
            linha=ocorrencia.linha,
            valido=_validar_por_tipo(ocorrencia),
        )
        for ocorrencia in ocorrencias
    ]


def _validar_por_tipo(ocorrencia: OcorrenciaExtraida) -> bool:
    if ocorrencia.tipo == TipoEntidade.DATA:
        return _validar_data(ocorrencia.valor)
    if ocorrencia.tipo == TipoEntidade.HORA:
        return _validar_hora(ocorrencia.valor)
    if ocorrencia.tipo == TipoEntidade.DATA_HORA:
        return _validar_data_hora(ocorrencia.valor)
    if ocorrencia.tipo == TipoEntidade.CPF:
        return _validar_cpf(ocorrencia.valor)

    return True


def _validar_data(valor: str) -> bool:
    dia, mes, ano = (int(parte) for parte in valor.split("/"))
    if ano < 100:
        ano += 2000 if ano <= 50 else 1900
    try:
        date(ano, mes, dia)
    except ValueError:
        return False
    return True


def _validar_hora(valor: str) -> bool:
    partes = valor.split(":")
    if len(partes) == 2:
        partes.append("00")
    elif len(partes) != 3:
        return False
    try:
        hora, minuto, segundo = map(int, partes)
        time(hora, minuto, segundo)
    except (TypeError, ValueError):
        return False
    return True


def _validar_data_hora(valor: str) -> bool:
    try:
        valor_data, valor_hora = valor.split(" ", maxsplit=1)
        data_valida = _validar_data(valor_data)
        hora_valida = _validar_hora(valor_hora)
        if data_valida and hora_valida:
            return True
    except ValueError:
        pass
    return False


def _validar_cpf(valor: str) -> bool:
    def calcular_digito(cpf_parcial: str) -> int:
        soma = sum(
            int(digito) * peso
            for digito, peso in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1))
        )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    cpf = "".join(filter(str.isdigit, valor))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    digito1 = calcular_digito(cpf[:9])
    digito2 = calcular_digito(cpf[:10])
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2
