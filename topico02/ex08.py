# Faça um programa para jogar Jokenpô (clássico pedra, papel 
# e tesoura) com você. Você deverá informar uma das opções, 
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.

import random
opcoes = ['pedra', 'papel', 'tesoura']
opcao_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
opcao_computador = random.choice(opcoes)

print(f"Você escolheu: {opcao_usuario}")
print(f"O computador escolheu: {opcao_computador}")

if opcao_usuario == opcao_computador:
    print("Empate!")
elif (opcao_usuario == 'pedra' and opcao_computador == 'tesoura') or (opcao_usuario == 'papel' and opcao_computador == 'pedra') or (opcao_usuario == 'tesoura' and opcao_computador == 'papel'):
    print("Você ganhou!")
else:
    print("O computador ganhou!")

print("Obrigado por jogar!")  