from APP.models import city_model
from APP.entidades.city import  City
from APP.extensoes.configuration_db import db
from datetime import datetime


def put_default_city(id_city, data_default, nome=None):
    city = City(id_city=id_city, nome=nome, data_default=data_default)
    old_city = get_city_default()
    old_city.id_city = city.id_city
    old_city.nome = city.nome
    old_city.data_default = city.data_default
    db.session.add(old_city)
    db.session.commit()

def get_city_default():
    return city_model.City.query.filter_by(id=1).first()

def get_id_city_default():
    return city_model.City.query.filter_by(id=1).first().id_city


def get_date_city_default():
    return city_model.City.query.filter_by(id=1).first().data_default

def is_possible_set_city():
    now = datetime.now()
    str_city = str(get_date_city_default())
    data_city = datetime.strptime(str_city, "%Y-%m-%d %H:%M:%S+00:00")
    dif = (now - data_city).total_seconds()
    return dif >= 86400

