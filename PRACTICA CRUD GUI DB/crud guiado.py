from tkinter import *
from tkinter import messagebox
import sqlite3

# --------------------------FUNCIONES-----------------------------

# --------------------------DB-----------------------------


def conexionDB():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
        CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR (50),
            APELLIDO_USUARIO VARCHAR (50),
            PASSWORD VARCHAR (50),
            DIRECCION_USUARIO VARCHAR (50),
            COMENTARIO VARCHAR (100)
        )
        ''')
        messagebox.showinfo("DB", "BASE DE DATOS CREADA EXITOSAMENTE!")
    except:
        messagebox.showwarning("ATENCION!", "LA BASE DE DATOS YA EXISTE!")
    miConexion.close()

# --------------------------SALIR-----------------------------


def salirAplicacion():
    valor = messagebox.askquestion("Salir", "Desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()

# --------------------------LIMPIAR ENTRIES-----------------------------


def limpiarEntries():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    # limpiar el area de texto desde el inicio 1.0 hasta el final (END)
    comentarioTexto.delete(1.0, END)


# --------------------------CRUD-----------------------------
# --------------------------CREAR-----------------------------

def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    # miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES (NULL, '" + miNombre.get() + "', '" + miApellido.get() +
    #                  "', '"+miPass.get()+"','"+miDireccion.get()+"','"+comentarioTexto.get("1.0", END)+"')")
    datos = miNombre.get(), miApellido.get(), miPass.get(
    ), miDireccion.get(), comentarioTexto.get(1.0, END)
    miCursor.execute(
        "INSERT INTO DATOS_USUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", (datos))

    miConexion.commit()
    messagebox.showinfo("DB", "REGISTRO INSERTADO CON EXITO")
    miConexion.close()

# --------------------------LEER-----------------------------


def leer():

    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID = " + miId.get())

    usuarioRecibido = miCursor.fetchall()
    for usuario in usuarioRecibido:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        comentarioTexto.insert(1.0, usuario[5])

    miCursor.commit()
    miCursor.close()

# --------------------------ACTUALIZAR-----------------------------


def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos = miNombre.get(), miApellido.get(), miPass.get(
    ), miDireccion.get(), comentarioTexto.get(1.0, END)
    miCursor.execute(
        "UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = ?, APELLIDO_USUARIO = ? PASSWORD = ? , DIRECCION_USUARIO = ?, COMENTARIO = ? WHERE ID = " + miId.get(), (datos))

    miConexion.commit()
    messagebox.showinfo("DB", "REGISTRO ACTUALIZADO CON EXITO")
    miConexion.close()

# --------------------------ELIMINAR-----------------------------


def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID = " + miId.get())

    miConexion.commit()
    messagebox.showinfo("DB", "REGISTRO ELIMINADO CON EXITO")
    miConexion.close()


root = Tk()


# --------------------------MENU-----------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
dbMenu = Menu(barraMenu, tearoff=0)
dbMenu.add_command(label="Conectar", command=conexionDB)
dbMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarEntries)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...")
ayudaMenu.add_command(label="licencia")

barraMenu.add_cascade(label="DB", menu=dbMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)

miFrame = Frame(root)
miFrame.pack()

# --------------------------LABELS-----------------------------

idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="NOMBRE:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="APELLIDO:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="PASSWORD:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="DIRECCION:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="COMENTARIO:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


# --------------------------ENTRIES-----------------------------

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

idEntry = Entry(miFrame, textvariable=miId)
idEntry.grid(row=0, column=1, padx=10, pady=10)

nombreEntry = Entry(miFrame, textvariable=miNombre)
nombreEntry.grid(row=1, column=1, padx=10, pady=10)
nombreEntry.config(foreground="#146984", justify="right")

apellidoEntry = Entry(miFrame, textvariable=miApellido)
apellidoEntry.grid(row=2, column=1, padx=10, pady=10)

passEntry = Entry(miFrame, textvariable=miPass)
passEntry.grid(row=3, column=1, padx=10, pady=10)
passEntry.config(show="*")

direccionEntry = Entry(miFrame, textvariable=miDireccion)
direccionEntry.grid(row=4, column=1, padx=10, pady=10)

comentarioTexto = Text(miFrame, width=16, height=5)
comentarioTexto.grid(row=5, column=1, padx=10, pady=10)
scrollbarvert = Scrollbar(miFrame, command=comentarioTexto.yview)
scrollbarvert.grid(row=5, column=2, sticky="nsew")
comentarioTexto.config(yscrollcommand=scrollbarvert.set)


# --------------------------BUTTONS-----------------------------

miFrame2 = Frame(root)
miFrame2.pack()

crearButton = Button(miFrame2, text="Crear", command=crear)
crearButton.grid(row=0, column=0, sticky='e', padx=10, pady=10)

leerButton = Button(miFrame2, text="Leer", command=leer)
leerButton.grid(row=0, column=1, sticky='e', padx=10, pady=10)

actualizarButton = Button(miFrame2, text="Actualizar", command=actualizar)
actualizarButton.grid(row=0, column=2, sticky='e', padx=10, pady=10)

eliminarButton = Button(miFrame2, text="Eliminar", command=eliminar)
eliminarButton.grid(row=0, column=3, sticky='e', padx=10, pady=10)


root.mainloop()
