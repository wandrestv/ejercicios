import math
class Ejercicio10:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def udcm(self, n1):
        mil = n1 / 1000
        cont = n1 % 1000
        cent = cont / 100
        cont = cont % 100
        dec = cont / 10
        uni = cont % 10
        print("Unidades: {}".format(uni))
        print("Decenas: {}".format(math.trunc(dec)))
        print("Centenas: {}".format(math.trunc(cent)))
        print("Unidades de mil: {}".format(math.trunc(mil)))

a1 = int(input("Ingrese un número de 4 dígitos: "))
ejercicio10Variable = Ejercicio10("Ejercicios")
ejercicio10Variable.udcm(a1)