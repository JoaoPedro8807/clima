from flask import Flask
from APP.extensoes import configuration_app, configuration_db, configuration_migrate, configuration_jwt, configuration_login, configuration_session
from APP.views import home_view, menu_view, recursos_view, user_view


app = Flask(__name__)

#app context
configuration_app.__init__config_app(app)
configuration_db.init_db(app)
configuration_migrate.init_migrate(app) #db já passei no própio arqv
configuration_jwt.init_jwt(app)

#views
home_view.init_rotas_home(app)
menu_view.init_rotas_menu(app)
recursos_view.init_rotas_recursos(app)
user_view.init_rotas_user(app)

#login
configuration_login.init_login_mangager(app)


#session -> Libary
configuration_session.init_session(app)

from APP.models import user_model


if __name__ == '__main__':
    app.run(debug=True)
