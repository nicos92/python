from tkinter import *

raiz = Tk()
raiz.title("Ventana Pruebas")
# raiz.geometry("800x500")
raiz.resizable(False, False)
raiz.iconbitmap(
    r"D:\Users\n.sandoval\Documents\pythonGits\python\interfaces graficas\alien-8bit.ico"
)
raiz.config(bg="#010101")

topFrame = Frame(master=raiz, height=50, bg="#102010")
topFrame.pack(fill="x")
imagen = PhotoImage(master=topFrame, file=r"D:\Users\n.sandoval\Documents\pythonGits\python\interfaces graficas\info16.png")

titulo = Label(master=topFrame, text="Primer App", bg="#102010", fg="#fdfdfd", font=("Hack Nerd Font", 12, "normal")) #, image=imagen)
titulo.pack()
mainFrame = Frame(master=raiz, width="800", height="450", bg="#101010")
mainFrame.config(width="800", height="450", bg="#101010", relief="flat", bd=2)
mainFrame.pack(fill="both")

labelNombre = Label(master=mainFrame, text="Nombre: ", bg="#101010", foreground="#fdfdfd", font=("Hack Nerd Font", 10, "normal"))
labelNombre.grid(row=0,column=0, sticky="w")
labelApellido = Label(
    master=mainFrame,
    text="Apellido: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
)
labelApellido.grid(row=1,column=0,sticky="w")
labelDireccion = Label(
    master=mainFrame,
    text="Direccion: ",
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
)
labelDireccion.grid(row=2, column=0, sticky="w")

txtNombre = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
)
txtNombre.grid(row=0,column=1)

txtApellido = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
)
txtApellido.grid(row=1,column=1)

txtDireccion = Entry(
    master=mainFrame,
    bg="#101010",
    foreground="#fdfdfd",
    font=("Hack Nerd Font", 10, "normal"),
)
txtDireccion.grid(row=2,column=1)

txtNombre.focus()
raiz.mainloop()
