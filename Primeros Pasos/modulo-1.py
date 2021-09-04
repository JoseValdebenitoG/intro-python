# =====> Importando modulos <====
import modulos as xs # con la palabra reservada de import, importamos otro modulo que hayamos creado u otro de los que vienen incluidos en python.
# con la palabra as cambiamos el nombre a nuestro archivo de "modulos" a "xs", con esto cada vez que llamemos a nuestro archivo modulos lo tendremos que nombrar "xs"

# print(modulos.mascotas) # con esto llamamos especificamente al elemento llamado mascotas en el archivo modulos
# modulos.saludo('Nicolas') # con esto llamamos a la funcions saludo del archvivo modulos
print(xs.mascotas)
xs.saludo('Felipe')

# ====> importar solo un elemento <====
# Para importar solo un elemento desde un modulo primero usamos from para indicar desde donde importaremos, y luego usamos import e indicamos el elemento que queremos importar
from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo('Nicolas')

c = CamelCase()
s = 'esta oracion necesita camelCase!'

camelcased = c.hump(s)
print(camelcased)
