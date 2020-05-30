import doctest


def areaTriangulo(base, altura):
    '''
    calcula el area de un triangulo dado
    >>> areaTriangulo(3,6)
    'El area del triangulo es: 9.0'
    >>> areaTriangulo(2,3)
    'El area del triangulo es: 3.0'
    >>> areaTriangulo(4,8)
    'El area del triangulo es: 16.0'
    '''
    return 'El area del triangulo es: ' + str((base * altura)/2)


def compruebaMail(mailUsuario):
    '''
    la funcion compruebaMail evalua un mail recibido en busca de la @ si tiene una @ es correcto, si tiene mas es incorrecto, si la @ está al final es incorrecto

    >>> compruebaMail('juan@cursos.es')
    True
    >>> compruebaMail('juancursos.es@')
    False
    >>> compruebaMail('juancursos.es')
    False
    >>> compruebaMail('juan@cursos@ejem.es')
    False
    '''
    arroba = mailUsuario.count('@')
    if(arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario) - 1) or mailUsuario.find('@') == 0):
        return False
    else:
        return True


doctest.testmod()
# print(areaTriangulo(2, 4))
