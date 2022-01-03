#¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
class Ejercicio1:
    def tipodedato(self):
        
        
        mensaje1 = "Hola Mundo" #string
        mensaje2 = True         #booleano
        mensaje3 = " "          #string
        mensaje4 = ",,1'"       #string
        mensaje5 = ",,c'"       #string
        mensaje6 = 256          #int
        mensaje7 = 8>19         #booleano

        print("Tipo de variable mensaje 1 es",mensaje1,type(mensaje1))
        print("Tipo de variable mensaje 2 es",mensaje2,type(mensaje2))
        print("Tipo de variable mensaje 3 es",mensaje3,type(mensaje3))
        print("Tipo de variable mensaje 4 es",mensaje4,type(mensaje4))
        print("Tipo de variable mensaje 5 es",mensaje5,type(mensaje5))
        print("Tipo de variable mensaje 6 es",mensaje6,type(mensaje6))
        print("Tipo de variable mensaje 7 es",mensaje7,type(mensaje7))

resultado = Ejercicio1()
resultado.tipodedato()