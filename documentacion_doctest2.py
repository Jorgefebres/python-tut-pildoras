import doctest
import math

# se utiliza ... para anidar una funcion es decir identar dentro de un bucle for x ejem


def raizCuadrada(listaNumeros):
    '''
    la funcion devuelve una lista con la raiz cuadrada calculada de cada elemento pasado por parametro
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,-9,16,50,-920]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    '''
    return [math.sqrt(n) for n in listaNumeros]


# print(raizCuadrada([9, 16, 25, 36]))


doctest.testmod()
