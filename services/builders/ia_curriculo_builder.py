
from models.curriculo import Curriculo
from models.contato import Contato
from models.experiencia import Experiencia
from models.formacao import Formacao


def criar_curriculo_com_dados(dados):

    contato = Contato(
        email=dados.get("email", ""),
        telefone=dados.get("telefone", ""),
        cidade=dados.get("cidade", ""),
        linkedin=dados.get("linkedin", ""),
        github=dados.get("github", "")
    )

    experiencias = [
        Experiencia(
            cargo=item.get("cargo", ""),
            empresa=item.get("empresa", ""),
            periodo=item.get("periodo", ""),
            descricao=item.get("descricao", "")
        )
        for item in dados.get("experiencias", [])
    ]

    formacoes = [
        Formacao(
            curso=item.get("curso", ""),
            instituicao=item.get("instituicao", "")
        )
        for item in dados.get("formacoes", [])
    ]

    return Curriculo(
        nome=dados.get("nome", ""),
        foto=dados.get("foto"),
        contato=contato,
        resumo=dados.get("resumo", ""),
        experiencias=experiencias,
        formacoes=formacoes,
        certificacoes=dados.get("certificacoes", []),
        habilidades=dados.get("habilidades", []),
        idiomas=dados.get("idiomas", [])
    )
