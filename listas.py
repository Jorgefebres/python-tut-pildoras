miLista = ["Maria", "Pepe", "Martha", "Antonio"]

print("primer elemento: ", miLista[1])
print("ultimo elemento: ", miLista[-1])

print("3 primeros elementos: ", miLista[0:3])
print("hasta el 3er elementos: ", miLista[:3])

print("2 elementos: ", miLista[1:3])

print("desde el 2do elemento: ", miLista[2:])

# agregar elemento al final:
miLista.append("Sandra")
print(miLista)

# agreagar elemento al inicio:
miLista.insert(0, "Paco")
print(miLista)

# concatenar elementos a una lista
miLista.extend(["Pablo", "Ana", "Lucia"])
print(miLista)

# obtiene el primer elemento encontrado en la lista que coincide con el criterio
print(miLista.index("Pablo"))

# imprime true si se encuentra, false si no
print("Pepe" in miLista)

# una lista con diferentes tipos de dato
miNuevaLista = ["Porfirio", 5, True, 78.85]
print(miNuevaLista)

# borrar un elemento de una lista
miNuevaLista.remove("Porfirio")
print(miNuevaLista)

# borrar el ultimo elemento de una lista
miNuevaLista.pop()
print(miNuevaLista)

# sumar listas
miLista3 = miLista + miNuevaLista
print(miLista3)

# repetir una lista 3 veces
print(miNuevaLista*3)
