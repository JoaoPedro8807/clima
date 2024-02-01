from flask import render_template, session
from APP.blueprints.services.api_services import city_is_default, conver_data_to_br
from APP.blueprints.services.city_services import city_services
from flask_login import login_required, current_user
def init_rotas_menu(app):
    @app.route('/menu')
    @login_required
    def menu():
        user = {
            "id": current_user.id,
            "nome": current_user.nome,
            "email": current_user.email,
            "is_admin": bool(session.get('rules') == 'admin'),
            "data_criacao": conver_data_to_br.format_data_hora_str(current_user.create_at),
            "roles": []
        }
        for role in current_user.roles:
            user['roles'].append(role.nome)

        time_to_set_defaultCity = city_is_default.verify_time_to_default_again()

        current_defaultCity = city_is_default.get_name_current_cityDefault()
        current_id_default_city = city_services.get_id_city_default()
        return render_template(
            'menu.html',
            user=user,
            time_to_set_defaultCity=time_to_set_defaultCity,
            current_defaultCity=current_defaultCity,
            current_id_city=current_id_default_city
        )





