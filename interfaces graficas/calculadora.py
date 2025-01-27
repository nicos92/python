from tkinter import *
from tkinter import ttk
from botones import *
from colores import *
import re


# * agrega el ultimo numero pulsado
def numeroPulsado(num:str):
    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        operacion=""
    else:    
        if numeroPantalla.get() == "0":
            numeroPantalla.set("")
            numeroPantalla.set(numeroPantalla.get()+num)
        else:
            numeroPantalla.set(numeroPantalla.get()+num)


# * elimina el ultimo caracter del cuadro de texto
def eliminar_ultimo_caracter():
    # Obtener el valor actual del StringVar
    valor_actual = numeroPantalla.get()

    # Verificar que el valor no esté vacío
    if valor_actual:
        # Eliminar el último carácter
        nuevo_valor = valor_actual[:-1]

        # Actualizar el StringVar con el nuevo valor
        numeroPantalla.set(nuevo_valor)

# * valida que la entrada de texto sea siempre un numero
def validate_input_number(P):
    # Expresión regular que permite letras, números y espacios
    pattern = r"^[0-9\-.\+\*/\%]*$"
    # Verifica si el nuevo texto coincide con el patrón
    return bool(re.match(pattern, P))

def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

def elResultado():
    global resultado
    resultado += int(numeroPantalla.get())
    numeroPantalla.set(resultado)
    resultado=0

# * variables globales
operacion = ""
resultado =0

#* comienzo de la ventana
root = Tk()



root.config(bg=MisColores.Black)
validarNumeros = root.register(validate_input_number)
# * PULSACION DE BOTON
numeroPantalla= StringVar()
numeroPantalla.set("0")

# * TOP FRAME CUENTA


topFrame = Frame(master=root, width=200, height=100, padx=16, pady=16, bg=MisColores.Black)
topFrame.pack()


cuadroCuenta = Entry(
    master=topFrame,
    textvariable=numeroPantalla,
    justify="right",
    font=("BigBlueTerm437 Nerd font", 18, "normal"),
    bg=MisColores.Black,
    foreground=MisColores.verdeConsola,
    validate="key",
    validatecommand=(validarNumeros, '%P'),
)
cuadroCuenta.pack()


# * MAIN FRAME BOTONES
mainFrame = Frame(
    master=root,
    width=200,
    height=300,
    padx=16,
    pady=16,
    bg=MisColores.Black
)
mainFrame.pack()
s = ttk.Style()
s.configure(
    "MyButton.TButton",
    padding=0,
    font=("Hack Nerd Font", 12, "normal"),
    anchor="ns",
)

# * BOTONES
# * FILA 0
mc = MiButtonNumerico(
    masters=mainFrame,
    texts="MC",
    stickys="wens",
    rows=0,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal")
)
mr = MiButtonNumerico(
    masters=mainFrame,
    texts="MR",
    stickys="wens",
    rows=0,
    columns=1,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
ms = MiButtonNumerico(
    masters=mainFrame,
    texts="MS",
    stickys="wens",
    rows=0,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
mmas = MiButtonNumerico(
    masters=mainFrame,
    texts="M+",
    stickys="wens",
    rows=0,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
mmenos = MiButtonNumerico(
    masters=mainFrame,
    texts="M-",
    stickys="wens",
    rows=0,
    columns=4,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)

# * FILA 1

back = MiButtonNumerico(
    masters=mainFrame,
    texts="\uf060",
    stickys="wens",
    rows=1,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("Symbols Nerd font", 14, "normal"),
    command1= eliminar_ultimo_caracter
)
CE = MiButtonNumerico(
    masters=mainFrame,
    texts="CE",
    stickys="wens",
    rows=1,
    columns=1,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
C = MiButtonNumerico(
    masters=mainFrame,
    texts="C",
    stickys="wens",
    rows=1,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
masMenos = MiButtonNumerico(
    masters=mainFrame,
    texts="\udb82\udd92",
    stickys="wens",
    rows=1,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("Symbols Nerd font", 14, "normal"),
)
raizCuadrada = MiButtonNumerico(
    masters=mainFrame,
    texts="\ueee0",
    stickys="wens",
    rows=1,
    columns=4,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("Symbols Nerd font", 14, "normal"),
    command1=lambda:print("holisolis")
)
# * FILA 2

siete = MiButtonNumerico(
    masters=mainFrame,
    texts="7",
    stickys="wens",
    rows=2,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda:numeroPulsado("7")
)
ocho = MiButtonNumerico(
    masters=mainFrame,
    texts="8",
    stickys="wens",
    rows=2,
    columns=1,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("8"),
)
nueve = MiButtonNumerico(
    masters=mainFrame,
    texts="9",
    stickys="wens",
    rows=2,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("9"),
)
dividir = MiButtonNumerico(
    masters=mainFrame,
    texts="\uedf3",
    stickys="wens",
    rows=2,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("Symbols Nerd font", 14, "normal"),
)
porciento = MiButtonNumerico(
    masters=mainFrame,
    texts="%",
    stickys="wens",
    rows=2,
    columns=4,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
# * FILA 3

cuatro = MiButtonNumerico(
    masters=mainFrame,
    texts="4",
    stickys="wens",
    rows=3,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("4"),
)
cinco = MiButtonNumerico(
    masters=mainFrame,
    texts="5",
    stickys="wens",
    rows=3,
    columns=1,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("5"),
)
seis = MiButtonNumerico(
    masters=mainFrame,
    texts="6",
    stickys="wens",
    rows=3,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("6"),
)
multiplicar = MiButtonNumerico(
    masters=mainFrame,
    texts="\udb80\udf82",
    stickys="wens",
    rows=3,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("Symbols Nerd font", 14, "normal"),
)
unoSobreX = MiButtonNumerico(
    masters=mainFrame,
    texts="1/x",
    stickys="wens",
    rows=3,
    columns=4,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
# * FILA 4

uno = MiButtonNumerico(
    masters=mainFrame,
    texts="1",
    stickys="wens",
    rows=4,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("1"),
)
dos = MiButtonNumerico(
    masters=mainFrame,
    texts="2",
    stickys="wens",
    rows=4,
    columns=1,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("2"),
)
tres = MiButtonNumerico(
    masters=mainFrame,
    texts="3",
    stickys="wens",
    rows=4,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("3"),
)
menons = MiButtonNumerico(
    masters=mainFrame,
    texts="-",
    stickys="wens",
    rows=4,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
igual = MiButtonNumerico(
    masters=mainFrame,
    texts="=",
    stickys="wens",
    rows=4,
    columns=4,
    padxs=2,
    padys=2,
    rowspan1=2,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda:elResultado()
)
# * FILA 5

cero = MiButtonNumerico(
    masters=mainFrame,
    texts="0",
    stickys="wens",
    rows=5,
    columns=0,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=2,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda: numeroPulsado("0"),
)
coma = MiButtonNumerico(
    masters=mainFrame,
    texts=",",
    stickys="wens",
    rows=5,
    columns=2,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
)
mas = MiButtonNumerico(
    masters=mainFrame,
    texts="+",
    stickys="wens",
    rows=5,
    columns=3,
    padxs=2,
    padys=2,
    rowspan1=1,
    columspan1=1,
    font1=("BigBlueTerm437 Nerd font", 14, "normal"),
    command1=lambda:suma(numeroPantalla.get())
)


"""
# *  no se usa, es un boton con imagen
# Crear un botón con texto
boton_texto = Button(root, text="Texto del botón")
imagen = PhotoImage(file="interfaces graficas\info48.png")
boton_texto_imagen = Button(root, text="Texto del botón", image=imagen, compound="left")
# Crear un botón con texto y una imagen

boton_texto.pack()
boton_texto_imagen.pack()
"""

root.mainloop()
