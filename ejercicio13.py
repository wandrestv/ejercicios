class Ejercicio13:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def equi_seg(self,hor,min):
        tot_ho = hor * 3600
        tot_mi = min * 60
        tot_seg = tot_ho + tot_mi

        print("Hay {} segundos en {} horas y {} minutos".format(tot_seg,hor,min))

h1 = int(input("Ingrese las horas a convertir: "))
m1 = int(input("Ingrese los minutos a convertir: "))

ejercicio13Variable = Ejercicio13("Ejercicios")
ejercicio13Variable.equi_seg(h1, m1)
