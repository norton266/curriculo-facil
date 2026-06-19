from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from services.componentes.estilos import (
    criar_estilos,
    criar_estilos_sidebar
)

from reportlab.lib import colors
from io import BytesIO
from services.componentes.estilos import criar_estilos
from services.componentes.sidebar import adicionar_sidebar
from services.componentes.corpo_principal import adicionar_corpo_principal


def gerar_pdf_duas_colunas(curriculo):

    buffer = BytesIO()

    estilos = criar_estilos(
        "#2563EB",
        "#1F2937"
    )

    estilos_sidebar = criar_estilos_sidebar()

    doc = SimpleDocTemplate(
        buffer
    )

    conteudo = []

    # Nome no topo

    conteudo.append(
        Paragraph(
            curriculo.nome,
            estilos["titulo"]
        )
    )

    conteudo.append(
        Spacer(1, 20)
    )

    # Coluna esquerda

    sidebar = []

    adicionar_sidebar(
        sidebar,
        estilos_sidebar,
        curriculo
    )

    # Coluna direita

    corpo_principal = []

    adicionar_corpo_principal(
        corpo_principal,
        estilos,
        curriculo
    )

    # Layout em duas colunas

    tabela = Table(
        [
            [sidebar, corpo_principal]
        ],
        colWidths=[170, 360]
    )

    tabela.setStyle(
        TableStyle(
            [

                # alinhamento
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),

                # cor da sidebar
                ('BACKGROUND', (0, 0), (0, 0),
                colors.HexColor("#1E293B")),

                # texto da coluna direita
                ('BACKGROUND', (1, 0), (1, 0),
                colors.white),

                # paddings
                ('LEFTPADDING', (0, 0), (-1, -1), 20),
                ('RIGHTPADDING', (0, 0), (-1, -1), 20),
                ('TOPPADDING', (0, 0), (-1, -1), 20),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 20)
            ]
        )
    )

    conteudo.append(
        tabela
    )

    doc.build(
        conteudo
    )

    buffer.seek(0)

    return buffer

    