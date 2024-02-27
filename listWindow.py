# importing tkinter module
from tkinter import *

class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("300x100")

        self.title = Label(self.listWindow, text = "Indbetalinger")
        self.title.pack()

        def OptionMenu_Select(event):
            self.label.config(text = f"{self.clicked.get()} har betalt {self.master.fodboldtur[self.clicked.get()]}kr")

        # datatype of menu text
        self.clicked = StringVar()
        # initial menu text
        self.clicked.set("Vælg en Spiller")

        # Dropdown menu
        OptionMenu(self.listWindow, self.clicked, *list(self.master.fodboldtur.keys()) , command=OptionMenu_Select).pack()

        self.label = Label(self.listWindow, text="Ingen spiller valgt")
        self.label.pack(pady = (10, 0))