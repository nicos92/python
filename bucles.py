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

print("final del programita")

palabra = "nicolas"
for letra in palabra:
    print("entrando al primer for")
    if letra == "o":
        continue
    print(letra )
print("")

