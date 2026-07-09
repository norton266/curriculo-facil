from io import BytesIO

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import (
    Paragraph,
    Spacer
)


class LayoutBase:

    def __init__(self):

        self.buffer = BytesIO()

        self.doc = SimpleDocTemplate(
            self.buffer
        )

        self.conteudo = []

    def adicionar(self, flowable):

        if isinstance(flowable, list):
            self.conteudo.extend(flowable)
        else:
            self.conteudo.append(flowable)

    def adicionar_titulo(
        self,
        texto,
        estilo
    ):

        self.adicionar(
            Paragraph(
                texto,
                estilo
            )
        )

        self.adicionar(
            Spacer(1,20)
        )

    def gerar(self):

        self.doc.build(
            self.conteudo
        )

        self.buffer.seek(0)

        return self.buffer