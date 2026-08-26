from services.ai.schemas import (
    RespostaCurriculoSchema
)


def test_resposta_curriculo_valida():

    resposta = RespostaCurriculoSchema(
        mensagem="Qual é o seu nome?",

        dados={
            "nome": "João"
        },

        proximo_campo="email"
    )

    assert resposta.mensagem == "Qual é o seu nome?"
    assert resposta.dados.nome == "João"
    assert resposta.proximo_campo == "email"


def test_experiencia_valida():

    resposta = RespostaCurriculoSchema(
        mensagem="Entendi sua experiência.",

        dados={
            "experiencias": [
                {
                    "cargo": "Desenvolvedor",
                    "empresa": "Empresa X",
                    "periodo": "2024-2025",
                    "descricao": "Desenvolvimento de sistemas."
                }
            ]
        },

        proximo_campo="formacoes"
    )

    experiencia = (
        resposta
        .dados
        .experiencias[0]
    )

    assert experiencia.cargo == "Desenvolvedor"
    assert experiencia.empresa == "Empresa X"


def test_listas_vazias():

    resposta = RespostaCurriculoSchema(
        mensagem="Vamos começar.",
        dados={},
        proximo_campo="nome"
    )

    assert resposta.dados.experiencias == []
    assert resposta.dados.formacoes == []
    assert resposta.dados.certificacoes == []
    assert resposta.dados.habilidades == []
    assert resposta.dados.idiomas == []