print("VERIFICAR NOTAS DEL ALUMNO")

nota_alumno = int(input("POR FAVOR INGRESE SU NOTA: "))


def calcularNota(nota):
    if nota < 5:
        print("INSUFICIENTE")
    elif nota < 7:
        print("MASO")
    elif nota < 9:
        print("BIEN")
    else:
        print("EXCELENTE")


calcularNota(nota_alumno)
