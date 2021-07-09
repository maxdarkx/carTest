from pista_model import pista_model
from os import system
from time import sleep

class juego:
    def __init__(self):
        self.p1 = pista_model()
        self.jugadores = ["jugador1", "jugador2", "jugador3", "jugador4", "jugador5"]
        self.tipo=[True, False, False, False, False]

    def menu(self):
        op = True
        while op:
            self.clear_screen()
            print("1. Seleccione los nombres de los jugadores")
            print("2. Selecciones los tipos de jugadores")
            print("3. jugar")
            a = input("Ingrese su opcion: ")
            try:
                b = int(a)

            except:
                print("Ha introducido un valor no valido. Intentelo de nuevo")
                sleep(2)
                continue
            if 0 < b < 4:
                op = False
            else:
                print("Opcion no valida, intentelo de nuevo")
                sleep(2)
                continue
            print(b)
        if b == 1:
            self.nombres_jugadores()
        elif b == 2:
            self.tipo_jugadores()
        else:
            self.jugar()

    @staticmethod
    def clear_screen():
        system('clear')

    def nombres_jugadores(self):
        op = True
        while op:
            self.clear_screen()
            for i in self.p1.jugador:
                print("Jugador", i.get_id(), ":", i.get_name(), sep=" ")
            a = input("Ingrese el id del jugador que desea cambiar: ")
            try:
                b = int(a)
            except:
                print("Ha introducido un valor no valido. Intentelo de nuevo")
                sleep(2)
                continue
            if 0 <= b <= 4:
                op = False
            else:
                print("Opcion no valida, intentelo de nuevo")
                sleep(2)
                continue
        print("Ingrese el nuevo nombre para el jugador ",b)
        c = input()
        self.p1.jugador[b].set_name(c)

        self.clear_screen()
        for i in self.p1.jugador:
            print("Jugador", i.get_id(), ":", i.get_name(), sep=" ")
        sleep(2)
        self.menu()

    def tipo_jugadores(self):
        op = True
        while op:
            self.clear_screen()
            for i in self.p1.jugador:
                print("Jugador", i.get_id(), i.get_name(),"Tipo:", sep=" ", end="")
                if i.get_tipo():
                    print(" Usuario")
                else:
                    print(" Maquina")
            a = input("Ingrese el id del jugador que desea cambiar: ")
            try:
                b = int(a)
            except:
                print("Ha introducido un valor no valido. Intentelo de nuevo")
                sleep(2)
                continue
            if 0 <= b <= 4:
                op = False
            else:
                print("Opcion no valida, intentelo de nuevo")
                sleep(2)
                continue

        self.p1.jugador[b].set_tipo()
        self.clear_screen()
        for i in self.p1.jugador:
            print("Jugador", i.get_id(), i.get_name(), "Tipo:", sep=" ", end="")
            if i.get_tipo():
                print(" Usuario")
            else:
                print(" Maquina")

        print("Ha cambiado el tipo del jugador",b,"exitosamente")
        sleep(2)
        self.menu()

    def jugar(self):
        print("jugar")
        sleep(2)
        self.menu()







"""" faltantes para que el juego funcione:
    ver 0.85: 
        *menu del juego:
            + menu inicial del juego
            + se ingresan los nombres de los jugadores (menu adicional) 
            + se ingresan los tipos de jugadores (menu adicional)(maquina o usuario), ya que si es maquina
                no se mostrara el mensaje para tirar el dado.
            + se ingresa la opcion de jugar
            + para ambas se debe verificar que el usuario no ingrese basura al juego ( no meter letras donde
                deben ir numeros)
            
    
    ver 0.9:
        - se visualizara la pista una vez y se mostrara el mensaje de ingresar una tecla para tirar el 
            dado, y una vez tirado se muestra la animacion del carro hacia la posicion que el dado haya 
            sugerido
        - si lo anterior funciona bien, se debe correr el juego tantas veces como sea necesario hasta 
            que haya un ganador (se deben crear los metodos para verificar que haya un ganador y que no 
            ingrese esto errores en el juego
        - cuando todos los carros hayan terminado el juego, se debe mostrar el podio (primera a tercera 
            posicion)
    
    ver 1.0:
        -se guarda el podio en un archivo podio.txt
     
     ver 1.1 (extra):
        -se guarda el podio en una base de datos (no requerido, pero seria un buen plus si hay tiempo) 
     
    MANOS A LA OBRA!!!"""
