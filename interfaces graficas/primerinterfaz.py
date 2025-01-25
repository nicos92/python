import re
from tkinter import Tk,Frame,Label,Entry,Text,Button,PhotoImage,Scrollbar,StringVar

azulBG = "#F3F7F9"
azulBG2 = "#002233"
colorLetra = "#121212"
colorLetra2 = "#f3f7f9"


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
root.config(bg="#010101")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

topFrame = Frame(master=root, height=50, bg=azulBG2, padx=16, pady=16)
topFrame.pack(fill="x")
imagen = PhotoImage(
    master=topFrame,
    file=r"C:\Users\nicos92\Documents\python\interfaces graficas\info16.png",
)

titulo = Label(
    master=topFrame,
    text="Primer App",
    bg=azulBG2,
    fg=colorLetra2,
    font=("Hack Nerd Font", 12, "normal"),
)  # , image=imagen)
titulo.pack()

# * MAIN FRAME
mainFrame = Frame(master=root, width="800", height="450", bg=azulBG, padx=20, pady=20)
mainFrame.config(width="800", height="450", bg=azulBG, relief="flat", bd=2)
mainFrame.pack(fill="both")
#? STRING VARS
nombre = StringVar()
apellido = StringVar()
direccion= StringVar()
password=StringVar()
comentario=StringVar()
# * Nombre
labelNombre = Label(
    master=mainFrame,
    text="Nombre: ",
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelNombre.grid(row=0, column=0, sticky="e")

txtNombre = Entry(
    master=mainFrame,
    textvariable=nombre,
    bg=azulBG,
    foreground=colorLetra,
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
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelApellido.grid(row=1, column=0, sticky="e")
txtApellido = Entry(
    master=mainFrame,
    textvariable=apellido,
    bg=azulBG,
    foreground=colorLetra,
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
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelDireccion.grid(row=2, column=0, sticky="e")


txtDireccion = Entry(
    master=mainFrame,
    textvariable=direccion,
    bg=azulBG,
    foreground=colorLetra,
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
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)

labelPassword.grid(row=3, column=0, sticky="e")


txtPassword = Entry(
    master=mainFrame,
    textvariable=password,
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    show="?",
)
txtPassword.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

# * comentarios
labelComentarios = Label(
    master=mainFrame,
    text="comentarios: ",
    bg=azulBG,
    foreground=colorLetra,
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelComentarios.grid(row=4, column=0, sticky="n")


txtcomentarios = Text(
    master=mainFrame,
    bg="#fdfdfd",
    foreground=colorLetra,
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

miButton = Button(
    master=mainFrame,
    text="Enviar",
    bg="#0C3950",
    foreground=colorLetra2,
    font=("Hack Nerd Font", 12, "normal"),
    command=Eventoboton
)
miButton.grid(row=5,column=1, sticky="ew", padx=8, pady=8)

txtNombre.focus()
root.mainloop()
