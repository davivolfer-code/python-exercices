# Faça um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O usuário deverá informar o valor
# da casa, a quantidade de parcelas que deseja pagar e seu
# salário. O empréstimo deverá ser negado caso o valor da
# parcela exceda 30% do salário.

valor = float(input("Digite o valor da casa: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
salario = float(input("Digite o seu salário: "))
valor_parcela = valor / parcelas
minimo_parcela = salario * 0.30

if valor_parcela > minimo_parcela:
    print("Empréstimo negado! O valor da parcela excede 30% do seu salário.")
else:
    print("Empréstimo aprovado! O valor da parcela é de R$ {:.2f}.".format(valor_parcela))