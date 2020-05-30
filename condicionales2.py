print("VERIFICAR SI PUEDE O NO PUEDE PASAR")

edad_usuario = int(input("POR FAVOR INGRESE SU EDAD: "))


def calcularEdad(edad):
    if edad > 18 and edad < 100:
        print("USTED PUEDE PASAR, ADELANTE")
    elif edad > 100:
        print("EDAD INCORRECTA")
    else:
        print("USTED NO PUEDE PASAR, SÁQUESE")


calcularEdad(edad_usuario)
