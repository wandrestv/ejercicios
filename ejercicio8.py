class Ejercicio8:
    def __init__(self,titulo):
        self.mensaje = titulo
        
    def paridad(self,a1):
        num_int = [int(i) for i in a1]
        b = num_int.count(1)
        if b % 2 == 0:
            print("El bit de paridad es impar")
        else:
            print("El bit de paridad es par")
        print(b)

a1 = input("Ingrese el número binario ")

ejecicio8Variable = Ejercicio8("Titulo")
ejecicio8Variable.paridad(a1)
