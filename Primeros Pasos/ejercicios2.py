# multiplicar dos números sin usar el símbolo de multiplicación
a = 35
b = 64
resultado = 0

# for x in range(a):
    # resultado += b

# print(resultado)

for x in range(b): # con esto tomaremos el valor y lo repetiremos b veces
    resultado += a # y al resultado le sumaremos el valor de a 

print(resultado)
# ingresar nombre y apellido e imprimirlo al reves
nombre = 'José'
apellido = 'Valdebenito'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1]) # con esta operacion invertimos el orden de los sting

# escribir una función que encuentre el elemento menor de una lista

lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init' # menor será igual al valor inicial

for x in lista:
    if menor == 'init': # si menor es igual al numero inicial será ese el numero menor
        menor = x
    else: # pero si no es igual buscará x, y revisará si x es menor a menor, esto con todos los elementos de la lista
        menor = x if x < menor else menor

print('menor', menor)

# escribir una función que devuelva el volumen e una esfera por su radio
# 4/3 * pi * r ** 3

def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(8)
print(resultado)

# escribir una función que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)
# escribir una función que indique si un número es par o impar

def esPar(n):
    return n % 2 == 0

resultado = esPar(15)
# print(resultado)

# escribir una función que indique cuantas vocales tienes una palabra

palabra = 'ChAnchitoFeliz'
vocales = 0

for x in palabra:
    y = x.lower()
# con este metodo solo comparaá los string en minusculas.
    # vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0
# con este otro metodo compará los string transformados a minusculas
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
# print(vocales)
# escribir una aplicación que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los números ingresados
#  lista = []
#  print('Ingrese numeros y para salir escriba "basta"')
#  while True:
    #  valor = input('Ingrese valor: ')
    #  if valor == 'basta':
        #  break
    #  else:
        #  try:
            #  valor = int(valor)
            #  lista.append(valor)
        #  except:
            #  print('Dato Inválido')
            #  exit()

#  resultado = 0
#  for x in lista:
    #  # resultado += x

# print(resultado)
# escribir una función que escriba nombre y apellido y los vaya agregando a 
# un archivo
def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Jose', 'Valdebenito')
