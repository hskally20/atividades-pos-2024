from xml.dom.minidom import parse 
import json

# Carregar o arquivo JSON
try:
    with open('parsers/imobiliaria.json', 'r') as json_file:
        parsed_data = json.load(json_file)  # Carrega o JSON e converte em dicionário Python
except FileNotFoundError:
    print("O arquivo 'imobiliaria.json' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")

def listar_imoveis(imoveis):
   for imovel in imoveis:
        print("\nDetalhes do imóvel encontrado:")
        print(f"Descrição: {imovel.get('descricao', 'N/A')}")
        print(f"Tamanho: {imovel.get('caracteristicas', {}).get('tamanho', 'N/A')} m²")
        print(f"Quartos: {imovel.get('caracteristicas', {}).get('numQuartos', 'N/A')}")
        print(f"Banheiros: {imovel.get('caracteristicas', {}).get('numBanheiros', 'N/A')}")
        
        # Informações do proprietário
        proprietario = imovel.get('proprietario', {})
        print(f"Nome do Proprietário: {proprietario.get('nome', 'N/A')}")
        print(f"Telefone do Proprietário: {proprietario.get('telefone', 'N/A')}")
        print(f"Email do Proprietário: {proprietario.get('email', 'N/A')}")
        
        print("---\n")

# Supondo que parsed_data tenha uma chave 'imoveis' que é uma lista
# Passa a lista de imóveis para a função



while True:
        print("\nMenu:")
        print("1. Ver detalhes do imovel")
        print("2. Sair")
        
        escolha = input("Escolha uma opção (1 ou 2): ").strip()
        
        if escolha == '1':
          if parsed_data:
             listar_imoveis(parsed_data.get('imoveis', []))  
        elif escolha == '2':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
