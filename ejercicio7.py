class Ejercicio7:
    def __init__(self, titulo):
        self.mensaje = titulo

    def parimpar(self, n1):
        if n1 % 2 == 0:
            print("El número {} es par".format(n1))
        else:
            print("El número {} es impar".format(n1))


a1 = float(input("Ingrese un número: "))
ejercicio7Variable = Ejercicio7("Ejercicio")
ejercicio7Variable.parimpar(a1)