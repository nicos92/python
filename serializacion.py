import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb")

pickle.dump(obj=lista_nombres, file=fichero_binario)

