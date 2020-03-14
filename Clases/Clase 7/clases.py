import funciones as p

numH = 0 
class Humano():
    def __init__(self, nom, eda, pes, est):
        global numH
        self.nombre = nom
        self.raza = "ser humano"
        self.edad = eda
        self.peso = pes       
        self.estatura = est
        numH += 1

MSJS = [
    "Me llamo {}",
    "soy un {}",
    "tengo {} años",
    "peso {}kg",
    "y mido {}m."
]

humano1 = Humano("daniel", 21, 75, 1.78)
humano2 = Humano("jose", 18, 45, 1.54)
humano3 = Humano("alveiro",39, 92, 1.98)

var_h1 = vars(humano1)
var_h2 = vars(humano2)
var_h3 = vars(humano3)

attr_h1 = []
for attr in var_h1:
    attr_h1.append(var_h1[attr])

attr_h2 = []
for attr in var_h2:
    attr_h2.append(var_h2[attr])

attr_h3 = []
for attr in var_h3:
    attr_h3.append(var_h3[attr])

attr_list = [
    attr_h1,
    attr_h2,
    attr_h3
]

for i in range(numH):
    p.printHum(i, MSJS, attr_list[i])