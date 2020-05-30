def divide():
    try:
        op1 = float(input("INGRESE EL PRIMER VALOR: "))
        op2 = float(input("INGRESE EL SEGUNDO VALOR: "))
        print("LA DIVISION ES: " + str(op1/op2))
    except ValueError:
        print("EL VALOR INGRESADO ES ERRONEO")
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR ENTRE 0")
    finally:
        print("CALCULO FINALIZADO")


divide()
