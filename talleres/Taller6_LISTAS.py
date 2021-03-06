from Funciones import showList, whileLoop

DICIONARIO_MENSAJES = {
    'FUERA DE RANGO': "El número ingresado no corresponde a una función de este programa, por favor intetalo de nuevo.\n",
    'FORMATO': "{} - {}",
    'VOLVER': "Salir"
}

PGA_NUEVO_PACIENTE = "¿ha ingresado algún paciente nuevo el dia de hoy?"
PGA_EDAD = "Ingrese la edad del nuevo paciente:"
EDADES_HOY = "Las edades de los pacientes ingresados el dia de hoy son:"
TODAS_EDADES = "y esta es la lista de todas las edades de los pacientes:"
DEMAS_DATOS = "el paciente mas longevo tiene {} años y el mas joven tiene {} años."
ASCENDENTE = "Lista en orden asendente:\n"
DESCENDENTE = "Lista en orden descendente:\n"
AUXILIAR = "la auxiliar la popoció:\n"
ADIOS_PACIENTE = "Un paciente se fue:\n"

listaEdades = [1,2,4,8,16,32,64]
_decision = 0
_edad_nuevo_paciente = ""
opciones_nuevo_paciente = ["Si", "No"]
rango_opciones_nuevo_paciente = 2 + len(opciones_nuevo_paciente)
lista_edades_nuevas = []

def ingresarEdadNuevoPaciente(_edad_nuevo_paciente):
    _edad_nuevo_paciente = int(input(PGA_EDAD))
    lista_edades_nuevas.append(_edad_nuevo_paciente)
    listaEdades.append(_edad_nuevo_paciente)

def preguntarPorNuevosPacientes(_input):
    if (_input == 1):
        ingresarEdadNuevoPaciente(_edad_nuevo_paciente)
    elif (_input == 2):
        lista_ordenada = listaEdades.copy()

        print(EDADES_HOY)
        showList(lista_edades_nuevas)

        print(TODAS_EDADES)
        showList(listaEdades)

        print(DEMAS_DATOS.format(max(listaEdades), min(listaEdades)))

        print(ASCENDENTE)
        lista_ordenada.sort()
        showList(lista_ordenada)

        print(DESCENDENTE)
        lista_ordenada.sort(reverse = True)
        showList(lista_ordenada)

        print(AUXILIAR)
        listaEdades.insert(4, 87)
        showList(listaEdades)

        print(ADIOS_PACIENTE)
        listaEdades.pop(6)
        showList(listaEdades)

        exit()
    else:
        exit()



print(PGA_NUEVO_PACIENTE)
whileLoop(DICIONARIO_MENSAJES, preguntarPorNuevosPacientes, _decision, rango_opciones_nuevo_paciente, opciones_nuevo_paciente)