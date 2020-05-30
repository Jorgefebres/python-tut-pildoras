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
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    # Sobreescribiendo el metodo estado
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enMarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nHCaballito: ", self.hcaballito)


miMoto = Moto("Harley Davidson", "Iron 883")
miMoto.caballito()
miMoto.estado()

print("---------------------------")


class Furgoneta(Vehiculo):
    # cargado = False
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return("La furgoneta está cargada")
        else:
            return("La furgoneta no está cargada")


miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


print("---------------------------")


class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Herencia Multiple


class BicicletaElectrica(VElectricos, Vehiculo):
    pass


# el constructor con preferencia es el que se pone primero es decir Vehiculo igual sucede con los metodos
miBici = BicicletaElectrica("Goliat", "HCT1030")
