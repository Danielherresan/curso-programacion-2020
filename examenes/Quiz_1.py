# MENSAJES
MSJ_BVN = "Bienvenido al programa que te juzga y te clasifica por tu lugar de origen y ademas te dice lo que ya deberias saber."
MSJ_EST = "En este momento te encuentras es un estado de {},"
DESP_OBSV = "porfavor dirigete al centro de monitoreo lo mas antes posible."
DESP_NORMAL = "que tengas un buen dia."
DESP_ALERTA = "se recomienda que estes alerta y te realices examenes de salud."
DESP_PELIGRO = "porfavor dirigete inmediatamente a un centro asistencial."
PRG_PAIS = "Porfavor ingresa tu pais de origen: "
PRG_TEMP = "Ingresa tu temperatura actual: "
PAISES_BAN = ["china", "italia", "iran"]
OBSV = "observacion"
HIPO = "hipotermia"
SALUD = "buena salud"
ALERTA = "alerta"
PELIGRO = "peligro"

# ENTRADAS 
_paisUsuario = ""
_tempUsuario = ""

# VARIABLES
estado = ""

# CODIGO
_paisUsuario = input(PRG_PAIS)

if(_paisUsuario in PAISES_BAN):
    estado = OBSV
    print(MSJ_EST.format(estado), DESP_OBSV)
    exit()

_tempUsuario = float(input(PRG_TEMP))

if(_tempUsuario <= 36):
    estado = HIPO
    print(MSJ_EST.format(estado), DESP_ALERTA)
elif(_tempUsuario <= 38.4):
    estado = SALUD
    print(MSJ_EST.format(estado), DESP_NORMAL)
elif(_tempUsuario <= 40):
    estado = ALERTA
    print(MSJ_EST.format(estado), DESP_ALERTA)
else:
    estado = PELIGRO
    print(MSJ_EST.format(estado), DESP_PELIGRO)

