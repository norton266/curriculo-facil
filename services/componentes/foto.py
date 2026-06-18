from reportlab.platypus import (
    Image,
    Table,
    TableStyle
)


def adicionar_foto(
        conteudo,
        caminho_foto
):

    foto = Image(
        caminho_foto,
        width=100,
        height=100
    )

    tabela = Table(
        [[foto]]
    )

    tabela.setStyle(
        TableStyle(
            [
                ('ALIGN', (0, 0), (-1, -1), 'CENTER')
            ]
        )
    )

    conteudo.append(
        tabela
    )