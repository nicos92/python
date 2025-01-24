import pickle


class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se creo una persona con el nombre ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class FicheroPersonas:

    personas = []

    def __init__(self):
        self.__fichero = "ficheroPersonas"

        self.ficheroPersonas = open(self.__fichero, "ab+")
        self.ficheroPersonas.seek(0)
        self.verificarCargaPersonas()

    def verificarCargaPersonas(self):
        try:
            self.personas = pickle.load(self.ficheroPersonas)
            print(len(self.personas))

        except:
            print("El fichero '{}' esta vacio".format(self.__fichero))
        finally:
            self.ficheroPersonas.close()
            del self.ficheroPersonas

    def guardarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasFicheroBinario()

    def verPersonas(self):
        print("La info del fichero binario es: ")
        for p in self.personas:
            print(p)

    def guardarPersonasFicheroBinario(self):
        self.ficheroPersonas = open(self.__fichero, "wb")
        pickle.dump(self.personas, self.ficheroPersonas)
        self.ficheroPersonas.close()
        del self.ficheroPersonas


miLista = FicheroPersonas()

p1 = Persona("FRAN", "M", 32)
p2 = Persona("MARIA", "F", 33)
p3 = Persona("NICO", "M", 34)
p4 = Persona("ANA", "F", 35)
miLista.guardarPersonas(p2)
miLista.guardarPersonas(p3)
miLista.guardarPersonas(p4)

miLista.guardarPersonas(p1)
miLista.verPersonas()




