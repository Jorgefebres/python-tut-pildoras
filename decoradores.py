# DECORADOR
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # Acciones adicionales del decorador
        print("Vamos a realizar un cálculo")
        funcion_parametro()
        # Acciones adicionales del decorador
        print("Hemos terminado un cálculo")
        print("-------------------------------")
    return funcion_interior
# # FUNCIONES COMUNES


@funcion_decoradora
def suma():
    print(15+20)


@funcion_decoradora
def resta():
    print(20-15)


suma()
resta()
