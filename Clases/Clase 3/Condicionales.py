# MENSAJES
PREGUNTA_NOMBRE = "Ingrese su nombre: "
PREGUNTA_EDAD = "Ingrese su edad: "
MSJ_BIENVENIDA = "Bienvenido"
MSJ_DESPEDIDA = "Adios"
MSJ_TOCAYO = "Guau somos tocayos"
MSJ_TOCAYO_PROFE = "No eres mi tocayo, pero si del profe"
MSJ_NO_TOCAYO = "No somos tocayos :c"
MSJ_ANCIANO = "Eres un vejestorio"
MSJ_JOVEN = "Estas en tu mejor momento"
MSJ_BEBE = "Bebecitoooo"
MSJ_INVALIDO = "La edad negativa no existe, coja oficio"

# VARIABLES
NOMBRE_PROPIO = "santiago"
NOMBRE_PROFE = "daniel"
tocayo = ""
edad = ""

# ENTRADAS
_nombreUsuario = ""
_edadUsuario = ""

# CODIGO
print(MSJ_BIENVENIDA)
_nombreUsuario = input(PREGUNTA_NOMBRE)

if(_nombreUsuario == NOMBRE_PROPIO):
    print(MSJ_TOCAYO)
    tocayo = "tocayo"
elif(_nombreUsuario == NOMBRE_PROFE):
    print(MSJ_TOCAYO_PROFE)
    tocayo = "tocayo del profe"
else:
    print(MSJ_NO_TOCAYO)
    tocayo = "no tocayo"

_edadUsuario = int(input(PREGUNTA_EDAD))

if(_edadUsuario >= 65):
    print(MSJ_ANCIANO)
    edad = "ten cuidado con la osteoporosis."
elif(_edadUsuario < 25) and (_edadUsuario >= 0):
    print(MSJ_BEBE)
    edad = "tomate toda tu sopita."
elif(_edadUsuario >= 25) and (_edadUsuario < 65):
    print(MSJ_JOVEN)
    edad = "disfruta tu juventud."
else:
    print(MSJ_INVALIDO)

print(MSJ_DESPEDIDA, tocayo, edad)