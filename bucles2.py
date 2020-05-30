# imprimir en la misma linea
for i in ["pildoras", "informaticas", "alumnos"]:
    print("HOLA", end=" ")
print()

# Verificar si una cadena contiene un arroba '@'
email = False
miEmail = input("INTRODUZCA SU DIRECCION DE EMAIL: ")
for i in miEmail:
    if i == "@" or i == ".":
        email = True

if email:
    print("EL EMAIL ES CORRECTO")
else:
    print("EL EMAIL NO ES CORRECTO")
