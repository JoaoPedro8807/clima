import requests, json
from datetime import datetime, timedelta
from APP.blueprints.services.api_services import Buscar_por_cidade, conver_data_to_br

API_TOKEN = '8f3c01212174df7c569441a5c42a55a7'

def verify_city_is_default(id_city):
   URL_REQUEST = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_TOKEN}/locales'
   request  = requests.request("GET", URL_REQUEST)
   response = json.loads(request.text)
   return response['locales'][0] == int(id_city) #response['locales'] retorna o id da cidade que é default na api


def get_name_current_cityDefault():
   #pegando o id da cidade que já está definida default
   URL_REQUEST = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_TOKEN}/locales'
   request = requests.request("GET", URL_REQUEST)
   response = json.loads(request.text)
   id_city = response['locales'][0]
   #pegando o nome apartir do id
   name_request_url = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city/{id_city}?token={API_TOKEN}'
   name_request = requests.request("GET", name_request_url)
   name_response = json.loads(name_request.text)
   return {
      "cidade": name_response['name'],
      "estado": name_response['state']
   }

def get_id_current_cityDefault():
   URL_REQUEST = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_TOKEN}/locales'
   request = requests.request("GET", URL_REQUEST)
   response = json.loads(request.text)
   id_city = response['locales'][0]
   return (id_city)

def verify_time_to_default_again(id_city=0):
   if verify_city_is_default(id_city):
      r = Buscar_por_cidade.set_city_default(id_city=id_city)
      d = r['detail']
      data_from_api = d[len(d)-45: len(d)-26] #fatiando para pegar apenas a data da resposta do JSON
      api_formatada = conver_data_to_br.format_data_hora_str(data_from_api)

      d_atual = datetime.now()
      atual_formatada = conver_data_to_br.format_data_hora_str(d_atual)

      #diferença entre duas datas (que irão como string), return a diferença em segundos
      result  = conver_data_to_br.diference_between_dates_str(date1=atual_formatada, date2=api_formatada)
      dif = 86400 - result.total_seconds()
      res = str(timedelta(seconds=dif)) #str já força o objeto datetime se formatar a uma string com 'h:m:s'
      return res
   return str(timedelta(seconds=0))


def has_default_city():
   URL_REQUEST = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_TOKEN}/locales'
   request = requests.request("GET", URL_REQUEST)
   response = json.loads(request.text)
   return bool(response['locales'][0])

