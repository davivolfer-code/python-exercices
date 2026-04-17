# Usando while, escreva um programa que leia um
# número inteiro qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Informe um número inteiro para calcular o fatorial: "))
fatorial = 1
contador = numero

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é {fatorial}.")
