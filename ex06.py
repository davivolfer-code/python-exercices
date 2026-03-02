# Peça para o usuário digitar o seu ano de nascimento. O programa deve calcular
# e mostrar a idade atual dele, considerando que o ano atual é 2026.

from datetime import datetime #biblioteca para pegar o ano atual do sistema automaticamente

ano = int(input("Digite o ano do seu nascimento: "))

ano_atual = datetime.today().year #atualiza o ano atual automaticamente

ano_total = ano_atual - ano

print(f"Sua idade é de {ano_total} anos")