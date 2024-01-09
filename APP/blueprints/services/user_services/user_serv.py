from APP.entidades.user import Usuario
from APP.models import user_model
from APP.extensoes.configuration_db import db

def create_user(user):
    if isinstance(user, Usuario):
        user_bd = user_model.Usuario(nome=user.nome, email=user.email, password=user.password, is_admin=user.is_admin)
        db.session.add(user_bd)
        db.session.commit()

def login_verify_user(email, password):
    _e = str(email).strip()
    _p = str(password).strip()
    _u = user_model.Usuario.query.filter_by(email=_e, password=_p).first()
    if not _u:
        return {
            "status": False,
            "error": "Email ou senha estão incorretos"
        }
    else:
        return {
            "status": True,
            "message": f"Login realizado com sucesso. Bem-vindo"
        }


def get_name_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first().nome

def get_email_by_name(name):
    return user_model.Usuario.query.filter_by(nome=name).first().email

def get_id_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first().id

def get_user_by_email(email):
    return user_model.Usuario.query.filter_by(email=email).first()