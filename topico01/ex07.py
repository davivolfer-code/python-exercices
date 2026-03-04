# Implemente um programa que tenha como entrada o valor em reais e mostre o valor correspondente em dólar.
import requests

response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")

print(response.status_code) # Verificar se a requisição foi bem-sucedida (código 200)
print(response.content) # Verificar o conteúdo da resposta para entender a estrutura dos dados

reais = float(input("Digite o valor em R$: "))

cotacao_atual = float(response.json()['USDBRL']['bid']) #Cotação atual do dólar em reais feita no dia 17/06/2024

dolar = reais / cotacao_atual

print(f"O valor total é de: $ {dolar:.2f}")

print(f"A cotação atual é de: R$ {cotacao_atual:.2f}")