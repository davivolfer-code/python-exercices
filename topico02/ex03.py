# Escreva um programa que leia a velocidade de um carro. 
# Se esta velocidade for maior que 80Km/h o programa deverá
# escrever uma mensagem na tela avisando que o usuário levou
# uma multa e o valor a ser pago. Considere R$ 7 reais por
# cada Km acima do limite.

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
velocidade_limite = 80.0
multa = 7.00

if velocidade > velocidade_limite:
    excesso = velocidade - velocidade_limite
    valor_multa = excesso * multa
    print(f"Você levou uma multa! Excedeu o limite em {excesso:.2f} Km/h.")
    print(f"O valor da multa que você levou é de R$ {valor_multa:.2f}")

else:
    print("Parabéns! Você está dentro do limite de velocidade.")