nombre_usuario = input("Introduce tu nombre: ")
print("El Nombre es: ", nombre_usuario.upper())
print("El Nombre es: ", nombre_usuario.lower())
print("El Nombre es: ", nombre_usuario.capitalize())

edad = input("Introduce tu edad: ")

while edad.isdigit() == False:
    print("Por Favor, introduce tu edad con numeros")
    edad = input("Introduce tu edad: ")

if int(edad) > 18:
    print("Puede pasar")
else:
    print("no puede pasar")

destacar_comision = lambda comision: "{}$$$ que comision hermano".format(comision) #* funcion format() para formatear strings

comision:float = '1234f124124' #! pense que declarando la variable coo float iba a tener que ser obligado a usar float

print(destacar_comision(comision=comision))
print(comision)

