from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


def renderizar_duas_colunas(
    sidebar,
    corpo
):

    tabela = Table(
        [
            [sidebar, corpo]
        ],
        colWidths=[170, 360]
    )

    tabela.setStyle(
        TableStyle(
            [

                ('VALIGN',(0,0),(-1,-1),'TOP'),

                ('BACKGROUND',(0,0),(0,0),
                    colors.HexColor("#1E293B")),

                ('BACKGROUND',(1,0),(1,0),
                    colors.white),

                ('LEFTPADDING',(0,0),(-1,-1),20),
                ('RIGHTPADDING',(0,0),(-1,-1),20),
                ('TOPPADDING',(0,0),(-1,-1),20),
                ('BOTTOMPADDING',(0,0),(-1,-1),20),

            ]
        )
    )

    return tabela