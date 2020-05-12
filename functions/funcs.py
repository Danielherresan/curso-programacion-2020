import matplotlib.pyplot as pyplot
import pandas
import os

# ======================================================================================== FUNCTIONS ======================================================================================== #

# --------------------------------------------- General Functions --------------------------------------------- #
def enter():
    print("")
    
def showList(lista):
    for elemento in lista:
        print(elemento)

# ------------------------------------------ Terminal Menu Functions ------------------------------------------ #
def menuLoop(dicionario, funcion_interna, variable_desicion, rango_de_desicion, lista_opciones):

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

# ----------------------------------------------- File Handling ----------------------------------------------- #
def readFile(file_name):
    new_file = open(file_name)
    line_list = new_file.read().splitlines()
    new_file.close()
    return line_list

def writeFile(file_name, line_list):
    split_lines_list = []

    for line in line_list:
        split_lines_list.append(line, "\n")

    new_file =  open(file_name, 'w')
    new_file.writelines(split_lines_list)
    new_file.close()

def appendLines(file_name, line):
    new_file = open(file_name, 'a')
    new_file.write(line)
    new_file.close()
    
# ============================================================================ CSV File Handling ============================================================================ #

def readCSV(file_name):
    file_path = "{}/assets/csv/{}".format(os.getcwd(), file_name)
    file_dicctionary = pandas.read_csv(file_path, encoding='UTF-8', header = 0, delimiter=';').to_dict()
    return file_dicctionary

def minCSV(file_dict, key_name, key_arg):
    min_var = ""

    if (key_arg == "length"):    
        min_var = min(file_dict[key_name].values(), key=len)
    else:
        min_var = min(file_dict[key_name].values())

    return min_var
    
def maxCSV(file_dict, key_name, key_arg):
    max_var = ""

    if (key_arg == "length"):    
        max_var = max(file_dict[key_name].values(), key=len)
    else:
        max_var = max(file_dict[key_name].values())

    return max_var

# ================================================================================== PIPLOT ================================================================================== #

def makePlot(file, type = "plot", title = "title", x_axis = ["label", None], y_axis = ["label", None], file_name = "plot", rotate_x_ticks = False, **kwargs):
    # Generate the output folder for this file
    file_directory_name = os.path.basename(file).replace(".py", "")
    output_path = "{}/output/{}/".format(os.getcwd(), file_directory_name)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if (type == "pie"):
        labels = []
        sizes = []
        explode = []

        for i in range(len(kwargs["pie_sections"])):
            labels.append(kwargs["pie_sections"][i]["name"])
            sizes.append(kwargs["pie_sections"][i]["size"])
            explode.append(kwargs["pie_sections"][i]["explode"])

        pyplot.pie(
            sizes,
            explode = explode,
            labels = labels,
            shadow = False,
            startangle = 0
        )

    else:
        pyplot.xlabel(x_axis[0])
        pyplot.ylabel(y_axis[0])

    if (type == "plot"):
        pyplot.plot( x_axis[1], y_axis[1])

    elif (type == "bar"):
        pyplot.bar(x_axis[1], y_axis[1])

    elif (type == "barh"):
        pyplot.barh( x_axis[1], y_axis[1])

    elif (type == "multiple"):
        for i in range(len(y_axis) - 1):
            pyplot.plot(x_axis[1], y_axis[i + 1])

        pyplot.legend(kwargs["legend"])

    if (rotate_x_ticks):
        pyplot.xticks(rotation=90)

    pyplot.title(title)

    # Check if the size argument was given
    try:
        figure = pyplot.gcf()
        figure.set_size_inches(kwargs["size"])
    except (KeyError):
        pass

    # save
    pyplot.savefig(output_path + file_name + ".png")

    # Check to show
    try:
        if(kwargs["show"]):
            pyplot.show()
    except (KeyError):
        pass

    pyplot.close()

# --------------------------------------------- Templates --------------------------------------------- #

# PLOT #
"""
makePlot(
    file=__file__,
    type="plot",
    title="ECG",
    file_name="ECG",
    rotate_x_ticks=False,
    show=True,
    x_axis = [
        "Tiempo(ms)",
        list(ecg["muestra"].values())
    ],
    y_axis = [
        "Volataje(uV)",
        list(ecg["valor"].values())
    ]
)
"""

# PIE #
"""
makePlot(
    file=__file__,
    type="pie",
    title="Grafico Pie",
    file_name="Grafico Pie",
    pie_sections= [
        {
            "name": "Bogota",
            "size": 80,
            "explode": 0
        },
        {
            "name": "Medellin",
            "size": 7,
            "explode": 0
        },
        {
            "name": "Leticia",
            "size": 5,
            "explode": 0.1
        },
        {
            "name": "Villavicencio",
            "size": 8,
            "explode": 0
        }
    ]
)
"""

# BAR #
"""
makePlot(
    file=__file__,
    type="bar",
    title="Barrios vs Agua",
    file_name="Barrios vs Agua",
    rotate_x_ticks=True,
    size=[7,12],
    x_axis = [
        "Barrios",
        list(barrios["Barrio"].values())
    ],
    y_axis = [
        "Agua",
        list(barrios["Agua"].values())
    ]
)
"""

# MULTIPLE #
"""
makePlot(
    file=__file__,
    type="multiple",
    title="multiple chart",
    file_name="multiple",
    rotate_x_ticks=True,
    size=[7,7],
    legend=[
            "Dolar en Pesos colombianos",
            "Dola en Soles",
            "Dolar en pesos mexicanos"
    ],
    x_axis = [
        "Año",
        year
    ],
    y_axis = [
        "Valor del dolar en pesos colombianos",
        dolar_pesos_colombianos,
        dolar_soles,
        dolar_mexico
    ]
)
"""