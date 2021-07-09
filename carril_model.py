from conductor_model import conductor_model
import time
import os

# esta clase se encarga de imprimir un carril con su respectiva senalizacion, y un carro asignado
# a un conductor
class carril_model:

    def __init__(self,id,size):
        self.id = id
        self.cond = conductor_model(self.id)
        self.size = size      #el tamano maximo de un carril es 100em, cada em son 10 metros
        self.pos = 0
        self.edge = "\u254D"

    # imprimir espacios antes de la impresion del carro
    def espacio_print (self):
        for i in range(self.cond.carro.get_pos()):
            print(" ", end="")

    # imprimir un retorno de carro para mostrar la siguiente seccion del carril y del carro
    def siguiente_linea_print(self):
        print()

    # borrar la pantalla
    def clear_screen(self):
        os.system('clear')

    # cambiar la posicion en la que se encuentra el carro
    def set_posicion(self,pos):
        self.pos=pos
        self.cond.carro.set_pos(pos)

    # imprimir una linea lateral al carril (mas bonito)
    def print_linea_lateral_carril(self):
        for i in range(self.size):
            print(self.edge, end="")
        self.siguiente_linea_print()

    # imprimir la parte superior del carro
    def print_sup_carro(self):
        self.espacio_print()
        print(self.cond.carro.carSup, end="")
        self.siguiente_linea_print()

    # imprimir la seccion media del carro, y las rayas del centro del carril
    def print_med_carro(self):
        k = 1
        for i in range(self.cond.carro.get_pos()):
            if k < 4:
                print("-", end="")
            elif k < 6:
                print(" ", end="")
            else:
                k = 0
                print(" ", end="")
            k += 1

        print(self.cond.carro.carMed, end="")

        for i in range(self.cond.carro.get_pos() + self.cond.carro.get_size(), self.size):
            if k < 4:
                print("-", end="")
            elif k < 6:
                print(" ", end="")
            else:
                k = 0
                print(" ", end="")
            k += 1

        self.siguiente_linea_print()

    # imprimir la parte inferior del carro
    def print_inf_carro(self):
        self.espacio_print()
        print(self.cond.carro.carInf, end="")
        self.siguiente_linea_print()

    # imprimir las lineas laterales, el carro, y la linea central
    def print_carril(self):
        self.print_linea_lateral_carril()
        self.print_sup_carro()
        self.print_med_carro()
        self.print_inf_carro()
        self.print_linea_lateral_carril()


    # hacer una animacion de carril, el carro se movera desde su posicion actual hasta pos
    # solo para imprimir un carril, solo usado en pruebas
    def mover_clear(self, pos):
        for i in range(self.pos, pos + 1):
            self.set_posicion(i)
            self.print_carril()
            time.sleep(0.1)
            if i < pos:
                self.clear_screen()
        self.pos = pos

