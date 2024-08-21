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
    print('digite 1 para criar um novo usuario')
    print('digite 2 para ver todos os usuario')
    print('dite 3 para deleta um usuario')
    print('digite 4 paraa tualizar um usuario')
    resp = input('digite aki : ')
    if resp == '1' :
       pass
    if resp == '2' :
       pass
    if resp == '3' :
       user_id = input('digite o id do usuario : ')
       response = requests.get( api_url+ '/' +user_id).json
       response = requests.delete(api_url).status_code()
       print(response.json())
       if response == '200':
          print('sucesso')
    if resp == '4' :
       pass
