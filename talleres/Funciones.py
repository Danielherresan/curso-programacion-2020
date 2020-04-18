import time

# FUNCIONES
def enter():
    print("")
    #time.sleep(0.3)

def whileLoop(dicionario, funcion_interna, variable_desicion, rango_de_desicion, lista_opciones):

    def CheckRange(variable_desicion, rango_de_desicion, mensaje_error_rango):
        if (variable_desicion in range(1, rango_de_desicion)):
            return True
        else:
            print(mensaje_error_rango)
            return False

    def showMenu(dicionario, lista_opciones, variable_desicion):
        for i in range(len(lista_opciones)):
            print(dicionario['FORMATO'].format(i+1, lista_opciones[i]))
            indice_opcion_de_volver = i + 2

        print(dicionario['FORMATO'].format(indice_opcion_de_volver, dicionario['VOLVER']))

        enter()

        variable_desicion = int(input()) 
        return variable_desicion

    variable_desicion = showMenu(dicionario, lista_opciones, variable_desicion)

    while not CheckRange(variable_desicion, rango_de_desicion, dicionario['FUERA DE RANGO']):
        variable_desicion = showMenu(dicionario, lista_opciones, variable_desicion)

    while (variable_desicion in range(1, rango_de_desicion)):
        funcion_interna(variable_desicion)
        variable_desicion = showMenu(dicionario, lista_opciones, variable_desicion)

        while not CheckRange(variable_desicion, rango_de_desicion, dicionario['FUERA DE RANGO']):
            variable_desicion = showMenu(dicionario, lista_opciones, variable_desicion)

    return(funcion_interna)

def showList(lista):
    for elemento in lista:
        print(elemento)

def readFile(file_name):
    new_file = open(file_name)
    line_list = new_file.read().splitlines()
    new_file.close()
    return line_list

def writeFile(file_name, line_list):
    split_lines_list = []

    for line in line_list:
        corrected_line = line + "\n"
        split_lines_list.append(corrected_line)

    new_file =  open(file_name, 'w')
    new_file.writelines(split_lines_list)
    new_file.close()

def appendLines(file_name, line):
    corrected_line = "\n" + line
    new_file = open(file_name, 'a')
    new_file.write(corrected_line)
    new_file.close()
    