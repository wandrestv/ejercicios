class Ejercicio17:
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def peso(self,peso,alt):

        pesot = peso * 0.453592
        talt = alt / 100
        prom = pesot / (talt ** 2)

        print("El peso en Kilogramos es: {} kg".format(pesot))
        print("Su altura en metros es: {} m".format(talt))
        print("El promedio es: {} ".format(round(prom,2)))

        if prom < 16:
            print("Su categoría es: Criterio de Ingreso.")
        elif prom >= 16 and prom <= 16.9:
            print("Su categoría es: Infra peso.")
        elif prom >= 17 and prom <= 18.4:
            print("Su categoría es: Bajo peso")
        elif prom >= 18.5 and prom <= 24.9:
            print("Su categoría es: Peso normal")
        elif prom >= 25 and prom <= 29.9:
            print("Su categoría es: Sobrepeso")
        elif prom >= 30 and prom <= 34.9:
            print("Su categoría es: Obesidad pre-mórbida")
        elif prom >= 40 and prom <= 45:
            print("Su categoría es: Obesidad mórbida")
        elif prom > 45:
            print("Su categoría es: Obesidad híper-mórbida")

a1 = int(input("Ingrese su peso en libras: "))
a2 = int(input("Ingrese su altura en centímetros: "))

ejercicio17Variable = Ejercicio17("Ejercicio")
ejercicio17Variable.peso(a1,a1)