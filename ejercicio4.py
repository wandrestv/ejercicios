class Ejercicio4:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def operacion(self, nu1, nu2):
        suma = nu1 + nu2
        resta = nu1 - nu2
        multiplicacion = nu1 * nu2
        modulo = nu1 // nu2
        print("La suma de {} y {} es {}".format(nu1,nu2,suma))
        print("La resta de {} y {} es {}".format(nu1,nu2,resta))
        print("La multiplicación de {} y {} es {}".format(nu1,nu2,multiplicacion))
        print("El módulo de {} y {} es {}".format(nu1,nu2,modulo))


a1 = int(input("Ingrese el primer número "))
a2 = int(input("Ingrese el segundo valor "))
ejercicio4Variable = Ejercicio4("Ejercicios")
ejercicio4Variable.operacion(a1,a2)