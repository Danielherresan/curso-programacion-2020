import time

# MENSAJES
MSJ_PGA = "1 - Elegir productos  \n2 - Mostrar lista \n3 - Eliminar productos \n4 - Salir \n\n"
PGA_EDAD = "Porfavor ingresa tu edad: "
ERR_EDAD = "Lo siento, este porgrama solo puede ser usado por personas mayores de edad."
MSJ_30 = "Felicidades, por ser mayor de 30 años tendras derecho a un descuento en tus compras del 30%"
MSJ_60 = "Felicidades, por ser mayor de 60 años tendras derecho a un descuento en tus compras del {}%"
PGA_ING_ITEM = "Deseas añadir otro producto a tu carrito?(s/n): "
MSJ_ING_ITEM = "Escribe el nombre del item que deseas añadir a tu carrito: "
ERR_LIST = "El caracter ingresado no fue reconocido, recuerda que: Si = s , No = n"
PGA_ELI = "Ingrese el numero del item que desea remover de su carrito: \n"
ERR_INDEX = "el numero que ingresaste no hace parte de tu lista de compras, intentalo de nuevo."
FORM_LIST = "{}. {}"
ERR_RAN = "El numero que ingresaste no corresponde a una funcion de este programa, intetalo de nuevo.\n"
MSJ_DESP = "Cuidate.."

# FUNCIONES
def enter():
    print("")

# VARIABLES
CARC = ["s", "n"] 
_opc = ""
_age = ""
_des = ""
_eli = ""
_listaCompras = []

# CODIGO
_age = int(input(PGA_EDAD))
enter()

if(_age > 60): 
    print(MSJ_60.format(_age))

elif(_age > 30):
    print(MSJ_30)

elif(_age > 17):
    pass

else:
    print(ERR_EDAD)
    exit()

enter()

_opc = int(input(MSJ_PGA))

while(_opc not in range(1,5)):
    print(ERR_RAN)
    time.sleep(1.5)
    _opc = int(input(MSJ_PGA))
    
while(_opc in range(1,5)):

    if(_opc == 1):
        _listaCompras.append(input(MSJ_ING_ITEM))      
        _des = input(PGA_ING_ITEM)

        while(_des not in CARC):
            print(ERR_LIST)
            _des = input(PGA_ING_ITEM)
        
        while(_des == "s"):
            _listaCompras.append(input(MSJ_ING_ITEM))        
            _des = input(PGA_ING_ITEM)
        enter()

    elif(_opc == 2):
        enter()
        for i in range(len(_listaCompras)):
            print(FORM_LIST.format(i+1, _listaCompras[i]))
        time.sleep(0.5)
        enter()

    elif(_opc == 3):
        _eli = int(input(PGA_ELI))

        try:
            _listaCompras.pop(_eli-1)
        except(IndexError):
            print(ERR_INDEX)
            time.sleep(0.5)
        enter()

    else:
        print(MSJ_DESP)
        exit()

    time.sleep(0.3)
    _opc = int(input(MSJ_PGA))

    while(_opc not in range(1,5)):
        print(ERR_RAN)
        time.sleep(1.5)
        _opc = int(input(MSJ_PGA))