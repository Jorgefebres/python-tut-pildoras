import pickle


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


coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seat", "Leon")
coche3 = Vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3]
# guardando info
archivo_coches = open("losCoches", "wb")
pickle.dump(coches, archivo_coches)
archivo_coches.close()
del(archivo_coches)


# recuperando info
archivo_leer_coches = open("losCoches", "rb")
misCoches = pickle.load(archivo_leer_coches)
archivo_leer_coches.close()

for coche in misCoches:
    print(coche.estado())
