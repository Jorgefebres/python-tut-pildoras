# continue para saltar una ejecucion dentro del loop
for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)

print("----------------------------")
# para encontrar el numero de letras obviando los espacios en blanco
nombre = "Pildoras Informaticas"
print(len(nombre))

contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1
print(contador)
