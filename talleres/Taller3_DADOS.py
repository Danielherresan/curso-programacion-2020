import random
import time

# MENSAJES
MSJ_ROLL = "Los dados que lanzaste cayeron {} y {}, los cuales suman {}."
MSJ_NUM = "Le tomo a los dados {} tiradas para sumar a 12, lo cual esta"
MSJ_DIS_AVG = "por {} del promedio de 36 tiradas."
MSJ_AVG = "exactamente el promedio de tiradas nesesarias para sumar 12"
DEB = "debajo"
ENC = "encima"

# VARIABLES
PROMEDIO = round(1/0.0278) # The expected value of a geometrically distributed random variable is 1/p, where p is the probability of success in one trial (p = 2.78% for double sixes).
dado1 = 0
dado2 = 0
suma = 0
intentos = 0

# CODIGO
def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    sm = d1 + d2
    return (d1, d2, sm)

while (suma < 12):
    tiro = roll()
    intentos += 1
    suma = tiro[2]
    print(MSJ_ROLL.format(tiro[0], tiro[1], suma))
    time.sleep(0.75)

if(intentos < PROMEDIO):
    print(MSJ_NUM.format(intentos), MSJ_DIS_AVG.format(DEB))
elif(intentos > PROMEDIO):
    print(MSJ_NUM.format(intentos), MSJ_DIS_AVG.format(ENC))
else:
    print(MSJ_NUM.format(intentos), MSJ_AVG)

    