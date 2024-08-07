from xml.dom.minidom import parse

file_path = "C:/Users/20211181110021/Desktop/atividades-pos-2024/xml/cardapio.xml"

try:

    dom = parse(file_path)
    print("Arquivo XML carregado com sucesso.")
    pratos = dom.getElementsByTagName('prato')
    print(f"Total de pratos diponiveis: {len(pratos)}")
    resposta = input('Digite o ID ou nome do prato que você quer saber mais detalhes: ').strip().lower() 
    prato_encontrado = None
    
    for prato in pratos:
        id_atributo = prato.getAttribute('id')
        nome_element = prato.getElementsByTagName('nome')
        nome = nome_element[0].firstChild.nodeValue.lower() if nome_element else ""
        
        if resposta == id_atributo or resposta == nome:
            prato_encontrado = prato
            break
    
    if prato_encontrado:
        # Obtém detalhes do prato encontrado
        id_atributo = prato_encontrado.getAttribute('id')
        
        descricao_element = prato_encontrado.getElementsByTagName('descricao')
        descricao = descricao_element[0].firstChild.nodeValue if descricao_element else "Não disponível"
        
        ingredientes_element = prato_encontrado.getElementsByTagName('ingredientes')
        if ingredientes_element:
            ingredientes = ingredientes_element[0]
            ingredientes_list = [item.firstChild.nodeValue for item in ingredientes.getElementsByTagName('ingrediente')]
        else:
            ingredientes_list = ["Não disponível"]
        
        preco_element = prato_encontrado.getElementsByTagName('preco')
        preco = preco_element[0].firstChild.nodeValue if preco_element else "Não disponível"
        
        calorias_element = prato_encontrado.getElementsByTagName('calorias')
        calorias = calorias_element[0].firstChild.nodeValue if calorias_element else "Não disponível"
        
        moeda_element = prato_encontrado.getElementsByTagName('moeda')
        moeda = moeda_element[0].firstChild.nodeValue if moeda_element else "Não disponível"

        
        print(f"ID: {id_atributo}")
        print("Nome:", nome_element[0].firstChild.nodeValue)
        print("Descrição:", descricao)
        print("Ingredientes:", ", ".join(ingredientes_list))
        print("Preço:", preco)
        print("Calorias:", calorias)
        print("Moeda:", moeda)
        print("---\n")
    else:
        print("Prato não encontrado. Verifique o ID ou nome e tente novamente.")

except FileNotFoundError:
    print(f"Arquivo não encontrado: {file_path}")
except Exception as e:
    print(f"Erro ao carregar o arquivo XML: {e}")
