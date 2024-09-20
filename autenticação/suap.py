import requests
from getpass import getpass
import json
from datetime import datetime
from tabulate import tabulate

api_url = "https://suap.ifrn.edu.br/api/"

# Função para autenticar o usuário e obter o token de acesso
def autentica(api_url):
    user = input("Usuário: ")
    password = getpass("Senha: ")
    data = {"username": user, "password": password}
    
    response = requests.post(api_url + "v2/autenticacao/token/", json=data)
    
    if response.status_code == 200:
        print("Autenticação bem-sucedida!")
        return response.json()["access"]
    else:
        print(f"Erro na autenticação: {response.status_code} - {response.text}")
        return None

# Função para obter o boletim
def obter_boletim(token, year, semester):
    headers = {"Authorization": f'Bearer {token}'}
    url = f"{api_url}v2/minhas-informacoes/boletim/{year}/{semester}/"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Boletim não encontrado para o ano {year} e semestre {semester}.")
        else:
            print(f"Erro ao obter boletim: {response.status_code} - {response.text}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Função para formatar e exibir o boletim
def exibir_boletim(boletim):
    if not boletim:
        print("Nenhum boletim para exibir.")
        return
    tabela = []
    # Itera sobre a lista de disciplinas (que está no boletim)
    for disciplina in boletim:
        nome_disciplina = disciplina.get("disciplina", )
        notas_unidades = [
            disciplina.get("nota_etapa_1", "--"),
            disciplina.get("nota_etapa_2", "--"),
            disciplina.get("nota_etapa_3", "--"),
            disciplina.get("nota_etapa_4", "--")
        ]
        tabela.append([nome_disciplina, *notas_unidades ])

    # Exibe a tabela formatada
    print(tabulate(tabela, headers=["Disciplina", "1ª Unidade", "2ª Unidade", "3ª Unidade", "4ª Unidade"], tablefmt="fancy_grid"))
    
def main():
    # Autenticação
    token = autentica(api_url)
    if not token:
        return
    
    # Definir ano letivo e semestre
    year = input('Digite o ano letivo: ') or datetime.now().year
    semester = input('Digite o semestre: ') or '1'
    
    # Obter boletim
    boletim = obter_boletim(token, year, semester)
    
    # Exibir boletim formatado
    exibir_boletim(boletim)

if __name__ == "__main__":
    main()

