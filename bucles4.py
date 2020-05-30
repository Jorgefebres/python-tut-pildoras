valido = False
email = input("INTRODUZCA SU EMAIL: "),

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("EMAIL ES CORRECTO")
else:
    print("EMAIL NO ES CORRECTO")
