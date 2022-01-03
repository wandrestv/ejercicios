class Ejercicio21: 
    def __init__(self,titulo):
        self.mensaje = titulo

    def digitos(self,n1):
        cont = len(str(n1))
        print("El número ingresado tiene {} dígito(s)".format(cont))

a1 = int(input("Ingrese un número entero"))
ejercicio21Variable = Ejercicio21("Ejercicio")
ejercicio21Variable.digitos(a1)
