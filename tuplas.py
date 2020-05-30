# Una tupla es una lista inmutable, son mas rapidas, ocupan menos espacio... etc.

# definicion
miTupla = ("Juan", 13, 1, 1995, "Juan")
print(miTupla)
print(miTupla[1])

# convertir tupla a una lista
miLista = list(miTupla)
print(miLista)

# convertir lista a tupla
miNuevaTupla = tuple(miLista)
print(miNuevaTupla)

# buscar un valor con IN
print("Juan" in miTupla)

# contar cuantos elementos hay en una tupla bajo un criterio determinado
print(miTupla.count("Juan"))

# averiguar longitud de una tupla
print(len(miTupla))

# crear tupla unitaria
miTuplaUnitaria = ("Juan",)
print(len(miTuplaUnitaria))

# crear una tupla sin paréntesis ó Empaquetado de una tupla
miTuplaSinParentesis = "Pedro", "Pablo", "Juan"
print(miTuplaSinParentesis)

# Desempaquetado de una tupla
miTuplaDesempaquetada = ("Pedro", 12, 1838)
nombre, mes, anio = miTuplaDesempaquetada
print(nombre)
print(mes)
print(anio)
