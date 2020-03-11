def calc(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    resultados = [suma, resta, mult, div]
    return resultados

operacion = [
    "suma",
    "resta",
    "multiplicacion",
    "division"
]

_num1 = int(input("Ingrese el primer numero: "))
_num2 = int(input("Ingrese el segundo numero: "))

resultado = calc(_num1, _num2)

for i in range(len(resultado)):
    print("La {} es igual a {}.".format(operacion[i], resultado[i]))
