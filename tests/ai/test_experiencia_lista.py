import pytest
from pydantic import ValidationError

from services.ai.schemas import RespostaCurriculoSchema


def test_experiencias_deve_ser_lista():

    with pytest.raises(ValidationError):

        RespostaCurriculoSchema(
            mensagem="Experiência recebida.",
            dados={
                "experiencias": "Trabalhei como desenvolvedor"
            },
            proximo_campo="formacoes"
        )