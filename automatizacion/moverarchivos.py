import os
import shutil
import tkinter

# Ruta donde se van a ordenar los archivos y se crean carpetas con las extensiones de los archivos

rutainicial = "C:/Users/nicos92/Downloads"

for archivo in os.listdir(rutainicial):
    
    nombre, extension = os.path.splitext(archivo)
    
    ruta_carpeta = os.path.join(rutainicial, extension)
    print(ruta_carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    shutil.move(os.path.join(rutainicial, archivo), os.path.join(ruta_carpeta, archivo))