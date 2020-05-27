import os
import sys

# esto es para que reconosca el archivo de funciones
sys.path.append(os.getcwd() + "/functions/")
from funcs import readCSV, makePlot

from tkinter import *
from tkinter import messagebox

# ==================================================================================== MESSAGES ==================================================================================== #
WINDOW_TITLES = {
    "mainMenu": "Taller Final",
    "optionsWindow": "Opciones de la grafica"
}

EMPY_AXIS_VALUE = "Ingresa un valor para los ejes de la gráfica."
KEY_NOT_FOUND = "La llave {} no fue encontrada en el archivo {}."

VALUE_ERROR_MESSAGEBOX_TITLE = "Error de valor"
SECTIONS_ERROR_MESSAGEBOX_TITLE = "Error secciones de la gráfica"
KEY_ERROR_MESSAGEBOX_TITLE = "Error de llave"

MULTIPLE_INFO_MESSAGEBOX_TITLE = "Multiples valores de Y"

SECTIONS_ERROR_MESSAGEBOX_MESSAGE = "El número de elementos en las diferentes secciones no concuerda, por favor verifica nuevamente."

MULTIPLE_INFO_MESSAGEBOX_MESSAGE = "Si deseas crear una grafica con multiples valores en el eje Y debes seleccionar 'Multiple' como tipo de grafica."

WINDOW_GEOMETRY = {
    "mainMenu": "250x240",
    "opinionTopLevel": "667x140"
}

EXCEPTION_VARS = {
    "section_size": "El tamaño de las secciones",
    "explode": "El nivel de explosión de las secciones"
}

NOT_ENOUGH_EXCEPTION = {
    "description": "not enough values",
    "message": "Es necesario ingresar tanto el valor del ancho como el de la altura, pero solo ingresaste {} valor."
}

TOO_MANY_EXCEPTION = {
    "description": "too many values",
    "message": "Solo es necesario ingresar el valor del ancho y el de la altura, pero ingresaste {} valores."
}

INT_VALUE_ERROR_EXCEPTION = {
    "message": "{} debe ser un valor de número entero, no un {}."
}

FLOAT_VALUE_ERROR_EXCEPTION = {
    "message": "{} debe ser un valor de número decimal, no un {}."
}

FILE_OPTION_LABELS = [
    "Archivo",
    "Nombre del archivo: ",
    "Titulo de la grafica: "
] 

PIE_OPTION_LABELS = [
    "Secciones",
    "Separadas por comas (,)",
    "Nombres de las secciones: ",
    "Tamaño de las secciones (%): ",
    "Explotar secciones: "
] 

REGULAR_OPTION_LABELS = [
    "Ejes de la grafica",
    "Nombres",
    "Nombre del eje X: ",
    "Nombre del eje Y: ",
    "Valores (campo del csv)",
    "Valor del eje X: ",
    "Valor(es) del eje Y: "
]

OTHER_OPTION_LABELS = [
    "Otros (Opcional)",
    "Tamaño en pulgadas (altura, ancho): ",
    "Rotar ticks de X: ",
    "Grafico horizontal: "
] 

PROTOCOLS = {
    "close": "WM_DELETE_WINDOW"
}

FONTS = [
    ("Arial", 14), # Title
    ("Arial", 12), # SubTitle
    ("Arial"), # Text
]

def onClose(parentWindow, childWindow):
    parentWindow.deiconify()
    childWindow.destroy()

def showAsPopup(parent, child):
    parent.withdraw()
    child.protocol(PROTOCOLS["close"], lambda: onClose(parent, child))

def createPlot(plot_type, plot_title, file_name, rotate_ticks, x_axis, y_axis, **kwargs):
    try:
        if (kwargs["sections"] != []):
            makePlot(
                file = __file__,
                type = plot_type,
                title = plot_title,
                file_name = file_name,
                show=True,
                rotate_x_ticks = rotate_ticks,
                size = kwargs["file_size"],
                pie_sections= kwargs["sections"]
            )
        else:
            makePlot(
                file = __file__,
                type = plot_type,
                title = plot_title,
                file_name = file_name,
                show=True,
                rotate_x_ticks = rotate_ticks,
                size = kwargs["file_size"],
                legend = kwargs["legend"],
                x_axis = x_axis,
                y_axis = y_axis
            )
    except ValueError as e:
        exception_string = str(e)
        
        if (NOT_ENOUGH_EXCEPTION["description"] in exception_string):
            message = NOT_ENOUGH_EXCEPTION["message"].format(len(kwargs["file_size"]))

        elif (TOO_MANY_EXCEPTION["description"] in exception_string):
            message = TOO_MANY_EXCEPTION["message"].format(len(kwargs["file_size"]))

        else:
            message = exception_string

        messagebox.showerror(ERROR_MESSAGEBOX_TITLES["createPlot"], message)
        return False

def makeInputs(parent, layout):
    for element in range(len(layout)):
        element_type = layout[element][0]

        if (element_type == "title"):
            Label(parent, text=layout[element][1], font =FONTS[0]).grid(row=element, column=0, columnspan=2 ,padx=14, pady=6)

        elif (element_type == "subTitle"):
            Label(parent, text=layout[element][1], font =FONTS[1]).grid(row=element, column=0, columnspan=2 ,padx=14, pady=6)

        elif (element_type == "entry"):
            Label(parent, text=layout[element][1], font =FONTS[2]).grid(row=element, column=0, sticky=W, padx=14, pady=6)
            Entry(parent, width=40, textvariable=layout[element][2], font =FONTS[2]).grid(row=element, column=1, sticky=W, padx=14, pady=6)

        else:
            Label(parent, text=layout[element][1], font =FONTS[2]).grid(row=element, column=0, sticky=W, padx=14, pady=6)
            Checkbutton(parent, onvalue=True, offvalue=False, variable=layout[element][2]).grid(row=element, column=1, sticky=W, padx=14, pady=6)

def optionsWindow(csv, file_name, plot_type, parent):
    optionsTopLevel = Toplevel(parent)
    optionsTopLevel.wm_title(WINDOW_TITLES["optionsWindow"])

    showAsPopup(parent, optionsTopLevel)

    _save_name = StringVar()
    _plot_title = StringVar()
    _section_name = StringVar()
    _section_size = StringVar()
    _section_explode = StringVar()
    _x_name = StringVar()
    _y_name = StringVar()
    _x_value = StringVar()
    _y_value = StringVar()
    _graph_size = StringVar()
    _rotate_ticks = BooleanVar()
    _rotate_graph = BooleanVar()

    complete_layout = []

    file_options = [
        ["title", FILE_OPTION_LABELS[0]],
        ["entry", FILE_OPTION_LABELS[1], _save_name],
        ["entry", FILE_OPTION_LABELS[2], _plot_title]
    ]

    pie_specific_options = [
        ["title", PIE_OPTION_LABELS[0]],
        ["subTitle", PIE_OPTION_LABELS[1]],
        ["entry", PIE_OPTION_LABELS[2], _section_name],
        ["entry", PIE_OPTION_LABELS[3], _section_size],
        ["entry", PIE_OPTION_LABELS[4], _section_explode]
    ]

    regular_options = [
        ["title", REGULAR_OPTION_LABELS[0]],
        ["subTitle", REGULAR_OPTION_LABELS[1]],
        ["entry", REGULAR_OPTION_LABELS[2], _x_name],
        ["entry", REGULAR_OPTION_LABELS[3], _y_name],
        ["subTitle", REGULAR_OPTION_LABELS[4]],
        ["entry", REGULAR_OPTION_LABELS[5], _x_value],
        ["entry", REGULAR_OPTION_LABELS[6], _y_value]
    ]

    other_options = [
        ["title", OTHER_OPTION_LABELS[0]],
        ["entry", OTHER_OPTION_LABELS[1], _graph_size],
        ["checkBox", OTHER_OPTION_LABELS[2], _rotate_ticks]
    ]

    rotate_graph_option = ["checkBox", OTHER_OPTION_LABELS[3], _rotate_graph]

    if (plot_type == "pie"):
        type_specific_options = pie_specific_options

    elif (plot_type == "bar"):
        type_specific_options = regular_options
        other_options.append(rotate_graph_option)

    else:
        type_specific_options = regular_options

    complete_layout = file_options + type_specific_options + other_options

    makeInputs(optionsTopLevel, complete_layout)
    

    def verifyInputs():
        graph_size_elements = _graph_size.get().split(",")
        y_value_elements = _y_value.get().split(",")
        section_element_names = _section_name.get().split(",")
        section_element_sizes = _section_size.get().split(",")
        section_elements_explode = _section_explode.get().split(",")

        save_name = _save_name.get()
        plot_title = _plot_title.get()
        rotate_ticks = _rotate_ticks.get()
        rotate_graph = _rotate_graph.get()

        size = []
        sections = []
        x_axis = []
        y_axis = []

        if (rotate_graph):
            real_plot_type = "barh"
        else:
            real_plot_type = plot_type

        if (save_name == ""):
            save_name = file_name

        for element in graph_size_elements:
            if (element != ""):
                size.append(int(element))
        
        if (real_plot_type == "pie"):
            if (len(section_element_names) == len(section_element_sizes) and len(section_element_sizes) == len(section_elements_explode)):
                for element in range(len(section_element_names)):
                    try:
                        sections.append({
                            "name": section_element_names[element],
                            "size": int(section_element_sizes[element]),
                            "explode": float(section_elements_explode[element])
                        })

                    except ValueError as e:
                        exception_string = str(e)

                        if ("int" in exception_string):
                            message = INT_VALUE_ERROR_EXCEPTION["message"].format(EXCEPTION_VARS["section_size"], type(section_element_sizes[element]).__name__)

                        elif ("float" in exception_string):
                            message = FLOAT_VALUE_ERROR_EXCEPTION["message"].format(EXCEPTION_VARS["explode"], type(section_element_sizes[element]).__name__)
                            
                        messagebox.showerror(VALUE_ERROR_MESSAGEBOX_TITLE, message)
                        return False
            
            else:
                messagebox.showerror(SECTIONS_ERROR_MESSAGEBOX_TITLE, SECTIONS_ERROR_MESSAGEBOX_MESSAGE)
                return False

        else:
            try:
                x_axis = [
                    _x_name.get(),
                    list(csv[_x_value.get()].values())
                ]

                y_axis = [
                    _y_name.get()
                ]

                for element in y_value_elements:
                    y_axis.append(list(csv[element].values()))

                if (plot_type != "multiple"):
                    if (len(y_axis) > 2):
                        messagebox.showinfo(MULTIPLE_INFO_MESSAGEBOX_TITLE, MULTIPLE_INFO_MESSAGEBOX_MESSAGE)
            
            except KeyError as e:
                exception_string = str(e)

                if (_x_value.get() == "" or _y_value.get() == ""):
                    message = EMPY_AXIS_VALUE

                else:
                    message = KEY_NOT_FOUND.format(exception_string, file_name)

                messagebox.showerror(KEY_ERROR_MESSAGEBOX_TITLE, message)
                return False

        createPlot(
            real_plot_type,
            plot_title,
            save_name,
            rotate_ticks,
            x_axis,
            y_axis,
            legend=y_value_elements,
            file_size=size,
            sections=sections
        )

    Button(optionsTopLevel, text="Aceptar", width=34, command=verifyInputs).grid(row=16, column=1, columnspan=2, pady=16)

def typeWindow(csv, file_name, parent):
    typeTopLevel = Toplevel(parent)
    typeTopLevel.wm_title("Tipo de grafica")

    showAsPopup(parent, typeTopLevel)

    Label(typeTopLevel, text="Selecciona el tipo de gráfica",font=FONTS[0]).grid(row=0, column=1, columnspan=2, padx=4, pady=4)
    
    Button(typeTopLevel, image = BlankBarImage, command=lambda: optionsWindow(csv, file_name, "bar", typeTopLevel)).grid(row=1, column=1, padx=14, pady=14)
    Button(typeTopLevel, image = BlankMultipleImage, command=lambda: optionsWindow(csv, file_name, "multiple", typeTopLevel)).grid(row=1, column=2, padx=14, pady=14)

    Label(typeTopLevel, text="Gráfico de Barras").grid(row=2, column=1, padx=4, pady=4)
    Label(typeTopLevel, text="Gráfico Multiple").grid(row=2, column=2, padx=4, pady=4)

    Button(typeTopLevel, image = BlankPieImage, command=lambda: optionsWindow(csv, file_name, "pie", typeTopLevel)).grid(row=3, column=1, padx=14, pady=14)
    Button(typeTopLevel, image = BlankPlotImage, command=lambda: optionsWindow(csv, file_name, "plot", typeTopLevel)).grid(row=3, column=2, padx=14, pady=14)

    Label(typeTopLevel, text="Gráfico de Pie").grid(row=4, column=1, padx=4, pady=4)
    Label(typeTopLevel, text="Gráfico de Lineas").grid(row=4, column=2, padx=4, pady=4)

def continueButtonCommand(file_name, parent):
    try:
        csv = readCSV(file_name)
        typeWindow(csv, file_name, parent)

    except FileNotFoundError:
        if (".csv" in file_name):
            message = "No incluyas el formato (.csv) en el nombre del archivo."

        else:
            message = "Verifica que el nombre del archivo es correcto, y si esta en la carpeta indicada."

        messagebox.showerror("Archivo no encontrado", message)

def graphGenerator(parent):
    generatorTopLevel = Toplevel(parent)
    generatorTopLevel.wm_title("Generador de Graficas")
    generatorTopLevel.geometry("420x180")

    showAsPopup(parent, generatorTopLevel)

    file_name = StringVar()

    Label(generatorTopLevel, text = "Por favor ingresa el nombre del archivo que deseas graficar", font =("Arial", 11)).pack(padx = 12, pady = 12) 
    Entry(generatorTopLevel, font =("Arial", 11), textvariable=file_name).pack(pady = 3)
    
    Button(generatorTopLevel, text="Continuar", command=lambda: continueButtonCommand(file_name.get(), generatorTopLevel)).pack(pady = 3)

    Label(generatorTopLevel, text = "Recuerda que el archivo debe estar ubicado\ndentro de ../assets/csv", font =("Arial", 11)).pack(padx = 12, pady = 12)

def showBMI(name, age, weight, height):
    try:
        bmi = weight / (height**2)
    except ZeroDivisionError:
        messagebox.showerror("Division por cero", "A menos que quieras implementar la ley de L'Hopital, nada de dividir por cero.")

    if (16 > bmi >= 0):
        category = "delgadez Severa"
    elif (17 > bmi >= 16):
        category = "delgadez moderada"
    elif (18.5 > bmi >= 17):
        category = "delgadez aceptable"
    elif (25 > bmi >= 18.5):
        category = "peso Normal"
    elif (30 > bmi >= 25):
        category = "sobrepeso"
    elif (35 > bmi >= 30):
        category = "obesidad tipo I"
    elif (40 > bmi >= 35):
        category = "obesidad tipo II"
    else:
        category = "obesidad tipo III"

    messagebox.showinfo("Tu IMC actual", "{}, en este momento te encuentras en un IMC de {}, lo cual te pone en el rango de {}.".format(name, round(bmi,2), category))

def bmi(parent):
    bmiTopLevel = Toplevel(parent)
    bmiTopLevel.wm_title("Calculadora de IMC")

    showAsPopup(parent, bmiTopLevel)

    _name = StringVar()
    _age = StringVar()
    _weight = StringVar()
    _height = StringVar()


    Label(bmiTopLevel, text="Ingresa tus datos", font =FONTS[0]).grid(row=0, column=1, columnspan=2 ,padx=14, pady=6)

    Label(bmiTopLevel, text="Nombre: ").grid(row=1,column=1, sticky=W, padx=14, pady=6)
    Entry(bmiTopLevel, width=40, textvariable=_name).grid(row=1, column=2, sticky=W, padx=14, pady=6)

    Label(bmiTopLevel, text="Edad: ").grid(row=2,column=1, sticky=W, padx=14, pady=6)
    Entry(bmiTopLevel, width=40, textvariable=_age).grid(row=2, column=2, sticky=W, padx=14, pady=6)

    Label(bmiTopLevel, text="Peso (kg): ").grid(row=3,column=1, sticky=W, padx=14, pady=6)
    Entry(bmiTopLevel, width=40, textvariable=_weight).grid(row=3, column=2, sticky=W, padx=14, pady=6)

    Label(bmiTopLevel, text="Altura (m): ").grid(row=4,column=1, sticky=W, padx=14, pady=6)
    Entry(bmiTopLevel, width=40, textvariable=_height).grid(row=4, column=2, sticky=W, padx=14, pady=6)

    def verifyInputs():
        try:
            name = _name.get()
            age = int(_age.get())
            weight = float(_weight.get())
            height = float(_height.get())

        except ValueError as e:
            exception_string = str(e)

            if ("int" in exception_string):
                message = "Tu edad debe ser un número entero."

            else:
                message = "Tu peso y altura deben ser un número entero o decimal."

            messagebox.showerror("Error tipo de variable", message)
            return False

        if (weight < 0):
            messagebox.showerror("Error peso negativo", "Dudo mucho que seas un agujero de gusano.")
            return False

        showBMI(name, age, weight, height)

    Button(bmiTopLevel, text="Continuar", width=34, command=verifyInputs).grid(row=5, column=1, columnspan=2, pady=16)

def showcompare(arroz, lentejas, frijoles, papa):
    names = ["arroz", "lentejas", "frijoles", "papa"]
    items = [arroz, lentejas, frijoles, papa]
    
    makePlot(
        file=__file__,
        type="bar",
        title="Inventario",
        file_name="Inventario",
        show=True,
        x_axis = [
            "Elemento",
            names
        ],
        y_axis = [   
            "Cantidad en Kg",
            items
        ]
    )

def comparePeaks():
    graphs = ["PPG", "ECG", "EEG"]
    peaks = [9,9,10]

    makePlot(
        file=__file__,
        type="bar",
        title="Picos en las graficas",
        file_name="picos",
        show=True,
        x_axis = [
            "Grafica",
            graphs
        ],
        y_axis = [   
            "Picos",
            peaks
        ]
    )
        

def feelings(parent):
    feelingsTopLevel = Toplevel(parent)
    feelingsTopLevel.wm_title("Sentimientos")

    showAsPopup(parent, feelingsTopLevel)

    _text = StringVar()

    Label(feelingsTopLevel, text="Cuentame como te has sentido", font =FONTS[0]).grid(row=0, column=1, columnspan=2 ,padx=14, pady=6)
    Entry(feelingsTopLevel, width=60, textvariable=_text).grid(row=1, column=1, padx=14, pady=6)

    def verifyInputs():
        feeling = _text.get()

        if not (feeling.endswith(".")):
            messagebox.showerror("Error de ortografia", "Recuerda simpre terminar tus parrafos en '.'")
            return False

        messagebox.showinfo("Sentimientos", "No se que escribiste pero quiero que sepas que te aprecio y comprendo.")
        onClose(parent, feelingsTopLevel)

    Button(feelingsTopLevel, text="Continuar", width=34, command=verifyInputs).grid(row=5, column=1, columnspan=2, pady=16)

def showSites():
    makePlot(
        file=__file__,
        type="pie",
        title="Tiempo en habitaciones",
        file_name="habitaciones",
        show=True,
        pie_sections= [
            {
                "name": "Habitación",
                "size": 70,
                "explode": 0.1
            },
            {
                "name": "Terraza",
                "size": 12,
                "explode": 0
            },
            {
                "name": "acera",
                "size": 8,
                "explode": 0
            },
            {
                "name": "Cocina",
                "size": 6,
                "explode": 0
            },
            {
                "name": "Baño",
                "size": 4,
                "explode": 0
            }
        ]
    )

def myOpinion(parent):
    messagebox.showwarning("Atención", "Lo siguiente es mi opinióm propia y personal.")

    opinionTopLevel = Toplevel(parent)
    opinionTopLevel.wm_title("Aprendizajes")
    opinionTopLevel.geometry(WINDOW_GEOMETRY["opinionTopLevel"])

    showAsPopup(parent, opinionTopLevel)

    opinion = "En mi opinion una gran parte de lo que es el aprendizaje es la disposición de la persona a la que se le estas enseñando. Si una persona no está interesada en el tema, no importa si se le respira en la nuca, lo único que se va a lograr es que haga entrega de trabajos y actividades solo por hacerlas y sion pensar. Por eso yo creeria que la importacia no esta en supervisar o no supervisar, sino en asegurarse de hacer todos los temas, actividades, talleres, examenes, etc. Despierten la curiosidad y pasión en los estudiantes y que además sean interesantes."

    text_box = Text(opinionTopLevel, padx=12, pady=12)
    text_box.insert("1.0", opinion)
    text_box.grid(sticky=W)



def createButtons(parent, button_object):
    for button_index in range(len(button_object)):
        Button(parent, text=button_object[button_index][0], width=21, command=button_object[button_index][1]).pack(padx = 4, pady=4)

def mainMenu(parent):
    parent.wm_title(WINDOW_TITLES["mainMenu"])
    parent.geometry(WINDOW_GEOMETRY["mainMenu"])

    Label(parent, text = "¿Qué quieres hacer?", font =("Arial", 11)).pack(padx = 12, pady = 12) 
    
    buttons = [
        ["Graficar", lambda: graphGenerator(parent)],
        ["Calcular IMC", lambda: bmi(parent)],
        ["Comparación de Picos", comparePeaks],
        ["Tiempo en habitaciones", showSites],
        ["Diferencias de aprendizajes", lambda: myOpinion(parent)]
    ]

    createButtons(parent, buttons)

    parent.mainloop() 

root = Tk()

BlankBarImage = PhotoImage(file = os.getcwd() + "/assets/images/BlankBar.png").subsample(2, 2)
BlankBarHImage = PhotoImage(file = os.getcwd() + "/assets/images/BlankBarH.png").subsample(2, 2)
BlankMultipleImage = PhotoImage(file = os.getcwd() + "/assets/images/BlankMultiple.png").subsample(2, 2)
BlankPieImage = PhotoImage(file = os.getcwd() + "/assets/images/BlankPie.png").subsample(2, 2)
BlankPlotImage = PhotoImage(file = os.getcwd() + "/assets/images/BlankPlot.png").subsample(2, 2)

mainMenu(root)