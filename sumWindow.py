# importing tkinter module
from tkinter import *

class sumWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.sumWindow = Toplevel(self.master.root)
        self.sumWindow.title("Sum Window")
        self.sumWindow.geometry("300x100")

        self.title = Label(self.sumWindow, text="Alle Inbetalinger")
        self.title.pack()

        self.leftFrame = Frame(self.sumWindow, relief = GROOVE)
        self.leftFrame.pack(side = LEFT, fill=BOTH, expand=True)
        for item in self.master.fodboldtur:
            Label(self.leftFrame, text = item).pack(side = TOP, anchor = "w", padx = (0, 15))

        self.rightFrame = Frame(self.sumWindow, relief = GROOVE)
        self.rightFrame.pack(side = RIGHT, fill=BOTH, expand=True   )
        for key in self.master.fodboldtur.keys():
            Label(self.leftFrame, text = f"{self.master.fodboldtur[key]} / {self.master.personalTarget}").pack(side = TOP, anchor = "w")