import pytest

from models.curriculo import Curriculo
from models.contato import Contato


@pytest.fixture
def contato_valido():

    return Contato(
        email="teste@email.com",
        telefone="51999999999",
        cidade="Porto Alegre",
        linkedin="",
        github=""
    )


@pytest.fixture
def curriculo_valido(contato_valido):

    return Curriculo(
        nome="Norton",
        contato=contato_valido,
        resumo="Resumo válido",
        experiencias=[],
        formacoes=[],
        certificacoes=[],
        habilidades=[],
        idiomas=[],
        foto=None
    )