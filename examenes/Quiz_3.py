from Funciones1 import readCSV, maxCSV, minCSV

MSJ_BARRIOS = "El barrio con el nombre mas largo es {} con {} letras, y el mas corto es {} con {}."
MSJ_AGUA = "El barrio que mas agua consume gasta {}, y el que menos consume gasta {}."
MSJ_ENERGIA = "El barrio que mas energia consume gasta {}, y el que menos consume gasta {}."
MSJ_GAS = "El barrio que mas gas consume gasta {}, y el que menos consume gasta {}."
MSJ_INTERNET = "El barrio que mas internet consume gasta {}, y el que menos consume gasta {}."
MSJ_HAB = "El barrio con mas habitantes tiene {} habitantes, y el que menos poblado tiene {} habitantes."
FILE_NAME = "barrios.csv"

readCSV(FILE_NAME)

max_bar_len = maxCSV(FILE_NAME, "Barrio", "length")
min_bar_len = minCSV(FILE_NAME, "Barrio", "length")

print(MSJ_BARRIOS.format(max_bar_len, len(max_bar_len), min_bar_len, len(min_bar_len)))

max_agu = maxCSV(FILE_NAME, "Agua", None)
min_agu = minCSV(FILE_NAME, "Agua", None)

print(MSJ_AGUA.format(max_agu, min_agu))

max_ene = maxCSV(FILE_NAME, "Energía", None)
min_ene = minCSV(FILE_NAME, "Energía", None)

print(MSJ_ENERGIA.format(max_ene, min_ene))

max_gas = maxCSV(FILE_NAME, "Gas", None)
min_gas = minCSV(FILE_NAME, "Gas", None)

print(MSJ_GAS.format(max_gas, min_gas))

max_int = maxCSV(FILE_NAME, "Internet", None)
min_int = minCSV(FILE_NAME, "Internet", None)

print(MSJ_INTERNET.format(max_int, min_int))

max_hab = maxCSV(FILE_NAME, "Habitantes", None)
min_hab = minCSV(FILE_NAME, "Habitantes", None)

print(MSJ_HAB.format(max_hab, min_hab))