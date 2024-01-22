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


def diference_between_dates_str(date1, date2): #2
    if type(date1) and type(date2) == str:
        _date1 = datetime.strptime(date1, '%d/%m/%Y %H:%M:%S')
        _date2 = datetime.strptime(date2, '%d/%m/%Y %H:%M:%S')
        tempo = _date1 - _date2
        return tempo
