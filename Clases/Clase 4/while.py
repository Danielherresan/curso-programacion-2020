import random

PGA_NUM = "Ingresa un numero entero entre 1-10: "
MSJ_FALLO = "Fallaste, intentalo de nuevo"
MSJ_ACIERTO = "Felicidades, acertaste"
MSJ_ABAJO = "intenta un numero mas alto"
MSJ_ARRIBA = "intenta un numero mas bajo"

NUM_FAV = random.randint(1, 10)

_numIngresado = int(input(PGA_NUM))

while (_numIngresado != NUM_FAV):
    print(MSJ_FALLO)

    if(_numIngresado < NUM_FAV): 
        print(MSJ_ABAJO)
    else: 
        print(MSJ_ARRIBA)

    _numIngresado = int(input(PGA_NUM))
print(MSJ_ACIERTO)
    