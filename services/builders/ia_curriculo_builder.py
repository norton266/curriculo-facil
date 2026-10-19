from models.curriculo import Curriculo
from models.contato import Contato


def criar_curriculo_com_dados(dados):

    contato = Contato(
        email=dados.get("email", ""),
        telefone=dados.get("telefone", ""),
        cidade=dados.get("cidade", ""),
        linkedin=dados.get("linkedin", ""),
        github=dados.get("github", "")
    )

    return Curriculo(
        nome=dados.get("nome", ""),
        foto=dados.get("foto"),
        contato=contato,
        resumo=dados.get("resumo", ""),
        experiencias=dados.get("experiencias", []),
        formacoes=dados.get("formacoes", []),
        certificacoes=dados.get("certificacoes", []),
        habilidades=dados.get("habilidades", []),
        idiomas=dados.get("idiomas", [])
    )