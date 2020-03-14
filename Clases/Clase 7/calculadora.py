MSJ_0 = "nada porque no se puede dividir por cero."

def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = a - b
    return resta

def multiplicacion(a, b):
    mult = a * b
    return mult

def division(a, b):
    try:
        div = a / b
    except(ZeroDivisionError):
        div = MSJ_0

    return div

#_num1 = int(input("Ingrese el primer numero: "))
#_num2 = int(input("Ingrese el segundo numero: "))

#resultado = calc(_num1, _num2)

#for i in range(len(resultado)):
#    print("La {} es igual a {}.".format(operacion[i], resultado[i]))

