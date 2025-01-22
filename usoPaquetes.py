from calculos.calculosGral import divir, multiplicar, redondear
from calculos.clases.vehiculos import Camion

print(divir(2, 2))
print(multiplicar(3, 4))

print(redondear(2.51))
print(redondear(2.5))

camion1 = Camion()
camion1.desplazamiento()