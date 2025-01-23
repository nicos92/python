from io import open
'''
archivo_txt = open("archivo.txt", "w")  # ? si el archivo no existe lo crea y luego abre el archivo

frase = " estupendo dia para estudiar python"

archivo_txt.writelines(frase)

archivo_txt.close()
'''

archivo_txt = open(
    "archivo.txt", "a"
)  # ? si el archivo no existe lo crea y luego abre el archivor

archivo_txt.write("\nFirma Nicolas")
archivo_txt.close()
archivo_txt = open(
    "archivo.txt", "r"
)  # ? si el archivo no existe lo crea y luego abre el archivor

texto = archivo_txt.read()
archivo_txt.close()
print(texto)

archivo_txt = open(
    "archivo.txt", "r"
)  # ? si el archivo no existe lo crea y luego abre el archivor

texto = archivo_txt.readlines()
archivo_txt.close()
print(texto)
for linea in texto:
    print(linea)
