from flask import Flask, render_template, request
from flask import jsonify

from services.gerador_pdf import gerar_pdf
from services.pdf.pdf_service import enviar_pdf

from services.builders.curriculo_builder import criar_curriculo
from services.validators.curriculo_validator import validar_curriculo

from services.ai.curriculo_ai import CurriculoAI

app = Flask(__name__)
assistente = CurriculoAI()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ia', methods=['POST'])
def conversar_ia():

    mensagem = request.json.get("mensagem")

    resposta = assistente.conversar(
        mensagem
    )

    return jsonify(resposta)


@app.route('/gerar', methods=['POST'])
def gerar():

    modelo = request.form["modelo"]

    curriculo = criar_curriculo(request)

    erros = validar_curriculo(curriculo)

    if erros:
        return render_template(
            "index.html",
            erros=erros
        )

    pdf = gerar_pdf(
        modelo,
        curriculo
    )

    return enviar_pdf(
        pdf,
        curriculo.nome
    )

if __name__ == "__main__":
    app.run(debug=True)