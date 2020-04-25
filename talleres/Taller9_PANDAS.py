from Funciones import maxCSV, minCSV

MSJ_NOMBRE_LARGO = "La ciudad con el nombre más largo es {} con {} letras."
MSJ_NOMBRE_CORTO = "La ciudad con el nombre más corto es {} con {} letras."
MSJ_GANANCIAS = "Las ganancias mas altas son de {}."
MSJ_PERDIDAS = "Las perdidas mas altas son de {}."

balance = "balance.csv"
ciudad = "Ciudad"
length = "length"
ganancias = "Ganancias"
perdidas = "Perdidas"

longest_name = maxCSV(balance, ciudad, length)
print(MSJ_NOMBRE_LARGO.format(longest_name, len(longest_name)))

shortest_name = minCSV(balance, ciudad, length)
print(MSJ_NOMBRE_CORTO.format(shortest_name, len(shortest_name)))

biggest_profits = maxCSV(balance, ganancias, None)
print(MSJ_GANANCIAS.format(biggest_profits))

biggest_expenses = maxCSV(balance, perdidas, None)
print(MSJ_PERDIDAS.format(biggest_expenses))