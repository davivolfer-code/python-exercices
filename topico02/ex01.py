# Escreva um programa que leia o salário de um
# funcionário e calcule o seu aumento. Caso o 
# salário atual seja superior a R$ 1.000,00 
# calcule um aumento de 10%, caso contrário, 
# calcule um aumento de 15%.

# Variáveis
salario = float(input("Digite o salário do funcionário: "))
min_salario = 1000.00
porcentagem_aumento1 = 0.1
porcentagem_aumento2 = 0.15

#Inicio e Saídas
if salario > min_salario:
    aumento = salario * porcentagem_aumento1
    salario_total = salario + aumento
    print(f"O salário atual é de R$ {salario:.2f}")
    print(f"O aumento do salário foi de R$ {aumento:.2f}")
    print(f"O salário total com o aumento foi de R$ {salario_total:.2f}")
else:
    print("O salário é inferior ou igual a R$ 1.000,00. O aumento será de 15%.")
    aumento = salario * porcentagem_aumento2
    salario_total = salario + aumento
    print(f"O salário atual é de R$ {salario:.2f}")
    print(f"O aumento do salário foi de R$ {aumento:.2f}")
    print(f"O salário total com o aumento foi de R$ {salario_total:.2f}")   
