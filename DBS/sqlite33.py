import sqlite3

miConexion = sqlite3.connect("TerceraDB")
miCursor = miConexion.cursor()

miCursor.execute('''
CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR (20)
)
''')
productos = [
    ("pelota", 20, "jugueteria"),
    ("pelota cuadrada", 200, "jugueteria monse"),
    ("camion", 20, "autos"),
    ("jarrón", 20, "otros"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()
