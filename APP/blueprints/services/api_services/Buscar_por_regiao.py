import requests
import json

API_KEY = '8f3c01212174df7c569441a5c42a55a7'

def search_region(region_name):
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/region/{str(region_name).title().strip()}?token=8f3c01212174df7c569441a5c42a55a7'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    regiao = r['region']
    tag_regiao = r['acronym']
    return {
        "regiao": regiao,
        "tag_regiao": tag_regiao,
        "results": r['data'] #indice 0 refere-se ao primeiro dia (dia atual)
    }




