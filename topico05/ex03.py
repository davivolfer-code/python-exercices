# Dadas três listas de números inteiros,
# imprima os elementos comuns entre elas.

x = [1, 2, 3]
y = [3, 4, 5]
z = [2, 3, 4]

comuns = set(x) & set(y) & set(z)
print("Elementos comuns entre as três listas: ", comuns)