from models.experiencia import Experiencia
from services.builders.base_builder import BaseBuilder


class ExperienciasBuilder(BaseBuilder):

    def build(self):

        cargos = self.get_list("cargo[]")
        empresas = self.get_list("empresa[]")
        periodos = self.get_list("periodo[]")
        descricoes = self.get_list("descricao[]")

        experiencias = []

        for cargo, empresa, periodo, descricao in zip(
            cargos,
            empresas,
            periodos,
            descricoes
        ):

            if cargo.strip():

                experiencias.append(
                    Experiencia(
                        cargo=cargo,
                        empresa=empresa,
                        periodo=periodo,
                        descricao=descricao
                    )
                )

        return experiencias