from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_contato(
        conteudo,
        estilos,
        curriculo
):

    adicionar_secao(
        conteudo,
        estilos,
        "Contato"
    )

    conteudo.append(
        Paragraph(
            curriculo.contato.telefone,
            estilos["normal"]
        )
    )

    conteudo.append(
        Paragraph(
            curriculo.contato.email,
            estilos["normal"]
        )
    )

    conteudo.append(
        Paragraph(
            curriculo.contato.cidade,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 15)
    )