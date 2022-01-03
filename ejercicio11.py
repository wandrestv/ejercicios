class Ejercicio11:
    def __init__(self, titulo):
        self.mensaje = titulo
    
    def bisiesto(self,f1):
        num_fec = [int(i) for i in f1]
        a1 = num_fec[4]
        a2 = num_fec[5]
        a3 = num_fec[6]
        a4 = num_fec[7]
        
        adef = int(str(a1) + str(a2) + str(a3) + str(a4))

        if adef % 4 != 0:
            print("El año no es bisiesto")
        elif adef % 4 == 0 and adef % 100 != 0:
            print("El año es bisiesto")
        elif adef % 4 == 0 and adef % 100 == 0 and adef % 400 != 0:
            print("El año no es Bisiesto")
        elif adef % 4 == 0 and adef % 100 == 0 and adef % 400 == 0:
            print("El año es Bisiesto")

fec = input("Ingrese un número entero con el formato ddmmaaaa: ")

ejercicio11Variable = Ejercicio11("Ejercicio")
ejercicio11Variable.bisiesto(fec)
