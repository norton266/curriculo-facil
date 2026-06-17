from reportlab.platypus import Paragraph, Spacer


def adicionar_cabecalho(
        conteudo,
        estilos,
        nome,
        telefone,
        email,
        cidade
):

    conteudo.append(
        Paragraph(
            nome.upper(),
            estilos["titulo"]
        )
    )

    conteudo.append(
        Paragraph(
            f"{telefone} | {email} | {cidade}",
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 25)
    )