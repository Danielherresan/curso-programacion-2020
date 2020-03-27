from funciones import *


# MENSAJES
DICCIONARIO_MENSAJES = {
    'FUERA DE RANGO': "El número ingresado no corresponde a una función de este programa, por favor intetalo de nuevo.\n",
    'FORMATO': "{} - {}",
    'VOLVER': "Salir"
}
ALTA = "alta"
BAJA = "baja"
PGA_NUEVO_PACIENTE = "Ingrese el peso del nuevo paciente:\n"
OPCIONES_MENU_PRINCIPAL = ["Añadir nuevo pacientes", "Calcular presiones", "Mostrar datos"]
PGA_SUBMENU_2 = "¿Deseas ver la lista en orden descendente?"
OPCIONES_SUBMENU_2 = ["Si", "No"]
PGA_SUBMENU_3 = "Que dato deseas visualizar:\n"
OPCIONES_SUBMENU_3 = ["Mayor presión", "Menor presión", "Número de pacientes actuales", "Promedio de toma de datos"]
FORMATO_NUMERO_DE_PACIENTES = "En este momento hay {} pacientes registrados en esta plataforma."
FORMATO_DE_LISTAS = "El paciente {} con un peso de {}kg tiene una presion calculada de {}mm/hg"
FORMATO_DE_PROMEDIO = "En promedio se estan tomando {} datos cada hora."
FORMATO_DE_PRESION = "El paciente con la presión más {} tiene una presion de {}mm/hg."
MSJ_DESPEDIDA = "Cuidate, y por tu seguridad quedate en casa..."
ERR_NO_CALCULO = "Debes calcular las presiones de tus pacientes antes de acceder a los datos."

# VARIABLES
lista_pesos = [98, 74, 122, 85, 115, 64, 127, 137, 148, 32] # como ya esta en orden la desorganicé
lista_presiones = []
rango_menu_principal = 2 + len(OPCIONES_MENU_PRINCIPAL)
rango_submenu_2 = 4
rango_submenu_3 = 6
ordenada = None
maximo = None
_decision = 0
_decision_submenu_2 = 0
_decision_submenu_3 = 0
_nuevoPaciente = 0

# FUNCIONES INTERNAS
def anadirPacientes(_input, lista):
    _input = int(input(PGA_NUEVO_PACIENTE))
    lista.append(_input)
    espacio()
    
def CalcularPresiones(lista, lista_de_presiones):
    for peso in lista:
        calculo = 6 * peso
        lista_de_presiones.append(calculo)
        
def MostrarPresiones(lista, lista_de_presiones, ordenada):
    espacio()
    CalcularPresiones(lista_pesos, lista_presiones)

    if ordenada:
        lista_decresiente = lista_de_presiones.copy()
        lista_decresiente_pacientes = lista.copy()
        lista_decresiente.sort()
        lista_decresiente_pacientes.sort()

        for i in range(len(lista_decresiente)):
            print(FORMATO_DE_LISTAS.format(i + 1, lista_decresiente_pacientes[i], lista_decresiente[i]))
            time.sleep(0.4)
        
        espacio()

    else:   
        for i in range(len(lista)):
            print(FORMATO_DE_LISTAS.format(i + 1, lista[i], lista_de_presiones[i]))
            time.sleep(0.4)

        espacio()

def numeroPacientes(lista):
    var = len(lista)
    return var

def promedio(lista):
    numItems = len(lista)
    promedio = round((numItems / 24), 2)
    return promedio

def subMenu2(decision):
    if (decision == 1):
        ordenada = True
    elif (decision == 2):
        ordenada = False
    
    else:
        espacio()
        whileLoop(DICCIONARIO_MENSAJES, funcionPrincipal, _decision, rango_menu_principal, OPCIONES_MENU_PRINCIPAL)

    MostrarPresiones(lista_pesos, lista_presiones, ordenada)

def subMenu3(decision):
    if (decision == 1):
        espacio()
        print(FORMATO_DE_PRESION.format(ALTA, max(lista_presiones)))
        espacio()

    elif (decision == 2):
        espacio()
        print(FORMATO_DE_PRESION.format(BAJA, min(lista_presiones)))
        espacio()

    elif (decision == 3):
        espacio()
        print(FORMATO_NUMERO_DE_PACIENTES.format(numeroPacientes(lista_pesos)))
        espacio()

    elif (decision == 4):
        espacio()
        print(FORMATO_DE_PROMEDIO.format(promedio(lista_pesos)))
        espacio()
    else:
        espacio()
        whileLoop(DICCIONARIO_MENSAJES, funcionPrincipal, _decision, rango_menu_principal, OPCIONES_MENU_PRINCIPAL)
        

def funcionPrincipal(_decision):
    if (_decision == 1):
        espacio()

        anadirPacientes(_nuevoPaciente, lista_pesos)

    elif (_decision == 2):
        espacio()

        print(PGA_SUBMENU_2)
        espacio()

        whileLoop(DICCIONARIO_MENSAJES, subMenu2, _decision_submenu_2, rango_submenu_2, OPCIONES_SUBMENU_2)

    elif (_decision == 3):
        espacio()
        if (lista_presiones != []):
            whileLoop(DICCIONARIO_MENSAJES, subMenu3, _decision_submenu_3, rango_submenu_3, OPCIONES_SUBMENU_3) 
        else:
            print(ERR_NO_CALCULO)
            espacio()

    else:
        espacio()
        print(MSJ_DESPEDIDA)
        exit()

# CODIGO
whileLoop(DICCIONARIO_MENSAJES, funcionPrincipal, _decision, rango_menu_principal, OPCIONES_MENU_PRINCIPAL)