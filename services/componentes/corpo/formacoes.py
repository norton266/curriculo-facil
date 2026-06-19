from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_formacoes(
        conteudo,
        estilos,
        curriculo
):

    adicionar_secao(
        conteudo,
        estilos,
        "Formação"

    )

    for formacao in curriculo.formacoes:

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
            Spacer(1, 15)
        )