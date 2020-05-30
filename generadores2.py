# * dice que va a recibir un numero indeterminado de elementos en forma de tupla
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento


ciudadesDevueltas = devuelveCiudades("Paris", "Madrid", "Berlin", "Lisboa")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

print("-------------------------------------")
# devolver subelementos


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento


ciudadesDevueltas = devuelveCiudades("Paris", "Madrid", "Berlin", "Lisboa")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

print("-------------------------------------")
# hacer lo mismo con yield from


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
        yield from elemento


ciudadesDevueltas = devuelveCiudades("Paris", "Madrid", "Berlin", "Lisboa")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
