import json

from services.ai.llm_service import LLMService
from services.ai.prompt import SYSTEM_PROMPT
from services.ai.estado_curriculo import EstadoCurriculo
from services.ai.resposta_validator import interpretar_resposta


class CurriculoAI:

    def __init__(self):

        self.llm = LLMService()

        self.estado = EstadoCurriculo()

        self.mensagens = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def conversar(self, mensagem):

        contexto = {
            "estado_atual": self.estado.obter(),
            "mensagem_usuario": mensagem
        }

        self.mensagens.append(
            {
                "role": "user",
                "content": json.dumps(
                    contexto,
                    ensure_ascii=False
                )
            }
        )

        resposta = self.llm.conversar(
            self.mensagens
        )

        dados = self._interpretar_resposta(
            resposta
        )

        self.estado.atualizar(
            dados["dados"]
        )

        self.mensagens.append(
            {
                "role": "assistant",
                "content": resposta
            }
        )

        return dados

    def _interpretar_resposta(self, resposta):

        dados, erros = interpretar_resposta(resposta)

        if erros:

            return {
                "mensagem": (
                    "Não consegui interpretar corretamente "
                    "a resposta da IA."
                ),
                "dados": {},
                "proximo_campo": "",
                "erros": erros
            }

        return dados

    def obter_curriculo(self):

        return self.estado.obter()