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