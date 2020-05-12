import os
import sys

# esto es para que reconosca el archivo de funciones
sys.path.append(os.getcwd() + "/functions/")
from funcs import readCSV, makePlot


barrios = readCSV("barrios.csv")
ecg = readCSV("ecg_taller.csv")

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

makePlot(
    file=__file__,
    type="bar",
    title="Barrios vs Gas",
    file_name="Barrios vs Gas",
    rotate_x_ticks=True,
    size=[7,12],
    x_axis = [
        "Barrios",
        list(barrios["Barrio"].values())
    ],
    y_axis = [
        "Gas",
        list(barrios["Gas"].values())
    ]
)

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