import requests
import json
from ..api_services import API_KEY

def  search_all_24_city(city_id):
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{str(city_id).strip()}/hours/72?token={(API_KEY)}'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    result = [{
        "nome": r['name'],
        "estado": r['state'],
        "pais": r['country']
    }]
    for i in range(0, 24):
        result.append({
            f'data': r['data'][i]['date_br'],
            f'humidade': r['data'][i]['humidity']['humidity'],
            f'chuva': r['data'][i]['rain']['precipitation'],
            f'vento': r['data'][i]['wind']['velocity'],
            f'vento_direcao': r['data'][i]['wind']['direction'],
            f'temperatura': r['data'][i]['temperature']['temperature']
        })
    return result
