from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import redirect, jsonify, url_for

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not verify_jwt_in_request():
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper