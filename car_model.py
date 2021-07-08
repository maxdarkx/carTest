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

    def espacio_print (self, espacio):
        for i in range(espacio):
            print(" ", end="")

    def med_print(self):
        print(self.carMed, end=None)

    def sup_print(self):
        print(self.carSup, end=None)

    def inf_print(self):
        print(self.carInf, end=None)

    def car_print(self, esp):
        self.espacio_print(esp)
        self.sup_print()
        self.espacio_print(esp)
        self.med_print()
        self.espacio_print(esp)
        self.inf_print()
