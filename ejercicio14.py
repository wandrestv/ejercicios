class Ejercicio14:
    def __init__(self,titulo):
        self.mensaje = titulo

    def conv_hor_min(args,seg):
        while seg <= 0:
            print("¡ERROR! Tiene que ingresar un número positivo mayor a 0")
            seg = int(input("Ingrese la cantidad en segundos: "))

        min = seg / 60
        hor = seg / 3600
        dia = seg / 86400
            
        print("Hay {} minuto(s) en {} segundos".format(round(min,2),seg))
        print("Hay {} hora(s) en {} segundos".format(round(hor,2),seg))
        print("Hay {} día(s) en {} segundos".format(round(dia,2),seg))

s = int(input("Ingrese la cantidad de segundos: "))
ejecicio14Variable = Ejercicio14("Ejercicio")
ejecicio14Variable.conv_hor_min(s)