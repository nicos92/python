import os
import shutil

# * NOMBRE DE LAS NUEVAS CARPETAS QUE SE VAN A CREAR
nuevas_carpetas = ["nicolas", "antonella", "sandoval", "patorenzi"]

# * RUTA DONDE SE VAN A CREAR LAS CARPETAS
ruta = r"C:\Users\nicos92\Pictures"

for carpeta in nuevas_carpetas:
    ruta_completa = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_completa): # ADV SI LA CARPETA NO EXISTE LA CREA
        os.mkdir(ruta_completa)

# * NOMBRE DE LAS CARPETAS QUE SE VAN A ELIMINAR
eliminar_carpetas = ["nicolas", "antonella", "sandoval", "patorenzi"]

# * RUTA DE DONDE SE VAN A ELIMINAR LAS CARPETAS
ruta = r"C:\Users\nicos92\Pictures"

for carpeta in eliminar_carpetas:
    ruta_completa = os.path.join(ruta, carpeta)
    if  os.path.exists(ruta_completa): # ADV SI LA CARPETA EXISTE SE ELIMINA
        shutil.rmtree(ruta_completa)

# * COPIAR CARPETA EN UNA CARPETA NUEVA
import shutil
import asyncio

rutaInicio = r"C:\Users\nicos92\Pictures\NuevaCarpeta2"
rutaFin = r"C:\Users\nicos92\Pictures\NuevaCarpeta3"

print("comenzo tare de copiado de carpeta")
asyncio.create_task(shutil.copytree(rutaInicio, rutaFin))
print("termino la tareA")
