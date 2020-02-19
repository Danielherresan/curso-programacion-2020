#vamos a hacerle preguntas a una persona

PREGUNTA_NOMBRE = "ingrese su nombre \n"
PREGUNTA_EDAD = "ingrese su edad \n"
PREGUNTA_ESTATURA = "ingrese su estatura \n"

MSJ_BIENVENIDA_I = "Bienvenido "
MSJ_BIENVENIDA_F = " a este programa."

MSJ_EDAD = "tu edad es "
MSJ_ESTATURA = "tu estatura es "

MSJ_DESPEDIDA = "Adios "

_nombrePersona = input(PREGUNTA_NOMBRE)
print(MSJ_BIENVENIDA_I + _nombrePersona + MSJ_BIENVENIDA_F)
#tambien sirve: print("Bienvenido",_nombrePersona,"a este programa")

_edadPersona = int(input(PREGUNTA_EDAD))
print(type(_edadPersona))
print(MSJ_EDAD + str(_edadPersona))

_estaturaPersona = float(input(PREGUNTA_ESTATURA))
print(type(_estaturaPersona))
print(MSJ_ESTATURA + str(_estaturaPersona))

print(MSJ_DESPEDIDA + _nombrePersona)