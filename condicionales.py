print("PROGRAMA DE EVALUACION DE NOTAS DEL ALUMNO")

# para utilizar el teclado
nota_alumno = input("INGRESE LA NOTA DEL ALUMNO: ")


def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "desaprobado"
    return valoracion

# print(evaluacion(6))
# print(evaluacion(4))


print("EL ALUMNO ESTÁ: ", evaluacion(int(nota_alumno)))
