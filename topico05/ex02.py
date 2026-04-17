# Faça um programa que crie dois conjuntos x e y,
# com dez números inteiros cada um. Em seguida, crie:
# 1) Um conjunto resultante da união de x e y (todos os
# elementos de x e os elementos de y que não estão em x).
# 2) Um conjunto resultante da diferença entre x e y (todos
# os elementos de x que não existam em y).
# 3) Um conjunto resultante interseção entre x e y

x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
y = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# 1) União de x e y
uniao = x | y

# 2) Diferença entre x e y
diferenca = x - y

# 3) Interseção entre x e y
intersecao = x & y

print("Conjunto x: ", x)
print("Conjunto y: ", y)
print("União de x e y: ", uniao)
print("Diferença entre x e y: ", diferenca)
print("Interseção entre x e y: ", intersecao)