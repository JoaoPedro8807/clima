from flask_jwt_extended import JWTManager
from APP.blueprints.services.user_services.user_serv import get_user_by_id

jwt = JWTManager()

def init_jwt(app):
    jwt.init_app(app)


