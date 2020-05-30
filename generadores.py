# funcion comun y corriente
def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num += 1
    return miLista

# print(generaPares(10))

# con generador


def generaPares2(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1


# devuelvePares = generaPares2(10)
# for i in devuelvePares:
#     print(i)
devuelvePares = generaPares2(10)
print(next(devuelvePares))
print("Aqui podría haber mas codigo")
print(next(devuelvePares))
print("Aqui podría haber mas codigo")
print(next(devuelvePares))
