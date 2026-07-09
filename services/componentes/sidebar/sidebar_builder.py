from services.componentes.sidebar.sidebar import adicionar_sidebar

def criar_sidebar(estilos, curriculo):

    conteudo = []

    adicionar_sidebar(
        conteudo,
        estilos,
        curriculo
    )

    return conteudo