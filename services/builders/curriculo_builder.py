from models.curriculo import Curriculo
from models.contato import Contato

from uploads.salvar_foto import salvar_foto

from services.builders.experiencias_builder import ExperienciasBuilder
from services.builders.formacoes_builder import FormacoesBuilder
from services.builders.certificacoes_builder import CertificacoesBuilder
from services.builders.habilidades_builder import HabilidadesBuilder
from services.builders.idiomas_builder import IdiomasBuilder

def criar_curriculo(request):

    contato = Contato(
        email=request.form["email"],
        telefone=request.form["telefone"],
        cidade=request.form["cidade"],
        linkedin=request.form.get("linkedin", ""),
        github=request.form.get("github", "")
    )

    foto = request.files.get("foto")
    caminho_foto = salvar_foto(foto) if foto and foto.filename else None

    experiencias = ExperienciasBuilder(request).build()
    formacoes = FormacoesBuilder(request).build()
    certificacoes = CertificacoesBuilder(request).build()
    habilidades = HabilidadesBuilder(request).build()
    idiomas = IdiomasBuilder(request).build()

    return Curriculo(
        nome=request.form["nome"],
        foto=caminho_foto,
        contato=contato,
        resumo=request.form["resumo"],
        experiencias=experiencias,
        formacoes=formacoes,
        certificacoes=certificacoes,
        habilidades=habilidades,
        idiomas=idiomas
    )