from models.formacao import Formacao
from services.builders.base_builder import BaseBuilder


class FormacoesBuilder(BaseBuilder):

    def build(self):

        cursos = self.get_list("curso[]")
        instituicoes = self.get_list("instituicao[]")

        formacoes = []

        for curso, instituicao in zip(
            cursos,
            instituicoes
        ):

            if curso.strip():

                formacoes.append(
                    Formacao(
                        curso=curso,
                        instituicao=instituicao
                    )
                )

        return formacoes