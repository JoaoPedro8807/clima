import datetime

from APP.entidades.user import Usuario
from APP.models import user_model
from APP.extensoes.configuration_db import db
from datetime import datetime
from pytz import timezone

fuso = timezone('America/Sao_Paulo')
def create_user(user):
    if isinstance(user, Usuario):
        user_bd = user_model.Usuario(nome=user.nome, email=user.email, password=user.password, is_admin=user.is_admin, create_at=datetime.now().astimezone(fuso))
        user_bd.criptografar_senha()
        db.session.add(user_bd)
        db.session.commit()
def update_user(old_user, new_user):
    if isinstance(new_user, Usuario):
        old_user.nome = new_user.nome
        old_user.password = new_user.password
        old_user.is_admin = bool(new_user.is_admin)
        old_user.criptografar_senha()
        db.session.commit()
        return {
            "status": True,
            "message": f"Usuario {old_user.nome} atualizado com sucesso!"
        }
def login_verify_user(email, password):
    _user = get_user_by_email(email)
    _p = user_model.Usuario.query.filter_by(email=email).first()

    if not _user or not _p.verify_senha(password):
        return {
            "status": False,
            "message": "Usuário ou senha estão incorretos!"
        }
    return {
        "status": True,
        "message": "Usuário logado com sucesso!"
    }
def is_admin(id):
    UR = user_model.UserRole.query.filter_by(user_id=id).first()
    if not UR:
        return False
    return UR.user_id == id and UR.role_id == 1

def add_new_userRole(id_user,id_role):
    userRole = user_model.UserRole(user_id=id_user, role_id=id_role)
    db.session.add(userRole)
    db.session.commit()


def get_name_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first().nome

def get_email_by_name(name):
    return user_model.Usuario.query.filter_by(nome=name).first().email

def get_id_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first().id
def get_user_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first()
def get_user_by_id(id):
    return user_model.Usuario.query.filter_by(id=id).first()


