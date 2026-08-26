import json


CAMPOS_CURRICULO = {
    "nome",
    "email",
    "telefone",
    "cidade",
    "resumo",
    "linkedin",
    "github",
    "experiencias",
    "formacoes",
    "certificacoes",
    "habilidades",
    "idiomas"
}


CAMPOS_EXPERIENCIA = {
    "cargo",
    "empresa",
    "periodo",
    "descricao"
}


CAMPOS_FORMACAO = {
    "curso",
    "instituicao",
    "periodo"
}


def validar_resposta(resposta):

    erros = []

    if not isinstance(resposta, dict):
        erros.append(
            "A resposta da IA deve ser um objeto JSON."
        )

        return erros

    # =========================
    # CAMPOS PRINCIPAIS
    # =========================

    if "mensagem" not in resposta:
        erros.append(
            "A resposta não possui o campo 'mensagem'."
        )

    elif not isinstance(resposta["mensagem"], str):
        erros.append(
            "O campo 'mensagem' deve ser uma string."
        )

    if "dados" not in resposta:
        erros.append(
            "A resposta não possui o campo 'dados'."
        )

    elif not isinstance(resposta["dados"], dict):
        erros.append(
            "O campo 'dados' deve ser um objeto."
        )

    if "proximo_campo" not in resposta:
        erros.append(
            "A resposta não possui o campo 'proximo_campo'."
        )

    elif not isinstance(resposta["proximo_campo"], str):
        erros.append(
            "O campo 'proximo_campo' deve ser uma string."
        )

    if erros:
        return erros

    dados = resposta["dados"]

    # =========================
    # CAMPOS DESCONHECIDOS
    # =========================

    for campo in dados:

        if campo not in CAMPOS_CURRICULO:

            erros.append(
                f"Campo desconhecido em 'dados': {campo}"
            )

    # =========================
    # EXPERIÊNCIAS
    # =========================

    if "experiencias" in dados:

        experiencias = dados["experiencias"]

        if not isinstance(experiencias, list):

            erros.append(
                "O campo 'experiencias' deve ser uma lista."
            )

        else:

            for experiencia in experiencias:

                if not isinstance(experiencia, dict):

                    erros.append(
                        "Cada experiência deve ser um objeto."
                    )

                    continue

                for campo in experiencia:

                    if campo not in CAMPOS_EXPERIENCIA:

                        erros.append(
                            f"Campo desconhecido em experiência: {campo}"
                        )

    # =========================
    # FORMAÇÕES
    # =========================

    if "formacoes" in dados:

        formacoes = dados["formacoes"]

        if not isinstance(formacoes, list):

            erros.append(
                "O campo 'formacoes' deve ser uma lista."
            )

        else:

            for formacao in formacoes:

                if not isinstance(formacao, dict):

                    erros.append(
                        "Cada formação deve ser um objeto."
                    )

                    continue

                for campo in formacao:

                    if campo not in CAMPOS_FORMACAO:

                        erros.append(
                            f"Campo desconhecido em formação: {campo}"
                        )

    # =========================
    # LISTAS SIMPLES
    # =========================

    for campo in [
        "certificacoes",
        "habilidades",
        "idiomas"
    ]:

        if campo in dados:

            valor = dados[campo]

            if not isinstance(valor, list):

                erros.append(
                    f"O campo '{campo}' deve ser uma lista."
                )

            else:

                for item in valor:

                    if not isinstance(item, str):

                        erros.append(
                            f"Os itens de '{campo}' devem ser strings."
                        )

    return erros


def interpretar_resposta(resposta):

    if not isinstance(resposta, str):

        return None, [
            "A resposta da IA não é uma string."
        ]

    try:

        dados = json.loads(resposta)

    except json.JSONDecodeError:

        return None, [
            "A IA retornou uma resposta que não é um JSON válido."
        ]

    erros = validar_resposta(dados)

    if erros:

        return None, erros

    return dados, []