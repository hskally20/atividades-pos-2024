from xml.dom.minidom import parse
file_path = "imobiliaria.json"
def listar_imoveis(imoveis):
    
    print("\nPratos disponíveis:")
    for imovel in imoveis:
        id_atributo = imovel.getAttribute('id')
        descricao_element = imovel.getElementsByTagName('descricao')
        nome = nome_element[0].firstChild.nodeValue if nome_element else "Nome não disponível"
        print(f"ID: {id_atributo} - Nome: {nome}")
while True:
        print("\nMenu:")
        print("1. Ver detalhes de um prato")
        print("2. Sair")
        
        escolha = input("Escolha uma opção (1 ou 2): ").strip()
        
        if escolha == '1':
            listar_pratos(pratos)
            resposta = input('\nDigite o ID ou nome do prato que você quer saber mais detalhes: ').strip().lower()
            prato_encontrado = None
            
            
            for prato in pratos:
                id_atributo = prato.getAttribute('id')
                nome_element = prato.getElementsByTagName('nome')
                nome = nome_element[0].firstChild.nodeValue.lower() if nome_element else ""

                if resposta == id_atributo or resposta == nome:
                    prato_encontrado = prato
                    break

            if prato_encontrado:
                exibir_detalhes(prato_encontrado)
            else:
                print("Prato não encontrado. Verifique o ID ou nome e tente novamente.")
        
        elif escolha == '2':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
