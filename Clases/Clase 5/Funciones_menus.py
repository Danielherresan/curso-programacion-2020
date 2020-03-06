import random
import time

# FUNCIONES
def edades(numPersonas):
    age = []
    ind = 0
    while(ind < numPersonas):
        age.append(random.randint(16,25))
        ind += 1
    return age

def notas(numPersonas):
    note = []
    ind = 0
    while(ind < numPersonas):
        note.append(round(random.uniform(0, 5), 2))
        ind += 1
    return note