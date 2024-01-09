from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'index' #a view da onde vem o post para logar, o redirect, caso não tenha feito o login, irá ser pra essa rota
login_manager.login_message = f"Para acessar essa página é preciso estar logado. Por favor faça o login"
def init_login_mangager(app):
    login_manager.init_app(app)
