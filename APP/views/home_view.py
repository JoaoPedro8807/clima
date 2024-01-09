from flask import render_template, redirect, url_for, flash, request
from APP.blueprints.services.user_services import user_serv
from APP.entidades import user
from datetime import timedelta
from flask_login import login_user, logout_user, login_required
def init_rotas_home(app):

    API_TOKEN = '8f3c01212174df7c569441a5c42a55a7'
    LOC_URL = 'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=your-app-token'

    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            _user = str(request.form['user_email']).strip()
            _pass = str(request.form['user_pass']).strip()
            iuser = user_serv.login_verify_user(email=_user, password=_pass)

            if iuser['status'] == True: #login sucessful
                user = user_serv.get_user_by_email(_user)
                login_user(
                    user,
                    remember=False,
                    duration=timedelta(minutes=10))


                flash(f'{iuser['message']}', category='sucess')
                return redirect(url_for('menu'))

            else:
                flash(f'{iuser['error']}', category='error')
                return redirect(url_for('index'))

    @app.route('/register', methods=['POST', 'GET'])
    def register():

        return render_template('register.html')



    @app.route('/registrar', methods=['POST'])
    def registrar():
        if request.method == 'POST':
            _nome = str(request.form.get('register_name')).strip()
            _email = str(request.form.get('register_email')).strip()
            _senha = str(request.form.get('register_senha')).strip()

            _user = user.Usuario(
                nome=_nome,
                email=_email,
                password=_senha,
                is_admin=False
            )
            create_user = user_serv.create_user(_user)
            flash("Usuario cadastrado com sucesso!", category='success')
            return redirect(url_for('index'))

    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))




