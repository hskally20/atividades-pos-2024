import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_city = "NO"

result = client.service.CapitalCity(
sCountryISOCode=country_city
)

print(f"A capital da {country_city} é {result}")
print(f"A capital da {country_city} é {result}")