from funciones import whileLoop, espacio

# ================================================================= MENSAJES ================================================================= #

MSJS_DICC = {
    'FUERA DE RANGO': "El número ingresado no corresponde a una función de este programa, por favor intetalo de nuevo.\n",
    'FORMATO': "{} - {}",
    'VOLVER': "Salir"
}

ATTRIBUTE_MSJS_DICC = {
    'ATTR_STU': "El estudiante {} tiene los siguientes atributos:",
    'ATTR_PRI': "El director {} tiene los siguientes atributos:",
    'ATTR_TEA': "El profesor {} tiene los siguientes atributos:",
    'AGE': "Tiene {} años",
    'GENDER': "Es de genero {}",
    'SCHOOL': "Se graduó del Colegio {}",
    'ASS_CLA': "Ha asistido a {} clases",        
    'EDU_LVL': "Tiene un nivel de educacion de {}",
    'GIV_LEC': "Ha dictado {} clases",         
    'HIR_TEA': "Ha contratado a {} nuevos profesores"
}

CHOOSE_MSJS_DICC = {
    'STU': "Escoge un estudiante para ver sus atributos: ",
    'TEA': "Escoge un profesor para ver sus atributos: ",
    'TEA_PRO': "Escoge un profesor para ascenderlo: ",
    'PRI': "Escoge un director para ver sus atributos: "
}

MSJ_PRO_SUC = "El profesor {} fue a ascendido a director!!"

MAIN_MENU_OPTIONS = ["Mostrar Atributos de los estudiantes", "Mostrar los atributos de los profesores", "Mostrar los atributos de los directores", "Ascender a un profesor"]

MSJ_DESPEDIDA = "Cuidate, y por tu seguridad quedate en casa..."

# ================================================================= CLASES ================================================================= #

class Student():
    student_object_list = []
    student_name_list = []

    def __init__(self, name, age, gender, school, class_assistances):
        self.name = name 
        self.age = age
        self.gender = gender
        self.school = school
        self.class_assistances = class_assistances
        Student.student_object_list.append(self)
        Student.student_name_list.append(self.name)

    def assistClass(self, amount_of_assistances):
        self.class_assistances += amount_of_assistances
        return self.class_assistances      

class Teacher():
    teacher_object_list = []
    teacher_name_list = []

    def __init__(self, name, age, education_level, lectures_given):
        self.name = name
        self.age = age
        self.education_level = education_level
        self.lectures_given = lectures_given
        Teacher.teacher_object_list.append(self)
        Teacher.teacher_name_list.append(self.name)

    def giveLecture(self, amount_of_lectures):
        self.lectures_given += amount_of_lectures
        return self.lectures_given
    
class Principal(Teacher):
    principal_object_list = []
    principal_name_list = []

    def __init__(self, Teacher):
        self.name = Teacher.name
        self.age = Teacher.age
        self.education_level = Teacher.education_level
        self.lectures_given = Teacher.lectures_given
        self.hired_teachers = 0
        Principal.principal_object_list.append(self)
        Principal.principal_name_list.append(self.name)

    def hireTeacher(self, teacher_name, teacher_age, teacher_education, teacher_given_lectures):
        new_teacher = Teacher(teacher_name, teacher_age, teacher_education, teacher_given_lectures)
        self.hired_teachers += 1
        return new_teacher

# ================================================================= OBJETOS ================================================================= #

student_1 = Student("mario", 19, "masculino", "Agustiniano", 2)
student_2 = Student("ana", 21, "femenino", "INEM", 3)
student_3 = Student("jose", 20, "masculino", "del espiritú santo", 6)
student_4 = Student("luisa", 23, "femenino", "La Salle", 3)
student_5 = Student("eliberto", 17, "masculino", "MONTESSORI", 2)

# Asistir a clase
student_1.assistClass(3)
student_2.assistClass(2)
student_3.assistClass(4)
student_4.assistClass(0)
student_5.assistClass(1)

teacher_1 = Teacher("Jilberto", 37, "Masters degree", 4)
teacher_2 = Teacher("Leon", 29, "Doctoral degree", 5)
teacher_3 = Teacher("Juan", 35, "PhD", 6)

# Dar clase
teacher_1.giveLecture(1)
teacher_2.giveLecture(4)
teacher_3.giveLecture(2)

principal_1 = Principal(teacher_3)

# Contratacion
teacher_4 = principal_1.hireTeacher("Maria", 23, "Associate degree", 1)
teacher_5 = principal_1.hireTeacher("Maikol", 31, "Bachelor's degree", 2)


# ================================================================= CODIGO ================================================================= #

# Variables del menu principal
_option = ""
main_menu_range = len(MAIN_MENU_OPTIONS) + 2

# Variables del menu de estudiantes
_show_student_attributes_option = ""
show_student_attributes_range = len(Student.student_name_list) + 2

# Variables del menu de profesores
_show_teacher_attributes_option = ""
show_teacher_attributes_range = len(Teacher.teacher_name_list) + 2

# Variables del menu de directores
_show_principal_attributes_option = ""
show_principal_attributes_range = len(Principal.principal_name_list) + 2


_promote_teacher_option = ""
promote_teacher_range = len(Teacher.teacher_name_list) + 2

def showStudentAttributes(_input):
    real_input = _input - 1
    espacio()

    try:
        print(ATTRIBUTE_MSJS_DICC['ATTR_STU'].format(Student.student_name_list[real_input]))
        print(ATTRIBUTE_MSJS_DICC['AGE'].format(str(Student.student_object_list[real_input].age)))
        print(ATTRIBUTE_MSJS_DICC['GENDER'].format(Student.student_object_list[real_input].gender))
        print(ATTRIBUTE_MSJS_DICC['SCHOOL'].format(Student.student_object_list[real_input].school))
        print(ATTRIBUTE_MSJS_DICC['ASS_CLA'].format(Student.student_object_list[real_input].class_assistances))
        espacio()

    except(IndexError): #si el indice da fuera de rango significa que la opcion es salir, ya que si estubiera fuera del rango de opciones la funcion whileLoop la hubiera rechazado
        whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)

def showTeacherAttributes(_input):
    real_input = _input - 1
    espacio()

    try:
        print(ATTRIBUTE_MSJS_DICC['ATTR_TEA'].format(Teacher.teacher_name_list[real_input]))
        print(ATTRIBUTE_MSJS_DICC['AGE'].format(str(Teacher.teacher_object_list[real_input].age)))
        print(ATTRIBUTE_MSJS_DICC['EDU_LVL'].format(Teacher.teacher_object_list[real_input].education_level))
        print(ATTRIBUTE_MSJS_DICC['GIV_LEC'].format(Teacher.teacher_object_list[real_input].lectures_given))
        espacio()

    except(IndexError):
        whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)

def showPrincipalAttributes(_input):
    real_input = _input - 1
    espacio()

    try:
        print(ATTRIBUTE_MSJS_DICC['ATTR_PRI'].format(Principal.principal_name_list[real_input]))
        print(ATTRIBUTE_MSJS_DICC['AGE'].format(str(Principal.principal_object_list[real_input].age)))
        print(ATTRIBUTE_MSJS_DICC['EDU_LVL'].format(Principal.principal_object_list[real_input].education_level))
        print(ATTRIBUTE_MSJS_DICC['GIV_LEC'].format(Principal.principal_object_list[real_input].lectures_given))
        print(ATTRIBUTE_MSJS_DICC['HIR_TEA'].format(Principal.principal_object_list[real_input].hired_teachers))
        espacio()

    except(IndexError):
        whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)

def promoteTeacher(teacher_object):
    new_principal = Principal(teacher_object)
    return new_principal

def showTeacherForPromotion(_input):
    real_input = _input - 1

    try:
        promoteTeacher(Teacher.teacher_object_list[real_input])
        espacio()

        print(MSJ_PRO_SUC.format(Teacher.teacher_object_list[real_input].name))
        espacio()

        whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)

    except(IndexError):
        whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)
          

# definir que hace el menu principal
def mainMenu(_input):
    espacio()
    if (_input == 1):
        print(CHOOSE_MSJS_DICC['STU'])
        espacio()

        whileLoop(MSJS_DICC, showStudentAttributes, _show_student_attributes_option, show_student_attributes_range, Student.student_name_list)

    if (_input == 2):
        print(CHOOSE_MSJS_DICC['TEA'])
        espacio()

        whileLoop(MSJS_DICC, showTeacherAttributes, _show_teacher_attributes_option, show_teacher_attributes_range, Teacher.teacher_name_list)

    if (_input == 3):
        print(CHOOSE_MSJS_DICC['PRI'])
        espacio()

        show_principal_attributes_range = len(Principal.principal_name_list) + 2 #Esto se hace para actualizar el rango ya que a pesar de que la lista tiene un nuevo elemento, el rango solo se calcula la primera vez que lo declaré

        whileLoop(MSJS_DICC, showPrincipalAttributes, _show_principal_attributes_option, show_principal_attributes_range, Principal.principal_name_list)

    if (_input == 4):
        print(CHOOSE_MSJS_DICC['TEA_PRO'])
        espacio()

        whileLoop(MSJS_DICC, showTeacherForPromotion, _promote_teacher_option, promote_teacher_range, Teacher.teacher_name_list)

    else:
        print(MSJ_DESPEDIDA)
        exit()

# start main loop
whileLoop(MSJS_DICC, mainMenu, _option, main_menu_range, MAIN_MENU_OPTIONS)