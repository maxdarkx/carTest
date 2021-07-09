from pista_model import pista_model
from os import system
from time import sleep

# Desde esta clase se controla el juego en su totalidad
class juego:
    def __init__(self):
        self.p1 = pista_model()
        self.pista_podio = 1

    # funcion para imprimir el menu principal, incluye correccion de errores anti usuario
    def menu(self):
        op = True
        while op:
            self.clear_screen()
            print("\t DRAG RACE\n")
            print("1. Seleccione los nombres de los jugadores")
            print("2. Selecciones los tipos de jugadores")
            print("3. jugar")
            a = input("Ingrese su opcion: ")

            #correccion de errores: el usuario debe ingresar un entero entre 1 y 3
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

    # funcion para borrar la pantalla
    @staticmethod
    def clear_screen():
        system('clear')

    # menu para cambiar los nombres de los jugadores, contiene correccion de errores
    def nombres_jugadores(self):
        op = True
        while op:
            self.clear_screen()
            for i in self.p1.jugador:
                print("Jugador", i.get_id(), ":", i.get_name(), sep=" ")
            a = input("Ingrese el id del jugador que desea cambiar: ")

            #correccion de errores: el usuario debe ingresar un numero entre 0 y 4 (id jugador)
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

    #menu para cambiar el tipo (maquina, jugador) a los jugadores
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

            #correccion de errores: el usuario debe ingresar un numero entre 0 y 4 (id jugador)
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

        print("Ha cambiado el tipo del jugador", b, "exitosamente")
        sleep(2)
        self.menu()

    # rutina principal del juego: si el jugador no ha llegado a la meta, tira el dado
    # y su vehiculo se mueve dado * 10 en su carril. Se verifica si el jugador llego
    # a la meta y se finaliza el juego cuando todos llegan a la meta
    # distancia carril = (150) == 1500 metros

    def jugar(self):
        clasificacion = []
        self.clear_screen()
        print("Pista Inicial")
        self.p1.print_pista()
        sleep(2)

        fin_juego = False
        while not fin_juego:
            self.clear_screen()
            for i in self.p1.jugador:
                if not i.termino:
                    dd = i.dado()
                    dat = int(dd)
                    self.clear_screen()
                    print("mover carril", i.get_id(), i.get_name(),"posicion: ", i.carril.cond.carro.get_pos(),"dados:", dat)
                    sleep(2)
                    self.clear_screen()
                    self.p1.mover_carril(i.get_id(), dat*10)
                    self.ganar()
                    fin_juego = self.finaliza_juego()
                    sleep(2)

        for i in range(1,4):
            for j in self.p1.jugador:
                if j.podio == i:
                    clasificacion.append("("+str(j.podio) + ") " + str(j.get_id())+". "+j.get_name())
        print(clasificacion)

    def ganar(self):
        for i in self.p1.jugador:
            if i.carril.cond.carro.get_pos() >= i.carril.size and not i.termino:
                i.ganador_podio(self.pista_podio)
                i.finaliza_juego()
                self.pista_podio += 1
                print(i.podio, " ganador:",i.get_id(), i.get_name())

    def finaliza_juego(self):
        k = 0
        for i in self.p1.jugador:
            if i.termino:
                k += 1
        print("acabaron", k)
        if k >= 5:
            return True
        else:
            return False








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
