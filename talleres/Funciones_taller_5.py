import random

# FUNCIONES
def enter():
    print("")

def printOpciones(formato_de_lista, lista_opciones, msj_volver):
    indice_opcion_de_volver = 0

    for i in range(len(lista_opciones)):
        print(formato_de_lista.format(i+1, lista_opciones[i]))
        indice_opcion_de_volver = i + 2
    print(formato_de_lista.format(indice_opcion_de_volver, msj_volver))

    enter()

    return indice_opcion_de_volver

def checkRange(opcion, rango):
    if(opcion in range(rango)):
        return True
    else:
        return False

def printErrorRango(msj_error_rango):
    print(msj_error_rango)

def printOpcionesDeLista(formato_de_lista, lista_opciones, msj_volver):
    indice_opcion_de_volver = 0

    for i in range(len(lista_opciones) - 1):
        print(formato_de_lista.format(i+1, lista_opciones[i + 1]))
        indice_opcion_de_volver = i + 2
    print(formato_de_lista.format(indice_opcion_de_volver, msj_volver))

    enter()

    return indice_opcion_de_volver

def checkListas(listas):
    if(listas == []):           
        return False
    else:
        return True

def anadirNuevaLista(nombre, elementos, lista_de_listas):
    nueva_lista = [nombre]
    lista_de_elementos = elementos.split(",")

    for elemento in lista_de_elementos:
        nueva_lista.append(elemento)

    lista_de_listas.append(nueva_lista)

def mostrarLista(lista, *punto_de_partida):
    if (punto_de_partida == ()):
        for elemento in range(len(lista)):
            print(lista[elemento])

    else:
        for elemento in range(len(lista) - punto_de_partida[0]):
            print(lista[elemento + punto_de_partida[0]])

def mostrarTodasLasListas(lista_de_listas):
    for lista in range(len(lista_de_listas)):
        print(lista_de_listas[lista][0] + ":")

        mostrarLista(lista_de_listas[lista], 1)
        enter()

def estadoLista(lista_de_doctores, posibles_estados_de_doctores, msj_formato_de_estado):
    lista_estado_de_doctores = []
    indice_doctor_actual = 0

    while(indice_doctor_actual < len(lista_de_doctores) - 1):
        lista_estado_de_doctores.append(random.choice(posibles_estados_de_doctores))
        indice_doctor_actual += 1

    for i in range(len(lista_estado_de_doctores)):
        print(msj_formato_de_estado.format(lista_de_doctores[i + 1], lista_estado_de_doctores[i]))

    enter()