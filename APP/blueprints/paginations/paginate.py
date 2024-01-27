from flask import request
from flask_paginate import Pagination
import math


def get_item_pagination(itens_list, offset, per_page):
        return itens_list[offset:offset+per_page]


def pagination(itens_list, total, nome:str, page, per_page):
    offset = (page - 1) * per_page
    itens_paginados = get_item_pagination(itens_list=itens_list, offset=offset, per_page=per_page)
    display = (per_page*page) - ((per_page*page) - total) if math.ceil(total/per_page) == page else offset+per_page #se for a última página, pega a última posição que seria apresentada na página e subtrai da diferença dessa última posição pelo total de itens
    pagination = Pagination(page=page, per_page=per_page, total=total, record_name=nome, display_msg=f'Mostrando do {offset+1}°  usuário ao {display}° do total de:  {total}')
    return {
        'itens_paginados': itens_paginados,
        'pagination': pagination
    }



