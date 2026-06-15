from flask import Flask, render_template, request, send_file
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib import colors

from reportlab.platypus import ListFlowable, ListItem

from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
titulo = styles['Title']
subtitulo = styles['Heading2']
normal = styles['Normal']
titulo.textColor = colors.HexColor("#2563EB")
subtitulo.textColor = colors.HexColor("#1F2937")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/gerar', methods=['POST'])
def gerar():

    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    cidade = request.form['cidade']
    resumo = request.form['resumo']
    experiencias_texto = request.form['experiencias']

    experiencias = []

    linhas = experiencias_texto.split('\n')

    for linha in linhas:

        partes = linha.split('|')

        if len(partes) == 4:

            experiencias.append({
                "cargo": partes[0].strip(),
                "empresa": partes[1].strip(),
                "periodo": partes[2].strip(),
                "descricao": partes[3].strip()
            })

    formacoes_texto = request.form['formacoes']
    formacoes = []

    linhas_formacao = formacoes_texto.split('\n')

    for linha in linhas_formacao:

        partes = linha.split('|')

        if len(partes) == 2:

            formacoes.append({
                "curso": partes[0].strip(),
                "instituicao": partes[1].strip()
            })

    certificacoes_texto = request.form['certificacoes']

    certificacoes = []

    linhas_certificacao = certificacoes_texto.split('\n')

    for linha in linhas_certificacao:

        linha = linha.strip()

        if linha:

            certificacoes.append(linha)


    habilidades = request.form['habilidades']
    habilidades_lista = habilidades.split(',')

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        "pdfs/curriculo.pdf"
    )

    conteudo = []

    conteudo.append(
        Paragraph(nome, titulo)
    )

    conteudo.append(
        Paragraph(
            f"{telefone} | {email} | {cidade}",
            normal
        )
    )

    conteudo.append(
        Spacer(1,20)
    )

    conteudo.append(
        Paragraph(
            "Resumo Profissional",
            subtitulo
        )
    )

    conteudo.append(
        Paragraph(
            resumo,
            normal
        )
    )

    conteudo.append(
        Spacer(1,20)
    )

    conteudo.append(
        Paragraph(
            "Experiência Profissional",
            subtitulo
        )
    )

    for experiencia in experiencias:

        conteudo.append(
            Paragraph(
                experiencia['cargo'],
                styles['Heading3']
            )
        )

        conteudo.append(
            Paragraph(
                f"<b>{experiencia['empresa']}</b> | {experiencia['periodo']}",
                normal
            )
        )

        conteudo.append(
            Paragraph(
                experiencia['descricao'],
                normal
            )
        )

        conteudo.append(
            Spacer(1,15)
        )

    conteudo.append(
        Paragraph(
            "Formação",
            subtitulo
        )
    )

    conteudo.append(
        Spacer(1,10)
    )

    for formacao in formacoes:

        conteudo.append(
            Paragraph(
                formacao['curso'],
                styles['Heading3']
            )
        )

        conteudo.append(
            Paragraph(
                formacao['instituicao'],
                normal
            )
        )

    conteudo.append(
        Spacer(1,25)
    )

    conteudo.append(
        Paragraph(
            "Certificações",
            subtitulo
        )
    )

    lista_certificacoes = []

    for cert in certificacoes:

        lista_certificacoes.append(
            ListItem(
                Paragraph(
                    cert,
                    normal
                )
            )
        )

    conteudo.append(
        ListFlowable(
            lista_certificacoes
        )
    )

    conteudo.append(
        Paragraph(
            "Habilidades",
            subtitulo
        )
    )

    lista_habilidades = []

    for habilidade in habilidades_lista:

        lista_habilidades.append(
            ListItem(
                Paragraph(
                    habilidade.strip(),
                    normal
                )
            )
        )

    conteudo.append(
        ListFlowable(
            lista_habilidades
        )
    )

    doc.build(conteudo)

    return send_file(
        "pdfs/curriculo.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)