import sqlite3

miConexionSqlite = sqlite3.connect("PrimerBase.db")
miCursor = miConexionSqlite.cursor()

# * crear tabla si no existe
miCursor.execute("create table if not exists producto(codigo_articulo integer primary key autoincrement,nombre_articulo varchar(50), precio integer, seccion varchar(20))" )

# *insertar un registro
miCursor.execute("insert into producto( nombre_articulo, precio, seccion ) values('pure de tomate', 650, 'almacen')")
# adv hacer el commit con la conexion para guardar lo ingresado
miConexionSqlite.commit()

#! insertar masivamente registros
for i in range(10):
    variosProductos = [
        ( "fideos", 900, "almacen"),
        ("leche", 1400, "lacteos"),
        ("atun", 2300, "almacen"),
        ("agua", 1200, "bebidas"),
        ("jabon", 800, "limpieza"),
    ]

    miCursor.executemany("insert into producto(nombre_articulo, precio, seccion) values(?,?,?)", variosProductos)
    miConexionSqlite.commit()


miCursor.execute("select * from producto order by codigo_articulo desc limit 10")

productos = miCursor.fetchall() # adv devuelve una lista de tuplas
# print(productos)

for producto in productos:
    print(producto)

miCursor.execute("select count(nombre_articulo) from producto")

cantidad = miCursor.fetchone()
print(r"la cantidad es: ", cantidad)
'''
for producto in productos:
    # print("nombre: ", producto[0]," precio: ", producto[1], " seccion: ", producto[2])
    pass

'''
'''
#! eliminar todos los registros de la tabla producto
miCursor.execute("delete from producto")
miConexionSqlite.commit()
'''
miCursor.execute("select count(nombre_articulo) from producto")

cantidad = miCursor.fetchone()
print(r"la cantidad es: ", cantidad)

miCursor.execute("update producto set precio = 100000 where seccion = 'lacteos'")
miConexionSqlite.commit()

miCursor.execute("select * from producto order by codigo_articulo desc limit 10")

productos = miCursor.fetchall()  # adv devuelve una lista de tuplas
# print(productos)

for producto in productos:
    print(producto)


miConexionSqlite.close()
