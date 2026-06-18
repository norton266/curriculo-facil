from copy import deepcopy

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def criar_estilos(cor_titulo, cor_subtitulo):

    styles = getSampleStyleSheet()

    titulo = deepcopy(styles["Title"])
    subtitulo = deepcopy(styles["Heading2"])
    cargo = deepcopy(styles["Heading3"])
    normal = deepcopy(styles["BodyText"])

    titulo.textColor = colors.HexColor(
        cor_titulo
    )

    subtitulo.textColor = colors.HexColor(
        cor_subtitulo
    )

    return {
        "titulo": titulo,
        "subtitulo": subtitulo,
        "cargo": cargo,
        "normal": normal
    }


def criar_estilos_sidebar():

    styles = getSampleStyleSheet()

    titulo = deepcopy(styles["Title"])
    subtitulo = deepcopy(styles["Heading2"])
    cargo = deepcopy(styles["Heading3"])
    normal = deepcopy(styles["BodyText"])

    titulo.textColor = colors.white
    subtitulo.textColor = colors.white
    cargo.textColor = colors.white
    normal.textColor = colors.white

    return {
        "titulo": titulo,
        "subtitulo": subtitulo,
        "cargo": cargo,
        "normal": normal
    }