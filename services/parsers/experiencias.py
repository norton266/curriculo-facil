def parse_experiencias(experiencias_texto):

    experiencias = []

    for linha in experiencias_texto.split('\n'):

        partes = linha.split('|')

        if len(partes) == 4:

            experiencias.append({
                "cargo": partes[0].strip(),
                "empresa": partes[1].strip(),
                "periodo": partes[2].strip(),
                "descricao": partes[3].strip()
            })

    return experiencias