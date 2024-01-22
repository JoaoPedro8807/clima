from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={'autoflush': False}) #alguns relacionamentos biderecional (back_populates) podem dar problema de flush

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()