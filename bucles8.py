# instruccion pass para devolver un nulo
while True:
    pass  # Para implementar mas tarde
# else de for para ejecutar cuando el bucle se complete
email = input("INTRODUZCA SU EMAIL: ")
for i in email:
    if i == "@":
        arroba = True
        break  # salta tambien el else
else:
    arroba = False
print(arroba)
