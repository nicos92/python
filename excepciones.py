"""
Excepciones ¿Qué son?
» Las excepciones son errores que ocurren durante la ejecución del programa.
La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado",

+ Este tipo de errores de ejecución se pueden
controlar para que la ejecución del programa
continue. Es lo que se conoce como manejo o
control de excepciones.
"""

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("no se puede dividir por cero")
        return "operacion invalida"
while True:
    try:
        op1 = int(input("Introduce el primer numero: "))
        op2 = int(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("ingreso invalido de numero")
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
    except:
        print("Ha ocurrido un error")
    finally:
        print("Ingresos Correctos")

operacion = input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")
