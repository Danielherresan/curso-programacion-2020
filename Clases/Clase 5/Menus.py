import time
import random
from Funciones_menus import *

# MENSAJES
MSJ_PGA = "1 - Mostrar nombres \n2 - mostrar edades \n3 - Notas \n4 - Salir \n"
MSJ_ERR = "El numero que ingresaste no corresponde a una funcion de este programa, intetalo de nuevo."
MSJ_EDAD = "{} tiene {} años."
MSJ_NOTA = "{} obtuvo una calificacion de {}."
MSJ_DESP = "Cuidate.."

# VARIABLES
_num = 0
nombres = [
"santiago",
"juanes",
"marco",
"elena",
"camila betancur",
"camila mesa",
"lesly",
"ysabella",
"santiago em",
"daniel",
"mafe",
"octavio",
"susi",
"daniel profe"
]

# CODIGO
_num = int(input(MSJ_PGA))

while(_num not in range(1,5)):
    print(MSJ_ERR)
    time.sleep(1.5)
    _num = int(input(MSJ_PGA))
    
while(_num in range(1,5)):
    

    if(_num == 1):
        for i in range(len(nombres)):
            print(nombres[i])
            time.sleep(0.3)

    elif(_num == 2):
        ListEdad = edades(len(nombres))
        for i in range(len(ListEdad)):
            print(MSJ_EDAD.format(nombres[i], ListEdad[i]))
            time.sleep(0.3)

    elif(_num == 3):
        ListNota = notas(len(nombres))
        for i in range(len(nombres)):
            print(MSJ_NOTA.format(nombres[i], ListNota[i]))
            time.sleep(0.3)

    else:
        print(MSJ_DESP)
        exit()

    time.sleep(0.3)
    _num = int(input(MSJ_PGA))

    while(_num not in range(1,5)):
        print(MSJ_ERR)
        time.sleep(1.5)
        _num = int(input(MSJ_PGA))