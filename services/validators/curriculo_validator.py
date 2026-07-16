def validar_curriculo(curriculo):

    erros = {}

    if not curriculo.nome.strip():
        erros["nome"] = "O nome é obrigatório."

    if not curriculo.contato.email.strip():
        erros["email"] = "O e-mail é obrigatório."

    if not curriculo.resumo.strip():
        erros["resumo"] = "O resumo profissional é obrigatório."

    if not curriculo.contato.telefone.strip():
        erros["telefone"] = "O número de telefone é obrigatório."

    return erros