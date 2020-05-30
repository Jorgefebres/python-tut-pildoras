# DECORADOR
def funcion_decoradora(funcion_parametro):
    # *args dice q la funcion puede recibir un numero indeterminado de parámetros
    # **kwargs argumentos con clave valor
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales del decorador
        print("Vamos a realizar un cálculo")
        funcion_parametro(*args, **kwargs)
        # Acciones adicionales del decorador
        print("Hemos terminado un cálculo")
        print("-------------------------------")
    return funcion_interior
# # FUNCIONES COMUNES


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2 + num3)


@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)


@funcion_decoradora
def potencia(base, exponente):
    print(base**exponente)


suma(7, 8, 18)
resta(12, 10)
potencia(base=5, exponente=10)
