import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


# Solicita o nome de usuário e a senha de forma segura
username = input("Digite seu nome de usuário GitHub: ")
password = getpass("Digite sua senha GitHub: ")


while True:
    print("\nEscolha uma opção:")
    print("1. Listar seguidores de um usuário")
    print("2. Seguir um usuário")
    print("3. Deixar de seguir um usuário")
    print("4. Sair")
   
    choice = input("Digite a opção desejada: ").strip()


    if choice == '1':
        user_to_check = input("Digite o login do usuário para conhecer seus seguidores: ").strip()
        response = requests.get(
            f'https://api.github.com/users/{user_to_check}/followers',
            auth=HTTPBasicAuth(username, password)
        )
       
        if response.status_code == 200:
            followers = response.json()
            if followers:
                print(f"Seguidores de {user_to_check}:")
                for follower in followers:
                    print(f"- {follower['login']}")
                print(f"Total de seguidores de {user_to_check}: {len(followers)}")
            else:
                print(f"{user_to_check} não tem seguidores.")
        else:
            print(f"Falha ao obter dados: {response.status_code}")


    elif choice == '2':
        user_to_follow = input("Digite o login do usuário que você deseja seguir: ").strip()
        response = requests.put(
            f'https://api.github.com/user/following/{user_to_follow}',
            auth=HTTPBasicAuth(username, password)
        )
       
        if response.status_code == 204:
            print(f"Você agora está seguindo {user_to_follow}.")
        else:
            print(f"Falha ao seguir o usuário: {response.status_code}")


    elif choice == '3':
        user_to_unfollow = input("Digite o login do usuário que você deseja deixar de seguir: ").strip()
        response = requests.delete(
            f'https://api.github.com/user/following/{user_to_unfollow}',
            auth=HTTPBasicAuth(username, password)
        )
       
        if response.status_code == 204:
            print(f"Você deixou de seguir {user_to_unfollow}.")
        else:
            print(f"Falha ao deixar de seguir o usuário: {response.status_code}")


    elif choice == '4':
        print("Saindo...")
        break


    else:
        print("Opção inválida! Tente novamente.")





