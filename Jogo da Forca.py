import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    return random.choice(palavras)
def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(estagios[tentativas])
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_" for _ in palavra]
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(tentativas)
    print(" ".join(palavra_oculta))

    # Passo 4: Loop Principal do Jogo
    while tentativas < 6 and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for index, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[index] = letra
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print(" ".join(palavra_oculta))

        # Passo 5: Verificação de Vitória e Derrota
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        elif tentativas == 6:
            print(f"Você perdeu! A palavra era '{palavra}'.")

    # Passo 6: Finalização do Jogo
    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
