
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de S/. {}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Director", 7500),
    Empleado("Jorge", "Presidente", 5000),
    Empleado("Alonso", "El papi", 1000),
    Empleado("Pedro", "El rajon", 2200),
    Empleado("Lobita", "El garca", 5222),
]


def calculo_comision(empleado):
    if empleado.salario < 3000:
        empleado.salario = empleado.salario * 1.03
    return empleado


listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)
