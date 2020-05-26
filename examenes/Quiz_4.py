import os
import sys

# esto es para que reconosca el archivo de funciones
sys.path.append(os.getcwd() + "/functions/")
from funcs import readCSV, makePlot

invetario = readCSV("inventario")
ppg = readCSV("ppg")

# BARRA
makePlot(
    file=__file__,
    type="bar",
    title="Elemento vs Unidades",
    file_name="Elemento vs Unidades",
    rotate_x_ticks=True,
    size=[7,13],
    x_axis = [
        "Elemento",
        list(invetario["Elemento"].values())
    ],
    y_axis = [
        "Unidades",
        list(invetario["Unidade "].values())
    ]
)

makePlot(
    file=__file__,
    type="bar",
    title="Elemento vs Elementos Viejos",
    file_name="Elemento vs Elementos Viejos",
    rotate_x_ticks=True,
    size=[7,13],
    x_axis = [
        "Elemento",
        list(invetario["Elemento"].values())
    ],
    y_axis = [
        "Elementos Viejos",
        list(invetario["Viejo "].values())
    ]
)

makePlot(
    file=__file__,
    type="bar",
    title="Elemento vs Elementos Nuevos",
    file_name="Elemento vs Elementos Nuevos",
    rotate_x_ticks=True,
    size=[7,13],
    x_axis = [
        "Elemento",
        list(invetario["Elemento"].values())
    ],
    y_axis = [
        "Elementos Nuevos",
        list(invetario["Nuevos"].values())
    ]
)

# PPG
makePlot(
    file=__file__,
    type="plot",
    title="PPG",
    file_name="PPG",
    rotate_x_ticks=False,
    show=True,
    x_axis = [
        "Tiempo(ms)",
        list(ppg["muestra"].values())
    ],
    y_axis = [
        "Volataje(uV)",
        list(ppg["valor"].values())
    ]
)

print("Se ven nueve picos en el ppg")

# PIE
makePlot(
    file=__file__,
    type="pie",
    title="Grafico Pie",
    file_name="Grafico Pie",
    pie_sections= [
        {
            "name": "Recuperandose en casa",
            "size": 85,
            "explode": 0
        },
        {
            "name": "Hospitalizado",
            "size": 10,
            "explode": 0
        },
        {
            "name": "En UCI",
            "size": 5,
            "explode": 0.1
        }
    ]
)