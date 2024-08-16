import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)
response = requests.get('https://jsonplaceholder.typicode.com/users/')
# print(response.status_code)
# for user in response.json():
#     print(f" {user['name']}")
print('digite 1 para listar todos os usuarios ')
print('digite 2 para listar as tarefas de um usuarios ')
print('digite 3 para criar CRUD de usuarios ')
opcao = input('digite aqui : ')

if opcao == '1' :
    response = requests.get(api_url).json()
    response = requests.get('https://jsonplaceholder.typicode.com/users/')
    print ("====== USUARIOS CADASTRADOS ========")
    for user in response.json():
      print(f" {user['name']}")
elif opcao == '2' :
    response = requests.get(f"{api_url}").json
    print (F"====== TAREFAS DO USUARIO  ========")
elif opcao == '1' :
    pass
elif opcao == '1' :
    pass