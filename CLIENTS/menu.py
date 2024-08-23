from wrapper_users import user_wrapper

# Instancia a API
api = user_wrapper()

# Exibe o menu de opções
print('Digite 1 para listar todos os usuários')
print('Digite 2 para listar as tarefas de um usuário')
print('Digite 3 para atualizar os dados de um usuário')
print('Digite 4 para deletar um usuário')
print('Digite 5 para criar um novo usuário')
opcao = input('Digite aqui: ')

if opcao == '1':
    # Listar todos os usuários
    print("====== USUÁRIOS CADASTRADOS ========")
    for user in api.list_user():
        print(f"{user['id']} - {user['name']}")

elif opcao == '2':
    user_id = str(input("Digite o ID do usuário: "))
    user = api.read_user(user_id)
    print(f"{user['name']} - {user['username']} - {user['email']}")

elif opcao == '3':
    # Atualizar dados de um usuário
    user_id = input('Digite o ID do usuário: ')
    old_user = api.read_user(user_id)
    print("-" * 30)
    print(f"Você está atualizando o usuário: {old_user['name']}")

    name = input("Digite o novo nome do usuário: ")
    username = input("Digite o novo apelido do usuário: ")
    email = input("Digite o novo email do usuário: ")

    print("-" * 30)
    print('Outros dados:')

    city = input('Informe a cidade: ')
    street = input('Informe a rua:')

    user_address = {
        'city': city,
        'street': street
    }

    user_data = {
        'name': name,
        'username': username,
        'email': email,
        'address': user_address
    }

    status = api.update_user(user_id, user_data)
    if status == 200:
        print('Usuário atualizado com sucesso!')
    else:
        print('Erro! Não foi possível atualizar o usuário.')

elif opcao == '4':
    # Deletar um usuário
    user_id = input('Digite o ID do usuário: ')
    user = api.read_user(user_id)  # Obter informações do usuário para exibir no prompt de confirmação
    campo = input(f"Deseja mesmo deletar o usuário {user['name']}? (s/n): ")
    if campo.lower() == 's':
        status = api.delete_user(user_id)
        if status == 200:
            print('Usuário deletado com sucesso!')
        else:
            print('Erro! Não foi possível deletar o usuário.')
    elif campo.lower() == 'n':
        print('Ação cancelada.')

elif opcao == '5':
    # Criar um novo usuário
    name = input("Digite o nome do usuário: ")
    username = input("Digite o apelido do usuário: ")
    email = input("Digite o email do usuário: ")

    print("-" * 30)
    print('Outros dados:')

    city = input('Informe a cidade: ')
    street = input('Informe a rua:')

    user_address = {
        'city': city,
        'street': street
    }

    user_data = {
        'name': name,
        'username': username,
        'email': email,
        'address': user_address
    }

    status = api.create_user(user_data)
    if status == 201:
        print('Novo usuário criado com sucesso!')
    else:
        print('Erro! Não foi possível criar o novo usuário.')
