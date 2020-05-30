# HERENCIA
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enMarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)


# asi se hereda en python
class Moto(Vehiculo):
    pass


miMoto = Moto("Harley Davidson", "Iron 880")
miMoto.estado()
