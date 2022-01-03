class Ejercicio19:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def fecha(self,f1):
        if f1 == 1:
            print("El número {} corresponde al mes de Enero".format(f1))
        elif f1 == 2:
            print("El número {} corresponde al mes de Febrero".format(f1))
        elif f1 == 3:
            print("El número {} corresponde al mes de Marzo".format(f1))
        elif f1 == 4:
            print("El número {} corresponde al mes de Abril".format(f1))
        elif f1 == 5:
            print("El número {} corresponde al mes de Mayo".format(f1))
        elif f1 == 6:
            print("El número {} corresponde al mes de Junio".format(f1))
        elif f1 == 7:
            print("El número {} corresponde al mes de Julio".format(f1))
        elif f1 == 8:
            print("El número {} corresponde al mes de Agosto".format(f1))
        elif f1 == 9:
            print("El número {} corresponde al mes de Septiembre".format(f1))
        elif f1 == 10: 
            print("El número {} corresponde al mes de Octubre".format(f1))
        elif f1 == 11:
            print("El número {} corresponde al mes de Noviembre".format(f1))
        else:
            print("El número {} corresponde al mes de Diciembre".format(f1))

a1 = int(input("Ingrese un número entre el 1 y el 12: "))
while a1 <= 0 or a1 > 12:
    print("Número incorrecto")
    a1 = int(input("Ingrese un número entre el 1 y el 12: "))

ejercicio19Variable = Ejercicio19("Ejercicio")
ejercicio19Variable.fecha(a1)
