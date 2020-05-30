nombreUsuario = input("INTRODUCE NOMBRE DE USUARIO: ")

print("EL NOMBRE DE USUARIO EN MAYUSCULAS ES: ", nombreUsuario.upper())

print("EL NOMBRE DE USUARIO EN MINUSCULAS ES: ", nombreUsuario.lower())

print("EL NOMBRE DE USUARIO CAPITALIZADO ES: ", nombreUsuario.capitalize())


edad = input("POR FAVOR INTRODUCE LA EDAD: ")
while edad.isdigit() == False:
    edad = input("POR FAVOR INTRODUCE UN VALOR NUMERICO ")
if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")
