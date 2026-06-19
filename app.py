from flask import Flask, render_template, request

from services.gerador_pdf import gerar_pdf
from services.pdf.pdf_service import enviar_pdf

from services.builders.curriculo_builder import criar_curriculo

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/gerar', methods=['POST'])
def gerar():

    modelo = request.form["modelo"]

    curriculo = criar_curriculo(request)

    pdf = gerar_pdf(
        modelo,
        curriculo
    )

    return enviar_pdf(pdf, curriculo.nome)

if __name__ == "__main__":
    app.run(debug=True)