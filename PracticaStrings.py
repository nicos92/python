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

