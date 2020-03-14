
def printHum(numHum, msj, att):
    print("\nHUMANO {}:".format(numHum+1))
    for i in range(len(msj)):
        print(msj[i].format(att[i]))
