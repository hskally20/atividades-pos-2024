from xml.dom.minidom import parse 
import json

# Carregar o arquivo JSON
try:
  with open('parsers/imobiliaria.json', 'r', encoding='utf-8') as json_file:
        parsed_data = json.load(json_file)  # Carrega o JSON e converte em dicionário Python
except FileNotFoundError:
    print("O arquivo 'imobiliaria.json' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")

def lista_nomes_imoveis(imoveis):
      print(" imoveis existentes :")
      for imovel in imoveis:
        print(f" {imovel.get('descricao' , 'NDA')} , id : {imovel.get('id' , 'NDA')}")
    

def exibir_detalhes_imovel(imoveis):
    for imovel in imoveis:
            print("\nDetalhes do imóvel selecionado:")
            print(f"ID: {imovel.get('id')}")
            print(f": {imovel.get('descricao', 'N/A')}")
            print(f"Tamanho: {imovel.get('caracteristicas', {}).get('tamanho', 'N/A')} m²")
            print(f"Quartos: {imovel.get('caracteristicas', {}).get('numQuartos', 'N/A')}")
            print(f"Banheiros: {imovel.get('caracteristicas', {}).get('numBanheiros', 'N/A')}")
            # Informações do proprietário
            proprietario = imovel.get('proprietario', {})
            print(f"Nome do Proprietário: {proprietario.get('nome', 'N/A')}")
            print(f"Telefone do Proprietário: {proprietario.get('telefone', 'N/A')}")
            print(f"Email do Proprietário: {proprietario.get('email', 'N/A')}")
            print("---\n")
            return
    print("Imóvel não encontrado.")


# Supondo que parsed_data tenha uma chave 'imoveis' que é uma lista
# Passa a lista de imóveis para a função


while True:
    print("\nMenu:")
    print("1. Ver a lista de imóveis disponíveis")
    print("2. Sair")
    
    escolha = input("Escolha uma opção (1 ou 2): ").strip()
    
    if escolha == '1':
        if parsed_data:
            lista_nomes_imoveis(parsed_data.get('imoveis', []))
            print("============  ===============")
            print("1 Ver detalhes do imóvel pesquisando pelo ID ? ")
            print("se sim digite 1  se nao digite 2 ")
            escolha2 = input(" Digite aqui o id aki  ").strip()
            if escolha2 == '1':
                id_imovel = input("Digite o ID do imóvel ").strip()
                exibir_detalhes_imovel(parsed_data.get('imoveis', []))

        else:
            print("Saindo do programa...")
    
    elif escolha == '2':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
