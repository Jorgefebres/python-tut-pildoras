# encapsulando atributos con __
class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if self.__enMarcha:
            return "EL COCHE ESTÁ EN MARCHA"
        else:
            return "EL COCHE ESTÁ PARADO"

    def estado(self):
        print("El coche tiene: ", self.__ruedas, " ruedas", " un ancho de: ",
              self.__anchoChasis, " y un largo de: ", self.__largoChasis)


miCoche = Coche()
print(miCoche.arrancar(False))
# aqui vemos que no puede modificar el atributo
miCoche.__ruedas = 5
miCoche.estado()
