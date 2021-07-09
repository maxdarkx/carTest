#modelo basico de un conductor

from car_model import car_model

# la clase conductor solo cuenta con un id y un carro correspondiente, y sera agregada a un jugador
# que podra ser la maquina o un usuario
class conductor_model:

    def __init__(self, id):
        self.id = id
        self.carro = car_model()

    def get_id(self):
        return self.id
