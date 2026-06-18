def parse_idiomas(idiomas_texto):

    idiomas = []

    for linha in idiomas_texto.split("\n"):

        linha = linha.strip()

        if linha:

            idiomas.append(linha)

    return idiomas
