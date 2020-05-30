class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self):
        self.enMarcha = True

    def parar(self):
        self.enMarcha = False

    def estado(self):
        if self.enMarcha:
            print("EL COCHE ESTÁ EN MARCHA")
        else:
            print("EL COCHE ESTÁ PARADO")


miCoche = Coche()
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, " ruedas")
print("El coche esta en marcha?: ", miCoche.enMarcha)
miCoche.arrancar()
miCoche.estado()
