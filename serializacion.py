# biblioteca pickle para crear archivos binarios
import pickle

lista_nombres = ["Pedro", "Ana", "María", "Jorge"]
# escritura binaria es wb
archivo_binario = open("lista_nombres", "wb")
pickle.dump(lista_nombres, archivo_binario)
archivo_binario.close()
# para borrar o limpiar de la memoria se utiliza del()
del(archivo_binario)
