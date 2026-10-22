
import json

from services.ai.llm_service import LLMService
from services.ai.prompt import SYSTEM_PROMPT
from services.ai.estado_curriculo import EstadoCurriculo
from services.ai.resposta_validator import interpretar_resposta

from services.builders.ia_curriculo_builder import (
    criar_curriculo_com_dados
)

from services.validators.curriculo_validator import (
    validar_curriculo
)


class CurriculoAI:

    def __init__(self):

        self.llm = LLMService()

        self.estado = EstadoCurriculo()

        # O currículo começa incompleto.
        self.curriculo_pronto = False

        self.mensagens = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def conversar(self, mensagem):

        # Uma nova mensagem exige uma nova verificação.
        self.curriculo_pronto = False

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

        # Se a resposta da IA for inválida,
        # não tentamos atualizar o estado.
        if dados.get("erros"):

            dados["curriculo_pronto"] = False
            dados["curriculo"] = self.obter_curriculo()

            self.mensagens.append(
                {
                    "role": "assistant",
                    "content": resposta
                }
            )

            return dados

        # Atualiza o estado com os dados extraídos.
        self.estado.atualizar(
            dados["dados"]
        )

        # Constrói o objeto usado pelo gerador de PDF.
        curriculo = criar_curriculo_com_dados(
            self.estado.obter()
        )

        # Confere se os campos obrigatórios estão válidos.
        erros_validacao = validar_curriculo(
            curriculo
        )

        # A IA precisa indicar que terminou a coleta.
        coleta_concluida = (
            dados.get("curriculo_pronto") is True
        )

        # As duas condições precisam ser verdadeiras.
        self.curriculo_pronto = (
            coleta_concluida
            and not erros_validacao
        )

        dados["curriculo_pronto"] = (
            self.curriculo_pronto
        )

        dados["erros_validacao"] = erros_validacao

        self.mensagens.append(
            {
                "role": "assistant",
                "content": resposta
            }
        )

        dados["curriculo"] = self.obter_curriculo()

        return dados

    def _interpretar_resposta(self, resposta):

        dados, erros = interpretar_resposta(
            resposta
        )

        if erros:

            return {
                "mensagem": (
                    "Não consegui interpretar corretamente "
                    "a resposta da IA. Pode tentar novamente?"
                ),
                "dados": {},
                "proximo_campo": "dados_pessoais",
                "erros": erros
            }

        return dados

    def obter_curriculo(self):

        return self.estado.obter()
