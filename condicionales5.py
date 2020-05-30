salario_presidente = int(input("INTRODUCE SALARIO PRESIDENTE: "))
print("SALARIO DEL PRESIDENTE: ", salario_presidente)

salario_director = int(input("INTRODUCE SALARIO DIRECTOR: "))
print("SALARIO DEL DIRECTOR: ", salario_director)

salario_lider_proyecto = int(input("INTRODUCE SALARIO LIDER DE PROYECTO: "))
print("SALARIO DEL LIDER DE PROYECTO: ", salario_lider_proyecto)

salario_administrativo = int(input("INTRODUCE SALARIO ADMINISTRATIVO: "))
print("SALARIO DEL ADMINISTRATIVO: ", salario_administrativo)


if salario_administrativo < salario_lider_proyecto < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")
