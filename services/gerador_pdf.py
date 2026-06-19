from services.modelos.moderno import gerar_pdf_moderno
from services.modelos.executivo import gerar_pdf_executivo
from services.modelos.minimalista import gerar_pdf_minimalista
from services.modelos.duas_colunas import gerar_pdf_duas_colunas

MODELOS = {
    "moderno": gerar_pdf_moderno,
    "executivo": gerar_pdf_executivo,
    "minimalista": gerar_pdf_minimalista,
    "duas_colunas": gerar_pdf_duas_colunas
}


def gerar_pdf(
        modelo,
        curriculo
):

    funcao_modelo = MODELOS.get(
        modelo,
        gerar_pdf_moderno
    )

    return funcao_modelo(
        curriculo
    )