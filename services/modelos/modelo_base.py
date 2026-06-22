from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from io import BytesIO
from services.componentes.estilos import criar_estilos
from services.componentes.cabecalho import adicionar_cabecalho
from services.componentes.secao import adicionar_secao
from services.componentes.experiencias import adicionar_experiencias
from services.componentes.formacoes import adicionar_formacoes
from services.componentes.lista import adicionar_lista


def gerar_pdf_modelo(
        cor_titulo,
        cor_subtitulo,
        curriculo
):

    estilos = criar_estilos(
        cor_titulo,
        cor_subtitulo
    )

    #bytesIO

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

    conteudo = []

    # CABEÇALHO

    adicionar_cabecalho(
        conteudo,
        estilos,
        curriculo.nome,
        curriculo.contato.telefone,
        curriculo.contato.email,
        curriculo.contato.cidade
    )

    # RESUMO

    adicionar_secao(
        conteudo,
        estilos,
        "Resumo Profissional"
    )

    conteudo.append(
        Paragraph(
            curriculo.resumo,
            estilos["normal"]
        )
    )

    conteudo.append(
        Spacer(1, 20)
    )

    # EXPERIÊNCIAS

    adicionar_experiencias(
        conteudo,
        estilos,
        curriculo.experiencias
    )

    # FORMAÇÕES

    adicionar_formacoes(
        conteudo,
        estilos,
        curriculo.formacoes
    )

    # CERTIFICAÇÕES

    adicionar_lista(
        conteudo,
        estilos,
        "Certificações",
        curriculo.certificacoes
    )

    # HABILIDADES

    adicionar_lista(
        conteudo,
        estilos,
        "Habilidades",
        curriculo.habilidades
    )

    # IDIOMAS

    adicionar_lista(
        conteudo,
        estilos,
        "Idiomas",
        curriculo.idiomas
    )
    
    doc.build(conteudo)

    buffer.seek(0)

    return buffer