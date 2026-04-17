# Usango while, faça um programa que mostre a tabuada 
# de um número informado.

numero = int(input("Informe um número para mostrar a tabuada: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
print("Tabuada finalizada.")