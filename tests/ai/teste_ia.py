print("ARQUIVO TESTE_IA FOI EXECUTADO")

from services.ai.curriculo_ai import CurriculoAI


def main():

    ia = CurriculoAI()

    print("=== TESTE DO CURRÍCULO FÁCIL ===")
    print("Digite 'sair' para encerrar.\n")

    while True:

        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            break

        try:

            resposta = ia.conversar(mensagem)

            print("\nIA:")
            print(resposta)

            print("\nEstado atual:")
            print(ia.obter_curriculo())

            print("\n" + "=" * 50 + "\n")

        except Exception as erro:

            print("\nERRO:")
            print(erro)

            break


if __name__ == "__main__":
    main()