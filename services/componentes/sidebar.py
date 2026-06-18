from reportlab.platypus import (
    Paragraph,
    Spacer,
    Image
)

from services.componentes.secao import adicionar_secao
from services.componentes.lista import adicionar_lista
from services.componentes.foto import adicionar_foto


def adicionar_sidebar(
        conteudo,
        estilos,
        curriculo
):

    # FOTO

    adicionar_foto(
        conteudo,
        curriculo.foto
    )

    conteudo.append(
        Spacer(1, 20)
    )

    conteudo.append(
        Spacer(1, 20)
    )

    # CONTATO

    adicionar_secao(
        conteudo,
        estilos,
        "Contato"
    )

    conteudo.append(
        Paragraph(
            curriculo.telefone,
            estilos["normal"]
        )
    )

    conteudo.append(
        Paragraph(
            curriculo.email,
            estilos["normal"]
        )
    )

    conteudo.append(
        Paragraph(
            curriculo.cidade,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 15)
    )

    # LINKEDIN

    if curriculo.linkedin:

        adicionar_secao(
            conteudo,
            estilos,
            "LinkedIn"
        )

        conteudo.append(
            Paragraph(
                curriculo.linkedin,
                estilos["normal"]
            )
        )

        conteudo.append(
            Spacer(1, 15)
        )

    # GITHUB

    if curriculo.github:

        adicionar_secao(
            conteudo,
            estilos,
            "GitHub"
        )

        conteudo.append(
            Paragraph(
                curriculo.github,
                estilos["normal"]
            )
        )

        conteudo.append(
            Spacer(1, 15)
        )

    # HABILIDADES

    adicionar_lista(
        conteudo,
        estilos,
        "Habilidades",
        curriculo.habilidades
    )

    # IDIOMAS

    adicionar_lista(
        conteudo,
        estilos,
        "Idiomas",
        curriculo.idiomas
    )