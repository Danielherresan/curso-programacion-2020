from Funciones_taller_5 import *

# MENSAJES
MSJ_PGA = "1 - Crear nueva lista  \n2 - Modificar listas creadas \n3 - Mostrar listas creadas \n4 - Mostrar estado \n5 - Salir \n\n"
MSJ_NOM_LIST = "Ingrese el nombre de su nueva lista, para tener aceso a la funcion de mostrar estado el nombre debe ser doctores, enfermeros o pacientes(sin mayusculas): \n"
MSJ_ELEM = "Ingrese los elementos de la lista separados por una(1) coma(,): \n"
MSJ_OPC_2 = "1 - Añadir elementos a una lista \n2 - Eliminar elementos de una lista \n3 - Volver al menú principal \n\n"
MSJ_NO_LISTAS = "En este momento no hay ninguna lista creada, crea una lista para poder editarla."
MSJ_NO_LISTAS_EST = "En este momento no hay ninguna lista creada, crea una lista para poder ver su estado."
MSJ_IND_ANA = "Selecciona el número de la lista a la que le deseas añadir elementos: \n"
FORM_LIST = "{} - {}"
MSJ_ELEM_ANA = "Ingrese los elementos que desea añadir a la lista separados por una(1) coma(,): \n"
MSJ_IND_ELI = "Selecciona el número de la lista a la que le deseas eliminar un elemento: \n"
MSJ_ELEM_ELI = "Ingrese el numero del elemento que desea eliminar de la lista (empezando desde 1): \n"
MSJ_EXI_ELI = "Se ha eliminado exitosamente el elemento '{}' de la lista {}."
MSJ_IND_EST = "Selecciona el número de la lista para ver su estado: \n"
MSJ_EST_DOC = "{} - El doctor {} se encuentra {} en este momento."
MSJ_EST_ENF = "{} - El enfermero {} se encuentra {} en este momento."
MSJ_EST_PAC = "{} - El paciente {} se encuentra {} en este momento."
PGA_ELI = "Ingrese el numero del item que desea remover de su carrito: \n"
ERR_RAN = "El numero que ingresaste no corresponde a una funcion de este programa, intetalo de nuevo.\n"
MSJ_ERR_EST = "La lista que seleccionaste no se llama doctores, enfermeros o pacientes, por lo tanto no te puedo dar el estado de los items en la lista."
MSJ_DESP = "Cuidate.."

# VARIABLES
listasCreadas = []
_nomList = ""
_elem = ""
elemList = []
_opc = ""
_opc2 = ""
_indexAnadir = ""

# CODIGO
_opc = int(input(MSJ_PGA))

while(_opc not in range(1,6)):
    enter()

    print(ERR_RAN)
    time.sleep(1.5)
    _opc = int(input(MSJ_PGA))
    
while(_opc in range(1,6)):

    while(_opc == 1):
        enter()

        _nomList = input(MSJ_NOM_LIST)
        #_nomList = _nomList + ":"

        enter()

        _elem = input(MSJ_ELEM)
        listaTemp = crearLista(_nomList, _elem)
        listasCreadas.append(listaTemp)

        enter()

        _opc = int(input(MSJ_PGA))   

    while(_opc == 2):

        enter()

        if(listasCreadas == []):
            print(MSJ_NO_LISTAS)
            time.sleep(2)

            enter()

        else:
            _opc2 = int(input(MSJ_OPC_2))

            while(_opc2 not in range(1,4)):
                enter()

                print(ERR_RAN)
                time.sleep(1.5)
                _opc2 = int(input(MSJ_OPC_2))
        
            while(_opc2 in range(1,4)):

                while(_opc2 == 1):

                    enter()

                    print(MSJ_IND_ANA)
                    for i in range(len(listasCreadas)):
                        print(FORM_LIST.format(i+1, listasCreadas[i][0]))

                    enter()   

                    _indexAnadir = int(input()) - 1

                    enter()

                    _elemAnadir = input(MSJ_ELEM_ANA)
                    elemAnadir = _elemAnadir.split(",")

                    enter()

                    for elemento in elemAnadir:
                        listasCreadas[_indexAnadir].append(elemento)

                    _opc2 = int(input(MSJ_OPC_2))
                
                while(_opc2 == 2):

                    enter()

                    print(MSJ_IND_ELI)
                    for i in range(len(listasCreadas)):
                        print(FORM_LIST.format(i+1, listasCreadas[i][0]))

                    enter()   

                    _indexEli = int(input()) - 1

                    enter()

                    print(MSJ_ELEM_ELI)
                    for i in range(len(listasCreadas[_indexEli]) - 1):
                        print(FORM_LIST.format(i+1, listasCreadas[_indexEli][i + 1]))

                    enter()

                    _elemEli = int(input())
                    elemEliminado = listasCreadas[_indexEli][_elemEli]  

                    enter()

                    listasCreadas[_indexEli].pop(_elemEli)

                    enter()

                    listActual = listasCreadas[_indexEli][0]                  
                    print(MSJ_EXI_ELI.format(elemEliminado, listActual))
                    time.sleep(0.5)

                    enter()

                    _opc2 = int(input(MSJ_OPC_2))
                
                while(_opc2 == 3):
                    _opc2 = 0           
    
            enter()

        _opc = int(input(MSJ_PGA))    

    while(_opc == 3):
        mostrarListas(listasCreadas)
        time.sleep(0.5)
        enter()
        _opc = int(input(MSJ_PGA))

    while(_opc == 4):
        enter()

        if(listasCreadas == []):
            print(MSJ_NO_LISTAS_EST)
            time.sleep(2)

            enter()

        else:
            print(MSJ_IND_EST)
            for i in range(len(listasCreadas)):
                print(FORM_LIST.format(i+1, listasCreadas[i][0]))
        
            enter()

            _indexEst = int(input()) - 1

            enter()

            
            if(listasCreadas[_indexEst][0] == "doctores"):
                listaDocEst = estadoDoctores(listasCreadas[_indexEst])
            
                for i in range(len(listasCreadas[_indexEst]) - 1):
                    print(MSJ_EST_DOC.format(i+1, listasCreadas[_indexEst][i+1], listaDocEst[i]))
                    time.sleep(0.5)
            elif(listasCreadas[_indexEst][0] == "enfermeros"):
                listaEnfEst = estadoEnfermeros(listasCreadas[_indexEst])
            
                for i in range(len(listasCreadas[_indexEst]) - 1):
                    print(MSJ_EST_ENF.format(i+1, listasCreadas[_indexEst][i+1], listaEnfEst[i]))
                    time.sleep(0.5)
            elif(listasCreadas[_indexEst][0] == "pacientes"):
                listaPacEst = estadoPacientes(listasCreadas[_indexEst])
            
                for i in range(len(listasCreadas[_indexEst]) - 1):
                    print(MSJ_EST_PAC.format(i+1, listasCreadas[_indexEst][i+1], listaPacEst[i]))
                    time.sleep(0.5)
            else:
                print(MSJ_ERR_EST)
                time.sleep(2)

        enter()

        _opc = int(input(MSJ_PGA))

    while(_opc == 5):
        print(MSJ_DESP)
        exit()

    while(_opc not in range(1,6)):
        enter()

        print(ERR_RAN)
        time.sleep(1.5)
        _opc = int(input(MSJ_PGA))