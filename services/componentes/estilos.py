from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def criar_estilos(cor_titulo, cor_subtitulo):

    styles = getSampleStyleSheet()

    titulo = styles["Title"]
    subtitulo = styles["Heading2"]
    cargo = styles["Heading3"]
    normal = styles["BodyText"]

    titulo.textColor = colors.HexColor(cor_titulo)
    subtitulo.textColor = colors.HexColor(cor_subtitulo)

    return {
        "titulo": titulo,
        "subtitulo": subtitulo,
        "cargo": cargo,
        "normal": normal
    }