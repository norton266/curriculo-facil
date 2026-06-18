def salvar_foto(foto):

    caminho = "uploads/foto.jpg"

    if foto:
        foto.save(caminho)

    return caminho