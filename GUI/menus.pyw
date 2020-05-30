from tkinter import *
from tkinter import messagebox

root = Tk()

# para la ventana emergente


def info_adicional():
    messagebox.showinfo("Procesador de Jorge",
                        "Procesador de textos version 2020")


def estado_licencia():
    messagebox.showwarning("Licencia vencida", "Por favor renueva tu licencia")


def verficar_salir():
    valor = messagebox.askquestion(
        "Salir", "Realmente desea salir de la aplicación?")
    print("OPCION ESCOGIDA: ", valor)
    if valor == "yes":
        root.destroy()


def verficar_cerrar():
    valor = messagebox.askretrycancel(
        "Cerrar", "No es posible cerrar el documento")
    if valor == False:
        root.destroy()


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=verficar_cerrar)
archivoMenu.add_command(label="Salir", command=verficar_salir)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=estado_licencia)
archivoAyuda.add_command(label="Acerca de ...", command=info_adicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
