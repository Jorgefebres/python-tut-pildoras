import sqlite3

miConexion = sqlite3.connect("SegundaDB")
miCursor = miConexion.cursor()

miCursor.execute('''
CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR (20)
)
''')
productos = [
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "pelota cuadrada", 200, "jugueteria monse"),
    ("AR03", "camion", 20, "autos"),
    ("AR04", "jarrón", 20, "otros"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()
miConexion.close()
