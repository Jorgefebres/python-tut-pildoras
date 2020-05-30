# def numero_par(num):
#     if num % 2 == 0:
#         print("ES PAR")
#     else:
#         print("NO ES PAR")

numeros = [7, 8, 9, 1, 2, 55, 54, 15, 15, 85]
print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))

print("_-------------------------------------_")


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de S/. {}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Director", 750000),
    Empleado("Jorge", "Presidente", 580000),
    Empleado("Alonso", "El papi", 10000),
    Empleado("Pedro", "El rajon", 150000),
    Empleado("Lobita", "El garca", 21000),
]

salarios_altos = filter(
    lambda empleado: empleado.salario > 50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
