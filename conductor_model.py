from car_model import car_model


class conductor_model:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre_conductor = nombre
        self.carro = car_model()

    def get_name(self):
        return self.nombre_conductor

    def get_id(self):
        return self.id
