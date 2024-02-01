from datetime import datetime, timedelta
def format_data(data):
    date = datetime.strptime(data, '%Y-%m-%d').date() # 'p'de  parse (tornar em um objeto datetime) passando o formato que já vem na string
    date_format = date.strftime('%d/%m/%y') # 'f'  de format
    return date_format

def format_data_hora_str(data_hora):
    if type(data_hora) == str:
        data_h = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S')
        data_h_string  = data_h.strftime('%d/%m/%Y %H:%M:%S')
        return data_h_string
    #se não será do tipo datetime
    data_h_string = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    return data_h_string

def form_hora_str(hora):
    hora_string = hora.strftime('%H:%M:%S')
    return hora_string

def diference_between_dates_str(hora1, hora2):
    _h1 = form_hora_str(hora1)

    hora_city_dt = datetime.strptime(hora2[0:19], '%Y-%m-%d %H:%M:%S')
    _h2 = form_hora_str(hora_city_dt)

    h1 = datetime.strptime(_h1, '%H:%M:%S')
    h2 = datetime.strptime(_h2, '%H:%M:%S')
    tempo = h2 - h1
    return tempo
