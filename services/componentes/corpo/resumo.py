from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_resumo(
        conteudo,
        estilos,
        curriculo
):

    adicionar_secao(
        conteudo,
        estilos,
        "Resumo Profissional"
    )

    conteudo.append(
        Paragraph(
            curriculo.resumo,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 20)
    )