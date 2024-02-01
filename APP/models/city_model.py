from APP.extensoes.configuration_db import db

class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_city = db.Column(db.Integer, nullable=False)#id da API referente a cidade padrão
    nome = db.Column(db.String(50), nullable=True)
    data_default = db.Column(db.DateTime(timezone=True), nullable=False)


