from flask import send_file

def criar_resposta_pdf(pdf, nome_arquivo):

    pdf.seek(0)  # GARANTE que está no início

    return send_file(
        pdf,
        as_attachment=True,
        download_name=nome_arquivo,
        mimetype="application/pdf"
    )