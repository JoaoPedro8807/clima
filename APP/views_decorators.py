from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import redirect, url_for, session

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session['rules'] == 'admin':
            return redirect(url_for('/login'))
        else:
            return f(*args, **kwargs)
    return wrapper()
