from flask import Flask, render_template, request, send_file

from services.gerador_pdf import gerar_pdf

from services.parsers.experiencias import parse_experiencias
from services.parsers.formacoes import parse_formacoes
from services.parsers.certificacoes import parse_certificacoes
from services.parsers.habilidades import parse_habilidades
from models.curriculo import Curriculo
from services.parsers.idiomas import parse_idiomas
from uploads.salvar_foto import salvar_foto

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/gerar', methods=['POST'])
def gerar():

    modelo = request.form["modelo"]

    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    cidade = request.form["cidade"]
    resumo = request.form["resumo"]
    linkedin = request.form["linkedin"]
    github = request.form["github"]
    foto = request.files["foto"]

    caminho_foto = salvar_foto(foto)

    experiencias = parse_experiencias(
        request.form["experiencias"]
    )

    formacoes = parse_formacoes(
        request.form["formacoes"]
    )

    certificacoes = parse_certificacoes(
        request.form["certificacoes"]
    )

    habilidades = parse_habilidades(
        request.form["habilidades"]
    )

    idiomas = parse_idiomas(
        request.form["idiomas"]
    )

    
    curriculo = Curriculo(
        nome=nome,
        email=email,
        telefone=telefone,
        cidade=cidade,
        foto=caminho_foto,

        linkedin=linkedin,
        github=github,

        resumo=resumo,

        experiencias=experiencias,
        formacoes=formacoes,
        certificacoes=certificacoes,
        habilidades=habilidades,
        idiomas=idiomas
    )


    gerar_pdf(
        modelo,
        curriculo
    )
    

    return send_file(
        "pdfs/curriculo.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)