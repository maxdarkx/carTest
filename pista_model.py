from carril_model import carril_model
from jugador import jugador
from os import system
from time import sleep

# La pista contendra 5 carriles, cada uno de ellos con su respectivo conductor y vehiculo
class pista_model:

    # name y tipo deben ser dos vectores de 5 posiciones con los nombres y los tipos de los jugadores
    def __init__(self, name=["jugador1", "jugador2", "jugador3", "jugador4", "jugador5"] ,
                 tipo=[True, False, False, False, False]):
        self.jugador = []
        for i in range(len(name)):
            self.jugador.append(jugador(i, name[i], tipo[i]))

    # borrar la pantalla
    def clear_screen(self):
            system('clear')

    #imprime la pista completa, teniendo en cuenta las posiciones en donde estan los carros
    def print_pista(self):
        for i in self.jugador:
            print(i.carril.id)
            i.carril.print_carril()
            i.carril.espacio_print()

    # imprime la pista completa, haciendo la animacion del carril en donde se mueve el carro
    def mover_carril(self, n_carril, pos):
        #print("imprimir pista moviendose", n_carril,pos)
        for i in range(self.jugador[n_carril].carril.cond.carro.get_pos() ,pos+1):
            for j in range(len(self.jugador)):
                print(self.jugador[j].id)
                if j == n_carril:
                    self.jugador[j].carril.set_posicion(i)
                self.jugador[j].carril.print_carril()
            sleep(0.1)

            if i<pos:
                self.jugador[j].carril.clear_screen()
