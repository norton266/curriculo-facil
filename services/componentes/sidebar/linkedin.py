from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_linkedin(
        conteudo,
        estilos,
        curriculo
):

    if not curriculo.contato.linkedin:
        return

    adicionar_secao(
        conteudo,
        estilos,
        "LinkedIn"
    )

    conteudo.append(
        Paragraph(
            curriculo.contato.linkedin,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 15)
    )