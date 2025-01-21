# GENERADORES

"""
Generadores ¿Qué son?
• Estructuras que extraen valores de una función y se almacenan en objetos iterables (que se
pueden recorrer).
• Estos valores se almacenan de uno en uno.
• Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que
se solicita el siguiente. Esta característica es conocida como "suspensión de estado".

| Generadores ¿Qué utilidad tienen?
+ Son más eficientes que las funciones tradicionales
+ Muy útiles con listas de valores infinitos
+ Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno.
+ Adicionalmente puede utilizar un return
"""


def generadorPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


guardaPares = generadorPares(8)

# * aprendiendo a usar generadores


# adv el bucle for no es una buena forma de usar el generador
"""
#! no poner un for antes por que sino el next ya no cumple su funcion
for i in guardaPares:
    print("lista: ", i)
"""
# mejor usar el metodo next

print(next(guardaPares))

print(       "Lineas de codigo al azar")

print(next(guardaPares))

print(           "Lineas de codigo al azar")


# * Yield from

# * Utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidados

# adv "*ciudades" puede recibiar 1 o varios elementos, numero indeterminado de elementos. los va reciir en forma de tupla
def devuelveCiudades(*ciudades):
    for elemto in ciudades:
        for subElem in elemto:
            yield subElem


guardaCiudades = devuelveCiudades("Buenos aires", "Cordoba", "Mendoza", "La Pampa")

print(next(guardaCiudades))
print(next(guardaCiudades))

# * Yield from
# // Yield from
# todo Yield from
# adv Yield from
# ? Yield from
# ! Yield from
# - Yield from 


# * Utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidados
# * usando yields from
# adv "*ciudades" puede recibiar 1 o varios elementos, numero indeterminado de elementos. los va reciir en forma de tupla
def devuelveCiudadess(*ciudades):
    for elemto in ciudades:
        yield from elemto


guardaCiudadess = devuelveCiudadess("Buenos aires", "Cordoba", "Mendoza", "La Pampa")


print(next(guardaCiudadess))
print(next(guardaCiudadess))

for a in range(len([1,2,2,2,2,2,2,2,2])):
    print(a)
