from io import open

archivo_texto = open("archivo.txt", "r+")  # lectura y escritura
# archivo_texto.write("Comienzo del Texto")
# print(archivo_texto.readlines())
# print("---------------------------------")

# modificando la 2da linea mediante una lista
lista_texto = archivo_texto.readlines()
lista_texto[1] = " Esta Linea ha sido incluida desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
