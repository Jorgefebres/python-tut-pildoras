from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
        ("Ficheros de Excel", "*.xls"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*")))
    print("fichero: ", fichero)


Button(root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()
