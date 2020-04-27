import webbrowser
import datetime
import pyperclip
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
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

SELECT = "Seleccionar"
YES = "Aceptar"
COPY = "Copiar"
CANCEL = "Cancelar"
ERR = "Error"
TITULO_VENT_OPC = "Clases Programadas"
TITULO_MSJBOX_PGA = "Link Aula Zoom"
DIALOG_VENT_OPC = "\nEn este momento hay múltiples clases programadas para empezar, \npor favor selecciona la clase a la que vas a asistir: "
DIALOG_MSJBOX_PGA = "\n¿Deseas entrar al aula de {}?"
DIALOG_ERR_MATERIAS = "\nNo hay ninguna clase programada a empezar en por lo menos una hora"

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
        "Martes": {"Salon": C303, "Inicio": 1400, "Final": 1600}
    },

    "m1": {
        "Lunes": {"Salon": C310, "Inicio": 1200, "Final": 1400}
    },

    "mys2": {
        "Miercoles": {"Salon": C313, "Inicio": 900, "Final": 1100}
    },

    "ag": {
        "Viernes": {"Salon": C314, "Inicio": 900, "Final": 1100}
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

# ============================================================== FUNCIONES PRELIMINARES ============================================================== #
def darHoraActual():
    dt_now = datetime.datetime.now().time()
    tiempo = (dt_now.hour * 100) + (dt_now.minute)
    return tiempo

def darDiaDeLaSemana():
    dt_dia = datetime.datetime.now().date().weekday()
    dia_de_hoy = dias_de_la_semana[dt_dia]
    return dia_de_hoy

# ============================================================== VARIABLES ============================================================== #
tiempo_actual = darHoraActual()
dia_de_la_semana = darDiaDeLaSemana()
lista_materia_seleccionada = []

# ============================================================== CODIGO ============================================================== #
for materia in range(len(Materias.lista_objetos_materia)):
    nombre_materia_aaaaa = Materias.lista_objetos_materia[materia].nombre
    objeto_materia = Materias.lista_objetos_materia[materia]

    try:
        if objeto_materia.revisarRangoHorario(dia_de_la_semana, tiempo_actual):
            lista_materia_seleccionada.append(Materias.lista_objetos_materia[materia])
            print(nombre_materia_aaaaa)
        else:
            pass

    except(KeyError):
        pass

# ============================================================== FUNCIONES KIVY ============================================================== #
def onYesButtonPress(self):
    webbrowser.open(lista_materia_seleccionada[0].horario[dia_de_la_semana]["Salon"])
    exit()

def onCopyButtonPress(self):
    pyperclip.copy(lista_materia_seleccionada[0].horario[dia_de_la_semana]["Salon"])
    exit()

def onCancelButtonPress(self):
    exit()

def onOptionSelecction(nombre_de_materia):
    try:
        for i in range(len(lista_materia_seleccionada)):
            if (lista_materia_seleccionada[i].nombre != nombre_de_materia):
                del lista_materia_seleccionada[i]
            else:
                pass
    except(IndexError):
        pass
 
    show_question_box()

def questionWindowLayout():
    layout = FloatLayout()

    layout_widgets = [
        Label(
            text= DIALOG_MSJBOX_PGA.format(lista_materia_seleccionada[0].nombre),
            size_hint= (0.6, 0.2),
            pos_hint= {"x": 0.2, "top":1}
        ),

        Button(
            text= YES,
            size_hint= (1/5, 0.3),
            pos_hint= {"x": 0.37, "y": 0.07},
            on_press = onYesButtonPress
        ),

        Button(
            text= COPY,
            size_hint= (1/5, 0.3),
            pos_hint= {"x": 0.58, "y": 0.07},
            on_press = onCopyButtonPress
        ),

        Button(
            text = CANCEL,
            size_hint = (1/5, 0.3),
            pos_hint = {"x": 0.79, "y": 0.07},
            on_press =  onCancelButtonPress
        )
    ]

    for widget in layout_widgets:
        layout.add_widget(widget)

    return layout
    
def show_question_box():
    popup_content = questionWindowLayout()

    question_box = Popup(
        title = TITULO_MSJBOX_PGA,
        content = popup_content,
        size_hint = (None, None),
        size = (450, 175)
    )

    question_box.open()

def optionsWindowLayout():
    layout = FloatLayout()

    layout_widgets = [
        Label(
            text= DIALOG_VENT_OPC,
            size_hint= (0.6, 0.2),
            pos_hint= {"x": 0.2, "top":1}
        )
    ]

    dropdown = DropDown()
    for i in range(len(lista_materia_seleccionada)):
        btn = Button(
            text=lista_materia_seleccionada[i].nombre,
            size_hint_x=1,
            size_hint_y=None,
            height=42,
            on_release=lambda btn: dropdown.select(btn.text)
        )

        dropdown.add_widget(btn)

    mainbutton = Button(
            text= SELECT,
            size_hint_x = 0.6,
            size_hint_y = None,
            height=32,
            pos_hint= {"x": 0.2, "y": 0.2},
            on_release=dropdown.open
        )

    dropdown.bind(on_select=lambda instance, x: onOptionSelecction(x))
    
    for widget in layout_widgets:
        layout.add_widget(widget)

    layout.add_widget(mainbutton)

    return layout
    
def show_option_box():
    popup_content = optionsWindowLayout()

    option_box = Popup(
        title = TITULO_VENT_OPC,
        content = popup_content,
        size_hint = (None, None),
        size = (550, 175)
    )

    option_box.open()

def errorWindowLayout():
    layout = FloatLayout()

    layout_widgets = [
        Label(
            text= DIALOG_ERR_MATERIAS,
            size_hint= (0.6, 0.2),
            pos_hint= {"x": 0.2, "top":1}
        ),
        Button(
            text = CANCEL,
            size_hint = (1/5, 0.3),
            pos_hint = {"x": 0.79, "y": 0.07},
            on_press =  onCancelButtonPress
        )
    ]
         
    for widget in layout_widgets:
        layout.add_widget(widget)

    return layout

def show_error_box():
    popup_content = errorWindowLayout()

    error_box = Popup(
        title = ERR,
        content = popup_content,
        size_hint = (None, None),
        size = (550, 175)
    )

    error_box.open()

class Widgets(Widget):
    if (len(lista_materia_seleccionada) == 0):
        show_error_box()
    elif (len(lista_materia_seleccionada) == 1):
        show_question_box()
    else:
        show_option_box()

class MyApp(App):
    def build(self):
        return Widgets()

if (__name__ == "__main__"):
    MyApp().run()