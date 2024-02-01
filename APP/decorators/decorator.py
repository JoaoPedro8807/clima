from functools import wraps
import requests
from flask_jwt_extended import get_current_user, get_jwt_identity, verify_jwt_in_request
from flask import redirect, url_for, flash, session



def check_admin(nome, senha):
    return nome == "admin" and senha == "123"

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('rules') != 'admin':
            flash("Apenas administadores podem acessar essa página!", 'error')
            return redirect(url_for('menu'))
        return f(*args, **kwargs)
    return decorated


def default_city_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        url = 'http://apiadvisor.climatempo.com.br/api-manager/user-token/db6786831ebdc54ac3b57cb043113ca5/locales'
        if not requests.request("GET", url=url).status_code == 200:
            flash(f'Nenhuma cidade padrão definida! Defina uma cidade antes de começar')
            return redirect(url_for('set_default'))
        else:
            return f(*args, **kwargs)
    return decorator


