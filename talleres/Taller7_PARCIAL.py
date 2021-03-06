import functions
import time
import random

DICCIONARIO_MENSAJES = {
    'FUERA DE RANGO': "El número ingresado no corresponde a una función de este programa, por favor intetalo de nuevo.\n",
    'FORMATO': "{} - {}",
    'VOLVER': "Salir"
}

OPCIONES_MENU_PRINCIPAL = ["Ver canguros", "Ver empleados", "Alimentar Canguros", "Opciones de jefe"]

MSJ_ALIMENTAR = "{} alimento al canguro {}, hasta ahora {} ha alimentado canguros {} veces"
MSJ_CONTRATAR = "El Jefe {} ha contratado un nuevo empleado, su nombre es {}"
MSJ_ANUNCIO = "El Jefe {} ha anunciado que: {}"
MSJ_SALTOS = "El canguro identificado con el numero {}, tiene {} años y ha dado {} saltos."
MSJ_DESP = "Cuidate.."

PGA_CANGURO = "Que canguro quieres alimentar:\n"
PGA_ANUNCIO = "Ingresa el anuncio público que quieres dar: \n"
PGA_CUIDADOR = "Selecciona el cuidador que desees que alimente los canguros:\n"

FORM_LIST_CANGURO = "Canguro {}"

class Canguro():
    instancias = []
    index = 1

    def __init__(self):
        self.identificacion = Canguro.index
        self.edad = random.randint(1, 20)
        self.saltos = random.randint(0, 7)
        Canguro.index += 1
        Canguro.instancias.append(self)

class Cuidador():
    instancias = []
    index = 1

    def __init__(self, nombre):
        self.contador_alimentar = 0
        self.identificacion = Cuidador.index
        self.nombre = nombre
        self.contador_alimentar = 0
        Cuidador.index += 1
        Cuidador.instancias.append(self)
    
    def alimentar(self, canguro):
        self.contador_alimentar += 1
        print(MSJ_ALIMENTAR.format(self.nombre, canguro.identificacion, self.nombre, self.contador_alimentar))
        return self.contador_alimentar

class Jefe(Cuidador):
    def __init__(self, Cuidador):
        self.nombre = Cuidador.nombre

    def contratar(self, nombre_nuevo_cuidador):
        Cuidador(nombre_nuevo_cuidador)
        print(MSJ_CONTRATAR.format(self.nombre, nombre_nuevo_cuidador))

    def darAnuncio(self, anuncio):
        print(MSJ_ANUNCIO.format(self.nombre, anuncio))

# CREACION DE OBJETOS
canguro_1 = Canguro()
canguro_2 = Canguro()
canguro_3 = Canguro()
canguro_4 = Canguro()
canguro_5 = Canguro()
canguro_6 = Canguro()
canguro_7 = Canguro()
canguro_8 = Canguro()
canguro_9 = Canguro()
canguro_10 = Canguro()

cuidador_1 = Cuidador("Jose")
cuidador_2 = Cuidador("Juan")
cuidador_3 = Cuidador("Covid de Jesús")
cuidador_4 = Cuidador("Juanita")
cuidador_5 = Cuidador("Manuel")
cuidador_6 = Cuidador("Daniel")

jefe_1 = Jefe(cuidador_3)

# VARIABLES
lista_cuidadores = []
for i in range(len(Cuidador.instancias)):
    lista_cuidadores.append(Cuidador.instancias[i].nombre)

_opcion = 0
_opcion_submenu_2 = 0
_nombre_nuevo = 0

rango_menu_principal = 2 + len(OPCIONES_MENU_PRINCIPAL)
rango_submenu_2 = 2 + len(Cuidador.instancias)


# CODIGO
def imprimirSaltos(lista):
    for i in lista:
            print(MSJ_SALTOS.format(i.identificacion, i.edad, i.saltos))
            time.sleep(0.3)
    functions.enter()

def mostrarEmpleados(lista):
    for i in range(len(lista)):
        print("El cuidador {}, tiene la identificación número {}.".format(lista[i].nombre, lista[i].identificacion))
        time.sleep(0.3)
    functions.enter()

def subMenu2(_opcion):
    functions.enter()
    if (_opcion in range(rango_submenu_2 - 1)):   
        print(PGA_CANGURO)
        for i in range(len(Canguro.instancias)):
            print(FORM_LIST_CANGURO.format(i+1))
        functions.enter()

        _canguro_seleccionado = int(input()) - 1
        functions.enter()
     
        Cuidador.instancias[_opcion - 1].alimentar(Canguro.instancias[_canguro_seleccionado]) 
        functions.enter()
        time.sleep(2)

    else:
        functions.menuLoop(DICCIONARIO_MENSAJES, mainMenu, _opcion, rango_menu_principal, OPCIONES_MENU_PRINCIPAL)
    
def mainMenu(_opcion):
    functions.enter()
    if (_opcion == 1):
        imprimirSaltos(Canguro.instancias)

    elif(_opcion == 2):
        mostrarEmpleados(Cuidador.instancias)

    elif(_opcion == 3):
        print(PGA_CUIDADOR)
        functions.menuLoop(DICCIONARIO_MENSAJES, subMenu2, _opcion_submenu_2, rango_submenu_2, lista_cuidadores)

    elif(_opcion == 4):

        _opcion_submenu_4 = int(input("1 - Dar anuncio\n2 - Contratar\n\n"))
        functions.enter()

        if (_opcion_submenu_4 == 1):
            _anuncio = input(PGA_ANUNCIO)
            functions.enter()

            jefe_1.darAnuncio(_anuncio)
            functions.enter()   
            time.sleep(2)   
        elif (_opcion_submenu_4 == 2):
            functions.enter()
            _nombre_nuevo = input("Ingresa el nombre del nuevo empleado:\n")

            jefe_1.contratar(_nombre_nuevo)  
            functions.enter()
            time.sleep(2)
        else:
            pass

    else:
        print(MSJ_DESP)
        exit()

functions.menuLoop(DICCIONARIO_MENSAJES, mainMenu, _opcion, rango_menu_principal, OPCIONES_MENU_PRINCIPAL)
    