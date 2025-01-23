from io import open

"""
archivo_txt = open("archivo.txt", "w")  # ? si el archivo no existe lo crea y luego abre el archivo en modo escritura (write)

frase = " estupendo dia para estudiar python"

archivo_txt.writelines(frase)

archivo_txt.close()


archivo_txt = open(
    "archivo.txt", "a"
)  # ? si el archivo no existe lo crea y luego abre el archivo en modo agregar texto (append)

archivo_txt.write("\nFirma Nicolas")
archivo_txt.close()
archivo_txt = open(
    "archivo.txt", "r"
)  # ? si el archivo no existe lo crea y luego abre el archivo en modo lectura (read)

texto = archivo_txt.read()
archivo_txt.close()
print(texto)

archivo_txt = open(
    "archivo.txt", "r"
)  # ? si el archivo no existe lo crea y luego abre el archivo en modo lectura (read)

texto = archivo_txt.readlines()
archivo_txt.close()
print(texto)
for linea in texto:
    print(linea)


"""

archivo = open("Archivo2.txt", "r+") # con el r+ se abre en modo escritura y lectura

# archivo.seek(5)
# print(archivo.read(2))
# print(archivo.read())
archivo.seek(0)
archivo.seek(len(archivo.read())/2)
print(archivo.read())
archivo.seek(0)

lineasTexto = archivo.readlines()

lineasTexto[1]= "esto esta cambiado por mi en python"
archivo.seek(0)
archivo.writelines(lineasTexto)
archivo.seek(0)
print(archivo.read())

archivo.close()
