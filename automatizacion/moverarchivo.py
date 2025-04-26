import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import shutil
import sys


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Mover Archivos")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Variable para almacenar la ruta seleccionada
        self.ruta_seleccionada = tk.StringVar()

        # Configuración del estilo
        self.estilo = ttk.Style()
        self.estilo.configure("TFrame", background="#f0f0f0")
        self.estilo.configure("TButton", font=("Arial", 10), padding=5)
        self.estilo.configure("TLabel", background="#f0f0f0", font=("Arial", 10))

        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Frame para la selección de carpeta
        self.frame_seleccion = ttk.Frame(self.frame_principal)
        self.frame_seleccion.pack(fill=tk.X, pady=(0, 20))

        # Etiqueta y entrada para la ruta
        ttk.Label(self.frame_seleccion, text="Carpeta:").pack(side=tk.LEFT)

        self.entrada_ruta = ttk.Entry(
            self.frame_seleccion, textvariable=self.ruta_seleccionada, width=50
        )
        self.entrada_ruta.pack(side=tk.LEFT, padx=5)

        # Botón para buscar carpeta
        self.boton_buscar = ttk.Button(
            self.frame_seleccion, text="Buscar...", command=self.buscar_carpeta
        )
        self.boton_buscar.pack(side=tk.LEFT)

        # Frame para el botón de ejecución
        self.frame_ejecucion = ttk.Frame(self.frame_principal)
        self.frame_ejecucion.pack(fill=tk.X)

        # Botón para ejecutar tarea
        self.boton_ejecutar = ttk.Button(
            self.frame_ejecucion,
            text="Ejecutar Tarea",
            command=self.ejecutar_tarea,
            state=tk.NORMAL,
        )
        self.boton_ejecutar.pack(pady=10)

        # Área de registro (simulado)
        self.frame_registro = ttk.Frame(self.frame_principal)
        self.frame_registro.pack(fill=tk.BOTH, expand=True)

        self.texto_registro = tk.Text(
            self.frame_registro, height=10, wrap=tk.WORD, font=("Consolas", 9)
        )
        self.texto_registro.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.texto_registro)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_registro.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.texto_registro.yview)

        # Configurar grid weights para que los frames se expandan correctamente
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(1, weight=1)

    def buscar_carpeta(self):
        """Abre un diálogo para seleccionar una carpeta y actualiza la entrada de texto."""
        carpeta_seleccionada = filedialog.askdirectory(
            title="Seleccionar carpeta", initialdir=os.path.expanduser("~")
        )

        if carpeta_seleccionada:
            self.ruta_seleccionada.set(carpeta_seleccionada)
            self.agregar_log(f"Carpeta seleccionada: {carpeta_seleccionada}")

    def ejecutar_tarea(self):
        """Ejecuta la tarea principal de la aplicación."""
        ruta = self.ruta_seleccionada.get()

        if not ruta:
            messagebox.showerror("Error", "Por favor, seleccione una carpeta primero.")
            return
        if not os.path.exists(ruta):
            messagebox.showerror("Error", "La Carpeta no existe.")
            return

        self.texto_registro.delete(1.0, tk.END)
        self.texto_registro.see(tk.END)
        self.texto_registro.update()
        self.agregar_log("Iniciando tarea...")
        self.boton_ejecutar.config(state=tk.DISABLED)

        try:
            # Simular una tarea que toma tiempo
            self.root.after(1000, self.simular_tarea)
        except Exception as e:
            self.agregar_log(f"Error: {str(e)}")
            self.boton_ejecutar.config(state=tk.NORMAL)

    def simular_tarea(self):
        """Simula una tarea que procesa archivos en la carpeta seleccionada."""
        ruta = self.ruta_seleccionada.get()

        # Aquí iría el código real de procesamiento
        # Por ahora solo simulamos
        self.agregar_log(f"Procesando archivos en: {ruta}")
        self.ordenar_carpeta()
        self.agregar_log("Tarea completada con éxito.")

        self.boton_ejecutar.config(state=tk.NORMAL)
        messagebox.showinfo("Éxito", "La tarea se ha completado correctamente.")

    def ordenar_carpeta(self):
        ruta = self.ruta_seleccionada.get()
        for archivo in os.listdir(ruta):
            print(archivo)
            _, extension = os.path.splitext(archivo)

            ruta_carpeta = os.path.join(ruta, extension)

            if not os.path.exists(ruta_carpeta):
                self.agregar_log(f"Creando Carpeta {ruta_carpeta}")
                os.makedirs(ruta_carpeta)
            shutil.move(
                os.path.join(ruta, archivo), os.path.join(ruta_carpeta, archivo)
            )

    def agregar_log(self, mensaje):
        """Agrega un mensaje al área de registro."""
        self.texto_registro.insert(tk.END, mensaje + "\n")
        self.texto_registro.see(tk.END)
        self.texto_registro.update()

# https://youtu.be/diZ4a4pTtUU?si=zzoxh0wpOUwMkWXx
def resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, útil para PyInstaller"""
    try:
        base_path = sys._MEIPASS  # Carpeta temporal de PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = tk.Tk()
    # Cargar el icono
    icon_path = resource_path("icons8-carpeta-de-documentos-32.ico")
    try:
        root.iconbitmap(icon_path)
    except tk.TclError:
        print("No se pudo cargar el icono")  # Manejo de errores
    app = Aplicacion(root)
    root.mainloop()
