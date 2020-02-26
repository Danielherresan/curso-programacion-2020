# MENSAJES
MSJ_BIENVENIDA = "Bienvenido al programa para calcular el riesgo de su hospital."
MSJ_ERROR = "El numero de pacientes no puede ser negativo."
PGA_PACIENTES = "Porfavor ingrese el numero de pacientes en su hospital: "
PGA_UCI = "Ingrese el numero de pacientes en UCI en su hopital: "
RIESGO_BAJO = "En este momento su hospital se encuentra en riesgo bajo."
RIESGO_MEDIO = "En este momento su hospital se encuentra en riesgo medio."
RIESGO_ALTO = "En este momento su hospital se encuentra en riesgo alto."

# ENTRADAS
_numPacientes = ""
_numPacientesUci = ""

# CODE
_numPacientes = int(input(PGA_PACIENTES))
_numPacientesUci = int(input(PGA_UCI))

if(_numPacientes < 0) or (_numPacientesUci <0):
    print(MSJ_ERROR)
    exit
elif(_numPacientes < 1000) and (_numPacientes > 0):
    print(RIESGO_BAJO)
elif(_numPacientes <= 5000):
    if(_numPacientesUci > 1000):
        print(RIESGO_ALTO)
    else:
        print(RIESGO_MEDIO)
else:
    print(RIESGO_ALTO)
