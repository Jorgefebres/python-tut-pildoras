from tkinter import *

root = Tk()
root.title = "Ejemplo"

playa = IntVar()
montania = IntVar()
turismo_rural = IntVar()


def opciones_viaje():
    opcion_escogida = ""
    if(playa.get() == 1):
        opcion_escogida += " Playa"
    if(montania.get() == 1):
        opcion_escogida += " Montaña"
    if(turismo_rural.get() == 1):
        opcion_escogida += " Turismo Rural"

    textoFinal.config(text=opcion_escogida)


# foto = PhotoImage(file="jeje.gif")
# label(root, image=foto).pack()
frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()


textoFinal = Label(frame)
textoFinal.pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1,
            offvalue=0, command=opciones_viaje).pack()
Checkbutton(root, text="Montaña", variable=montania, onvalue=1,
            offvalue=0, command=opciones_viaje).pack()
Checkbutton(root, text="Turismo Rural", variable=turismo_rural,
            onvalue=1, offvalue=0, command=opciones_viaje).pack()

root.mainloop()
