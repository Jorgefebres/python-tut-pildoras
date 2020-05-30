import sqlite3

miConexion = sqlite3.connect("CuartaDB")
miCursor = miConexion.cursor()

# miCursor.execute('''
# CREATE TABLE PRODUCTOS(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     CODIGO_ARTICULO VARCHAR(4) UNIQUE,
#     NOMBRE_ARTICULO VARCHAR(50),
#     PRECIO INTEGER,
#     SECCION VARCHAR (20)
# )
# ''')
# productos = [
#     ("AR01", "pelota", 20, "jugueteria"),
#     ("AR02", "pelota cuadrada", 200, "jugueteria monse"),
#     ("AR03", "camion", 20, "autos"),
#     ("AR04", "jarrón", 20, "otros"),
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'autos'")
productos = miCursor.fetchall()
for producto in productos:
    print(producto)

miCursor.execute(
    "UPDATE PRODUCTOS set SECCION = 'coches' WHERE SECCION = 'autos'")

miCursor.execute(
    "DELETE FROM PRODUCTOS WHERE SECCION = 'coches'")

miConexion.commit()
miConexion.close()
