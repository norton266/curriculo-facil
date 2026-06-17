def parse_formacoes(formacoes_texto):

    formacoes = []

    for linha in formacoes_texto.split('\n'):

        partes = linha.split('|')

        if len(partes) == 2:

            formacoes.append({
                "curso": partes[0].strip(),
                "instituicao": partes[1].strip()
            })

    return formacoes