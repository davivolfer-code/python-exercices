# Usando for, faça um programa que leia um número 
# inteiro e mostre na tela se é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
nao_primo = False

for i in range(2, numero):
    if numero % i == 0:
        nao_primo = True
        break

if nao_primo:
    print("Não é primo")
else:
    print("É primo")