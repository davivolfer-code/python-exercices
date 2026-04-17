# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.

import random
numeros = []
for i in range(10):
    numeros.append(random.randint(1, 100))
numeros_unicos = list(set(numeros))
print(numeros_unicos)

