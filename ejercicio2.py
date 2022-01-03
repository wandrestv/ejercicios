class Ejercicio1:
    def variableDelResultado(self):

        #operación 1
        num1 = 5
        num2 = 3
        num3 = 2
        num4 = 9
        num5 = 3
        num6 = 5
        num7 = 14
        num8 = 3

        resp = (num1 + num2 * num3) + num4 > num5 * num6 * num7 % num8
        print("El tipo de variable del resultado es",resp,type(resp))
        import gc
        gc.collect()

        #operación 2
        num1 = 2
        num2 = 4
        num3 = 10
        num4 = 8
        num5 = 2
        num6 = 36
        num7 = 1
        num8 = 2

        resp = num1 * (num2 - num3 + num4) / num5 * num6 * (num7 / num8)
        print("El tipo de variable del resultado es",resp,type(resp))
        import gc
        gc.collect

        #operacion 3
        num1 = 260
        num2 = 12
        num3 = 54
        num4 = 3
        num5 = 85
        num6 = 7

        resp = num1 / num2 + num3 % num4 - num5 % num6
        print("El tipo de variable del resultado es",resp,type(resp))
        import gc
        gc.collect

        #operacion 4
        num1 = 48
        num2 = 2
        num3 = 3
        num4 = 2
        num5 = 7
        num6 = 12

        resp = (num1 < num2 * num3) or (num4 * num5 < num6)
        print("El tipo de variable del resultado es",resp,type(resp))
        import gc
        gc.collect

        #operación 5
        num1 = 8
        num2 = 2
        num3 = 932
        num4 = 23
        num5 = 4
        num6 = 2

        resp = ((num1 > num2) or (num3 < num4)) and num5 == num6
        print("El tipo de variable del resultado es",resp,type(resp))

resultado = Ejercicio1()
resultado.variableDelResultado()