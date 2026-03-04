# Faça um program que leia o ano de nascimento de uma
# pessoa e informe se ele ainda vai se alistar ao serviço 
# militar ou se ele está no período de se alistar ou se 
# ele perdeu o prazo para se alistar. Além disso, mostre 
# também a quantidade de anos que falta para se alistar 
# ou que passou do prazo.
from datetime import date
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
anos_para_alistamento = 18

if idade < anos_para_alistamento:
    anos_faltando = anos_para_alistamento - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {anos_faltando} anos para o alistamento.")
elif idade == anos_para_alistamento:
    print("Procure a junta militar para efetuar o seu alistamento.")
else:
    anos_passados = idade - anos_para_alistamento
    print(f"Você ja passou do prazo para se alistar. Passaram {anos_passados} anos desde quando você deveria ter se alistado.")