from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao
from services.componentes.experiencias import adicionar_experiencias
from services.componentes.formacoes import adicionar_formacoes
from services.componentes.lista import adicionar_lista


def adicionar_corpo_principal(
        conteudo,
        estilos,
        curriculo
):

    # RESUMO

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

    # EXPERIÊNCIAS

    adicionar_experiencias(
        conteudo,
        estilos,
        curriculo.experiencias
    )

    # FORMAÇÕES

    adicionar_formacoes(
        conteudo,
        estilos,
        curriculo.formacoes
    )

    # CERTIFICAÇÕES

    adicionar_lista(
        conteudo,
        estilos,
        "Certificações",
        curriculo.certificacoes
    )