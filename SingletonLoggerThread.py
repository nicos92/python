import threading
from datetime import datetime


class Logger:
    _instance = None
    _lock = threading.Lock()  # Bloqueo para sincronizar el acceso

    def __new__(cls, *args, **kwargs):
        # Usamos el bloqueo para asegurar que solo un hilo pueda crear la instancia
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, log_file: str):
        # Usamos el bloqueo para asegurar que la inicialización sea thread-safe
        with self._lock:
            if not self._initialized:
                self.log_file = log_file
                self._initialized = True

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")
        print(datetime.now(), end=" ")
        print(f"Log: {message}")


"""


# Función para probar el Logger en un entorno multihilo
def worker(logger, message):
    logger.log(message)
"""

# Uso del Logger Singleton en un entorno multihilo
logger1 = Logger("app.log")
logger1.log("Este es el primer mensaje de log.")

"""
# Creamos varios hilos que usan el mismo Logger
threads = []
for i in range(5):
    thread = threading.Thread(
        target=worker, args=(logger1, f"Mensaje desde el hilo {i+1}")
    )
    threads.append(thread)
    thread.start()

# Esperamos a que todos los hilos terminen
for thread in threads:
    thread.join()

# Verificamos si todas las instancias son la misma
logger2 = Logger()
print(logger1 is logger2)  # Output: True
"""
