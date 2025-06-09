def receber_palavra():
    palavra = input("Jogador 1, digite a palavra secreta: ").lower()
    print("\n" * 50)  # Limpa a tela (truque simples)
    return palavra

def mostrar_progresso(palavra, letras_certas):
    progresso = ""
    for letra in palavra:
        if letra in letras_certas:
            progresso += letra + " "
        else:
            progresso += "_ "
    print(progresso)

def jogo_forca():
    palavra = receber_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    while tentativas > 0:
        mostrar_progresso(palavra, letras_certas)
        letra = obter_letra()

        if letra in palavra and letra not in letras_certas:
            letras_certas.append(letra)
        elif letra in letras_erradas or letra in letras_certas:
            print("Você já tentou essa letra.")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"Letra errada! Tentativas restantes: {tentativas}")
        
        if all(letra in letras_certas for letra in palavra):
            print(f"\nParabéns! Você acertou a palavra: {palavra}")
            return

    print(f"\nFim de jogo! A palavra era: {palavra}")

jogo_forca()