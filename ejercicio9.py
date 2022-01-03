class Ejercicio9:
    def __init__(self, titulo):
        self.mensaje = titulo
    
    def binario(self,nbin):
        ndecimal = 0
        
        for posi, digistring in enumerate(nbin[::-1]):
            ndecimal += int(digistring) * 2 ** posi

        print("El valor del número binario: {}".format(ndecimal))
    
nbina = input("Ingrese un número binario de 4 dígitos ")

ejercicio9Variable = Ejercicio9("Ttitulo")
ejercicio9Variable.binario(nbina)