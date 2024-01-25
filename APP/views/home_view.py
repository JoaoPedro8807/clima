from flask import render_template, redirect, url_for, flash, request, current_app, session
from APP.blueprints.services.user_services import user_serv
from APP.entidades import user
from datetime import timedelta
from flask_login import login_user, logout_user, login_required, current_user
def init_rotas_home(app):
    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            _user = str(request.form['user_email']).strip()
            _pass = str(request.form['user_pass']).strip()

            iUser = user_serv.login_verify_user(email=_user, password=_pass)
            if iUser['status'] == True:
                user = user_serv.get_user_by_email(_user)
                if user_serv.is_admin(user.id):
                    session['rules'] = 'admin'
                else:
                    session['rules'] = 'user'
                session.permanent = True

                login_user(
                    user,
                    remember=False,
                    duration=timedelta(minutes=60))

                flash(f'{iUser['message']}', category='sucess')
                return redirect(url_for('menu'))

            else:
                flash(f'{iUser['message']}', category='error')
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
            _isadmin = bool(request.form.get('register_admin'))
            _user = user.Usuario(
                nome=_nome,
                email=_email,
                password=_senha,
                is_admin=_isadmin
            )
            create_user = user_serv.create_user(_user)
            if _isadmin:
                user_serv.add_new_userRole(id_user=create_user.id, id_role=1)
            flash("Usuario cadastrado com sucesso!", category='success')
            return redirect(url_for('index'))

    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        session.pop('rules', default=None)
        logout_user()
        return redirect(url_for('index'))




