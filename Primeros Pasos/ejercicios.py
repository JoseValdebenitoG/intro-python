# Mini Juego
# dato = input('Ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
   # print('El dato existe:', dato)
#else:
   # print('El Dato No Existe : ', dato)
#==========================================

# Calculadora que suma

# primero = input('Ingrese primer número: ')
# segundo = input('Ingrese segundo número: ')
# Cuando el usuario ingresa los numeros, python los toma como string, por ello debemos cambiarlos a numbero con la instrucción int(), o solo los concatenará
# primerNumero = int(primero)
# segundoNumero = int(segundo)
# Despues de este proceso si podra sumar los numeros
# print(primerNumero + segundoNumero)

# En el caso que el usuario ingrese una palabra en vez de numero tambien nos dará error
# En ese caso haremos lo siguiente
# primero = input('Ingrese primer número: ')

# try:
   # primero = int(primero) # Intentará convertir en un entero
# except:
   # primero = 'chanchito feliz' # excepto cuando sean palabras

# segundo = input('Ingrese segundo número: ')

# try:
   # segundo = int(segundo)
#except:
   # segundo = 'chanchito feliz'
# Evaluará si los datos ingresados son paralabras o numeros, en imprimirá segun corresponda
# if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
   # print('Ingresaste mal un dato, prueba de nuevo solo con números')
# else:
   # print(primero + segundo)

# Tambien podemos salir del script inmediatamente con la siguiente forma.

primero = input('Ingrese primer número: ')

try:
  primero = int(primero) # Intentará convertir en un entero
except:
primero = 'chanchito feliz' # excepto cuando sean palabras
if primero == 'chanchito feliz': 
    print('El valor ingresado no es un entero')
    exit() # Si el valor no es un numero el script se cierra

segundo = input('Ingrese segundo número: ')

try:
   segundo = int(segundo)
except:
   segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()
# Ahora agregamos las demas operaciones

simbolo = input('ingrese operacion: ')

if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
else:
   print('El simbolo ingresado no es valido')


