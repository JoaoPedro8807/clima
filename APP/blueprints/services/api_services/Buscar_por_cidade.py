import requests
import json
from ..api_services import API_KEY

LOC_URL = 'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=your-app-token'
LOC_BAURU_AUTORIZADA = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6655/current?token=your-app-token'


def find_id_city(city_name):
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={str(city_name).strip()}&state=SP&token={API_KEY}'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    c = []
    for city in r:
        c.append({
            "id": city['id'],
            "nome": city['name'],
            "estado": city['state']
        })
    return c #escolher quais das cidades encontradas na API é a correta, depois passar para find_data_locale


def set_city_default(id_city): #1 mudança por dia.
    url_request = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_KEY}/locales'
    payload = f'localeId[]={str(id_city).strip()}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("PUT", url_request, headers=headers, data=payload)
    r = json.loads(response.text)
    return r


def find_data_locale(id_city): #pesquisar dados de uma ciddade já autorizada na api
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{str(id_city)}/current?token={API_KEY}'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    return {
        "id": r['id'],
        "nome": r['name'],
        "estado": r['state'],
        "pais": r['country'],
        "dados": r['data']
    }




