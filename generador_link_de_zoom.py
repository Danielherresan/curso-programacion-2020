import webbrowser
import datetime
import pyperclip
import tkinter
from tkinter import Toplevel, OptionMenu, Label, mainloop, StringVar, Button, messagebox
from sys import exit

# ============================================================== MENSAJES ============================================================== #
dias_de_la_semana = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
]

FORM_GEOMETRIA_VENTANA = "+{}+{}"
CANCEL = "Cancelar"
ERR = "Error"
TITULO_VENT_OPC = "Clases Programadas"
TITULO_MSJBOX_PGA = "Link Aula Zoom"
DIALOG_VENT_OPC = "En este momento hay múltiples clases programadas para empezar, \npor favor selecciona la clase a la que vas a asistir: "
DIALOG_MSJBOX_PGA = "¿Deseas entrar al aula de {}? \n(si no se copiara el link al portapapeles)"
DIALOG_ERR_MATERIAS = "No hay ninguna clase programada a empezar en por lo menos una hora"

# ----- Links de salones del C ----- #
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

# ----- Links de salones del B ----- #
B201 = "https://zoom.us/j/4889066915"
B1102 = "https://zoom.us/j/5916268075"
B1103 = "https://zoom.us/j/2965629593"

# ============================================================== HORARIOS ============================================================== #
horarios = {
    "sssi": {
        "Martes": {"Salon": C407, "Inicio": 700, "Final": 900}
    },

    "fce1": {
        "Martes": {"Salon": B201, "Inicio": 1200, "Final": 1400},
        "Jueves": {"Salon": C311, "Inicio": 1200, "Final": 1400}
    },

    "fce2": {
        "Miercoles": {"Salon": C406, "Inicio": 1400, "Final": 1600},
        "Viernes": {"Salon": B1103, "Inicio": 1400, "Final": 1600}
    },

    "cd": {
        "Lunes": {"Salon": B1102, "Inicio": 700, "Final": 900},
        "Martes": {"Salon": C306, "Inicio": 700, "Final": 900}
    },

    "cied": {
        "Miercoles": {"Salon": C404, "Inicio": 500, "Final": 700},
        "Viernes": {"Salon": C404, "Inicio": 500, "Final": 700}
    },

    "cvv": {
        "Lunes": {"Salon": B1103, "Inicio": 900, "Final": 1100},
        "Miercoles": {"Salon": C406, "Inicio": 700, "Final": 900}   
    },
    
    "agyes": {
        "Martes": {"Salon": C502, "Inicio": 500,"Final": 700},
        "Jueves": {"Salon": C502, "Inicio": 500,"Final": 700}   
    },

    "tyhdf": {
        "Miercoles": {"Salon": C303, "Inicio": 1500, "Final": 1700}
    },

    "iygdlc": {
        "Martes": {"Salon": C303, "Inicio": 1400, "Fin": 1600}
    },

    "m1": {
        "Lunes": {"Salon": C310, "Inicio": 1200, "Fin": 1400}
    },

    "mys2": {
        "Miercoles": {"Salon": C313, "Inicio": 900, "Fin": 1100}
    },

    "ag": {
        "Viernes": {"Salon": C314, "Inicio": 900, "Fin": 1100}
    }
}

# ============================================================== CLASES ============================================================== #
class Materias():
    lista_objetos_materia = []
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario
        Materias.lista_objetos_materia.append(self)
        
    def revisarRangoHorario(self, dia, hora):
        try:
            if (hora in range(int(self.horario[dia]["Inicio"]), int(self.horario[dia]["Final"]))):
                return True
            else:
                return False
        except(KeyError):
            return False

# ---------------------------- Inicializar Objetos ---------------------------- #
sssi = Materias("Sistema de Seguridad Social Integral", horarios["sssi"])
fce1 = Materias("Física Conceptual y Experimental I", horarios["fce1"])
fce2 = Materias("Física Conceptual y Experimental II", horarios["fce2"])
cd = Materias("Cálculo Diferencial", horarios["cd"])
cied = Materias("Cálculo Integral y Ecuaciones Diferenciales", horarios["cied"])
cvv = Materias("Cálculo de Varias Variables", horarios["cvv"])
agyes = Materias("Administración General y en Salud", horarios["agyes"])
tyhdf = Materias("Tendencias y hospitales del futuro", horarios["tyhdf"])
iygdlc = Materias("Introducción y Gestión de la Calidad", horarios["iygdlc"])
m1 = Materias("Morfofisiología I", horarios["m1"])
mys2 = Materias("Modelación y Simulación II", horarios["mys2"])
ag = Materias("Antropología General", horarios["ag"])

# ============================================================== FUNCIONES ============================================================== #
def darHoraActual():
    dt_now = datetime.datetime.now().time()

    tiempo = (dt_now.hour * 100) + (dt_now.minute)
    return tiempo

def darDiaDeLaSemana():
    dt_dia = datetime.datetime.now().date().weekday()
    dia_de_hoy = dias_de_la_semana[dt_dia]
    return dia_de_hoy

def esconderPestanaTk():
    root = tkinter.Tk()
    root.withdraw()

def centrar(ventana):
    ancho_pantalla = ventana.winfo_screenwidth() / 2
    ancho_ventana = ventana.winfo_reqwidth()
    alto_pantalla = ventana.winfo_screenheight() / 2
    alto_ventana = ventana.winfo_reqheight() / 2

    coordenada_horizontal = int(ancho_pantalla - ancho_ventana)
    coordenada_vertical = int(alto_pantalla - alto_ventana)

    ventana.geometry(FORM_GEOMETRIA_VENTANA.format(coordenada_horizontal, coordenada_vertical))

def preguntar(materia):
    link_materia = materia.horario[dia_de_la_semana]["Salon"]
    pregunta = tkinter.messagebox.askyesnocancel(title = TITULO_MSJBOX_PGA, message = DIALOG_MSJBOX_PGA.format(materia.nombre))
    
    if pregunta:
        webbrowser.open(link_materia)
    else:
        pyperclip.copy(link_materia)

    exit()

def seleccionarMateria(indice_de_materia, lista_de_objetos):
    preguntar(lista_de_objetos[indice_de_materia])

def crearNuevoBoton(ventana, texto, indice, materias):
    nuevo_boton = Button(ventana, text = texto, width = 47, command = lambda: seleccionarMateria(indice, materias)).pack(side = "top",padx = 24, pady = 2) # se le asigna una variable al boton porque sino este se sobreescribe con el valor del ultimo boton creado

def crearVentanaOpciones(lista_de_materias_seleccionadas):
    ventana_de_opciones = Toplevel()
    ventana_de_opciones.title(TITULO_VENT_OPC)
    centrar(ventana_de_opciones)

    Label(ventana_de_opciones, text = DIALOG_VENT_OPC).pack(anchor = "nw", padx = 10, pady = 10)
    for i in range(len(lista_de_materias_seleccionadas)):
        crearNuevoBoton(ventana_de_opciones, lista_de_materias_seleccionadas[i].nombre, i, lista_de_materias_seleccionadas)

    Button(ventana_de_opciones, text =  CANCEL, width = 47, command = botonCancelar).pack(side = "top",padx = 24, pady = 2)
    Label(ventana_de_opciones, text = None).pack(side = "bottom")

    mainloop()

def botonCancelar():
    exit()

# ============================================================== VARIABLES ============================================================== #
tiempo_actual = darHoraActual()
dia_de_la_semana = darDiaDeLaSemana()
lista_de_materias_en_rango = {}
lista_nombres_de_materias_en_rango = []

lista_materia_seleccionada = []

# ============================================================== CODIGO ============================================================== #
esconderPestanaTk()

for materia in range(len(Materias.lista_objetos_materia)):
    nombre_materia_aaaaa = Materias.lista_objetos_materia[materia].nombre
    objeto_materia = Materias.lista_objetos_materia[materia]

    try:
        if objeto_materia.revisarRangoHorario(dia_de_la_semana, tiempo_actual):
            lista_materia_seleccionada.append(Materias.lista_objetos_materia[materia])
        else:
            pass

    except(KeyError):
        pass

if (len(lista_materia_seleccionada) == 0):
    messagebox.showerror(title = ERR, message = DIALOG_ERR_MATERIAS)

elif (len(lista_materia_seleccionada) == 1):
    preguntar(lista_materia_seleccionada[0])

else:
    crearVentanaOpciones(lista_materia_seleccionada)
    
exit()