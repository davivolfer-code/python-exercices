# Dada uma lista de números inteiros, 
# imprima todos os elementos distintos.

numeros = [1, 2, 3, 3, 4, 5]

for numero in numeros:
    if numeros.count(numero) == 1:
        print(numero)
