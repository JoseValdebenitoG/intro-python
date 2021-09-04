# Funciones
def miFuncion():
    print('Mi primera funcion!!')

# miFuncion()

def imprimeDato(argumentoUno): # el argumento es lo que se pide con la funcion
    print('Mi argumento es', argumentoUno)

# imprimeDato('parametro') # para darle informacion al argumento, al momento de ejecutar le entregamos un parametro que irá en el espacio del argumento

def imprimeDato(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

# imprimeDato('Chanchito', 'Feliz') # si la funcions se define con dos argumentos, se debe pasarle dos parametros.

#pero tambien se puene ingresar argumentos variables, de la sgte foma

def imprimeDato(*nombre):
    print('El nombre completo es:', nombre[1]) # si no indicamos que numero de elemento estamos eligiendo, la funcion nos imprimirá una tupla, para esto usamos los parentesis cuadrados

# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')

# tambien podemos entregarle los parametros al momento de crear la funcion

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')

# Tambien lo podemos hacer, ingresando los argumentos como diccionario
def nombreCompleto2(**kwargs): # kwargs significa argumentos por llaves
    print(kwargs['nombre'],kwargs['apellido'])

# nombreCompleto2(nombre='Chanchito', apellido='Feliz') # con kwargs estamos obligados a indicarle los parametros que llevaran los argumentos.

# le podemos ingresar un argumento por defecto al definir la funcion
def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

# miFuncion2('Batman')
# miFuncion2()

# y tambien podemos los argumentos como lista.
def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])

# tambien se puede usar elementos de una lista anterior
def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i


#  nombres = concatenaNombres(['Chanchito', 'Feliz'])
#  print(nombres)

# ==> Recursividad <==
def recursion(i):
    if(i < 1): # con esto evaluamo si i es menor que 1
        return i # si es asi nos devuelve el valor de 1
    print(i) # si no es menor que i imprimira i
    recursion(i - 1) # y le restará 1 a i para volver al inicio.

recursion(6)

