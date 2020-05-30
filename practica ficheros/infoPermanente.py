import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("SE HA CREADO UNA PERSONA CON EL NOMBRE: ", self.nombre)

    # convierte en texto la informacion del objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        # ab+ para agregar informacion binaria
        ListaPersonas = open("archivoExterno", "ab+")
        # desplazar el cursor al inicio para insertarlas ahi
        ListaPersonas.seek(0)

        try:
            self.personas = pickle.load(ListaPersonas)
            print("Se cargaron {} personas del fichero externo".format(
                len(self.personas)))
        except:
            print("El fichero está vacio")
        finally:
            ListaPersonas.close()
            del(ListaPersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.__guardarPersonasEnFichero()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def __guardarPersonasEnFichero(self):
        ListaPersonas = open("archivoExterno", "wb")
        pickle.dump(self.personas, ListaPersonas)
        del(ListaPersonas)

    def mostrarPersonasEnFichero(self):
        print("la informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()
p = Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(p)
p = Persona("Antonio", "Masculino", 20)
miLista.agregarPersonas(p)
p = Persona("Ana", "Femenino", 9)
miLista.agregarPersonas(p)

miLista.mostrarPersonasEnFichero()
