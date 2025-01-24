from tkinter import *

raiz = Tk()
raiz.title("Ventana Pruebas")
# raiz.geometry("800x500")
raiz.resizable(False, False)
raiz.iconbitmap(
    r"D:\Users\n.sandoval\Documents\pythonGits\python\interfaces graficas\alien-8bit.ico"
)
raiz.config(bg="#010101")

topFrame = Frame(master=raiz, height=50, bg="#102010", padx=16, pady=16)
topFrame.pack(fill="x")
imagen = PhotoImage(master=topFrame, file=r"D:\Users\n.sandoval\Documents\pythonGits\python\interfaces graficas\info16.png")

titulo = Label(master=topFrame, text="Primer App", bg="#102010", fg="#fdfdfd", font=("Hack Nerd Font", 12, "normal")) #, image=imagen)
titulo.pack()
mainFrame = Frame(master=raiz, width="800", height="450", bg="#101010", padx=20, pady=20)
mainFrame.config(width="800", height="450", bg="#101010", relief="flat", bd=2)
mainFrame.pack(fill="both")

labelNombre = Label(
    master=mainFrame,
    text="Nombre: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelNombre.grid(row=0,column=0, sticky="w")
txtNombre = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    justify= "left"
    
)
txtNombre.grid(row=0,column=1)
labelApellido = Label(
    master=mainFrame,
    text="Apellido: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4,
)
labelApellido.grid(row=1,column=0,sticky="w")
txtApellido = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
)
txtApellido.grid(row=1,column=1)
labelDireccion = Label(
    master=mainFrame,
    text="Direccion: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4
)
labelDireccion.grid(row=2, column=0, sticky="w")
txtDireccion = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
)
txtDireccion.grid(row=2,column=1)
labelPassword = Label(
    master=mainFrame,
    text="Password: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4
)
labelPassword.grid(row=3, column=0, sticky="w")



txtPassword = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    justify="left",
    show="?"
)
txtPassword.grid(row=3,column=1)
labelComentarios = Label(
    master=mainFrame,
    text="comentarios: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    padx=4,
    pady=4
)
labelComentarios.grid(row=4, column=0, sticky="w")



txtcomentarios = Text(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
    width=4,
    height=20,
    max=4,
    maxundo=4
)
txtcomentarios.grid(row=4,column=1)

txtNombre.focus()
raiz.mainloop()
