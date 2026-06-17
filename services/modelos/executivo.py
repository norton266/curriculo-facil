from services.modelos.modelo_base import gerar_pdf_modelo


def gerar_pdf_executivo(curriculo):

    gerar_pdf_modelo(
        "#1E293B",  # Cor do título
        "#475569",  # Cor dos subtítulos
        curriculo
    )
