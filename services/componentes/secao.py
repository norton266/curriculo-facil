from reportlab.platypus import Paragraph, Spacer


def adicionar_secao(
        conteudo,
        estilos,
        titulo
):

    conteudo.append(
        Paragraph(
            titulo,
            estilos["subtitulo"]
        )
    )

    conteudo.append(
        Spacer(1, 10)
    )