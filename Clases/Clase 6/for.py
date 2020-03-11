#_cantidadSaltos = int(input("Escribe el numero de saltos: "))

#for i in range(_cantidadSaltos):
#    print("salto {}".format(i+1))

NOMBRES = [
"santiago",
"juanes",
"marco",
"elena",
"camila betancur",
"camila mesa",
"lesly",
"ysabella",
"santiago em",
"daniel",
"mafe",
"octavio",
"susi",
"daniel profe"
]

EDADES = [
    14,
    34,
    23,
    56,
    78,
    24,
    35,
    21,
    31,
    18,
    45,
    32,
    22,
    21
]

sum_edad = 0

for i in range(len(EDADES)):
    if (EDADES[i] >= 18):
        print("{}. {} tiene {} años.".format(i, NOMBRES[i], EDADES[i]))

for edad in EDADES:
    sum_edad += edad
print(sum_edad)