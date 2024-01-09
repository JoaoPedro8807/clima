import requests
import json

API_TOKEN = '8f3c01212174df7c569441a5c42a55a7'
LOC_URL = 'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=your-app-token'
LOC_BAURU_AUTORIZADA = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6655/current?token=your-app-token'


def find_id_city(city_name):
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={str(city_name).strip()}&state=SP&token=8f3c01212174df7c569441a5c42a55a7'
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


def set_city_default(id_city): #set default city one change for day.
    #id_bauru = '6655'  # dinamizar
    url_request = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_TOKEN}/locales'
    payload = f'localeId[]={str(id_city).strip()}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("PUT", url_request, headers=headers, data=payload)
    r = json.loads(response.text)
    return r


def find_data_locale(id_city): #metodo para pesquisar dados de uma ciddade já autorizada na api (aplicar um decorator)
    url_request = f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{str(id_city)}/current?token={API_TOKEN}'
    response = requests.request("GET", url_request)
    r = json.loads(response.text)
    return {
        "id": r['id'],
        "nome": r['name'],
        "estado": r['state'],
        "pais": r['country'],
        "dados": r['data']
    }




