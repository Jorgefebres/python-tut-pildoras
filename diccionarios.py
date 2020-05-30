miDiccionario = {"Alemania": "Berlin", "Francia": "Paris",
                 "España": "Madrid", "Reino Unido": "Londres"}

print(miDiccionario)
print(miDiccionario["Francia"])
print(miDiccionario["España"])

# Agregar elemento al diccionario
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

# Modificar un elemento
print(miDiccionario)
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# Eliminar un elemento
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)

# Diccionario con varios tipos de datos
miDiccionario2 = {"Alemania": "Berlin", 23: "Jordan", "Mosqueteros": 3}
print(miDiccionario2)


miTupla = ("España", "Francia", "Reino Unido", "Alemania")
miDiccionario3 = {miTupla[0]: "Madrid", miTupla[1]                  : "Paris", miTupla[2]: "Londres", miTupla[3]: "Berlin"}
print(miDiccionario3)


miDiccionario4 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "Anillos": {"Temporadas": [1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario4)
print(miDiccionario4["Anillos"])
print(miDiccionario4["Anillos"]["Temporadas"])

# Devolver claves de un diccionario
print(miDiccionario4.keys())

# Devolver values de un diccionario
print(miDiccionario4.values())


# Devolver longitud de un diccionario
print(len(miDiccionario4))
