from io import open

archivo_texto = open("archivo.txt", "r")
print(archivo_texto.read())
print("---------------------------------")
# el cursor se situa al final al momento de abrir el archivo por eso no vuelve a imprimir lo mismo
print(archivo_texto.read())
print("---------------------------------")
# para situar al puntero se utiliza la instruccion seek()
archivo_texto.seek(0)
print(archivo_texto.read())
print("---------------------------------")
# para situar al puntero se utiliza la instruccion seek()
archivo_texto.seek(11)
print(archivo_texto.read())
print("---------------------------------")
# seek() posiciona el puntero pero read lee hasta el caracter q se le pasa
archivo_texto.seek(0)
print(archivo_texto.read(11))

print("---------------------------------")
# leer desde la mitad del texto
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

print("---------------------------------")
# leer a partir de la 2da linea del texto
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
