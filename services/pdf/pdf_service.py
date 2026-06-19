from services.pdf.pdf_response import criar_resposta_pdf


def enviar_pdf(
        pdf,
        nome
):

    nome_arquivo = f"{nome}.pdf"

    return criar_resposta_pdf(
        pdf,
        nome_arquivo
    )