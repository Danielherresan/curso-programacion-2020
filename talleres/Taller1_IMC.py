# MENSAJES
DISCLAIMER = "Este programa fue realizado por un estudiante de ingenieria, los resultados de esta calculadora pueden variar de los resultados de otras calculadoras de IMC ante cualquier duda consulte su profesional de la salud."
MSJ_BIENVENIDA = "BIENVENIDO A LA CALCULADORA BIOMEDICA DE IMC"
MSJ_IMC = "Tu IMC es actualmente "
MSJ_TU_IMC = ", tu IMC es"
MSJ_TOCAYO = "Por cierto, ¡somos tocayos!"
MSJ_TOCAYO_PROFE = "Talvez no seas mi tocayo pero si del profe."
MSJ_FUERA_RANGO_EDAD = "ten en cuenta que esta calculadora esta diseñada para edades desde 16 hasta 90 años, por ende tu calculo puede variar o ser inacertado."
MSJ_BAJO_PESO = "Segun tu IMC actualmente sufres de bajo peso, en especifico de "
MSJ_PESO_NORMAL = "Segun tu IMC actualmente tienes un peso normal."
MSJ_SOBREPESO = "Segun tu IMC actualmente sufres de sobrepeso, en especifico de "
NOMBRE_PROFE = "daniel"
NOMBRE_PROPIO = "santiago"
MSJ_OBESIDAD = "Segun tu IMC actualmente sufres de obesidad, en especifico de "
PGA_NOMBRE = "Porfavor ingrese su nombre: "
PGA_EDAD = "Ingresa tu edad: "
PGA_ALTURA = "Ingrese su altura (en metros): "
PGA_PESO = "Ingrese su peso (en kilogramos): "
EPC_DE_SE = "delgadez severa."
EPC_DE_MO = "delgadez moderada."
EPC_DE_LE = "delgadez leve."
EPC_PRE_OB = "pre-Obesidad."
EPC_OB_I = "obesidad tipo I." 
EPC_OB_II = "obesidad tipo II." 
EPC_OB_III = "obesidad tipo III." 

# INPUTS
_nombreUsuario = ""
_edadUsuario = ""
_alturaUsuario = ""
_pesoUsuario = ""

# VARIABLES
indice = 0

# CODIGO
print(DISCLAIMER)
print(MSJ_BIENVENIDA)

_nombreUsuario = input(PGA_NOMBRE)
_edadUsuario = int(input(PGA_EDAD))
_alturaUsuario = float(input(PGA_ALTURA))
_pesoUsuario = float(input(PGA_PESO))

#Check si la edad esta en el rango adecuado
if(_edadUsuario < 16) or (_edadUsuario >90):
    print(_nombreUsuario, MSJ_FUERA_RANGO_EDAD)

#calcular IMC
indice = round((_pesoUsuario) / (_alturaUsuario)**2, 2)

#Determinar rango de IMC
if(indice < 18.5):
    if(indice <16):
        msj_imc = MSJ_BAJO_PESO + EPC_DE_SE
    elif(indice >= 16) and (indice < 17):
        msj_imc = MSJ_BAJO_PESO + EPC_DE_MO
    else:
        msj_imc = MSJ_BAJO_PESO + EPC_DE_LE

elif(indice >= 18.5) and (indice < 25):
    msj_imc = MSJ_PESO_NORMAL

elif(indice >= 25):
    if(indice < 30):
        msj_imc = MSJ_SOBREPESO + EPC_PRE_OB
    elif(indice >= 30) and (indice < 35):
        msj_imc = MSJ_OBESIDAD + EPC_OB_I
    elif(indice >= 35) and (indice <40):
        msj_imc = MSJ_OBESIDAD + EPC_OB_II
    else:
        msj_imc = MSJ_OBESIDAD + EPC_OB_III

#Mostrar resultados
print(_nombreUsuario + MSJ_TU_IMC, indice, msj_imc)

#Tocayos??
if(_nombreUsuario == NOMBRE_PROPIO):
    print(MSJ_TOCAYO)
elif(_nombreUsuario == NOMBRE_PROFE):
    print(MSJ_TOCAYO_PROFE)


