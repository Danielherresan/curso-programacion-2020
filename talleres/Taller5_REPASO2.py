from Funciones import time

# MENSAJES
FORMATO_DE_LISTA = "{} - {}"
FORMATO_NOMBRE_DE_LISTA = "{}:"

DOCTORES = "doctores"
ENFERMEROS = "enfermeros"
PACIENTES = "pacientes"
SALIR = "salir"
VOLVER = "volver"
EDITAR = "editar"
MOSTRAR = "mostrar"
ESTADO = "estado"

OPCIONES_MENU_PRINCIPAL = ["Crear nueva lista", "Modificar listas creadas", "Mostrar listas creadas", "Mostrar estado"]
OPCIONES_SUBMENU_1 = ["lista predeterminada", "lista personalizada"]
OPCIONES_SUBMENU_2 = ["Añadir elementos a una lista", "Eliminar elementos de una lista"]
OPCIONES_SUBMENU_3 = ["Mostrar todas las listas", "Elegir lista para mostrar"]
OPCIONES_LISTAS_PREDETERMINADAS = ["Doctores", "Enfermeros", "Pacientes"]

MSJS_RETROCEDER = {SALIR: "Salir", VOLVER: "Volver"}

MSJ_NINGUNA_LISTA_CREADA= "En este momento no hay ninguna lista creada, crea una lista para poder {}."
DICC_NINGUNA_LISTA_CREADA = {EDITAR: "editarla", MOSTRAR: "mostrar su contenido", ESTADO: "ver el estado de sus integrantes"}

PGA_SUBMENU_1 = "Ingresa el tipo de lista que deseas crear, ten en cuenta que la funcion: 'Mostrar estado' solo se encuentra disponible para listas predeterminadas): \n"
PGA_MOSTRAR_LISTA = "Selecciona el número de la lista que quires mostrar: \n"
PGA_LISTAS_PREDETERMINADAS = "Que lista deseas crear: \n"

PGA_NOMBRAR_NUEVA_LISTA = "Ingrese el nombre personalizado de su nueva lista: \n"
PGA_INGRESAR_ELEMENTOS = "Ingrese los elementos de la lista separados por una coma(,): \n"

PGA_OPCION_ANADIR = "Selecciona el número de la lista a la que le deseas añadir elementos: \n"
PGA_ELEMENTOS_ANADIR = "Ingrese los elementos que desea añadir separados por una coma(,): \n"
MSJ_EXITO_ANADIR = "Se han agregado exitosamente los elementos especificados a la lista {}."

PGA_OPCION_ELIMINAR = "Selecciona el número de la lista a la que le deseas eliminar un elemento: \n"
PGA_ELEMENTOS_ELIMINAR = "Selecciona el número del elemento que deseas eliminar de la lista: \n"
MSJ_EXITO_ELIMINAR = "Se ha eliminado exitosamente el elemento '{}' de la lista {}."

PGA_OPCION_MOSTRAR_ESTADO = "Selecciona el número de la lista para ver el estado de sus integrantes: \n"
MSJ_ESTADO_ACTUAL = "{} se encuentra {} en este momento."
DICC_POSIBLES_ESTADOS = {
                        DOCTORES: ["disponible", "operando", "fuera del hospital", "en su descanso"],
                        ENFERMEROS: ["disponible", "asistiendo una operacion", "cuidando pacientes", "fuera del hospital", "en su descanso"],
                        PACIENTES: ["en estado critico", "estable", "esperando salida", "en coma"]
                        }

ERR_OPCION_FUERA_DE_RANGO = "El número ingresado no corresponde a una función de este programa, por favor intetalo de nuevo.\n"
ERR_LISTA_YA_CREADA = "La lista ya fue creada, si deseas editarla selecciona la ópcion en el menú principal"
ERR_LISTA_SIN_ESTADO = "La lista que seleccionada no es predeterminada, por lo cual no es posible mostrar el estado de los integrantes de dicha lista."

MSJ_DESPEDIDA = "Cuidate.."

# VARIABLES
rango_menu_principal = 5
rango_submenu_1 = 3
rango_submenu_2 = 3
rango_submenu_3 = 3
rango_submenu_4 = 0
rango_listas_predeterminadas = 4

indice_volver = 0
indice_nombre_de_lista = 0

_opcion = ""
_opcion_submenu_1 = ""
_opcion_submenu_2 = ""
_opcion_submenu_3 = ""
_opcion_submenu_4 = ""

listas_creadas = []
nombre_listas_creadas = []

_nombre_nueva_lista = ""
_elementos_nueva_lista = ""

_lista_seleccionada_para_anadir = 0
lista_a_donde_se_anadio = ""
_elementos_para_anadir = ""
lista_elementos_para_anadir = []

_lista_seleccionada_para_eliminar = 0
lista_de_donde_se_elimino = ""
_elemento_seleccionado_para_eliminar = 0
elemento_que_fue_eliminado = ""

_lista_seleccionada_para_mostrar_estado = 0

# CODIGO
printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
_opcion = int(input()) - 1

while not checkRange(_opcion, rango_menu_principal): 
    enter()

    print(ERR_OPCION_FUERA_DE_RANGO)

    printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
    _opcion = int(input()) - 1

while checkRange(_opcion, rango_menu_principal):
    while(_opcion == 0):
        enter()
        print(PGA_SUBMENU_1)
        printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_1, MSJS_RETROCEDER[VOLVER])
        _opcion_submenu_1 = int(input()) - 1

        while not checkRange(_opcion_submenu_1, rango_submenu_1): 
            enter()

            print(ERR_OPCION_FUERA_DE_RANGO)

            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_1, MSJS_RETROCEDER[VOLVER])
            _opcion_submenu_1 = int(input()) - 1

        while(checkRange(_opcion_submenu_1, rango_submenu_1)):
            while(_opcion_submenu_1 == 0):
                enter()

                print(PGA_LISTAS_PREDETERMINADAS)
                printOpciones(FORMATO_DE_LISTA, OPCIONES_LISTAS_PREDETERMINADAS, MSJS_RETROCEDER[VOLVER])
                _opcion_listas_predeterminadas = int(input()) - 1

                while not checkRange(_opcion_listas_predeterminadas, rango_listas_predeterminadas): 
                    enter()

                    print(ERR_OPCION_FUERA_DE_RANGO)

                    printOpciones(FORMATO_DE_LISTA, OPCIONES_LISTAS_PREDETERMINADAS, MSJS_RETROCEDER[VOLVER])
                    _opcion_listas_predeterminadas = int(input()) - 1

                while checkRange(_opcion_listas_predeterminadas, rango_listas_predeterminadas):
                    enter()

                    if (_opcion_listas_predeterminadas != 3):
                        if (_opcion_listas_predeterminadas == 0): 
                            _nombre_nueva_lista = DOCTORES   

                        elif (_opcion_listas_predeterminadas == 1): 
                            _nombre_nueva_lista = ENFERMEROS     

                        else: 
                            _nombre_nueva_lista = PACIENTES           

                        if (_nombre_nueva_lista not in nombre_listas_creadas):        

                            _elementos_nueva_lista = input(PGA_INGRESAR_ELEMENTOS)
                            enter()
                            
                            anadirNuevaLista(_nombre_nueva_lista, _elementos_nueva_lista, listas_creadas)   
                            nombre_listas_creadas.append(_nombre_nueva_lista)    
                        else:
                            print(ERR_LISTA_YA_CREADA)
                            enter()

                    else:
                        printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_1, MSJS_RETROCEDER[VOLVER])
                        _opcion_submenu_1 = int(input()) - 1
                        break

                    print(PGA_LISTAS_PREDETERMINADAS)
                    printOpciones(FORMATO_DE_LISTA, OPCIONES_LISTAS_PREDETERMINADAS, MSJS_RETROCEDER[VOLVER])
                    _opcion_listas_predeterminadas = int(input()) - 1
                    
                    while not checkRange(_opcion_listas_predeterminadas, rango_menu_principal): 
                        enter()

                        print(ERR_OPCION_FUERA_DE_RANGO)

                        printOpciones(FORMATO_DE_LISTA, OPCIONES_LISTAS_PREDETERMINADAS, MSJS_RETROCEDER[VOLVER])
                        _opcion_listas_predeterminadas = int(input()) - 1

            while(_opcion_submenu_1 == 1):
                enter()

                _nombre_nueva_lista = input(PGA_NOMBRAR_NUEVA_LISTA)
                enter()

                if (_nombre_nueva_lista not in nombre_listas_creadas):
                    _elementos_nueva_lista = input(PGA_INGRESAR_ELEMENTOS)
                    anadirNuevaLista(_nombre_nueva_lista, _elementos_nueva_lista, listas_creadas)
                    nombre_listas_creadas.append(_nombre_nueva_lista)   
                    enter()

                    print(PGA_SUBMENU_1)
                    printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_1, MSJS_RETROCEDER[VOLVER])
                    _opcion_submenu_1 = int(input()) - 1  
                else:
                    print(ERR_LISTA_YA_CREADA)
                    enter()

            if(_opcion_submenu_1 == 2):
                enter()
                break

            while not checkRange(_opcion_submenu_1, rango_submenu_1): 
                enter()

                print(ERR_OPCION_FUERA_DE_RANGO)

                printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_1, MSJS_RETROCEDER[VOLVER])
                _opcion_submenu_1 = int(input()) - 1

        printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
        _opcion = int(input()) - 1        

    while(_opcion == 1):
        enter()

        if checkListas(listas_creadas):    
            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
            _opcion_submenu_2 = int(input()) - 1

            while not checkRange(_opcion_submenu_2, rango_submenu_2): 
                enter()

                print(ERR_OPCION_FUERA_DE_RANGO)

                printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
                _opcion_submenu_2 = int(input()) - 1

            while checkRange(_opcion_submenu_2, rango_submenu_2):
                while(_opcion_submenu_2 == 0):
                    enter()

                    print(PGA_OPCION_ANADIR)
                    indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1

                    _lista_seleccionada_para_anadir = int(input()) - 1

                    while not checkRange(_lista_seleccionada_para_anadir, len(nombre_listas_creadas) + 1): 
                        enter()

                        print(ERR_OPCION_FUERA_DE_RANGO)

                        print(PGA_OPCION_ANADIR)
                        indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
                        _lista_seleccionada_para_anadir = int(input()) - 1
                       
                    while checkRange(_lista_seleccionada_para_anadir, len(nombre_listas_creadas) + 1):
                        enter()
                        
                        if (_lista_seleccionada_para_anadir != indice_volver):
                            lista_a_donde_se_anadio = listas_creadas[_lista_seleccionada_para_anadir][0]  

                            _elementos_para_anadir = input(PGA_ELEMENTOS_ANADIR)
                            lista_elementos_para_anadir = _elementos_para_anadir.split(",")

                            enter()

                            for elemento in lista_elementos_para_anadir:
                                listas_creadas[_lista_seleccionada_para_anadir].append(elemento)

                            print(MSJ_EXITO_ANADIR.format(lista_a_donde_se_anadio))
                            enter()
                            break

                        else:
                            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
                            _opcion_submenu_2 = int(input()) - 1 
                            break

                        while not checkRange(_opcion_submenu_2, rango_submenu_2): 
                            enter()

                            print(ERR_OPCION_FUERA_DE_RANGO)

                            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
                            _opcion_submenu_2 = int(input()) - 1

                while(_opcion_submenu_2 == 1):
                    enter()
                    print(PGA_OPCION_ELIMINAR)
                    indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1

                    _lista_seleccionada_para_eliminar = int(input()) - 1

                    if (_lista_seleccionada_para_eliminar != indice_volver):
                        lista_de_donde_se_elimino = listas_creadas[_lista_seleccionada_para_eliminar][0]  
                        enter()

                        print(PGA_ELEMENTOS_ELIMINAR)
                        indice_volver = printOpcionesDeLista(FORMATO_DE_LISTA, listas_creadas[_lista_seleccionada_para_eliminar], MSJS_RETROCEDER[VOLVER]) - 1

                        _elemento_seleccionado_para_eliminar = int(input()) - 1

                        if (_elemento_seleccionado_para_eliminar != indice_volver):
                            enter()

                            elemento_que_fue_eliminado = listas_creadas[_lista_seleccionada_para_eliminar][_elemento_seleccionado_para_eliminar + 1]   # +1 para no borrar el nombre de la lista

                            listas_creadas[_lista_seleccionada_para_eliminar].pop(_elemento_seleccionado_para_eliminar)
                              
                            print(MSJ_EXITO_ELIMINAR.format(elemento_que_fue_eliminado, lista_de_donde_se_elimino))

                        else:
                            break

                    else:
                        enter()
                        printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
                        _opcion_submenu_2 = int(input()) - 1 
                
                if(_opcion_submenu_2 == 2):
                    enter()
                    break   

                while not checkRange(_opcion_submenu_2, rango_submenu_2): 
                    enter()

                    print(ERR_OPCION_FUERA_DE_RANGO)

                    printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_2, MSJS_RETROCEDER[VOLVER])
                    _opcion_submenu_2 = int(input()) - 1 

            printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
            _opcion = int(input()) - 1

        else:
            print(MSJ_NINGUNA_LISTA_CREADA.format(DICC_NINGUNA_LISTA_CREADA[EDITAR]))
            #time.sleep(2)
            enter()           

            printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
            _opcion = int(input()) - 1   

    while(_opcion == 2):
        enter()

        if checkListas(listas_creadas):
            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_3, MSJS_RETROCEDER[VOLVER])
            _opcion_submenu_3 = int(input()) - 1

            while not checkRange(_opcion_submenu_3, rango_submenu_3): 
                enter()

                print(ERR_OPCION_FUERA_DE_RANGO)

                printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_3, MSJS_RETROCEDER[VOLVER])
                _opcion_submenu_3 = int(input()) - 1

            while checkRange(_opcion_submenu_3, rango_submenu_3):
                while(_opcion_submenu_3 == 0):
                    enter()
                    mostrarTodasLasListas(listas_creadas)

                    printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_3, MSJS_RETROCEDER[VOLVER])
                    _opcion_submenu_3 = int(input()) - 1

                while(_opcion_submenu_3 == 1):
                    enter()

                    print(PGA_MOSTRAR_LISTA)
                    indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
                    _opcion_mostrar_lista = int(input()) - 1

                    while not checkRange(_opcion_mostrar_lista, len(nombre_listas_creadas) + 1): 
                        enter()

                        print(ERR_OPCION_FUERA_DE_RANGO)

                        print(PGA_MOSTRAR_LISTA)
                        indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
                        _opcion_mostrar_lista = int(input()) - 1

                    while checkRange(_opcion_mostrar_lista, len(nombre_listas_creadas) + 1): 
                        enter()

                        if (_opcion_mostrar_lista != indice_volver):
                            enter()

                            print(FORMATO_NOMBRE_DE_LISTA.format(nombre_listas_creadas[_opcion_mostrar_lista]))
                            mostrarLista(listas_creadas[_opcion_mostrar_lista], 1)
                            break

                        else:
                            enter()
                            printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_3, MSJS_RETROCEDER[VOLVER])
                            _opcion_submenu_3 = int(input()) - 1 
                            break

                        while not checkRange(_opcion_mostrar_lista, len(nombre_listas_creadas) + 1): 
                            enter()

                            print(ERR_OPCION_FUERA_DE_RANGO)

                            print(PGA_MOSTRAR_LISTA)
                            indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
                            _opcion_mostrar_lista = int(input()) - 1

                if (_opcion_submenu_3 == 2):
                    enter()
                    break

                while not checkRange(_opcion_submenu_3, rango_submenu_3): 
                    enter()

                    print(ERR_OPCION_FUERA_DE_RANGO)

                    printOpciones(FORMATO_DE_LISTA, OPCIONES_SUBMENU_3, MSJS_RETROCEDER[VOLVER])
                    _opcion_submenu_3 = int(input()) - 1 

            printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
            _opcion = int(input()) - 1


        else:
            print(MSJ_NINGUNA_LISTA_CREADA.format(DICC_NINGUNA_LISTA_CREADA[MOSTRAR]))
            enter()

            printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
            _opcion = int(input()) - 1   

    while(_opcion == 3):
        if checkListas(listas_creadas):
            rango_submenu_4 = len(nombre_listas_creadas) + 1

            print(PGA_OPCION_MOSTRAR_ESTADO)
            indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
            _lista_seleccionada_para_mostrar_estado = int(input()) - 1

            while not checkRange(_lista_seleccionada_para_mostrar_estado, rango_submenu_4): 
                enter()

                print(ERR_OPCION_FUERA_DE_RANGO)

                print(PGA_OPCION_MOSTRAR_ESTADO)
                indice_volver = printOpciones(FORMATO_DE_LISTA, nombre_listas_creadas, MSJS_RETROCEDER[VOLVER]) - 1
                _lista_seleccionada_para_mostrar_estado = int(input()) - 1
                    
            if (_lista_seleccionada_para_mostrar_estado != indice_volver):
                if(listas_creadas[_lista_seleccionada_para_mostrar_estado][indice_nombre_de_lista] == DOCTORES):
                    _tipo_de_lista_para_estado = DOCTORES

                elif(listas_creadas[_lista_seleccionada_para_mostrar_estado][indice_nombre_de_lista] == ENFERMEROS):
                    _tipo_de_lista_para_estado = ENFERMEROS

                elif(listas_creadas[_lista_seleccionada_para_mostrar_estado][indice_nombre_de_lista] == PACIENTES):
                    _tipo_de_lista_para_estado = PACIENTES

                else:
                    print(ERR_LISTA_SIN_ESTADO)
                    break

                enter()
                estadoLista(listas_creadas[_lista_seleccionada_para_mostrar_estado], DICC_POSIBLES_ESTADOS[_tipo_de_lista_para_estado], MSJ_ESTADO_ACTUAL)

            else:
                enter()
                printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
                _opcion = int(input()) - 1               
 
    while(_opcion == 4):
        enter()
        print(MSJ_DESPEDIDA)
        exit()

    while not checkRange(_opcion, rango_menu_principal): 
        enter()

        print(ERR_OPCION_FUERA_DE_RANGO)
        printOpciones(FORMATO_DE_LISTA, OPCIONES_MENU_PRINCIPAL, MSJS_RETROCEDER[SALIR])
        _opcion = int(input()) - 1    