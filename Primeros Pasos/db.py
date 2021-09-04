import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Alonso01',
    database = 'prueba'
)

cursor = midb.cursor()

# == listar datos
cursor.execute('SELECT * FROM Usuarios') # con esto consultamos la tabla
resultado = cursor.fetchall() # con esto consultamos los datos de la tabla
print(resultado) # con esto mostramos los datos por consola

# para limitar la consulta usaremos:
cursor.execute('SELECT * FROM Usuarios limit 1')
resultado = cursor.fetchall()
print(resultado)


# == Ver definiciones de tablas
# cursor.execute('show create table Usuarios') # con esto consultamos la estructura de nuestra tabla

# == Insertar datos
# sql = 'INSERT INTO Usuarios(email, username, edad) VALUES (%s, %s, %s)' #indicamos los datos que modificaremos
# values = ('micorreo@correo.com', 'nombreususario', 45) #aqui ingresamos los valores nuevos que tendran los datos 

# == Actualizar datos
# sql = 'update Usuarios set email = %s where id = %s'
# values = ('micorreo@correo.com', 4)
# cursor.execute(sql, values) # con esto ejecutamos las consultas

# midb.commit() # con esto se ejecutan los cambios

# print(cursor.rowcount)

# == Eliminar datos
# sql = 'DELETE FROM Usuarios WHERE id = %s'
# values = (4, )
# cursor.execute(sql, values)
# midb.commit()

