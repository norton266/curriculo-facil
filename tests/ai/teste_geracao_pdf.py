from services.builders.ia_curriculo_builder import (
    criar_curriculo_com_dados
)

from services.gerador_pdf import gerar_pdf

from services.validators.curriculo_validator import (
    validar_curriculo
)


dados = {

    "nome": "João Silva",

    "email": "joao@email.com",

    "telefone": "51999999999",

    "cidade": "Porto Alegre",

    "linkedin": "",

    "github": "",

    "resumo": (
        "Profissional da área de tecnologia "
        "com experiência em suporte técnico "
        "e desenvolvimento de sistemas."
    ),

    "experiencias": [],

    "formacoes": [],

    "certificacoes": [],

    "habilidades": [
        "Python",
        "SQL",
        "Suporte técnico"
    ],

    "idiomas": [
        "Inglês — Intermediário"
    ]

}


print("Criando objeto Curriculo...")

curriculo = criar_curriculo_com_dados(
    dados
)


print("Validando currículo...")

erros = validar_curriculo(
    curriculo
)


if erros:

    print("ERROS:")

    for erro in erros:
        print("-", erro)

    raise SystemExit


print("Gerando PDF...")

pdf = gerar_pdf(
    "moderno",
    curriculo
)


with open(
    "curriculo_teste.pdf",
    "wb"
) as arquivo:

    arquivo.write(
        pdf.getvalue()
    )


print()
print("PDF GERADO COM SUCESSO!")
print("Arquivo: curriculo_teste.pdf")