import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)
api = requests.get('https://jsonplaceholder.typicode.com/users/')

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
    response = requests.get( api_url+ '/' +user_id).json
    print(response)
    print (F"====== TAREFAS DO USUARIO  ========")
    for todo in response:
        print(todo['title'])
elif opcao == '3' :
    user_id = input('digite o id do usuario : ')
    old_usser = requests(api_url+'/'+user_id ).status_code
     
elif opcao == '1' :
    pass