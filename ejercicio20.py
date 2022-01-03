class Ejercicio20: 
    def __init__(self,titulo):
        self.mensaje = titulo

    def descuento(self,prec):
        if prec > 1000:
            tot_pag = prec * 0.80
            print("El total a pagar aplicando el descuento es: {} $".format(tot_pag))
        else:
            print("El total a pagar es: {} $".format(prec))

a1 = float(input("Ingrese el precio a pagar: "))
ejercicio20Variable = Ejercicio20("Ejercicio")
ejercicio20Variable.descuento(a1)