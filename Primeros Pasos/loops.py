# ==== loop while =====
# i = 0

# while i < 5:
    # print(i)
   # i += 1 # tambien se puede escribir i = i + 1
#con esto se irá aumentando en uno a la variable i cada vez que se repite el scipt

# ==== While con break and continue ====
# ==== break ====
# i = 0

# while i < 5:
   # print(i)
   # if i == 3: # si i es igual a 3 se llevará a cabo la palabra reservada break y detendrá el script
       # break
   # i += 1

# ==== continue ====
# i = 0

# while i < 5:
   # print(i)
   # if i == 3:
       # continue # si ponemos la palabla reservada continue en este lugar, el script volverá al inicio desde este punto y no se sumara 1 a la letra i, asi i sera igual a 3 infinitamente.
   # i += 1

# para que continue funcione lo escribimos en el siguiente orden

# i = 0

# while i < 5:
   # i += 1
   # if i == 3: # en este caso se saltará el 3
       # continue
   # print(i) # al estar el print despues del incremento de valor se imprimirá hasta el 5

# ==== for loop ====
# sirve para iterar listas o tuplas, y tambien diccionarios

# usuarios = ['Chanchito Feliz', 'Felipe', 'Roberto', 'nicolas']

# == con esto ingresamos a cada elemnto de nuestra lista ==
# for usuario in usuarios:   
# print(usuario)


# usuario = 'Chanchito Feliz'

# == con esta forma ingresamos a cada caracter del string ==
#for c in usuario:
  # print(c)

# ==== break ====
# con esto se para la iteración en el valor que asignamos a la condicion if
# usuarios = ['Chanchito Feliz', 'Felipe', 'Roberto', 'nicolas']

# for usuario in usuarios:
   # if usuario == 'Roberto':
       # break
   # print(usuario)

# ==== continue ====
# con este se salta el valor asignado a la condicion if
# usuarios = ['Chanchito Feliz', 'Felipe', 'Roberto', 'nicolas']

# for usuario in usuarios:
   # if usuario == 'Roberto':
       # continue
    #print(usuario)


# ==== funcion range ====


#for x in range(1, 6): # hara un rango comenzando por el uno hasta el cinco
   # print(x)


#for x in range(3, 30, 3): # esto hará que comience desde el 3 hasta el 30 pero de 3 en 3.
   # print(x)
#else:  # con else despues de un for podemos comentar algo cuanto este termine.
   # print('Hemos terminado!!')

# === for anidados ===

# usuarios = ['Chanchito Feliz', 'Felipe', 'Roberto', 'nicolas']

# edades = [24, 25, 26, 35]

# for usuario in usuarios:
   # for  edad in edades:
       # print(usuario, edad)



