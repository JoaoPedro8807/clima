class City():
    def __init__(self, id_city, nome, data_default):
        self._id_city = id_city
        self._nome = nome
        self._data_default = data_default

    @property
    def id_city(self):
        return self._id_city

    @id_city.setter
    def id_city(self, id_city):
        self._id_city = id_city

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_default(self):
        return self._data_default
    @data_default.setter
    def data_default(self, data):
        self._data_default = data



