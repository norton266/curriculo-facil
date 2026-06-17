def parse_certificacoes(certificacoes_texto):

    certificacoes = []

    for linha in certificacoes_texto.split('\n'):

        linha = linha.strip()

        if linha:

            certificacoes.append(linha)

    return certificacoes