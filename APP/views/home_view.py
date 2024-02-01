import datetime
from flask import render_template, redirect, url_for, flash, request, session
from APP.blueprints.services.user_services import user_serv
from APP.blueprints.services.api_services import Buscar_por_cidade
from APP.blueprints.services.city_services import city_services
from APP.entidades import user
from datetime import timedelta
from flask_login import login_user, logout_user, login_required

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

                if city_services.is_possible_set_city():
                    flash('Nenhuma cidade definida, defina uma cidade padrão para prosseguir!')
                    return redirect(url_for('set_default'))
                else:
                    flash(f'{iUser["message"]}', category='sucess')
                    return redirect(url_for('menu'))
            else:
                flash(f'{iUser["message"]}', category='error')
                return redirect(url_for('index'))


    @app.route('/set_default', methods=["POST", "GET"])
    @login_required
    def set_default():
        if request.method == 'POST':
            city_name = str(request.form['register_city'])
            citys = Buscar_por_cidade.find_id_city(city_name)
            if citys:
                return render_template('set_default.html', citys=citys, len_city=len(citys))
            else:
                flash(f'Nenhuma cidade com o nome {city_name} foi encontrada', 'error')
                return redirect(url_for('set_default'))
        return render_template('set_default.html')



    @app.route('/define_default/<int:city_id>')
    def define_default(city_id):
        if city_services.is_possible_set_city():
            city_defualt = Buscar_por_cidade.set_city_default(city_id)
            if city_defualt['status']:
                city_services.put_default_city(id_city=city_id, data_default=datetime.datetime.now())
                flash('Cidade definida como padrão com sucesso!')
                return redirect(url_for('menu'))
            else:
                flash(f'Algum erro ao definir cidade padrão: {city_defualt["error"]} ')
                return redirect(url_for('set_default'))

        return redirect(url_for('menu'))


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




