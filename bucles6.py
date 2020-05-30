import math
print("PROGRAMA DE CALCULO DE RAIZ CUADRADA")

numero = int(input("INTRODUCE UN NUMERO POR FAVOR: "))

intentos = 0

while numero < 0:
    print("NO SE PUEDE HALLAR LA RAIZ DE UN NUMERO NEGATIVO")
    if intentos == 2:
        print("DEMASIADOS INTENTOS... FINALIZANDO EL PROGRAMA")
        break
    numero = int(input("INTRODUCE UN NUMERO POR FAVOR: "))
    if numero < 0:
        intentos += 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("LA RAIZ CUADRADA DE: " + str(numero) + " ES: " + str(solucion))
