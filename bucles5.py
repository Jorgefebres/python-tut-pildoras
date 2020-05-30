i = 1
while i <= 10:
    print(i)
    i += 1

print("------------------------")

edad = int(input("INTRODUZCA SU EDAD: "))
while edad < 0 or edad > 100:
    print("Ha introducido una edad negativa")
    edad = int(input("INTRODUZCA NUEVAMENTE SU EDAD: "))

print("SU EDAD ES: ", str(edad))
