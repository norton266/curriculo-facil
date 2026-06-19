from services.builders.base_builder import BaseBuilder


class IdiomasBuilder(BaseBuilder):

    def build(self):

        idiomas = self.get_list("idioma[]")

        return [
            i.strip()
            for i in idiomas
            if i.strip()
        ]