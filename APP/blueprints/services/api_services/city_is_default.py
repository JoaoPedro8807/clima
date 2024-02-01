import requests, json
from datetime import datetime, timedelta, timezone
from APP.blueprints.services.city_services import city_services
from ..api_services import API_KEY
from APP.models import city_model
from APP.blueprints.services.api_services import conver_data_to_br

def verify_city_is_default(id_city):
   URL_REQUEST = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{API_KEY}/locales'
   request  = requests.request("GET", URL_REQUEST)
   response = json.loads(request.text)
   return response['locales'][0] == int(id_city) #response['locales'] retorna o id da cidade que é default na api

def get_name_current_cityDefault():
   id_city = city_model.City.query.filter_by(id=1).first().id_city
   #pegando o nome apartir do id
   name_request_url = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city/{id_city}?token={API_KEY}'
   name_request = requests.request("GET", name_request_url)
   name_response = json.loads(name_request.text)
   return {
      "cidade": name_response['name'],
      "estado": name_response['state']
   }

def verify_time_to_default_again():
      now = datetime.now(timezone.utc) - timedelta(hours=3)
      hora_city = str(city_services.get_date_city_default())
      dif = conver_data_to_br.diference_between_dates_str(hora1=now, hora2=hora_city)
      return dif


