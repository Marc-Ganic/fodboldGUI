# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("300x150")

        def OptionMenu_Select(event):
            self.label.config(text = "Hej " + self.clicked.get() + " indtast ønskede indbetaling")
            self.label.pack(pady = (5, 0))

        # datatype of menu text
        self.clicked = StringVar()

        # initial menu text
        self.clicked.set("Vælg Spiller")

        self.names = list(self.master.fodboldtur.keys())

        OptionMenu(self.payWindow, self.clicked, *self.names, command = OptionMenu_Select).pack(pady = (5, 0))

        # Create Label
        self.label = Label(self.payWindow, text = "")
        self.label.pack()

        self.money = Entry(self.payWindow)
        self.money.pack(pady = (5, 0))

        self.button = Button(self.payWindow, text = "Betal", command=lambda: [self.addMoney(), self.belowZero()])
        self.button.pack(pady = (5, 0))

    def belowZero(self): #todo. her vil jeg tjekke at spillerene ikke prøver at indsende negative beløb
        try:
            amount = int(self.money.get()) < 0 #Error if input is less then 0
        except:
            messagebox.showerror(parent = self.payWindow, title = "Beløb fejl!", message = "Prøv igen.\nKun Positive Beløb Tilladt!")
            return

    def addMoney(self):
        try:
            amount = int(self.money.get()) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent = self.payWindow , title = "Beløb fejl!", message = "Prøv igen.\nKun Hele Tal!")
            return

        self.master.fodboldtur[self.clicked.get()] += amount
        self.master.total = sum(self.master.fodboldtur.values())
        print(f"TOTAL {self.master.total}")
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        self.master.gemFilen()