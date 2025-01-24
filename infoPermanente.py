import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero= genero
        self.edad = edad
        print("Se creo una persona con el nombre " , self. nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas =[]

    def guardarPersonas(self, p):
        self.personas.append(p)


    def verPersonas(self):
        for p in self.personas:
            print(p)

class MiFichero:
    def __init__(self, lista_personas):
        self.__fichero = "ficheroPersonas"
        
        self.ficheroPersonas = open(self.__fichero, "ab+")
        self.ficheroPersonas.seek(0)
        self.verificarCargaPersonas(lista_personas)

    def verificarCargaPersonas(self, lista_personas):
        try:
            lista_personas = pickle.load(self.ficheroPersonas)
            print(len(lista_personas))

        except:
            print("El fichero '{}' esta vacio".format(self.__fichero))
        finally:
            self.ficheroPersonas.close()
            del(self.ficheroPersonas) 

    def guardarPersonasFicheroBinario(self):
        self.ficheroPersonas = open(self.__fichero, "wb")
        pickle.dump(lista_personas, self.ficheroPersonas)
        self.ficheroPersonas.close()
        del(self.ficheroPersonas)


lista_personas = ListaPersonas()
MiFichero(lista_personas)

'''

p1 = Persona("FRAN", "M", 32)
p2 = Persona("MARIA", "F", 33)
p3 = Persona("NICO", "M", 34)
p4 = Persona("ANA", "F", 35)
lista_persona.guardarPersonas(p1)
lista_persona.guardarPersonas(p2)
lista_persona.guardarPersonas(p3)
lista_persona.guardarPersonas(p4)

lista_persona.verPersonas()
'''
