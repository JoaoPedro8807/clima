from APP.extensoes.configuration_db import db
from flask_login import UserMixin
from APP.extensoes.configuration_login import login_manager
from sqlalchemy.sql import func #biblioteca para o banco capturar a hora de criação da linha. É melhor capturar no banco do q no cliente

class Usuario(UserMixin, db.Model): #UserMixin biblioteca para o flask_login reconhecer o model aonde está as credencias de login e conseguir interagir
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)
    data_criacao = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=True) #Server default serve para que o banco insira alguma data padrão quando adicionarmos alguma linha na tabela. Passamos para ele uma função sql do sqlalchemy que captura a data no ato da gravação
    #também poderiamos criar uma coluna para data de atualização da linha: time_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())


    @login_manager.user_loader #método obrigatório para carregar um usuário ao login ser efetuado.
    def load_user(user_id):
        return Usuario.query.get(int(user_id))