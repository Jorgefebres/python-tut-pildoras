import re

# cadena = "Vamos a aprender de expresiones regulares en Python. Python es un lenguaje de aplicaciones sencillas"
# textoBuscar = "Python"
# if re.search(textoBuscar, cadena) is not None:
#     print("HE ENCONTRADO EL TEXTO")
# else:
#     print("NO HE ENCONTRADO EL TEXTO")

# print("-----------------------------------------")
# textoEncontrado = re.search(textoBuscar, cadena)
# print(textoEncontrado.start())
# print(textoEncontrado.end())
# print(textoEncontrado.span())
# print(re.findall(textoBuscar, cadena))
# print(len(re.findall(textoBuscar, cadena)))

# print("-----------------------------------------")
# lista_nombres = ['Hombres', 'Mujeres', 'Camion', 'Camión', 'Mascotas', 'niños', 'niñas', 'Ana Gómez', 'Maria Martin',
#                  'Sandra Lopez', 'Rogelio Núñez', 'Santiago Martin', 'Sandra Fernández', 'http://pildorasinformaticas.com', 'http://pildorasinformaticas.es', 'http://pildorasinformaticas.pe']

# # ^ PARA EMPEZAR
# for el in lista_nombres:
#     if re.findall('^Sandra', el):
#         print(el)
# print("-----------------------------------------")
# # $ PARA FINALIZAR
# for el in lista_nombres:
#     if re.findall('Martin$', el):
#         print(el)
# print("-----------------------------------------")
# # $ PARA FINALIZAR
# for el in lista_nombres:
#     if re.findall('.pe$', el):
#         print(el)
# # [] SI SE ENCUENTRAN DICHOS CARACTERES SIN ORDEN ALGUNO
# print("-----------------------------------------")
# for el in lista_nombres:
#     if re.findall('[ñ]', el):
#         print(el)

# print("-----------------------------------------")
# for el in lista_nombres:
#     if re.findall('niñ[oa]s', el):
#         print(el)
# print("-----------------------------------------")
# for el in lista_nombres:
#     if re.findall('Cami[oó]n', el):
#         print(el)

# print("-----------------------------------------")
# # RANGO
# for el in lista_nombres:
#     if re.findall('[c-f]', el):
#         print(el)
# print("-----------------------------------------")
# # TERMINAN CON RANGO
# for el in lista_nombres:
#     if re.findall('[c-f]$', el):
#         print(el)

# print("-----------------------------------------")
# # RANGO NEGADO
# for el in lista_nombres:
#     if re.findall('[^e-f]$', el):
#         print(el)

nombre1 = 'Jara López'
nombre2 = 'Antonio López'
nombre3 = 'Lara Gómez'

# match busca al inicio y search al medio y final

# IGNORECASE para evitar q reconozca mayusculas o minusculas
# . para obviar un caracter al inicio
if re.match('.ara', nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")


if re.search('lópez', nombre2, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")
