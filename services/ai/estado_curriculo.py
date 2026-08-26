class EstadoCurriculo:

    def __init__(self):

        self.dados = {
            "nome": "",
            "email": "",
            "telefone": "",
            "cidade": "",
            "resumo": "",
            "linkedin": "",
            "github": "",
            "experiencias": [],
            "formacoes": [],
            "certificacoes": [],
            "habilidades": [],
            "idiomas": []
        }

    def atualizar(self, novos_dados):

        for campo, valor in novos_dados.items():

            if valor:

                if isinstance(valor, list):

                    self.dados[campo] = valor

                else:

                    self.dados[campo] = valor

    def obter(self):

        return self.dados