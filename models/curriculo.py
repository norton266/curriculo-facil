class Curriculo:

    def __init__(
            self,
            nome,
            email,
            telefone,
            cidade,
            resumo,
            experiencias,
            formacoes,
            certificacoes,
            habilidades
    ):

        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cidade = cidade
        self.resumo = resumo

        self.experiencias = experiencias
        self.formacoes = formacoes
        self.certificacoes = certificacoes
        self.habilidades = habilidades