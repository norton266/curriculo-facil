from services.ai.llm_service import LLMService


llm = LLMService()

mensagens = [
    {
        "role": "user",
        "content": "Olá! Estou criando um currículo e preciso de ajuda."
    }
]

resposta = llm.conversar(mensagens)

print("\nResposta da Gemini:")
print(resposta)