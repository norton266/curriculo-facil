from services.modelos.modelo_base import gerar_pdf_modelo


def gerar_pdf_executivo(curriculo):

    return gerar_pdf_modelo(
        "#0F172A",
        "#334155",
        curriculo
    )
