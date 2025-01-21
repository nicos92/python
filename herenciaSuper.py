class Persona:
    def __init__(self, nombre: str, edad: int, ciudad: str):
        self.Nombre = nombre
        self.Edad = edad
        self.Ciudad = ciudad

    def descripcion(self):
        print("Nombre: ", self.Nombre, "\nEdad: ", self.Edad, "\nCiudad: ", self.Ciudad)


class Empleado(Persona):
    def __init__(
        self, salario: float, antiguedad: int, nombre: str, edad: int, ciudad: str
    ):
        super().__init__(nombre, edad, ciudad)
        self.Salario = salario
        self.Antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.Salario, "\nAntiguaedad: ", self.Antiguedad)


nicolas: Empleado = Persona("nicolas", 32, "Argentina")
nicolas.descripcion()

antonio: Empleado = Empleado(140000., 12, "Antonio", 23, "Santa Fe")
antonio.descripcion()

print(isinstance(antonio, Persona))
