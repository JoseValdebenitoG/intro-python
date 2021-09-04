# =====> Clases, instancias y metodos <=====

# class Usuario: # Al momento de crear una clase se debe comenzar con mayusculas
    # nombre = "Felipe"
    # apellido = "Feliz"

# usuario = Usuario() # las instancias se escriben con minusculas, asi instanciamos nuestra clase como si fuera una funcion al poner parentesis al final

# print(usuario) # de esta forma llamamos al usuario como un objeto de la clase.

# Para acceder a la propiedades lo hacemos de la sgte forma.
# print(usuario.nombre)
# Para llamar a todas las propiedades debemos mencionarlas, con la instancia seguida de la pripiedad
# print(usuario.nombre, usuario.apellido)

# ===> para crear varios elementos dentro de una clase <===

# class Usuario:
    # def __init__(self, nombre, apellido):
      # self.nombre = nombre
      # self.apellido = apellido

# usuario = Usuario('Felipe', 'Feliz')
# usuario2 = Usuario('Chanchito', 'Feliz')
# usuario3 = Usuario('Pandora', 'Loca')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido, usuario3.nombre, usuario3.apellido)

# ====>Tambien podemos agregarle otro metodo, que por ejemplo no muestre un saludo junto con el nombre y apelldo. <====

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

#  usuario = Usuario('Felipe', 'Feliz')
#  usuario2 = Usuario('Chanchito', 'Feliz')

# para acceder a los metodos creados en la clase no es necesario volver a escribir print, sino que mensionamos dicho metodo.
#  usuario.saludo()
#  usuario2.saludo()
# Tambien podemos cambiar las propiedades de nuestras instancias, de la siguiente forma
#  usuario.nombre = 'Perrito'
#  usuario.saludo() # Con esto cambiamos la instancia nombre
# Tambien podemos eliminar instancias
# del usuario.nombre
# usuario.saludo()

# O podemos eliminar al elemento completo de la siguiente forma:
# del usuario
# print(usuario)

# HERENCIAS

class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, 'y soy administrador')


#  admin.saludo()
#  admin.superSaludo() # con esto podemos llamar a las istancias de la clase padre, pero no podemos llamar instancias de las clases hijo.
#  usuario.superSaludo() # Esta no se imprimirá

# =======> EJERCICIOS <======
class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un gato y mi sonido es el', self.onomatopeya)


class Perro:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un perro y mi sonido es el', self.onomatopeya)

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

# Otra forma de hacer esto es que primero creamos una clase general, como animales, y despues creamos clases con los tipos de animales.

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # acá definimos un nuevo init con los mismos atributos de la clase padre
        Animal.__init__(self, nombre, onomatopeya) # acá llamamos a la clase padre y le volvemos a entregar los mismos atributos incluyendo self, para que siga el mismo comportamiento
        print('Hola soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # con la funcion super no es necesario volver a llamar a self dentro de init
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
