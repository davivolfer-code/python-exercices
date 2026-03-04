# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.

import random

numero_sorteado = random.randint(0, 5)
numero_usuario = int(input("Tente adivinhar o número sorteado entre 0 e 5: "))

if numero_usuario == numero_sorteado:
    print("Parabéns! Você acertou o número sorteado!")
else:
    print(f"Que pena! Você errou. O número sorteado era {numero_sorteado}.")
    print("Tente novamente!")