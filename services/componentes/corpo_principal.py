from services.componentes.corpo.resumo import adicionar_resumo
from services.componentes.corpo.experiencias import adicionar_experiencias
from services.componentes.corpo.formacoes import adicionar_formacoes
from services.componentes.corpo.certificacoes import adicionar_certificacoes


def adicionar_corpo_principal(
        conteudo,
        estilos,
        curriculo
):

    adicionar_resumo(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_experiencias(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_formacoes(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_certificacoes(
        conteudo,
        estilos,
        curriculo
    )