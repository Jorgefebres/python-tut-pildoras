print("Asignaturas optativas año 2017")
print("Asignaturas optativas: Informática grafica - Pruebas de software - Usabilidad y Accesibilidad")

asignatura = input("Escribe la asignatura escogida: ")

if asignatura.lower() in ("informática grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida está contemplada: ", asignatura)
else:
    print("Asignatura elegida no está contemplada: ", asignatura)
