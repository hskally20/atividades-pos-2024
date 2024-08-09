from xml.dom.minidom import parse
import json
# Importar o arquivo XML
file_path = "C:/Users/20211181110021/Documents/atividades-pos-2024/xml/imobiliaria.xml"

dom = parse(file_path)
print("Arquivo XML carregado com sucesso.")

imoveis = dom.getElementsByTagName('imovel')

imobiliaria = {}
listas_imoveis = []

for imovel in imoveis:
    descricao_element = imovel.getElementsByTagName('descricao')[0]
    descricao = descricao_element.firstChild.nodeValue 

    propietario_element = imovel.getElementsByTagName('proprietario')[0]
    nome_element = propietario_element.getElementsByTagName('nome')[0]
    nome = nome_element.firstChild.nodeValue 

    email_element = propietario_element.getElementsByTagName('email')[0]
    email = email_element.firstChild.nodeValue 
    telefone_element = propietario_element.getElementsByTagName('telefone')[0]
    telefone = telefone_element.firstChild.nodeValue 

    endereco_element = imovel.getElementsByTagName('endereco')[0]
    rua = endereco_element.getElementsByTagName('rua')[0].firstChild.nodeValue
    bairro = endereco_element.getElementsByTagName('bairro')[0].firstChild.nodeValue
    cidade = endereco_element.getElementsByTagName('cidade')[0].firstChild.nodeValue
    numero_element = endereco_element.getElementsByTagName('numero')
    numero = numero_element[0].firstChild.nodeValue 

    caracteristicas_element = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho = caracteristicas_element.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    numQuartos = caracteristicas_element.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    numBanheiros = caracteristicas_element.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue

    valor_element = imovel.getElementsByTagName('valor')[0]
    valor = valor_element.firstChild.nodeValue

    # Criando o dicionário para o imóvel
    imovel_data = {
        "descricao": descricao,
        "proprietario": {
            "nome": nome,
            "email": email,
            "telefone": telefone
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    }

    # Adicionando o imóvel à lista de imóveis
    listas_imoveis.append(imovel_data)

# Atribuindo a lista de imóveis ao dicionário imobiliária
imobiliaria["imoveis"] = listas_imoveis


with open('C:/Users/20211181110021/Documents/atividades-pos-2024/Parsers/imobiliaria.json', 'w') as json_file:
    json.dump(imobiliaria, json_file, indent=4)



