from reportlab.platypus import Spacer

from services.componentes.foto import adicionar_foto

from services.componentes.sidebar.contato import adicionar_contato
from services.componentes.sidebar.linkedin import adicionar_linkedin
from services.componentes.sidebar.github import adicionar_github
from services.componentes.sidebar.habilidades import adicionar_habilidades
from services.componentes.sidebar.idiomas import adicionar_idiomas


def adicionar_sidebar(
        conteudo,
        estilos,
        curriculo
):

    adicionar_foto(
        conteudo,
        curriculo.foto
    )

    conteudo.append(
        Spacer(1, 20)
    )

    adicionar_contato(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_linkedin(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_github(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_habilidades(
        conteudo,
        estilos,
        curriculo
    )

    adicionar_idiomas(
        conteudo,
        estilos,
        curriculo
    )