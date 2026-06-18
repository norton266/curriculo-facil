from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_formacoes(
        conteudo,
        estilos,
        formacoes
):

    adicionar_secao(
        conteudo,
        estilos,
        "Formação"
    )

    for formacao in formacoes:

        conteudo.append(
            Paragraph(
                formacao.curso,
                estilos["cargo"]
            )
        )

        conteudo.append(
            Paragraph(
                formacao.instituicao,
                estilos["normal"]
            )
        )

        conteudo.append(
            Spacer(1, 10)
        )