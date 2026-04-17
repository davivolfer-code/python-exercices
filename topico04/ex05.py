# Faça um programa em que o usuário deverá digitar
# os nomes de dez alunos da sala de aula. Em seguida,
# caso o programa encontre nomes repetidos, ele deverá
# alterar o nome adicionando o número sequencial. Por
# exemplo, se na lista tivermos dois "José", após o
# processamento a lista deverá conter "José 1" e "José 2".

# nomes = ['Maria', 'Pedro', 'Maria', 'João', 'Pedro']

nomes = []
for i in range(10):
    nome = input("Digite o nome do aluno: ")
    if nome in nomes:
        contador = 1
        while f"{nome} {contador}" in nomes:
            contador+= 1
        nome = f"{nome} {contador}"
        nomes.append(nome)
    else:
        nomes.append(nome)
print(nomes)
