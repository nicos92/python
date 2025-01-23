import pickle

# * guardar datos en formato binario
lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb") #* abre el archivo en formato binario

pickle.dump(obj=lista_nombres, file=fichero_binario)

fichero_binario.close() #* para cerrar el archivo
del(fichero_binario) #* se borra de la memoria

fichero = open("lista_nombres", "rb") #* abre elarchivo con lectura binaria
carga_nombres = pickle.load(fichero) #* guarda los datos en la lista
print(carga_nombres)


class Coche:

    # * Metodo constructor
    def __init__(self, marca, modelo):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False
        self.__conbustible = False
        self.__marca=marca
        self.__modelo=modelo

    def Arrancar(
        self, arrancamos
    ):  # adv 'self' hace referencia al propio objeto. 'this'
        self.__enMarcha = arrancamos
        self.Estado()

    def Estado(self):
        if self.__conbustible:
            if self.__enMarcha:
                return "El coche está en marcha"
            else:
                return "El coche está detenido"
        else:
            return "El coche no tiene combustible"

    def __ChequeoInterno(self):
        print("Verificando que haya combustible")
        return self.__conbustible

    def VerDatos(self):
        return (
            "Marca: ", self.__marca,
            "Modelo: ", self.__modelo,
            "el Coche tiene: ",
            self.__largoChasis,
            " de largo, ",
            self.__anchoChasis,
            " de ancho, ",
            self.__ruedas,
            " ruedas",
        )


coche1 = Coche("Renault", "Kiwi")
coche2 = Coche("Chevrolet", "Cruze")
coche3 = Coche("Ford", "focus")

lista_coches = [coche1,coche2,coche3]

file_coche = open(file="file_coche2", mode="wb")
pickle.dump(lista_coches, file_coche)
file_coche.close()
del(file_coche)

file_coche = open(file="file_coche2",mode= "rb")
lista_coches2 = pickle.load(file_coche)

for coche in lista_coches2:

    print(coche.VerDatos())
file_coche.close()
del(file_coche)

