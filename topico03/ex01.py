# Usando while, escreva um programa que cadastre o estado civil 
# de uma pessoa, entretanto, o programa deve continuar
# perguntando enquanto o valor informado for diferente 
# de "solteiro" ou "casado".

estado_civil = ""

while estado_civil != "solteiro" and estado_civil != "casado":
    estado_civil = input("Informe seu estado civil (solteiro ou casado): ")
    print("Estado civil cadastrado:", estado_civil)
print("Cadastro concluído.")