import webbrowser
import datetime
import tkinter
import subprocess
import sys
from tkinter import messagebox

# intentar importar pyperclip y si no funciona instalarlo con pip
try:
    import pyperclip
except(ModuleNotFoundError):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
    import pyperclip

# ocultar la pestaña principal de tkinter
root = tkinter.Tk()
root.withdraw()

hour = datetime.datetime.now().time().hour * 100
minutes = datetime.datetime.now().time().minute
hora = hour + minutes
date = datetime.datetime.now().date().weekday()

dia_de_la_semana = ""

if (date == 0):
    dia_de_la_semana = "Lunes"
elif (date == 1):
    dia_de_la_semana = "Martes"
elif (date == 2):
    dia_de_la_semana = "Miercoles"
elif (date == 3):
    dia_de_la_semana = "Jueves"
elif (date == 4):
    dia_de_la_semana = "Viernes"
else:
    pass

# Links de los salones
C310 = "https://zoom.us/j/8431135588"
C313 = "https://zoom.us/j/8190054125"
C314 = "https://zoom.us/j/4855338074"
C404 = "https://zoom.us/j/7304425672"
C406 = "https://zoom.us/j/8494462737"
C407 = "https://zoom.us/j/3439221195"
B1103 = "https://zoom.us/j/2965629593"

lista_de_materias = [
    #"Cálculo Integral y Ecuaciones Diferenciales": 
    {
        "Miercoles": {
            "Salon": C404,
            "Inicio": 500,
            "Fin": 700
        },
        "Viernes": {
            "Salon": C404,
            "Inicio": 500,
            "Fin": 700
        }
    },

    #"Sistema de Seguridad Social Integral": 
    {
        "Martes": {
            "Salon": C407,
            "Inicio": 700,
            "Fin": 900
        }
    },    

    #"Física Conceptual y Experimental II": 
    {
        "Miercoles": {
            "Salon": C406,
            "Inicio": 1400,
            "Fin": 1600
        },
        "Viernes": {
            "Salon": B1103,
            "Inicio": 1400,
            "Fin": 1600
        }
    },

    #"Cálculo de Varias Variables": 
    {
        "Lunes": {
            "Salon": B1103,
            "Inicio": 900,
            "Fin": 1100
        },
        "Miercoles": {
            "Salon": C406,
            "Inicio": 700,
            "Fin": 900
        }   
    },   

    #"Morfofisiología I": 
    {
        "Lunes": {
            "Salon": C310,
            "Inicio": 1200,
            "Fin": 1400
        }
    },

    #"Modelación y Simulación II": 
    {
        "Miercoles": {
            "Salon": C313,
            "Inicio": 900,
            "Fin": 1100
        }
    },

    #"Antropología General": 
    {
        "Viernes": {
            "Salon": C314,
            "Inicio": 900,
            "Fin": 1100
        }
    }
]

lista_nombre_de_materias = [
    "Cálculo Integral y Ecuaciones Diferenciales",
    "Sistema de Seguridad Social Integral",
    "Física Conceptual y Experimental II",
    "Cálculo de Varias Variables",
    "Morfofisiología I",
    "Modelación y Simulación II",
    "Antropología General"
]

for materia in range(len(lista_de_materias)):
    try:
        if (hora in range(lista_de_materias[materia][dia_de_la_semana]["Inicio"], lista_de_materias[materia][dia_de_la_semana]["Fin"])):
            abrir_link = tkinter.messagebox.askyesnocancel(title = "Link Aula Zoom", message = "¿Deseas entrar al aula de {}? \n(si no se copiara el link al portapapeles)".format(lista_nombre_de_materias[materia]))
            link = lista_de_materias[materia][dia_de_la_semana]["Salon"]

            if abrir_link:
                webbrowser.open(link)
            else:
                pyperclip.copy(link)
            
            exit()

        else:
            pass
        
    except(KeyError):
        pass

# si depues del loop no encuentra una clase:
messagebox.showerror(title = "Error", message = "No hay ninguna clase programada a empezar en por lo menos una hora")

exit()