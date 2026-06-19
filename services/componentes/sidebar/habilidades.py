from services.componentes.lista import adicionar_lista


def adicionar_habilidades(
        conteudo,
        estilos,
        curriculo
):

    adicionar_lista(
        conteudo,
        estilos,
        "Habilidades",
        curriculo.habilidades
    )