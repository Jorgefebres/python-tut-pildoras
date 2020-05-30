print("PROGRAMA PARA OBTENER BECAS DEL GOBIERNO")

distancia_escuela = int(input("INTRODUCE LA DISTANCIA A TU ESCUELA EN KM: "))
numero_hermanos = int(input("INTRODUCE EL NUMERO DE HERMANOS QUE TIENES: "))
salario_familiar = int(input("INTRODUCE EL SALARIO ANUAL BRUTO: "))

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 2000:
    print("TIENES DERECHO A BECA")
else:
    print("NO TIENES DERECHO A BECA")
