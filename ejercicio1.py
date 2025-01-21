email = input("Introduce tu Email: ")


def validarEmail(email: str):
    cantArrobas: int = email.count("@")
    #!validarCantArrobas: bool = lambda cantArrobas: cantArrobas != 1
    #!valCantArrobas = validarCantArrobas(cantArrobas)
    comienzaArroba: bool = email.startswith("@")
    terminaArroba: bool = email.endswith("@")
    return (validarCantArrobas(cantArrobas), comienzaArroba, terminaArroba)

def validarCantArrobas(cantArrobas: int):
    return cantArrobas != 1

valCantArrobas, comienzaArroba, terminaArroba = validarEmail(email=email)

while valCantArrobas or comienzaArroba or terminaArroba:
    print("El mail no es valido")
    if comienzaArroba:
        print("Su email comienza con un @")

    if terminaArroba:
        print("Su email termina con un @")

    if valCantArrobas:
        print("Su email tiene mas de 1 o ningun @")

    email = input("Por favor ingrese un email valido: ")

    valCantArrobas, comienzaArroba, terminaArroba = validarEmail(email=email)

print("Ingreso Coorecto: ", email)
