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

ERROR_MESSAGEBOX_TITLES = {
    "createPlot": "Error de valor"
}

WINDOW_GEOMETRY = {
    "mainMenu": "250x240"
}


NOT_ENOUGH_EXCEPTION = {
    "description": "not enough values",
    "message": "Es necesario ingresar tanto el valor del ancho como el de la altura, pero solo ingresaste {} valor."
}

TOO_MANY_EXCEPTION = {
    "description": "too many values",
    "message": "Solo es necesario ingresar el valor del ancho y el de la altura, pero ingresaste {} valores."
}

def onClose(parentWindow, childWindow):
    parentWindow.deiconify()
    childWindow.destroy()

def showAsPopup(parent, child):
    parent.withdraw()
    child.protocol("WM_DELETE_WINDOW", lambda: onClose(parent, child))

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

    Label(optionsTopLevel, text="Archivo", font =("Arial", 14)).grid(row=1, column=1, columnspan=2 ,padx=14, pady=6)

    Label(optionsTopLevel, text="Nombre del archivo: ").grid(row=2,column=1, sticky=W, padx=14, pady=6)
    Entry(optionsTopLevel, width=40, textvariable=_save_name).grid(row=2, column=2, sticky=W, padx=14, pady=6)

    Label(optionsTopLevel, text="Titulo de la grafica: ").grid(row=3,column=1, sticky=W, padx=14, pady=6)
    Entry(optionsTopLevel, width=40, textvariable=_plot_title).grid(row=3, column=2, sticky=W, padx=14, pady=6)

    if (plot_type == "pie"):
        Label(optionsTopLevel, text="Secciones de la grafica", font =("Arial", 14)).grid(row=4, column=1, columnspan=2 ,padx=14, pady=6)
        Label(optionsTopLevel, text="separadas por comas (,)", font =("Arial", 12)).grid(row=5, column=1, columnspan=2 ,padx=14, pady=6)

        Label(optionsTopLevel, text="Nombres de las secciones: ").grid(row=6,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_section_name).grid(row=6, column=2, sticky=W, padx=14, pady=6)

        Label(optionsTopLevel, text="Tamaño de las secciones (%): ").grid(row=7,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_section_size).grid(row=7, column=2, sticky=W, padx=14, pady=6)

        Label(optionsTopLevel, text="Explotar secciones: ").grid(row=8,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_section_explode).grid(row=8, column=2, sticky=W, padx=14, pady=6)

    else:
        Label(optionsTopLevel, text="Ejes de la grafica", font =("Arial", 14)).grid(row=4, column=1, columnspan=2 ,padx=14, pady=6)
        Label(optionsTopLevel, text="Nombres", font =("Arial", 12)).grid(row=5, column=1, columnspan=2 ,padx=14, pady=6)

        Label(optionsTopLevel, text="Nombre del eje X: ").grid(row=6,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_x_name).grid(row=6, column=2, sticky=W, padx=14, pady=6)

        Label(optionsTopLevel, text="Nombre del eje Y: ").grid(row=7,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_y_name).grid(row=7, column=2, sticky=W, padx=14, pady=6)

        Label(optionsTopLevel, text="Valores", font =("Arial", 12)).grid(row=8, column=1, columnspan=2 ,padx=14, pady=6)
        Label(optionsTopLevel, text="Ingresa el nombre del campo del csv", font =("Arial", 10)).grid(row=9, column=1, columnspan=2 ,padx=14, pady=6)

        Label(optionsTopLevel, text="Valor del eje X: ").grid(row=10,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_x_value).grid(row=10, column=2, sticky=W, padx=14, pady=6)

        Label(optionsTopLevel, text="Valor(es) del eje Y: ").grid(row=11,column=1, sticky=W, padx=14, pady=6)
        Entry(optionsTopLevel, width=40, textvariable=_y_value).grid(row=11, column=2, sticky=W, padx=14, pady=6)

    Label(optionsTopLevel, text="Otros (Opcional)", font =("Arial", 14)).grid(row=12, column=1, columnspan=2 ,padx=14, pady=6)

    Label(optionsTopLevel, text="Tamaño en pulgadas (altura, ancho): ").grid(row=13,column=1, sticky=W, padx=14, pady=6)
    Entry(optionsTopLevel, width=40, textvariable=_graph_size).grid(row=13, column=2, sticky=W, padx=14, pady=6)

    Label(optionsTopLevel, text="Rotar ticks de X: ").grid(row=14,column=1, sticky=W, padx=14, pady=6)
    Checkbutton(optionsTopLevel, onvalue=True, offvalue=False, variable=_rotate_ticks).grid(row=14, column=2, sticky=W, padx=14, pady=6)

    if (plot_type == "bar"):
        Label(optionsTopLevel, text="Grafico horizontal: ").grid(row=15,column=1, sticky=W, padx=14, pady=6)
        Checkbutton(optionsTopLevel, onvalue=True, offvalue=False, variable=_rotate_graph).grid(row=15, column=2, sticky=W, padx=14, pady=6)

    def setOptions(plot_type):
        graph_size_elements = _graph_size.get().split(",")
        y_value_elements = _y_value.get().split(",")
        section_element_names = _section_name.get().split(",")
        section_element_sizes = _section_size.get().split(",")
        section_elements_explode = _section_explode.get().split(",")

        size = []
        sections = []
        x_axis = []
        y_axis = []

        plot_title = _plot_title.get()
        rotate_ticks = _rotate_ticks.get()

        if (_rotate_graph.get()):
            plot_type = "barh"

        if (_save_name.get() == ""):
            save_name = file_name

        for element in graph_size_elements:
            if (element != ""):
                size.append(int(element))
        
        if (plot_type == "pie"):
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
                            message = "El tamaño de las secciones debe ser un valor de número entero, no un {}.".format(type(section_element_sizes[element]).__name__)
                        elif ("float" in exception_string):
                            message = "El nivel de explosión de las secciones debe ser un valor de número decimal, no un {}.".format(type(section_element_sizes[element]).__name__)
                            
                        messagebox.showerror("Error de valor", message)
                        return False
            
            else:
                messagebox.showerror("Error secciones de la gráfica", "El número de elementos en las diferentes secciones no concuerda, por favor verifica nuevamente.")
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
                        messagebox.showinfo("Multiples valores de Y", "Si deseas crear una grafica con multiples valores en el eje Y debes seleccionar 'Multiple' como tipo de grafica.")
            
            except KeyError as e:
                exception_string = str(e)

                if (_x_value.get() == "" or _y_value.get() == ""):
                    message = "Ingresa un valor para los ejes de la gráfica."

                else:
                    message = "La llave {} no fue encontrada en el archivo {}.".format(exception_string, file_name)

                messagebox.showerror("Error de llave", message)
                return False

        createPlot(
            plot_type,
            plot_title,
            save_name,
            rotate_ticks,
            x_axis,
            y_axis,
            legend=y_value_elements,
            file_size=size,
            sections=sections
        )

    Button(optionsTopLevel, text="Aceptar", width=34, command=lambda: setOptions(plot_type)).grid(row=16, column=1, columnspan=2, pady=16)

def typeWindow(csv, file_name, parent):
    typeTopLevel = Toplevel(parent)
    typeTopLevel.wm_title("Tipo de grafica")

    showAsPopup(parent, typeTopLevel)

    Label(typeTopLevel, text="Selecciona el tipo de gráfica",font=("Arial", 14)).grid(row=0, column=1, columnspan=2, padx=4, pady=4)
    
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


    Label(bmiTopLevel, text="Ingresa tus datos", font =("Arial", 14)).grid(row=0, column=1, columnspan=2 ,padx=14, pady=6)

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

def showStock(arroz, lentejas, frijoles, papa):
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

def stock(parent):
    stockTopLevel = Toplevel(parent)
    stockTopLevel.wm_title("Inventario")

    showAsPopup(parent, stockTopLevel)

    _arroz = StringVar()
    _lentejas = StringVar()
    _frijoles = StringVar()
    _papa = StringVar()

    Label(stockTopLevel, text="¿Cúantos kilos tienes de estos elementos?", font =("Arial", 14)).grid(row=0, column=1, columnspan=2 ,padx=14, pady=6)

    Label(stockTopLevel, text="Arroz: ").grid(row=1,column=1, sticky=W, padx=14, pady=6)
    Entry(stockTopLevel, width=40, textvariable=_arroz).grid(row=1, column=2, sticky=W, padx=14, pady=6)

    Label(stockTopLevel, text="Lentejas: ").grid(row=2,column=1, sticky=W, padx=14, pady=6)
    Entry(stockTopLevel, width=40, textvariable=_lentejas).grid(row=2, column=2, sticky=W, padx=14, pady=6)

    Label(stockTopLevel, text="Frijoles: ").grid(row=3,column=1, sticky=W, padx=14, pady=6)
    Entry(stockTopLevel, width=40, textvariable=_frijoles).grid(row=3, column=2, sticky=W, padx=14, pady=6)

    Label(stockTopLevel, text="Papa: ").grid(row=4,column=1, sticky=W, padx=14, pady=6)
    Entry(stockTopLevel, width=40, textvariable=_papa).grid(row=4, column=2, sticky=W, padx=14, pady=6)

    def verifyInputs():
        try:
            if (_arroz.get() == ""):
                arroz = 0
            else:
                arroz = float(_arroz.get())

            if (_lentejas.get() == ""):
                lentejas = 0
            else:
                lentejas = float(_lentejas.get())

            if (_frijoles.get() == ""):
                frijoles = 0
            else:
                frijoles = float(_frijoles.get())

            if (_papa.get() == ""):
                papa = 0
            else:
                papa = float(_papa.get())

        except ValueError:
            messagebox.showerror("Error tipo de variable", "Los valores ingresados deben ser enteros o decimales.")
            return False

        showStock(arroz, lentejas, frijoles, papa)

    Button(stockTopLevel, text="Continuar", width=34, command=verifyInputs).grid(row=5, column=1, columnspan=2, pady=16)

def feelings(parent):
    feelingsTopLevel = Toplevel(parent)
    feelingsTopLevel.wm_title("Sentimientos")

    showAsPopup(parent, feelingsTopLevel)

    _text = StringVar()

    Label(feelingsTopLevel, text="Cuentame como te has sentido", font =("Arial", 14)).grid(row=0, column=1, columnspan=2 ,padx=14, pady=6)
    Entry(feelingsTopLevel, width=60, textvariable=_text).grid(row=1, column=1, padx=14, pady=6)

    def verifyInputs():
        feeling = _text.get()

        if not (feeling.endswith(".")):
            messagebox.showerror("Error de ortografia", "Recuerda simpre terminar tus parrafos en '.'")
            return False

        messagebox.showinfo("Sentimientos", "No se que escribiste pero quiero que sepas que te aprecio y comprendo.")
        onClose(parent, feelingsTopLevel)

    Button(feelingsTopLevel, text="Continuar", width=34, command=verifyInputs).grid(row=5, column=1, columnspan=2, pady=16)

def showStoreSales():
    makePlot(
        file=__file__,
        type="pie",
        title="Ventas de la tienda",
        file_name="tienda",
        show=True,
        pie_sections= [
            {
                "name": "Leche",
                "size": 12,
                "explode": 0
            },
            {
                "name": "Huevo",
                "size": 8,
                "explode": 0
            },
            {
                "name": "Vino",
                "size": 4,
                "explode": 0
            },
            {
                "name": "Arroz",
                "size": 26,
                "explode": 0
            },
            {
                "name": "Queso",
                "size": 30,
                "explode": 0.1
            },
            {
                "name": "Salchichas",
                "size": 20,
                "explode": 0
            }
        ]
    )

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
        ["Graficar Inventario", lambda: stock(parent)],
        ["Expresar sentimientos", lambda: feelings(parent)],
        ["Compras de la tienda", showStoreSales]
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