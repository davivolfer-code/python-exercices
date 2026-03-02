# Faça um programa que leia o preço de um produto
# e mostre o valor com 5% de desconto.
preco_base = float(input("Digite o preço do produto em R$: "))
desconto = preco_base * 0.05
preco_total = preco_base - desconto
print(f"O preço total do produto com desconto é: R$ {preco_total:.2f}")
print(f"O desconto foi de: R$ {desconto:.2f}")