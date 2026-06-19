from services.builders.base_builder import BaseBuilder


class CertificacoesBuilder(BaseBuilder):

    def build(self):

        certificacoes = self.get_list("certificacao[]")

        return [
            cert.strip()
            for cert in certificacoes
            if cert.strip()
        ]