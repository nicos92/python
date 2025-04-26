def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kgargs):
        # adv acciones adicionales que decorar
        print("Vamos a realizar un calculo: ")

        funcion_parametro(*args, **kgargs)

        # adv acciones adicionales que decorar
        print("Hemos terminado el calculo")

    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 -num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base=base, exp=exponente))
suma(10,15, 5)

resta(15,10)

potencia(5,3)

