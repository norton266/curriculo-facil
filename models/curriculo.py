
from dataclasses import dataclass


@dataclass
class Curriculo:

    nome: str
    email: str
    telefone: str
    cidade: str
    foto: str

    linkedin: str
    github: str

    resumo: str

    experiencias: list
    formacoes: list
    certificacoes: list
    habilidades: list
    idiomas: list