# encapsulando metodo con __
class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def intentarArranque(self, arrancamos):
        self.__enMarcha = arrancamos
        if self.__enMarcha:
            chequeo = self.__chequeoInterno()
        if self.__enMarcha and chequeo:
            return "EL COCHE ESTÁ EN MARCHA"
        elif self.__enMarcha and chequeo == False:
            return "ALGO HA IDO MAL EN EL CHEQUEO, NO SE PUEDE ARRANCAR"
        else:
            return "EL COCHE ESTÁ PARADO"

    def estado(self):
        print("El coche tiene: ", self.__ruedas, " ruedas", " un ancho de: ",
              self.__anchoChasis, " y un largo de: ", self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()
print(miCoche.intentarArranque(True))
