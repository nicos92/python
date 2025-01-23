class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, log_file="app.log"):
        if not self._initialized:
            self.log_file = log_file
            self._initialized = True

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")
        print(f"Log: {message}")


# Uso del Logger Singleton
logger1 = Logger()
logger1.log("Este es el primer mensaje de log.")

logger2 = Logger()  # Intento de crear otra instancia
logger2.log("Este es el segundo mensaje de log.")

# Verificamos si ambas variables apuntan a la misma instancia
print(logger1 is logger2)  # Output: True
