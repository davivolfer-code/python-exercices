# Dadas duas listas que são duplicadas uma da
# outra, exceto por um elemento, ou seja, um 
# elemento de uma das listas está faltando. 
# Mostre-o usando conjuntos.

x = [1, 2, 3, 4]
y = [1, 2, 4]

faltando = set(x) - set(y)
print("O elemento faltando é: ", faltando)
