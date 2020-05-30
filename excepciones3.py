def evaluaEdad(edad):
    if edad <= 0:
        raise ValueError("No se permiten edades negativas")
    elif edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Aun eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Eres abuelito"


print(evaluaEdad(0))
