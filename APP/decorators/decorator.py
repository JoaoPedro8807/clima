from functools import wraps
from flask_jwt_extended import get_current_user, get_jwt_identity, verify_jwt_in_request
from flask import redirect, url_for, flash, request, session, abort
from APP.models.user_model import UserRole


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
