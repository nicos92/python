import math
def evaluaEdad(edad):
    if edad < 0:
        raise ZeroDivisionError(
            "No se permiten edades negativas"
        )  # // MiPropioError("No se permiten edades negativas")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres Joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"


print(evaluaEdad(0))


def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("EL NUMERO NO PUEDE SER NEGATIVO")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un número: "))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Programa terminado")