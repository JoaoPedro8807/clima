from flask import render_template, request, redirect, flash, url_for, session
from flask_login import current_user
from APP.extensoes.configuration_db import db
from APP.blueprints.services.api_services import conver_data_to_br, city_is_default
from APP.blueprints.services.user_services import user_serv
from APP.entidades import user
from APP.models import user_model
from APP.decorators.decorator import admin_required
from requests.auth import HTTPBasicAuth

def init_rotas_user(app):
    #### #
    #     @app.route('/authentication')
    #     def authentication():
    #         nome = 'admin'   #current_user.nome
    #         senha = '123' #current_user.password
    #         url = "http://127.0.0.1:5000/list_user"
    #         response =  requests.get(url, auth=HTTPBasicAuth(nome, senha))#####


    @app.route('/list_user')
    @admin_required
    def list_user():
        users = user_model.Usuario.query.all()
        for user in users:
            if user.create_at != None:
                user.create_at = conver_data_to_br.format_data_hora_str(user.create_at)

        user = {
            "id": current_user.id,
            "nome": current_user.nome,
            "email": current_user.email,
            "is_admin": bool(session.get('rules') == 'admin'),
            "data_criacao": current_user.create_at,
            "roles": []
        }
        for role in current_user.roles:
            user['roles'].append(role.nome)

        time_to_set_defaultCity = city_is_default.verify_time_to_default_again(city_is_default.get_id_current_cityDefault())
        current_defaultCity = city_is_default.get_name_current_cityDefault()
        current_id_default_city = city_is_default.get_id_current_cityDefault()
        return render_template('list_user.html', users=users, user=user, time_to_set_defaultCit=time_to_set_defaultCity, current_defaultCity=current_defaultCity, current_id_default_city=current_id_default_city )

    @app.route('/edit_user/<int:id>/')
    def edit_user(id):
        user = user_model.Usuario.query.filter_by(id=id).first()
        return render_template('edit_user.html', user=user)


    @app.route('/update_user', methods=['POST', 'GET'])
    def update_user():
        if request.method == 'POST':
            _nome = request.form.get('register_name')
            _email = request.form.get('register_email')
            _password = request.form.get('register_senha')
            _admin = request.form.get('register_admin')
            _user = user.Usuario(nome=_nome, email=_email, password=_password, is_admin=_admin)

            old_user = user_model.Usuario.query.filter_by(email=_email).first()
            update = user_serv.update_user(old_user=old_user, new_user=_user)

            if update['status'] == True:
                if _admin:
                    user_serv.add_new_userRole(id_user=old_user.id, id_role=1)#adicionando mais um admin na tabela user_roles!
                flash(update['message'])
                return redirect(url_for('list_user'))
            else:
                flash(f'Error')
                return redirect(url_for('edit_user'))


    @app.route('/delete_user/<int:id>', methods=['POST'])
    def delete_user(id):
        if request.method == 'POST':
            user = user_model.Usuario.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            flash(f'Usuario {user.nome} excluido com sucesso!')
            return redirect(url_for('list_user'))



