class Coche:
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def Arrancar(self):  # adv 'self' hace referencia al propio objeto. 'this'
        self.enMarcha = True

    def Estado(self):
        if self.enMarcha:
            return "El coche está en marcha"
        else:
            return "El coche está detenido"


coche1 = Coche()  # * instanciacion de una clase sin el new como en otros lenguajes

print("Ancho del coche: ", coche1.anchoChasis)
print("Largo del coche: ", coche1.largoChasis)
print("El coche tiene: ", coche1.ruedas, " ruedas")

print(coche1.Estado())
coche1.Arrancar()

print(coche1.Estado())
