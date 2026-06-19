from services.builders.base_builder import BaseBuilder


class HabilidadesBuilder(BaseBuilder):

    def build(self):

        habilidades = self.get_list("habilidade[]")

        return [
            h.strip()
            for h in habilidades
            if h.strip()
        ]