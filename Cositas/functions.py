import random

def whileLoop(dicionario, funcion_interna, variable_desicion, rango_de_desicion, lista_opciones):

    def CheckRange(variable_desicion, rango_de_desicion, mensaje_error_rango):
        if (variable_desicion in range(1, rango_de_desicion)):
            return True
        else:
            print(mensaje_error_rango)
            return False

    def mostrarMenu(dicionario, lista_opciones, variable_desicion):
        for i in range(len(lista_opciones)):
            print(dicionario['FORMATO'].format(i+1, lista_opciones[i]))
            indice_opcion_de_volver = i + 2

        print(dicionario['FORMATO'].format(indice_opcion_de_volver, dicionario['VOLVER']))
        variable_desicion = int(input()) 
        return variable_desicion


    variable_desicion = mostrarMenu(dicionario, lista_opciones, variable_desicion)

    while not CheckRange(variable_desicion, rango_de_desicion, dicionario['FUERA DE RANGO']):
        variable_desicion = mostrarMenu(dicionario, lista_opciones, variable_desicion)

    while (variable_desicion in range(1, rango_de_desicion)):

        funcion_interna(variable_desicion)
        variable_desicion = mostrarMenu(dicionario, lista_opciones, variable_desicion)

        while not CheckRange(variable_desicion, rango_de_desicion, dicionario['FUERA DE RANGO']):
            variable_desicion = mostrarMenu(dicionario, lista_opciones, variable_desicion)

def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return (d1, d2)