from services.componentes.lista import adicionar_lista


def adicionar_certificacoes(
        conteudo,
        estilos,
        curriculo
):

    adicionar_lista(
        conteudo,
        estilos,
        "Certificações",
        curriculo.certificacoes
    )