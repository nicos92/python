import math

error = 0


while error <= 10:
    error = error + 1
    print("Error: ", error)

print(math.sqrt(12))
print("fin")
lista = ["verano", "otoño", "invierno", "primavera"]
for i in lista:
    print(i)

palabra = "antonella"
for i in palabra:
    print(i, end="")
print("")
for a in range(19, 28, 2):
    print(f"el valor del rango es: {a}")

print("")

    
print(        "final del programita")

palabra = "nicolas salomon sandoval"
contador = 0
for letra in palabra:
    if letra == " ":
        continue
    contador+=1
    print(letra )
print("contadodr ", contador)

print(contador)


'''
while True: # se utiliza para usar con Ctl + c
    pass

'''

class MiClase:
    pass # Para implementar más tarde

email = input("Ingrse su email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print("arroba: " , arroba)

