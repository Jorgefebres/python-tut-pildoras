# biblioteca pickle para crear archivos binarios
import pickle

# leer binario es rb
archivo_binario = open("lista_nombres", "rb")
lista_nombres = pickle.load(archivo_binario)
print(lista_nombres)
archivo_binario.close()
# para borrar o limpiar de la memoria se utiliza del()
del(archivo_binario)
