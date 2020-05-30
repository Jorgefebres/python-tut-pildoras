from modulos import funciones_matematicas

# DOCUMENTACION - COMENTARIOS


class Areas():
    def area_cuadrado(lado):
        """ calcula el area de un cuadrado pasando el lado """
        return "El area del cuadrado es: " + str(lado*lado)

    def area_triangulo(base, altura):
        """ calcula el area de un triangulo pasando la base y multiplicando por la altura todo esto entre 2 """
        return "El area del triangulo es: " + str((base*altura)/2)


# __doc__ para imprimir la documentacion
print(Areas.area_cuadrado.__doc__)
# help para mostrar la documentacion
# help(Areas)
print(Areas.area_cuadrado(3))

print(Areas.area_triangulo(3, 5))

# comentarios para modulos
help(funciones_matematicas)
