import sqlite3

miConexion = sqlite3.connect("PrimeraDB")

# creamos el cursor o puntero
miCursor = miConexion.cursor()

# crear table
# miCursor.execute(
#     "CREATE TABLE PRODUCTOS( NOMBRE_ARTICULO VARCHAR(30), PRECIO INTEGER, SECCION VARCHAR(20))")

# Insertar registro
# miCursor.execute(
#     "INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")

# insertar registros por lote
# variosProductos = [
#     ("Camiseta", 10, "deportes"),
#     ("Jarrón", 90, "cerámica"),
#     ("Camión", 20, "Juguetería")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", variosProductos)

# seleccionar la data
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductosLectura = miCursor.fetchall()
# print(variosProductosLectura)
for producto in variosProductosLectura:
    # print(producto)
    print("Nombre Artículo: ",
          producto[0], " precio: ", producto[1], " seccion: ", producto[2])

miConexion.commit()
miConexion.close()
