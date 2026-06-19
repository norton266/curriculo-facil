from services.modelos.modelo_base import gerar_pdf_modelo


def gerar_pdf_minimalista(curriculo):

    return gerar_pdf_modelo(
        "#111827",
        "#6B7280",
        curriculo
    )
