from flask import render_template, redirect, url_for, flash, request
from APP.blueprints.services.api_services import city_is_default, conver_data_to_br
from flask_login import login_required, user_accessed, current_user


def init_rotas_menu(app):
    @app.route('/menu')
    @login_required #decorator do flask_login, basicamente usa o session para controlar o acesso a determinadas  rotas
    def menu():
        user = {
            "id": current_user.id,
            "nome": current_user.nome,
            "email": current_user.email,
            "admin": current_user.is_admin,
        }

        time_to_set_defaultCity = city_is_default.verify_time_to_default_again(city_is_default.get_id_current_cityDefault()) #verificar o tempo p/ definir dnv passando o id da cidade default
        current_defaultCity = city_is_default.get_name_current_cityDefault()
        current_id_default_city = city_is_default.get_id_current_cityDefault()
        return render_template(
            'menu.html',
            user=user,
            time_to_set_defaultCity=time_to_set_defaultCity,
            current_defaultCity=current_defaultCity,
            current_id_city=current_id_default_city
        )





