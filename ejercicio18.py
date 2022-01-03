class Ejercicio18: 
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def tdias(self,dia,mes):
        dmes = [00,31,28,31,30,31,30,31,31,30,31,30,31]
        b = 0
        acum = 0
        while b <= mes - 1:
            acum = acum + dmes[b]
            b = b + 1
        tot = acum + dia
        print("Han transcurrido {} días desde el 1 de enero del 2014".format(tot))


a1 = int(input("Ingrese un día del mes: "))
while a1 <= 0 or a1 > 31:
    print("El {} es un número no válido".format(a1))
    a1 = int(input("Ingrese un día del mes: "))
a2 = int(input("Ingrese un mes del año 2014: "))
while a2 <= 0 or a2 > 12:
    print("El {} es un número no válido")
    a2 = int(input("Ingrese un mes del año 2014: "))

ejercicio18Variable = Ejercicio18("Ejercicio")
ejercicio18Variable.tdias(a1,a2)
