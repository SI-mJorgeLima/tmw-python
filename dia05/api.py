import requests

url = "https://api.opendota.com/api/heroes"

resposta = requests.get(url)

#verifica se a API está conectada
print(resposta.status_code)

dados = resposta.json()

print(dados)


for c in dados:
    print(c['localized_name'])
    