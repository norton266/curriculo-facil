from services.componentes.corpo_principal import adicionar_corpo_principal

def criar_corpo(estilos, curriculo):

    conteudo = []

    adicionar_corpo_principal(
        conteudo,
        estilos,
        curriculo
    )

    return conteudo