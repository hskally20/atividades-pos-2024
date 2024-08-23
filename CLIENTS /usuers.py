import requests
api_url= 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(api_url)

print('digite 1 para listar todos os usuarios ')
print('digite 2 para listar as tarefas de um usuarios ')
print('digite 3 para criar CRUD de usuarios ')
opcao = input('digite aqui : ')

if opcao == '1' :
    response = requests.get(api_url).json()
    response = requests.get('https://jsonplaceholder.typicode.com/users/')
    print ("====== USUARIOS CADASTRADOS ========")
    for user in response.json():
      print(f" {user['id']} - {user['name']} ")

elif opcao == '2' :
    user_id = input('digite o id do usuario : ')
    response = requests.get( api_url+ '/' +user_id+'/todos').json()
    usuario = requests.get(f"{api_url}/{user_id}").json()
    print (F"====== TAREFAS DO USUARIO : {usuario['name']}  ==========")
    print("-"*30)
    for todo in response:
        print(f"  {todo['title']}")

elif opcao == '3' :
    print('digite 1 para criar um novo usuario')
    print('digite 2 para ver todos os usuario')
    print('dite 3 para deleta um usuario')
    print('digite 4 paraa tualizar um usuario')
    resp = input('digite aki : ')   
    if resp == '1':
       
        name = input("Digite o nome do usuário: ")
        username = input("Digite o apelido do usuário: ")
        email =  input("Digite o email do usuário: ")

        print("-"*30)
        print('Outros dados:')

        city= input('Informe a cidade: ')
        street = input('Informe a rua:')

        user_address={
            'city': city,
            'street':street
        }

        user_data= {
            'name': name,
            'username':username,
            'email': email,
            'address': user_address
        }
        response = requests.post(api_url, json=user_data).status_code
        if response == 201:
             print(' novo usuário criado com sucesso ')
        else:
            print(' erro !! nao foi possivel criar novo usuario')
    if resp == '2' :
        user_id= int(input("Digite o Id do usuário: "))
        response = requests.get(f"{api_url}/{user_id}").json()
        print("-"*30)
        print(f"Nome: {response['name']}\nNome de usuário: {response['username']}\nEmail: {response['email']}")

    if resp == '3' :
       user_id = input('digite o id do usuario : ')
       user_url = (f"{api_url}/{user_id}")
       response = requests.get(user_url).json()
       campo= input(f"deseja mesmo deleta o usuario {response['name']}? (s/n):  ")
       if campo =='s':
            response = requests.delete(user_url).status_code 
            if response == 200:
                print('Usuário deletado!')
            else:
                print('Aconteceu algo de errado!')
       elif campo =='n':
            print('Tudo bem!')
    if resp == '4' :
        user_id= int(input("Digite o ID do usuário: "))

        user_url = (f"{api_url}/{user_id}")
        response = requests.get(user_url).json()
        print(f"Você está atualizando o usuário: {response['name']}")
        name = input("Digite o novo nome do usuário: ")
        username = input("Digite o novo apelido do usuário: ")
        email =  input("Digite o novo email do usuário: ")
         
        user_data= {
            'name': name,
            'username':username,
            'email': email

        }
        response = requests.patch(user_url, json=user_data).status_code
        if response == 200:
            print(' usuário atualizado com sucesso ')
        else:
            print('erro tente novamente ')
