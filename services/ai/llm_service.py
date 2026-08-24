import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY não encontrada no arquivo .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def conversar(self, mensagens):

        contents = []

        for mensagem in mensagens:

            role = mensagem["role"]
            content = mensagem["content"]

            if role == "system":
                continue

            gemini_role = "model" if role == "assistant" else "user"

            contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[
                        types.Part.from_text(text=content)
                    ]
                )
            )

        resposta = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=contents
        )

        return resposta.text