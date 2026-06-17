from services.modelos.modelo_base import gerar_pdf_modelo


def gerar_pdf_minimalista(curriculo):

    gerar_pdf_modelo(
        "#000000",  # Cor do título
        "#000000",  # Cor dos subtítulos
        curriculo
    )
