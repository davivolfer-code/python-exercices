# Usando while, faça um programa que leia um número 
# inteiro N e mostre na tela os N primeiros números da 
# Sequência de Fibonacci.
# Por exemplo, N = 7
# Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

numero = int(input("Informe um número inteiro: "))
a = 0
b = 1
contador = 0

while contador < numero:
    print(a, end=" -> ")
    c = a + b
    a = b
    b = c
    contador += 1 

print("Sequência finalizada.")