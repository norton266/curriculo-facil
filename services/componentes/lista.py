from reportlab.platypus import (
    Paragraph,
    ListFlowable,
    ListItem,
    Spacer
)

from services.componentes.secao import adicionar_secao


def adicionar_lista(
        conteudo,
        estilos,
        titulo,
        itens,
        
):

    adicionar_secao(
        conteudo,
        estilos,
        titulo
    )

    lista = []

    for item in itens:

        lista.append(
            ListItem(
                Paragraph(
                    item,
                    estilos["normal"]
                )
            )
        )

    conteudo.append(
        ListFlowable(lista)
    )

    conteudo.append(
        Spacer(1, 20)
    )