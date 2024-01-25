from flask import request
from flask_paginate import Pagination


def get_item_pagination(itens_list, offset, per_page):
        return itens_list[offset:offset+per_page]


def pagination(itens_list, total, nome:str, page, per_page):
    offset = (page - 1) * per_page
    itens_paginados = get_item_pagination(itens_list=itens_list, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, record_name=nome)
    return {
        'itens_paginados': itens_paginados,
        'pagination': pagination
    }



