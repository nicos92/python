

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

