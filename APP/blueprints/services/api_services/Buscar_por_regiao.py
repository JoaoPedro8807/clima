import requests
import json
from ..api_services import API_KEY

def search_region(region_name):
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/region/{str(region_name).title().strip()}?token={API_KEY}'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    if response.status_code == 200:
        return {
            "regiao": r['region'],
            "tag_regiao": r['acronym'],
            "results": r['data'] #indice 0 refere-se ao primeiro dia (dia atual)
        }
    else:
        return False




