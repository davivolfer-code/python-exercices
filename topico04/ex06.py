# Implemente o jogo da forca. Um usuário deverá entrar 
# com uma palavra. Em seguida, outro usuário deverá 
# indicar as letras dessa palavra. Caso exista, deverá 
# ser mostrada as letras e as suas posições na palavra. 
# Caso não exista, o usuário perderá uma chance. No total, 
# o usuário terá 6 chances para acertar.

palavra = input("Digite a palavra: ")
chances = 6
letras_acertadas = ['_'] * len(palavra)
while chances > 0:
    print(' '.join(letras_acertadas))
    letra = input("Digite uma letra: ")
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_acertadas[i] = letra
    else:
        chances -= 1
        print(f"Letra incorreta! Você tem {chances} chances restantes.")
    if '_' not in letras_acertadas:
        print("Parabéns! Você acertou a palavra:", palavra)
        break
else:    print("Game Over! Você perdeu todas as chances. A palavra era:", palavra)