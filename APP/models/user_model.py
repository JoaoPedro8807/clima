from datetime import datetime
from APP.extensoes.configuration_db import db
from flask_login import UserMixin
from APP.extensoes.configuration_login import login_manager
from passlib.hash import pbkdf2_sha256
from sqlalchemy.sql import func #biblioteca que capturar a hora de criação da linha no banco. É melhor capturar no banco
class Usuario(UserMixin, db.Model): #UserMixin biblioteca para o flask_login reconhecer o model aonde está as credencias de login e conseguir interagir
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)
    create_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=True)
    #update_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), onupdate=datetime.now(),  nullable=True)             #Server default serve para que o banco insira alguma data padrão quando adicionarmos alguma linha na tabela. Passamos para ele uma função sql do sqlalchemy que captura a data no ato da gravação    #também poderiamos criar uma coluna para data de atualização da linha: time_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    roles = db.relationship('Role', secondary='user_roles', back_populates='users')

    def has_role(self, role):
        return bool(Role.query.
                    join(Role.users)
                    .filter(Usuario.id == self.id)
                    .filter(Role.slug == role)
                    .count() == 1
                    )

    def criptografar_senha(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.password)

    @login_manager.user_loader #método obrigatório para carregar um usuário ao login ser efetuado.
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)

    users = db.relationship('Usuario', secondary='user_roles', back_populates='roles')


class UserRole(db.Model):
    __tablename__ = 'user_roles'


    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)

