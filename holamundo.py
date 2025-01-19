mensaje = "hola mundo, estoy aprendiendo python"
print(mensaje)


def funfor():

    for a in range(4):
        a+1
        print(a)

# esto es un comentario de una sola linea
"""
esto es un comentario multilinea
"""
'''
esto tambien
'''


nombre = "nicolas"
print(nombre)


def suma(num1, num2):
    """funcion para sumar dos numero

    Args:
        num1 (int): primer numero
        num2 (int): segundo numero

    Returns:
        int: resultado de la suma
    """
    return num1 + num2

print(suma(3,5))


miLista = ["maria", "pepe", "Marta", "antonio", 5, 34.3] # un array puede ser de varios tipos de datos
print(miLista[:])       # imprime todo con corchetes
print(miLista[3])       # imiprime solo el indice indicado
print(miLista[1:3])     # imprime hasta el limite no incluido

miLista.extend(["marcos", "Fabian"]) # añade elementos a la lista

print(miLista[:])

print(miLista.index("pepe")) # busca el elemento y nos devuelve su indice o el inidice del primer elemento igual que encuentra

print("marcos" in miLista) # nos devuelve true o false si encuentra el elemento en la lista

miLista.remove("Fabian") # si encuentra el elemento lo elimina
miLista.pop() # elimina el ulltimo elemento de la lista
print(miLista[:])

miLista2 = ["anto","nico"]

miLista3 = miLista + miLista2 
print("mi lista 3" , miLista3[:])
print("mi lista 3 * 3" , miLista3[:]*3)

# TUPLAS
# comenzando a ver tuplas
'''
las tuplas son inmutables.
no las podemos modificar
no permiten busquedas.
no permiten añadir, eliminar, mover elementos.
si permite comprobar si un elemento se encuentra en la tupla

son mas rapidas.
menos epsacio (mayor optimizacion)
formatean strings
pueden utilizarse como claves de un diccionario

sintaxis de las tuplas:
nombre_tupla = (elem1, elem2, elem3 ...)
'''

miTupla = ("primerp", "segundo", "tercero")
print(miTupla[2]) # imprime en colsola el elemento del indice indicado

miLista4 = list(miTupla) # convierte una tupla en una lista
print(miLista4)

mitupla2 = tuple(miLista) # convierte una lista en una tupla
print(mitupla2)

print("pepe"in mitupla2) # devuelve un booleano si encuenta el elemento en la tupla

print(mitupla2.count("pepe")) # devuelte un int de la cantidad de veces que encuentra elemento indicado

print(len(mitupla2)) # devuelve un int d ela cantidad de elementos que tiene la tupla

miTupla3 = "t1", "t2","t3" # es posible no poner los parentis para declarar tuplas, se lo conoce como empaquetado de tuplas.

miTupla4 = ("nico", 14, 6, 1992)
nombre, dia, mes, agno = miTupla4 # desempaquetado de tupla

print(miTupla4)
print(nombre, " ", dia, " ", mes, " ", agno)

# DICCIONARIOS

'''
¿Qué son los diccionarios? 
* Estructura de datos que nos permite almacenar valores de diferente tipo (enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios. 
* La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociación de tipo clave : valor para cada elemento almacenado.
* Los elementos almacenados no están ordenados. El orden es indiferente a la hora de almacenar información en un diccionario.
'''

miDiccionario = {"Argentina":"Buenos aires", "Francia":"Paris", "Brasil":"Brasilia"}
print(miDiccionario["Argentina"]) # se ingresa al valor a traves de la clave

print(miDiccionario["Brasil"])

miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)
miDiccionario["Italia"] = "Roma" # modifica el valor de la clave
print(miDiccionario)

del miDiccionario["Italia"] # el,mina la clave y el valor del diccionario
print(miDiccionario)
miDiccionario2 = {"Alemiania": "Berlin", 23:"Jordan","Mosqueteros": 3}
mitupla5 = ("España", "Francia", "Reino Unido")
miDiccionario3 = {mitupla5[0]: "Madrid",
                mitupla5[1]:"Paris",
                mitupla5[2]:"Londres"}

print(miDiccionario3[mitupla5[0]])
michaelJordan = {"numero": 23, "nombre":"Michael","apellido":"Jordan","anillos": {"temporadas":[1992,1993]}}
print(michaelJordan.keys())
print(michaelJordan.values())
print(len(michaelJordan))
print(michaelJordan["anillos"])
print(michaelJordan["anillos"]["temporadas"])
print(michaelJordan["anillos"]["temporadas"][0])

