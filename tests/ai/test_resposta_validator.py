from services.ai.resposta_validator import (
    validar_resposta,
    interpretar_resposta
)


def resposta_valida():

    return {
        "mensagem": "Qual é o seu nome?",
        "dados": {
            "nome": "João"
        },
        "proximo_campo": "email"
    }


def test_resposta_valida():

    erros = validar_resposta(
        resposta_valida()
    )

    assert erros == []


def test_resposta_sem_mensagem():

    resposta = resposta_valida()

    del resposta["mensagem"]

    erros = validar_resposta(
        resposta
    )

    assert "A resposta não possui o campo 'mensagem'." in erros


def test_dados_deve_ser_objeto():

    resposta = resposta_valida()

    resposta["dados"] = "João"

    erros = validar_resposta(
        resposta
    )

    assert "O campo 'dados' deve ser um objeto." in erros


def test_experiencias_deve_ser_lista():

    resposta = resposta_valida()

    resposta["dados"]["experiencias"] = "programador"

    erros = validar_resposta(
        resposta
    )

    assert "O campo 'experiencias' deve ser uma lista." in erros


def test_lista_de_habilidades_deve_conter_strings():

    resposta = resposta_valida()

    resposta["dados"]["habilidades"] = [
        "Python",
        123
    ]

    erros = validar_resposta(
        resposta
    )

    assert (
        "Os itens de 'habilidades' devem ser strings."
        in erros
    )


def test_campo_desconhecido():

    resposta = resposta_valida()

    resposta["dados"]["salario"] = "R$ 5.000"

    erros = validar_resposta(
        resposta
    )

    assert (
        "Campo desconhecido em 'dados': salario"
        in erros
    )


def test_json_invalido():

    dados, erros = interpretar_resposta(
        "isso não é json"
    )

    assert dados is None
    assert len(erros) == 1


def test_interpretar_json_valido():

    import json

    texto = json.dumps(
        resposta_valida()
    )

    dados, erros = interpretar_resposta(
        texto
    )

    assert erros == []
    assert dados["dados"]["nome"] == "João"