from reportlab.platypus import Paragraph, Spacer

from services.componentes.secao import adicionar_secao


def adicionar_experiencias(
        conteudo,
        estilos,
        experiencias
):

    adicionar_secao(
        conteudo,
        estilos,
        "Experiência Profissional"
    )

    for experiencia in experiencias:

        conteudo.append(
            Paragraph(
                experiencia["cargo"],
                estilos["cargo"]
            )
        )

        conteudo.append(
            Paragraph(
                f"<b>{experiencia['empresa']}</b> | {experiencia['periodo']}",
                estilos["normal"]
            )
        )

        conteudo.append(
            Paragraph(
                experiencia["descricao"],
                estilos["normal"]
            )
        )

        conteudo.append(
            Spacer(1, 15)
        )