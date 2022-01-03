class Ejercicio16:
    def __init__(self,titulo):
        self.mensaje = titulo

    def estacionamiento(self,hora_e,tiempo,hora_s,sis_hora):
        t_hora = hora_s - hora_e
        tp = t_hora * 4
        if tiempo > 30:
            tpm = tp + 2.50
            print("El total a pagar es {}$".format(tpm))
        else:
            print("El total a pagar es: {}$".format(tp))
a1 = int(input("Ingrese la hora en formato 12 horas en la que ingresó su vehículo al estacionamiento: "))
while a1 < 0 or a1 > 12:
    print("#$¡ ERROR !$# La hora ingresada no es válida")
    a1 = int(input("Ingrese la hora en formato 12 horas en la que ingresó su vehículo al estacionamiento: "))

a2 = int(input("Ingrese el tiempo en minutos: "))
while a2 < 0 or a2 > 60:
    print("#$¡ ERROR !$# El tiempo ingresado no es válido")
    a2 = int(input("Ingrese el tiempo en minutos: "))

a3 = int(input("Ingrese la hora de salida en formato 12 horas: "))
while a3 < 0 or a3 > 12:
    print("#$¡ ERROR !$# La hora ingresada no es válida")
    a3 = int(input("Ingrese la hora de salida en formato 12 horas: "))

a4 = str(input("Ingrese la letra 'A' si es AM y la letra 'P' si es PM respectivamente: "))
while a4 != 'a' and a4 != 'A' and a4 != 'p' and a4 != 'P':
    print("#$¡ ERROR !$# La letra ingresada no es correcta con respecto al sistema horario")
    a4 = str(input("Ingrese la letra 'A' si es AM y la letra 'P' si es PM respectivamente: "))

ejercicio16Variable = Ejercicio16("Ejercicio")
ejercicio16Variable.estacionamiento(a1,a2,a3,a4)