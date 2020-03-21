import time
import random

# FUNCIONES
def enter():
    print("")

def crearLista(nombre, elementos):
    lista = [nombre]
    elemList = elementos.split(",")
    for element in elemList:
        lista.append(element)

    return lista    

def mostrarListas(listas):
    for i in range(len(listas)):
        enter()
        time.sleep(0.4)
        print(listas[i][0] + ":")
        time.sleep(0.4)
        for e in range(len(listas[i]) - 1):
            print(listas[i][e+1]) 
            time.sleep(0.2)

def estadoDoctores(listaDoctores):
    choiceDoctores = ["disponible", "operando", "fuera del hospital", "en su descanso"]
    listEstadoDoc = []
    x = 0
    while(x < len(listaDoctores) - 1):
        listEstadoDoc.append(random.choice(choiceDoctores))
        x += 1
    return listEstadoDoc

def estadoEnfermeros(listaEnfermeros):
    choiceEnfermeros = ["disponible", "asistiendo una operacion", "cuidando pacientes", "fuera del hospital", "en su descanso"]
    listEstadoEnf = []
    x = 0
    while(x < len(listaEnfermeros) - 1):
        listEstadoEnf.append(random.choice(choiceEnfermeros))
        x += 1
    return listEstadoEnf

def estadoPacientes(listaPacientes):
    choicePacientes = ["en estado critico", "estable", "en coma"]
    listEstadoPac = []
    x = 0
    while(x < len(listaPacientes) - 1):
        listEstadoPac.append(random.choice(choicePacientes))
        x += 1
    return listEstadoPac