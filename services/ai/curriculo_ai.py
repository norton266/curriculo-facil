from services.ai.llm_service import LLMService
from services.ai.prompt import SYSTEM_PROMPT


class CurriculoAI:

    def __init__(self):

        self.llm = LLMService()

        self.mensagens = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def conversar(
        self,
        mensagem
    ):

        self.mensagens.append(
            {
                "role": "user",
                "content": mensagem
            }
        )

        resposta = self.llm.conversar(
            self.mensagens
        )

        self.mensagens.append(
            {
                "role": "assistant",
                "content": resposta
            }
        )

        return resposta