class Persona():
    def __init__(self, nombre, edad, lugar_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.lugar_nacimiento = lugar_nacimiento

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad,
              " Lugar de Nacimiento: ", self.lugar_nacimiento)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugar_nacimiento_empleado):
        # la instruccion super llama al metodo init de la clase padre
        super().__init__(nombre_empleado, edad_empleado, lugar_nacimiento_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    # sobreescribiendo el metodo
    def descripcion(self):
        # la instruccion super llama al metodo descripcion de la clase padre
        super().descripcion()
        print("Salario: ", self.salario, " Antiguedad: ", self.antiguedad)


antonio = Empleado(1500, 15, "Antonio", 35, "Colombia")
antonio.descripcion()


manuel = Empleado(500, 2, "Manuel", 55, "Venezuela")
manuel.descripcion()
# isinstance se usa para comprobar que una instancia pertenece a una clase
print(isinstance(manuel, Empleado))


paco = Persona("Paco", 35, "Peru")
paco.descripcion()
# isinstance se usa para comprobar que una instancia pertenece a una clase
print(isinstance(paco, Persona))
