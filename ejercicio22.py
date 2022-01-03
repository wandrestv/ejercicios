class Ejercicio22:
    def __init__(self,titulo):
        self.mensaje = titulo

    def capicua2(self,n1):
        num_cap = [int(i) for i in n1]
        a1 = num_cap[0]
        a2 = num_cap[1]
        a3 = num_cap[2]
        a4 = num_cap[3]
        a5 = num_cap[4]
        
        if a1 == a5:
            if a2 == a4:
                print("El número {} es capicúa".format(n1))
            else:
                print("El número {} no es capicúa".format(n1))
        else:
            print("El número {} no es capicúa".format(n1))

b1 = input("Ingrese un número de 5 dígitos: ")

ejercicio12Variable = Ejercicio22("Ejercicio")
ejercicio12Variable.capicua(b1)