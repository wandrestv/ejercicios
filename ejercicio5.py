class Ejercicio5():
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def resolvente(self,a,b,c):
        
        x1 = ( -b + (((b**2) - (4*a*c)) **0.5)) / (2*a)
        x2 = ( -b - (((b**2) - (4*a*c)) **0.5)) / (2*a)
        print("X1 es igual a {}".format(x1))
        print("X2 es igual a {}".format(x2))

a1 = int(input("Ingrese el valor de A:"))
b1 = int(input("Ingrese el valor de B:"))
c1 = int(input("Ingrese el valor de C:"))

ejercicio5Variable = Ejercicio5("Ejercicio")
ejercicio5Variable.resolvente(a1,b1,c1)