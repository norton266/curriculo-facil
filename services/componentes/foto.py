from reportlab.platypus import Image, Spacer, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def adicionar_foto(conteudo, caminho_foto):

    if not caminho_foto:
        return

    foto = Image(caminho_foto)
    foto.drawWidth = 100
    foto.drawHeight = 100

    conteudo.append(foto)
    conteudo.append(Spacer(1, 10))