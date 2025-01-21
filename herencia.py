# adv HERENCIA
# * Para reutilizar código en caso de crear objetos similares


class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            "Marca: ",
            self.marca,
            "\nModelo: ",
            self.modelo,
            "\nEn Marcha: ",
            self.enMarcha,
            "\nAcelera: ",
            self.acelera,
            "\nFrena: ",
            self.frena,
        )


class Furgoneta(Vehiculo):
    def carga(self, cargar: bool):
        self.cargado = cargar
        if self.cargado:
            return "La Furgoneta esta cargada"
        else:
            return "La Furgoneta esta vacia"


class Moto(Vehiculo):
    caballito = ""

    def HaceCaballito(self):
        self.caballito = "voy haciendo caballito"

    def estado(self):
        print(
            "Marca: ",
            self.marca,
            "\nModelo: ",
            self.modelo,
            "\nEn Marcha: ",
            self.enMarcha,
            "\nAcelera: ",
            self.acelera,
            "\nFrena: ",
            self.frena,
            "\n",
            self.caballito,
        )

class VElectricos():
    def __init__(self, marca:str, modelo:str):
        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True


class BicicletaElectrica(VElectricos, Vehiculo):
    pass

miBici = BicicletaElectrica("Vairo", "Totem")
miBici.estado()




miMoto = Moto("Zanella", "Sol")
miMoto.HaceCaballito()
miMoto.estado()

miFurgoneta = Furgoneta("Ford", "Rural")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
