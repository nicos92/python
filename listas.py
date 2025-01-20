
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

