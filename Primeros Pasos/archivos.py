c = open('chanchito.txt') # con la funcion open() podemos importar archivos de texto dentro de nuestro codigo.

# Ademas, dentro del parentesis de open, podemos darle permisos a python para trabajar con nuestro archivo de texto.
# estos los pondremos entre comillas, separados por coma y solo la inicial.
# 'r'= read, 'a'= append (para agregar datos al final del archivo), 
# 'w'= whrite (para escribir mas datos a nuestro archivo)
# 'x'= (para crear un archivo)

# print(c.read()) # con c.read() leemos la totalidad de datos dentro del archivo que le hayamos designado a nuestra variable
# print(c.readline()) # con readline lee solo una linea, si queremos leer mas lineas debemos repetir la funcion
# print(c.readline())

# for x in c: # con esta funcion tambien podemos leer todas las lineas, donde x es cada una de las lineas en c
    # print(x)

c.close() # con este metodo cerramos el archivo de texto para evitar errores

c = open('chanchito.txt', 'a') # con 'a' agregamos elementos al final, con 'w' borra todo lo que habia anteriormente e incluye los datos que le entreguemos

# c.write('\nagregaremos una nueva linea a nuestro archivo') # con\n ingresamos el texto en una nueva linea

c.close()

c = open('chanchito.txt', 'w')

c.write('\nagregaremos una nueva linea a nuestro archivo')

c.close()

# Eliminar archivos
import os # con esto usamos comando del sistema operativo para borrar archivos 

if os.path.exists('chanchito.txt'): # Con esto comprobamos si el archivo existe
    os.remove('chanchito.txt') # con esto eliminamos el archivo
else:
    print('El archivo no existe') # y una vez eliminado nos responde.

# os.rmdir() # con esto eliminamos directorios
