# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.

lista_nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]
lista_notas = [8.5, 10.0, 7.0, 9.5, 6.0]
maior_nota = max(lista_notas)
menor_nota = min(lista_notas)
indice_maior = lista_notas.index(maior_nota)
indice_menor = lista_notas.index(menor_nota)
print(f"Aluno com a maior nota: {lista_nomes[indice_maior]} - Nota: {maior_nota}")
print(f"Aluno com a menor nota: {lista_nomes[indice_menor]} - Nota: {menor_nota}")