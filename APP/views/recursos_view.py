from flask import render_template, redirect, url_for, flash, request
from APP.blueprints.services.api_services import Buscar_por_cidade, city_is_default, conver_data_to_br, Buscar_24H, Buscar_por_regiao
from APP.blueprints.services.city_services import city_services
from flask_login import current_user, login_required
from flask_paginate import Pagination
from datetime import datetime
from APP.decorators.decorator import default_city_required


user = current_user
def get_temperatura(offset=0, per_page=4):
    JsonTemp = Buscar_24H.search_all_24_city(city_services.get_id_city_default())
    global temp
    temp = JsonTemp[1:len(JsonTemp)]
    return temp[offset:offset+per_page]

def init_rotas_recursos(app):

    @app.route('/cidade', methods=['GET', 'POST']) #Já pronto para receber qualquer cidade, caso a API deixe  de ser grratuita
    @login_required
    @default_city_required
    def cidade():
        current_defaultCity = city_is_default.get_name_current_cityDefault()
        current_id_default_city = city_services.get_id_city_default()

        if request.method == 'POST':
            cidade_input = request.form.get('cidade_input').strip()
            cidades = Buscar_por_cidade.find_id_city(cidade_input)
            if cidades:
                return render_template('escolher_cidade.html', cidades=cidades, len_cidades=len(cidades), user=user, current_defaultCity=current_defaultCity, current_id_default_city=current_id_default_city)
            flash(f'Cidade {cidade_input} não encontrada, digite corretamente', 'error')
            return redirect(url_for('cidade'))
        return render_template('escolher_cidade.html', user=user, current_defaultCity= current_defaultCity, current_id_default_city=current_id_default_city)


    @app.route('/cidade/<int:id_city>/clima')
    @login_required
    @default_city_required
    def clima(id_city):
        if city_is_default.verify_city_is_default(id_city):
            dados = Buscar_por_cidade.find_data_locale(id_city)
            data = dados['dados']['date'].split(' ')
            data_busc = {
                "data": conver_data_to_br.format_data(data[0]),
                "horario": data[1]
            }
            return render_template('show_temp_cidade.html',
                                   dados=dados, results=dados['dados'],
                                   data_busc=data_busc)
        #tratando dados da API
        default_city = city_is_default.get_name_current_cityDefault()
        time = city_is_default. verify_time_to_default_again()

        flash(f'Cidade escolhida não é a padrão, atual cidade padrão: {default_city["cidade"]} ({default_city["estado"]})' 
             f'Você pode definir uma nova cidade padrão em: {time}', 'error')
        return redirect(url_for('cidade'))


    @app.route('/cidade/<int:id_city>/clima24h')
    @login_required
    @default_city_required
    def clima24h(id_city):
        #definindo os parâmetros pro pagination
        page = request.args.get('page', 1, type=int)
        per_page = 4
        offset = (page - 1) * per_page #contador da amostragem do resultado
        pagination_temperaturas = get_temperatura(offset=offset, per_page=4)
        total = len(temp)
        #definindo a pagina de começo de acordo com o horário atual do client
        hora = datetime.now().hour
        pag = int((hora / per_page) + 1) #pegando a hora atual do client subtraindo pela qntd de horarios por pag e somando 1, para saber em qual pagina estará o horario

        pagination = Pagination(page=page, per_page=per_page, total=total, record_name='horários', inner_window=pag)

        return render_template(
            'show_temp_24h_city.html',
            offset=offset,
            itens=pagination_temperaturas,
            pagination=pagination)


    @app.route('/regiao')
    @login_required
    @default_city_required
    def regiao():
        current_defaultCity = city_is_default.get_name_current_cityDefault()
        current_id_default_city = city_services.get_id_city_default()
        return render_template('escolher_regiao.html', user=user, current_defaultCity=current_defaultCity, current_id_default_city=current_id_default_city)

    @app.route('/regiao/clima', methods=('GET', 'POST'))
    @login_required
    @default_city_required
    def regiao_clima():
        if request.method == 'POST':
            region_name = request.form.get('regiao_input').strip()
            r = Buscar_por_regiao.search_region(region_name)
            if not r:
                flash(f'Região {region_name} não encontrada, por favor, digite corretamente', 'error')
                return redirect(url_for('regiao'))

            regiao = r['regiao']
            tag = r['tag_regiao']
            results = r['results']
            return render_template('show_temp_regiao.html', regiao=regiao, tag=tag, results=results)




