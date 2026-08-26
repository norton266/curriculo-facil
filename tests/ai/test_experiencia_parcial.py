from services.ai.schemas import RespostaCurriculoSchema


def test_experiencia_parcial():

    resposta = RespostaCurriculoSchema(
        mensagem="Entendi sua experiência.",
        dados={
            "experiencias": [
                {
                    "empresa": "Empresa X",
                    "periodo": "2024-2025",
                    "descricao": "Desenvolvimento de sistemas."
                }
            ]
        },
        proximo_campo="cargo"
    )

    experiencia = resposta.dados.experiencias[0]

    assert experiencia.cargo == ""
    assert experiencia.empresa == "Empresa X"
    assert experiencia.periodo == "2024-2025"
    assert experiencia.descricao == "Desenvolvimento de sistemas."