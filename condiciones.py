# CONDICIONES IF primer

print("PROGRAMA DE EVALUCION DE NOTAS DE ALUMNOS")

notaAlumno = input("ingrese la nota del alumno: ")


def evalucion(nota):

    if nota >= 7:
        return "muy bien"
    elif nota >= 4:
        return "bien"
    else:
        return "desaprobado"


nota = int(notaAlumno)
print(evalucion(nota))


edad = int(input("ingrese una edad: "))


def verificarEdad(edad):
    if 0 < edad < 100:
        return "edad Correcta"
    else:
        return "Edad Incorrecta"


print(verificarEdad(edad))


print("PROGRAMA DE BECAS")

distaciaEscuela = int(input("introduce la distacion de la escuela: "))
numeroHermanos = int(input("introduce la cantidad de hermanos: "))
salarioFamiliar = int(input("introduce el salario familiar: "))


def verificarBeca(distanciaEscuela, numerohermanos, salarioFamiliar):
    if distanciaEscuela > 40 and numerohermanos > 4 and salarioFamiliar < 10000:
        return "merece beca"
    else:
        return "no merece beca"


print(verificarBeca(distaciaEscuela, numeroHermanos, salarioFamiliar))

materias = ("lengua", "matematicas", "sociales")

materia = input("escoje una materia: " +  str(materias) +  ": ")

if materia in materias:
    print("se eligio una materia")
