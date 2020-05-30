from tkinter import *

root = Tk()
varOpcion = IntVar()


def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text="Has Elegido Masculino")
    else:
        etiqueta.config(text="Has Elegido Femenino")
    print(varOpcion.get())


Label(root, text="Género").pack()
Radiobutton(root, text="Masculino", variable=varOpcion,
            value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion,
            value=2, command=imprimir).pack()


etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
