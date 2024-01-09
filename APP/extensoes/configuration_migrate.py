from flask_migrate import Migrate
from .configuration_db import db

migrate = Migrate()

def init_migrate(app, db=db):
    migrate.init_app(app, db)