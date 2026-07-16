from models.curriculo import Curriculo

from services.validators.curriculo_validator import (
    validar_curriculo
)


def test_curriculo_sem_nome_deve_gerar_erro(curriculo_valido):

    curriculo_valido.nome = ""

    erros = validar_curriculo(curriculo_valido)

    assert "nome" in erros


def test_curriculo_sem_email_deve_gerar_erro(curriculo_valido):

    curriculo_valido.contato.email = ""

    erros = validar_curriculo(curriculo_valido)

    assert "email" in erros


def test_curriculo_sem_resumo_deve_gerar_erro(curriculo_valido):

    curriculo_valido.resumo = ""

    erros = validar_curriculo(curriculo_valido)

    assert "resumo" in erros


def test_curriculo_valido_nao_deve_gerar_erros(curriculo_valido):

    erros = validar_curriculo(curriculo_valido)

    assert erros == {}