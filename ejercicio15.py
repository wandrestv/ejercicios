class Ejercicio15:
    def __init__(self,titulo):
        self.mensaje = titulo

    def num_may(self,n1,n2,n3):
        while n1 < 0 or n2 < 0 or n3 < 0:
            print("#$¡ ERROR !$# Los números ingresados deben ser mayores a 0")
            n1 = int(input("Ingrese el primer número"))
            n2 = int(input("Ingrese el segundo número"))
            n3 = int(input("Ingrese el tercer número"))
        
        if n1 > n2:
            if n1 > n3:
                print("El número {} es el mayor".format(n1))
            else:
                print("El número {} es el mayor".format(n3))
        elif n2 > n3:
            print("El número {} es el mayor".format(n2))
        else:
            print("El número {} es el mayor".format(n3))

a = int(input("Ingrese el primer número(entero positivo): "))
b = int(input("Ingrese el segundo número(entero positivo): "))
c = int(input("Ingrese el tercer número(entero positivo): "))

ejercicio15Variable = Ejercicio15("Ejercicio")
ejercicio15Variable.num_may(a,b,c)
