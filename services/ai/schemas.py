from pydantic import BaseModel, Field
from typing import List


class ExperienciaSchema(BaseModel):

    cargo: str = ""
    empresa: str = ""
    periodo: str = ""
    descricao: str = ""


class FormacaoSchema(BaseModel):

    curso: str = ""
    instituicao: str = ""
    periodo: str = ""


class DadosCurriculoSchema(BaseModel):

    nome: str = ""
    email: str = ""
    telefone: str = ""
    cidade: str = ""

    resumo: str = ""

    linkedin: str = ""
    github: str = ""

    experiencias: List[ExperienciaSchema] = Field(
        default_factory=list
    )

    formacoes: List[FormacaoSchema] = Field(
        default_factory=list
    )

    certificacoes: List[str] = Field(
        default_factory=list
    )

    habilidades: List[str] = Field(
        default_factory=list
    )

    idiomas: List[str] = Field(
        default_factory=list
    )


class RespostaCurriculoSchema(BaseModel):

    mensagem: str = Field(
        description="Mensagem natural da IA para o usuário."
    )

    dados: DadosCurriculoSchema = Field(
        description="Dados do currículo identificados pela IA."
    )

    proximo_campo: str = Field(
        description="Próximo campo que deve ser solicitado."
    )

    curriculo_pronto: bool = Field(
        default=False,
        description=(
            "True somente quando todos os dados necessários "
            "foram coletados e a conversa pode ser finalizada. "
            "False enquanto houver informações necessárias pendentes."
        )
    )