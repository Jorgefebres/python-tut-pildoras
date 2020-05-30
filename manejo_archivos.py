from io import open

# se puede abrir el archivo en modo lectura, escritura y append
# abrir en modo escritura "w"
archivo_texto = open("archivo.txt", "w")
frase = "Que estupenda noche para estudiar python\njejeje...."
archivo_texto.write(frase)
archivo_texto.close()

print("----------------------------------")
# abrir en modo lectura "r"
archivo_texto = open("archivo.txt", "r")
texto = archivo_texto.read()
archivo_texto.close()
print(texto)


print("----------------------------------")
# leer solo algunas lineas
archivo_texto = open("archivo.txt", "r")
lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print("LINEA 0: ", lineas_texto[0])


print("----------------------------------")
# abrir en modo append "a"
archivo_texto = open("archivo.txt", "a")
archivo_texto.write("\nSiempre es una buena ocasion para estudiar python")
archivo_texto.close()
