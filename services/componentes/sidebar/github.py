from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_github(
        conteudo,
        estilos,
        curriculo
):

    if not curriculo.contato.github:
        return

    adicionar_secao(
        conteudo,
        estilos,
        "GitHub"
    )

    conteudo.append(
        Paragraph(
            curriculo.contato.github,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 15)
    )