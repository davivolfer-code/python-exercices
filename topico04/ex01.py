# Faça um programa que carregue uma lista com dez
# números inteiros. Em seguida, 
# crie e mostre uma lista resultante ordenada de maneira 
# crescente e crie e mostre uma lista resultante ordenada 
# de maneira decrescente.

numeros = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
numeros_crescente = sorted(numeros)
numeros_decrescente = sorted(numeros, reverse=True)
print(numeros_crescente)
print(numeros_decrescente)