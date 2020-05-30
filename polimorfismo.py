class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("me desplazo utilizando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")


# miVehiculo = Moto()
# miVehiculo.desplazamiento()

# miVehiculo2 = Coche()
# miVehiculo2.desplazamiento()

# miVehiculo3 = Camion()
# miVehiculo3.desplazamiento()


# POLIMORFISMO:
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)

miVehiculo = Coche()
desplazamientoVehiculo(miVehiculo)

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
