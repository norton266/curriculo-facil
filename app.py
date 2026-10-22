from flask import Flask, render_template, request, jsonify

from services.gerador_pdf import gerar_pdf
from services.pdf.pdf_service import enviar_pdf

from services.builders.curriculo_builder import criar_curriculo
from services.builders.ia_curriculo_builder import criar_curriculo_com_dados

from services.validators.curriculo_validator import validar_curriculo

from services.ai.curriculo_ai import CurriculoAI


app = Flask(__name__)

assistente = CurriculoAI()

@app.route('/debug/estado-curriculo')
def debug_estado_curriculo():
    return jsonify(assistente.obter_curriculo())


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/ia')
def pagina_ia():
    return render_template("ia.html")


@app.route('/api/ia/conversar', methods=['POST'])
def conversar_ia():

    mensagem = request.json.get("mensagem")

    if not mensagem:
        return jsonify({
            "erro": "Mensagem não informada."
        }), 400

    resposta = assistente.conversar(
        mensagem
    )

    return jsonify(resposta)


@app.route('/api/ia/gerar', methods=['POST'])
def gerar_curriculo_ia():

    # Primeiro, verificamos se a IA concluiu a coleta.
    if not assistente.curriculo_pronto:

        return jsonify({
            "erro": (
                "Seu currículo ainda não está pronto. "
                "Continue a conversa com o assistente."
            )
        }), 400

    dados = assistente.obter_curriculo()

    curriculo = criar_curriculo_com_dados(
        dados
    )

    print("=== DEBUG CURRÍCULO ===")
    print("Tipo do currículo:", type(curriculo).__name__)
    print(
        "Tipos das formações:",
        [type(item).__name__ for item in curriculo.formacoes]
    )
    print(
        "Tipos das experiências:",
        [type(item).__name__ for item in curriculo.experiencias]
    )
    print("=======================")

    # Segunda verificação: validamos novamente os dados
    # antes de gerar o arquivo.
    erros = validar_curriculo(curriculo)

    if erros:

        assistente.curriculo_pronto = False

        return jsonify({
            "erro": "Não foi possível gerar o currículo.",
            "detalhes": erros
        }), 400

    pdf = gerar_pdf(
        "moderno",
        curriculo
    )

    return enviar_pdf(
        pdf,
        curriculo.nome
    )



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