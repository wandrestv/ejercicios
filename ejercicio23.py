class Ejercicio23:
    def __init__(self,titulo):
        self.mensaje = titulo

    def num_prim(self,n1):
        cont = 0
        for a in range(1,n1+1):
            if n1 % a == 0:
                cont += 1
        if cont == 2:
            print("Es un número primo")
        else:
            print("No es un número primo")

a1 = int(input("Ingrese un número: "))
ejercicio23Variable = Ejercicio23("Ejercicio")
ejercicio23Variable.num_prim(a1)