
from dataclasses import dataclass
from models.contato import Contato

@dataclass
class Curriculo:

    nome: str
    foto: str

    contato: Contato

    resumo: str

    experiencias: list
    formacoes: list
    certificacoes: list
    habilidades: list
    idiomas: list