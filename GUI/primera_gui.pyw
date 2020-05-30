from tkinter import *

root = Tk()

miNombre = StringVar()

# root.iconbitmap("logo.ico")
root.title("Ventana de pruebas")
root.resizable(False, False)
root.geometry("650x650")
root.config(bg="#146986")

# haciendo un frame
miFrame = Frame(root)
miFrame.pack()
miFrame.config(bg="#dbdbda")
miFrame.config(width="300", height="300")
miFrame.config(bd="10")
# miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
# miLabel = Label(miFrame, text="Nombre:",
#                 fg="#146986", font=("Comic Sans MS", 11))
# miLabel.place(x=10, y=100)
# # miImagen = PhotoImagefile="jeje.gif")
# miEntry = Entry(miFrame,
#                 fg="#146986", font=("Comic Sans MS", 11))
# miEntry.place(x=80, y=100)


miLabelNombre = Label(miFrame, text="Nombre:",
                      fg="#146986", bg="#dbdbda", font=("Comic Sans MS", 11))
miLabelNombre.grid(row=0, column=0, sticky="e", pady=10)
miEntryNombre = Entry(miFrame, textvariable=miNombre,
                      fg="#146986", bg="#fff", justify="center", font=("Comic Sans MS", 11))
miEntryNombre.grid(row=0, column=1, pady=10)

miLabelApellido = Label(miFrame, text="Apellido:",
                        fg="#146986", bg="#dbdbda", font=("Comic Sans MS", 11))
miLabelApellido.grid(row=1, column=0, sticky="e", pady=10)
miEntryApellido = Entry(miFrame,
                        fg="#146986", bg="#fff", justify="center", font=("Comic Sans MS", 11))
miEntryApellido.grid(row=1, column=1, pady=10)

miLabelDireccion = Label(miFrame, text="Direccion:",
                         fg="#146986", bg="#dbdbda", font=("Comic Sans MS", 11))
miLabelDireccion.grid(row=2, column=0, sticky="e", pady=10)
miEntryDireccion = Entry(miFrame,
                         fg="#146986", bg="#fff", justify="center", font=("Comic Sans MS", 11))
miEntryDireccion.grid(row=2, column=1, pady=10)

miLabelPassword = Label(miFrame, text="Password:",
                        fg="#146986", bg="#dbdbda", font=("Comic Sans MS", 11))
miLabelPassword.grid(row=3, column=0, sticky="e", pady=10)
miEntryPassword = Entry(miFrame,
                        fg="#146986", bg="#fff", justify="center", show="*", font=("Comic Sans MS", 11))
miEntryPassword.grid(row=3, column=1, pady=10)

miLabelComentarios = Label(miFrame, text="Comentarios:",
                           fg="#146986", bg="#dbdbda", font=("Comic Sans MS", 11))
miLabelComentarios.grid(row=4, column=0, sticky="e", pady=10)

textoComentario = Text(miFrame, width="22", height="5")
textoComentario.grid(row=4, column=1, pady=10)
scrollv = Scrollbar(miFrame, command=textoComentario.yview)
scrollv.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollv.set)


def codigoBoton():
    miNombre.set("Jorge")


botonEnvio = Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()
