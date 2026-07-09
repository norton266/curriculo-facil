from reportlab.platypus import (
    Paragraph,
    Spacer
)

from services.componentes.estilos import (
    criar_estilos,
    criar_estilos_sidebar
)

from services.componentes.sidebar.sidebar_builder import criar_sidebar
from services.componentes.corpo.corpo_builder import criar_corpo

from services.layouts.duas_colunas import LayoutDuasColunas


def gerar_pdf_duas_colunas(curriculo):

    estilos = criar_estilos(
        "#2563EB",
        "#1F2937"
    )

    estilos_sidebar = criar_estilos_sidebar()

    layout = LayoutDuasColunas()

    layout.adicionar_titulo(
        curriculo.nome,
        estilos["titulo"]
    )

    sidebar = criar_sidebar(
        estilos_sidebar,
        curriculo
    )

    corpo = criar_corpo(
        estilos,
        curriculo
    )

    layout.adicionar_colunas(
        sidebar,
        corpo
    )

    return layout.gerar()