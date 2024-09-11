import requests
from getpass import getpass
import pandas as pd

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)
token = response.json().get("access")
if not token:
    print("Falha na autenticação.")
    exit()

headers = {
    "Authorization": f'Bearer {token}'
}

ano_letivo = input('Digite seu ano letivo: ')
periodo_letivo = input('Digite seu período letivo: ')

response = requests.get(api_url + f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/", headers=headers)
data = response.json()

# Supondo que a resposta seja uma lista de dicionários com informações do boletim
# Verifique a estrutura real da resposta JSON e ajuste conforme necessário
if 'data' in data:  # Verifique se a chave 'data' existe na resposta
    boletim_data = data['data']
    df = pd.DataFrame(boletim_data)
    
    # Exibindo a tabela
    print(df.to_string(index=False))
else:
    print("Dados não encontrados ou formato inesperado.")
