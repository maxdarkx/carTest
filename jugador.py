# modelo basico de un jugador

from carril_model import carril_model

# a un jugador se asigna un carril, conductor y carro. Si el jugador es un usuario, su tipo sera True
# si es la maquina su tipo sera False
class jugador:
    def __init__(self, id, nombre, tipo=False, size=150):
        self.id = id
        self.name = nombre
        self.tipo = tipo
        self.size = size
        self.carril = carril_model(id)

    def get_name(self):
        return self.name

    def get_tipo(self):
        return self.tipo

    def set_name(self, nom):
        self.name = nom
        return self.name

    def set_tipo(self):
        self.tipo = not self.tipo
        return self.tipo

    def get_id(self):
        return self.id

