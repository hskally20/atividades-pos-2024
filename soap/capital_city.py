import requests
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
pais = input('digite a cigla do pais : ')
print('digite 1 para CapitalCity  2 para CountryName e 3 para ListOfContinentsByName ')
fucao = input ('digite a fução que voce deseja utilizar :' )
result = 'sCountryISOCode'

if fucao == '1':
    fucao = 'CapitalCity'
    descricao = "Capital da cidade"
elif fucao == '2':
    fucao = 'CountryName'
    descricao = "Nome do país"
elif fucao == '3':
    fucao = 'ListOfContinentsByName'
    descricao = "Lista de continentes por nome"
payload = F"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{fucao} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{pais}</sCountryISOCode>
					</{fucao}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

print(f"\nResultado para a função '{descricao}':")
print(response.text)
