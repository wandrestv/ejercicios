import math
class Ejercicio6:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def hipotenusa(self,n1,n2):

        hip = math.sqrt((n1**2) + (n2**2))
        print("La hipotenusa es: {}".format(hip))

a1 = float(input("Ingrese el primer lado:"))
b1 = float(input("Ingrese el primer lado:"))

ejercicio6Variable = Ejercicio6("Titulo")
ejercicio6Variable.hipotenusa(a1,b1)