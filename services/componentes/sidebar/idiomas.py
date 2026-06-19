from services.componentes.lista import adicionar_lista


def adicionar_idiomas(
        conteudo,
        estilos,
        curriculo
):

    adicionar_lista(
        conteudo,
        estilos,
        "Idiomas",
        curriculo.idiomas
    )