import os
import sys

# esto es para que reconosca el archivo de funciones
sys.path.append(os.getcwd() + "/functions/")
from funcs import readCSV, minCSV, maxCSV

MSJ_BARRIOS = "El barrio con el nombre mas largo es {} con {} letras, y el mas corto es {} con {}."
MSJ_AGUA = "El barrio que mas agua consume gasta {}, y el que menos consume gasta {}."
MSJ_ENERGIA = "El barrio que mas energia consume gasta {}, y el que menos consume gasta {}."
MSJ_GAS = "El barrio que mas gas consume gasta {}, y el que menos consume gasta {}."
MSJ_INTERNET = "El barrio que mas internet consume gasta {}, y el que menos consume gasta {}."
MSJ_HAB = "El barrio con mas habitantes tiene {} habitantes, y el que menos poblado tiene {} habitantes."
FILE_NAME = "barrios.csv"

file_dict = readCSV(FILE_NAME)

max_bar_len = maxCSV(file_dict, "Barrio", "length")
min_bar_len = minCSV(file_dict, "Barrio", "length")

print(MSJ_BARRIOS.format(max_bar_len, len(max_bar_len), min_bar_len, len(min_bar_len)))

max_agu = maxCSV(file_dict, "Agua", None)
min_agu = minCSV(file_dict, "Agua", None)

print(MSJ_AGUA.format(max_agu, min_agu))

max_ene = maxCSV(file_dict, "Energía", None)
min_ene = minCSV(file_dict, "Energía", None)

print(MSJ_ENERGIA.format(max_ene, min_ene))

max_gas = maxCSV(file_dict, "Gas", None)
min_gas = minCSV(file_dict, "Gas", None)

print(MSJ_GAS.format(max_gas, min_gas))

max_int = maxCSV(file_dict, "Internet", None)
min_int = minCSV(file_dict, "Internet", None)

print(MSJ_INTERNET.format(max_int, min_int))

max_hab = maxCSV(file_dict, "Habitantes", None)
min_hab = minCSV(file_dict, "Habitantes", None)

print(MSJ_HAB.format(max_hab, min_hab))