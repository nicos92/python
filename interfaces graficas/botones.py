from tkinter import *
from colores import *


class MiButtonNumerico:
    def __init__(
        self,
        masters: Tk,
        texts: str,
        stickys: str,
        rows: int,
        columns: int,
        padxs: int,
        padys: int,
        rowspan1: int,
        columspan1: int,
        font1= ("Hack Nerd Font", 12, "normal"),
        command1 = lambda:None
    ):
        return Button(
            master=masters,
            text=texts,
            bg=MisColores.Black,
            foreground=MisColores.White,
            font=font1,
            command=command1
        ).grid(
            row=rows,
            column=columns,
            sticky=stickys,
            padx=padxs,
            pady=padys,
            columnspan=columspan1,
            rowspan=rowspan1,
        )
    
class MiButton:
    def __init__(
        self,
        masters: Tk,
        texts: str,
        stickys: str,
        rows: int,
        columns: int,
        padxs: int,
        padys: int,
        rowspan1: int,
        columspan1: int,
        font1:tuple
    ):
        return Button(
            master=masters,
            text=texts,
            bg=MisColores.Black,
            foreground=MisColores.White,
            font=font1
        ).grid(
            row=rows,
            column=columns,
            sticky=stickys,
            padx=padxs,
            pady=padys,
            columnspan=columspan1,
            rowspan=rowspan1,
        )
    
