class Coche:

    # * Metodo constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False
        self.__conbustible = False
        

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
            return("El coche no tiene combustible")    
		
        
    def __ChequeoInterno(self):
        print("Verificando que haya combustible")
        return self.__conbustible
        
    def VerDatos(self):
        return "el Coche tiene: ", self.__largoChasis, " de largo, ", self.__anchoChasis, " de ancho, ", self.__ruedas, " ruedas"


coche1 = Coche()  # * instanciacion de una clase sin el new como en otros lenguajes

#//print("Ancho del coche: ", coche1.__anchoChasis)
#//print("Largo del coche: ", coche1.__largoChasis)
#//print("El coche tiene: ", coche1.__ruedas, " ruedas")

print(coche1.Estado())
coche1.Arrancar(True)

print(coche1.Estado())


print(coche1.VerDatos())
print(coche1.VerDatos())