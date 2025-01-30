from tkinter import messagebox
import re
from tkinter import *
from colores import *


def verLicencia():
    messagebox.showinfo(title="Licencia Libre", message="Primera App esta bajo un lincencia GNU")

def acercaDe():
    messagebox.showwarning(title="Primer app", message="Primer App version 0.1")

def salirQuestion():
    valor = messagebox.askquestion(title="Salir de la App", message="Estas Seguro que desas salir de la app")
    if valor == "yes":
        root.destroy()

    valor = messagebox.askokcancel(title="Salir de la App", message="Estas Seguro que desas salir de la app")
    if valor == True:
        root.destroy()

def cerrarDoc():
    valor = messagebox.askretrycancel(
        title="Reintentar", message="no es posible cerrar el documento"
    )

def pruebaMessage():
    messagebox.IGNORE()


def validate_number_input(P):
    # Verifica si el nuevo texto es un número o está vacío
    return P.isdigit() or P == ""


def validate_letter_input(P):
    # Verifica si el nuevo texto es una letra o está vacío
    return P.isalpha() or P == ""


def validate_alphanumeric_input(P):
    # Verifica si el nuevo texto es alfanumérico o está vacío
    return P.isalnum() or P == ""


def validate_input_letter(P):
    # Expresión regular que permite letras, números y espacios
    pattern = r"^[a-zA-Z\s\-]*$"
    # Verifica si el nuevo texto coincide con el patrón
    return bool(re.match(pattern, P))


def validate_input_number(P):
    # Expresión regular que permite letras, números y espacios
    pattern = r"^[0-9\-]*$"
    # Verifica si el nuevo texto coincide con el patrón
    return bool(re.match(pattern, P))


def validate_input_alphanum(P):
    # Expresión regular que permite letras, números y espacios
    pattern = r"^[a-zA-Z0-9\s\-]*$"
    # Verifica si el nuevo texto coincide con el patrón
    return bool(re.match(pattern, P))


root = Tk()
# Registrar la función de validación
validate_number_cmd = root.register(validate_number_input)

# Registrar la función de validación
validate_letter_cmd = root.register(validate_letter_input)

# Registrar la función de validación
validate_alphanumeric_cmd = root.register(validate_alphanumeric_input)

# Registrar la función de validación
validate_cmd_alphanum = root.register(validate_input_alphanum)
# Registrar la función de validación
validate_cmd_letter = root.register(validate_input_letter)
# Registrar la función de validación
validate_cmd_number = root.register(validate_input_number)
root.title("Ventana Pruebas")
# root.geometry("800x500")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\nicos92\Documents\python\interfaces graficas\alien-8bit.ico")
root.config(bg=MisColores.White)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


# * barra de menu
barraMenu = Menu(master=root)
root.config(menu=barraMenu)

archivoMenu = Menu(master=barraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=salirQuestion)

edicionMenu = Menu(master=barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_command(label="Deshacer")

herramientasMenu = Menu(master=barraMenu, tearoff=0)
herramientasMenu.add_command(label="Fuente")
herramientasMenu.add_command(label="Prueba MB", command=pruebaMessage)

ayudaMenu = Menu(master=barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=verLicencia)
ayudaMenu.add_command(label="Acerca de...",command=acercaDe)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

topFrame = Frame(master=root, height=50, bg=MisColores.White, padx=16, pady=16)
topFrame.pack(fill="x")
imagen = PhotoImage(
    master=topFrame,
    file=r"C:\Users\nicos92\Documents\python\interfaces graficas\info16.png",
)

titulo = Label(
    master=topFrame,
    text="Primer App",
    bg=MisColores.White,
    fg=MisColores.Black,
    font=("Hack Nerd Font", 12, "normal"),
)  # , image=imagen)
titulo.pack()

# * MAIN FRAME
mainFrame = Frame(master=root, width="800", height="450", bg=MisColores.White, padx=20, pady=20)
mainFrame.config(relief="flat", bd=2)
mainFrame.pack(fill="both")
# ? STRING VARS
nombre = StringVar()
apellido = StringVar()
direccion= StringVar()
password=StringVar()
comentario=StringVar()
# * Nombre
labelNombre = Label(
    master=mainFrame,
    text="Nombre: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelNombre.grid(row=0, column=0, sticky="e")

txtNombre = Entry(
    master=mainFrame,
    textvariable=nombre,
    bg=MisColores.Light,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    validate="key",
    validatecommand=(validate_cmd_letter, "%P"),
)
txtNombre.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# * Apellido
labelApellido = Label(
    master=mainFrame,
    text="Apellido: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelApellido.grid(row=1, column=0, sticky="e")
txtApellido = Entry(
    master=mainFrame,
    textvariable=apellido,
    bg=MisColores.Light,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    validate="key",
    validatecommand=(validate_cmd_letter, "%P"),
)
txtApellido.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

# * Direccion
labelDireccion = Label(
    master=mainFrame,
    text="Direccion: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelDireccion.grid(row=2, column=0, sticky="e")


txtDireccion = Entry(
    master=mainFrame,
    textvariable=direccion,
    bg=MisColores.Light,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    validate="key",
    validatecommand=(validate_cmd_alphanum, "%P"),
)

txtDireccion.grid(row=2, column=1, sticky="ew", padx=10, pady=10)


# * password
labelPassword = Label(
    master=mainFrame,
    text="Password: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)

labelPassword.grid(row=3, column=0, sticky="e")


txtPassword = Entry(
    master=mainFrame,
    textvariable=password,
    bg=MisColores.Light,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    show="?",
)
txtPassword.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

# * comentarios
labelComentarios = Label(
    master=mainFrame,
    text="comentarios: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelComentarios.grid(row=4, column=0, sticky="n")


txtcomentarios = Text(
    master=mainFrame,
    bg=MisColores.Light,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    width=40,
    height=10,
    max=4,
    maxundo=4,
)
txtcomentarios.grid(row=4, column=1)

miScroll = Scrollbar(master=mainFrame, command=txtcomentarios.yview)
miScroll.grid(row=4,column=2, sticky="nsew")
txtcomentarios.config(yscrollcommand=miScroll.set)


def Eventoboton():
    nombre.set("")
    apellido.set("")
    direccion.set("")
    password.set("")
    txtcomentarios.delete("1.0","end")
    txtNombre.focus()
    print(radioOpcion.get())

miButton = Button(
    master=mainFrame,
    text="Enviar",
    bg=MisColores.Success,
    foreground=MisColores.Light,
    font=("Hack Nerd Font", 12, "normal"),
    command=Eventoboton
)
miButton.grid(row=5,column=1, sticky="ew", padx=8, pady=8)

# * radio boton
radioOpcion = BooleanVar()

labelGenero = Label(
    master=mainFrame,
    text="Genero: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelGenero.grid(row=0, column=3, sticky="e")

masculino = Radiobutton(
    master=mainFrame,
    text="Masculino",
    variable=radioOpcion,
    value=False,
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
)
masculino.grid(row=0, column=4)
femenino = Radiobutton(
    master=mainFrame,
    text="Femenino",
    variable=radioOpcion,
    value=True,
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
)
femenino.grid(row=0,column=5)

# * DESTINOS

labelDestino = Label(
    master=mainFrame,
    text="Destinos: ",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)

labelDestino.grid(row=1, column=3, sticky="e")

ckplaya = BooleanVar()
ckbosque = BooleanVar()
ckmontania = BooleanVar()
destinos = StringVar()
destinos.set("Mis destinos")


def mostrarDestinos():
    laplaya = "La Playa " if ckplaya.get() else ""
    lamontania = " La Montaña " if ckmontania.get() else ""
    elbosque = " El Bosque" if ckbosque.get() else ""
    destinos.set("{}{}{}".format(laplaya, lamontania, elbosque))


playa = Checkbutton(
    master=mainFrame,
    text="Playa",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    variable=ckplaya,
    onvalue=True,
    offvalue=False,
    command=lambda:mostrarDestinos(),
)
playa.grid(row=2, column=3, sticky="wens")

montania = Checkbutton(
    master=mainFrame,
    text="Montania",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    variable=ckmontania,
    onvalue=True,
    offvalue=False,
    command=lambda: mostrarDestinos(),
)
montania.grid(row=2, column=4, sticky="wens")

bosque = Checkbutton(
    master=mainFrame,
    text="Bosque",
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    variable=ckbosque,
    onvalue=True,
    offvalue=False,
    command=lambda:mostrarDestinos()
)
bosque.grid(row=2, column=5, sticky="wens")


labelMostrarDestinos = Label(
    master=mainFrame,
    textvariable=destinos,
    bg=MisColores.White,
    foreground=MisColores.Black,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)

labelMostrarDestinos.grid(row=3, column=3, sticky="wens")

txtNombre.focus()
root.mainloop()
