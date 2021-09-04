# comentarios
if 3 > 5:  # Esto no se va a imprimir
    print('5 es mayor que 3')  # con este comando de imprime la orden

#if 5 > 3:  #Esto si se va a imprimir
   #print('5 es mayor que 3')

x = 4
y = 'chanchito feliz'
 
print(x, y)

correo = 'chanchito@feliz.com'

#print(correo)

# Formas de escribir las variables
_mi_var = 'chanchito'
MIVAR = 'chanchito'
miVar = 'chanchito' # esta forma se llama camelCase

a, b, c = 'Lala', 'Lele', 'Lili'

print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

print(valor1, valor2, valor3)

# Concatenar
inicio = 'Hola'
final = 'mundo'
# para concatenar dos variables usamos el simbolo +
# print(inicio + final)

# Tipos de datos
palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string
entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j

# print(palabra, oracion, entero, conDecimales, complejo)

# Para definir una lista usamos parentesis cuadrado
lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista2 = lista.copy() # Con el metodo .copy() Hace una copia de la lista
lista.append('Chanchito triste') # Con el metodo .append() agrega elementos a la lista
# lista.clear() # Con el metodo .clear() borra los elementos de la lista
# print(lista, lista2.count(3)) #el metodo .count() cuenta cuantas veces se retipe el elemnto que esta entre en el parentesis
# print(len(lista), len(lista2)) # con la funcion len() cuenta los elementos que hay dentro de una lista
# Crear variable usando funcion len
largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

# print(lista[2]) # Imprime solo el elemento indicado en el parentesis
# el orden de los elemntos comienzan desde el cero
# lista.pop() # este elimina el último elemento de la lista
# lista.remove('Hola') # este elimina un elemento por su valor
lista.reverse() # este metodo da vuelta la lista
lista.sort() # ordena los elementos de la lista

# Tuplas, estas de indican con parentesis 
tupla = ('hola', 'mundo', 'somos', 'tupla') # a diferencia de las listas, las tuplas no se pueden modificar
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
# print(listaDeTupla)

# los rangos nos serviran mas adelante
rango = range(6)
# print(rango)

# los diccionarios se definen con parentesis de llave
diccionario = {
    "nombre": "Chanchito feliz", # la coma es obligatoria para ingresar mas valores
    "raza": "Persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre']) # para acceder solo al item indicado en el parentesis cuadrado
# print(diccionario['raza'])
# print(diccionario.get('nombre')) # con el metodo .get() remplazamos los parentesis cuadrados
diccionario['nombre'] = 'Fluffy' # con esto cambiamos el nombre

# print(len(diccionario))

diccionario['ronronea'] = 'Si' # Agrena un elemento al diccionario

# print(diccionario)
# diccionario.pop('ronronea') # para eliminar el valor indicado en el parentesis
# diccionario.popitem() # con este metodo se elimina el ultimo valor agregado
# copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario) # otra forma de copiar el diccionario
# del diccionario['ronronea'] # otra forma de borrar un elemnto 
diccionario.clear() # con este metodo eliminamos todos los valores
# print(diccionario, copiaGatito)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

#print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6) # esta funcion crea un diccionario 
print(perritos)

# Datos Booleanos
verdadero = True
falso = False

print(verdadero, falso)


