from xml.dom.minidom import parse
file_path = "C:/Users/20211181110021/Desktop/atividades-pos-2024/teste/biblioteca.xml"
import json

# Importar de um arquivo
with open('C:/Users/20211181110021/Documents/atividades-pos-2024/xml/imobiliaria.xml') as json_file:
    parsed_imobiliaria= json.load(json_file)

# Importar de uma string
json_string = '{"key": "value", "array": [1, 2, 3]}'
parsed_imobiliaria = json.loads(json_string)

# Escrever em um arquivo:
imobiliaria = {}
listas_imoveis = []
for imobiliaria in imovel:
        descricao_element = imovel.getElementsByTagName('descricao')
        propietario_element = imovel.getElementsByTagName('propietario')
        nome = elemente_propietario.getAttribute('nome')
        # propietario = elemento_propietario.firstChild.nodeValue
       
        # calorias_element = prato_encontrado.getElementsByTagName('calorias')
        # calorias = calorias_element[0].firstChild.nodeValue if calorias_element else "Não disponível"
        
        # moeda_element = prato_encontrado.getElementsByTagName('moeda')
        # moeda = moeda_element[0].firstChild.nodeValue if moeda_element else "Não disponível"


with open("imobiliaria.json", "w") as json_file:
    json.dump(imobiliaria, json_file)

json_string = json.dumps(imobiliaria)
