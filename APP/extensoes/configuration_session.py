from flask_session import Session

session = Session()

def init_session(app):
    session.init_app(app)

