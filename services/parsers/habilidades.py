def parse_habilidades(habilidades_texto):

    habilidades = []

    for habilidade in habilidades_texto.split(','):

        habilidade = habilidade.strip()

        if habilidade:

            habilidades.append(habilidade)

    return habilidades