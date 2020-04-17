import webbrowser
import datetime
import subprocess
import sys
import tkinter
from tkinter import Toplevel, OptionMenu, Label, mainloop, StringVar, Button, messagebox

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
C303 = "https://zoom.us/j/2625951983"
C306 = "https://zoom.us/j/8735340733"
C310 = "https://zoom.us/j/8431135588"
C311 = "https://zoom.us/j/6078474859"
C313 = "https://zoom.us/j/8190054125"
C314 = "https://zoom.us/j/4855338074"
C404 = "https://zoom.us/j/7304425672"
C406 = "https://zoom.us/j/8494462737"
C407 = "https://zoom.us/j/3439221195"
C502 = "https://zoom.us/j/7478971624"

B201 = "https://zoom.us/j/4889066915"
B1102 = "https://zoom.us/j/5916268075"
B1103 = "https://zoom.us/j/2965629593"

lista_de_materias = [
    #"Sistema de Seguridad Social Integral": 
    {
        "Martes": {
            "Salon": C407,
            "Inicio": 700,
            "Fin": 900
        }
    },    

    #"Física Conceptual y Experimental I": 
    {
        "Martes": {
            "Salon": B201,
            "Inicio": 1200,
            "Fin": 1400
        },
        "Jueves": {
            "Salon": C311,
            "Inicio": 1200,
            "Fin": 1400
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

    #"Cálculo Diferencial": 
    {
        "Lunes": {
            "Salon": B1102,
            "Inicio": 700,
            "Fin": 900
        },
        "Martes": {
            "Salon": C306,
            "Inicio": 700,
            "Fin": 900
        }
    },

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

    #"Administración General y en Salud": 
    {
        "Martes": {
            "Salon": C502,
            "Inicio": 500,
            "Fin": 700
        },
        "Jueves": {
            "Salon": C502,
            "Inicio": 500,
            "Fin": 700
        }   
    },  

    #"Tendencias y hospitales del futuro": 
    {
        "Miercoles": {
            "Salon": C303,
            "Inicio": 1500,
            "Fin": 1700
        }
    },

    #"Introducción y Gestión de la Calidad": 
    {
        "Martes": {
            "Salon": C303,
            "Inicio": 1400,
            "Fin": 1600
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
    "Sistema de Seguridad Social Integral",
    "Física Conceptual y Experimental I",
    "Física Conceptual y Experimental II",
    "Cálculo Diferencial",
    "Cálculo Integral y Ecuaciones Diferenciales",
    "Cálculo de Varias Variables",
    "Administración General y en Salud",
    "Tendencias y hospitales del futuro",
    "Introducción y Gestión de la Calidad",
    "Morfofisiología I",
    "Modelación y Simulación II",
    "Antropología General"
]

def center(master):
    screenwidth = master.winfo_screenwidth() / 2
    windowWidth = master.winfo_reqwidth()
    screenheight = master.winfo_screenheight() / 2
    windowHeight = master.winfo_reqheight()

    positionRight = int(screenwidth - windowWidth)
    positionDown = int(screenheight - windowHeight)

    master.geometry("+{}+{}".format(positionRight, positionDown))

lista_de_materias_en_rago = {}
lista_nombres_de_materias_en_rago = []

for materia in range(len(lista_de_materias)):
    try:
        if (hora in range(lista_de_materias[materia][dia_de_la_semana]["Inicio"], lista_de_materias[materia][dia_de_la_semana]["Fin"])):
            #abrir_link = tkinter.messagebox.askyesnocancel(title = "Link Aula Zoom", message = "¿Deseas entrar al aula de {}? \n(si no se copiara el link al portapapeles)".format(lista_nombre_de_materias[materia]))
            #link = lista_de_materias[materia][dia_de_la_semana]["Salon"]

            lista_de_materias_en_rago[lista_nombre_de_materias[materia]] = [lista_de_materias[materia][dia_de_la_semana]]
            lista_nombres_de_materias_en_rago.append(lista_nombre_de_materias[materia])

        else:
            pass
   
    except(KeyError):
        pass

def preguntar(nombre_materia, materia):
    link_materia = materia[0]["Salon"]

    pregunta = tkinter.messagebox.askyesnocancel(title = "Link Aula Zoom", message = "¿Deseas entrar al aula de {}? \n(si no se copiara el link al portapapeles)".format(nombre_materia))
    
    if pregunta:
        webbrowser.open(link_materia)
    else:
        pyperclip.copy(link_materia)

    exit()

def materiaSelecionada(indice_de_materia):
    nombre_materia_seleccionada = lista_nombres_de_materias_en_rago[indice_de_materia]
    materia_seleccionada = lista_de_materias_en_rago[nombre_materia_seleccionada]
    print(materia_seleccionada)

    preguntar(nombre_materia_seleccionada, materia_seleccionada)
    return materia_seleccionada

def botonCancelar():
    exit()

def crearNuevoBoton(ventana, texto, indice):
    nuevo_boton = Button(ventana, text = texto, width = 47, command = lambda: materiaSelecionada(indice)).pack(side = "top",padx = 24, pady = 2)
    return nuevo_boton


if (len(lista_de_materias_en_rago) == 0):
    messagebox.showerror(title = "Error", message = "No hay ninguna clase programada a empezar en por lo menos una hora")

elif (len(lista_de_materias_en_rago) == 1):
    nombre_materia_seleccionada = lista_nombres_de_materias_en_rago[0]
    preguntar(nombre_materia_seleccionada, lista_de_materias_en_rago[nombre_materia_seleccionada])

elif (len(lista_de_materias_en_rago) > 1):
    abrir_link_2 = Toplevel()
    abrir_link_2.title("Clases Programadas")
    center(abrir_link_2)

    Label(abrir_link_2, text = "En este momento hay múltiples clases programadas para empezar, \npor favor selecciona la clase a la que vas a asistir: ").pack(anchor = "nw", padx = 10, pady = 10)

    for i in range(len(lista_nombres_de_materias_en_rago)):
        crearNuevoBoton(abrir_link_2, lista_nombres_de_materias_en_rago[i], i)

    Button(abrir_link_2, text = "Cancelar", width = 47, command = botonCancelar).pack(side = "top",padx = 24, pady = 2)
    Label(abrir_link_2, text = "").pack(side = "bottom")#, command = but)

    mainloop()

# si depues del loop no encuentra una clase:
exit()