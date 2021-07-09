class car_model:
    # caracteres utiles para la construccion del carro
    triRell =           "\u25E3"
    tri =               "\u25FA"
    cir =               "\u25EF"
    medCir =            "\u25E1"
    rayaHoz =           "\u2500"
    rayaHozGruesa =     "\u2501"
    rayaVer =           "\u2502"
    rayaVerGruesa =     "\u2503"
    medRayaHoz =        "\u257A"
    anguloSupDer =      "\u250C"
    anguloInfDer =      "\u2514"
    anguloInfIzq =      "\u2518"
    rayaDiagonalIzq =   "\u2572"
    angulo1 =           "\u256E"
    angulo2 =           "\u2570"

    # seccion superior, media e inferior del carro
    carSup = anguloSupDer + rayaHoz + rayaHoz + rayaHoz + rayaHoz + angulo1
    carMed = rayaVer + "    " + angulo2 + triRell
    carInf = anguloInfDer + medCir + rayaHozGruesa + rayaHozGruesa + medCir + rayaHozGruesa + anguloInfIzq

    # Inicializacion del carro: posicion del carro en el eje x
    def __init__(self):
        self.posicion = 0
        self.size = 7

    # para cambiar la posicion del carro
    def set_pos(self, pos):
        self.posicion = pos

    def get_pos(self):
        return self.posicion

    def get_size(self):
        return self.size

    #impresion de espacios y retornos de carro, solo para pruebas
    def espacio_print (self):
        for i in range(self.posicion):
            print(" ", end="")

    def siguiente_seccion(self):
        print()


    #impresiones de las partes superior, media e inferior del carro. las imprime la pista o el propio carro para pruebas
    def med_print(self):
        print(self.carMed, end="")

    def sup_print(self):
        print(self.carSup, end="")

    def inf_print(self):
        print(self.carInf, end="")

    # metodo para imprimir el carro y una pista basica sin adornos. Solo para pruebas
    # imprime el carro en la posicion guardada en self.posicion
    def car_print(self):

        self.espacio_print()
        self.sup_print()
        self.siguiente_seccion()

        self.espacio_print()
        self.med_print()
        self.siguiente_seccion()

        self.espacio_print()
        self.inf_print()
        self.siguiente_seccion()
