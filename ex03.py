# Supondo que queremos pintar o muro da instituição, faça um programa
# que leia a altura e a largura do muro e mostre a quantidade de tinta
# necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).
altura = float(input("Digite a altura do muro em metros: "))
largura = float(input("Digite a largura do muro em metros: "))
area = altura * largura
tinta_necessaria = area / 2
print(f"A quantidade de tinta necessária é: {tinta_necessaria:.2f} litros")
