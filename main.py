# importing tkinter module
import pickle
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *   #progressba

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass
from sumWindow import sumWindowClass
class mainWindow:
    def __init__(self):
        # Setup Pickle File
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        self.total = 0
        # creating tkinter window
        self.root = Tk()

        try:
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except:
            messagebox.showerror(parent=self.root, title="Fil Fejl", message="Filen kunne ikke findes")
            #todo: åben filen
        print(self.fodboldtur)
        self.total = sum(self.fodboldtur.values())
        print(f"TOTAL {self.total}")

        self.players = len(self.fodboldtur.keys())
        self.personalTarget = 4500
        self.target = self.personalTarget * self.players

        # Text
        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx=20)

        listButton = Button(self.root,text ="Hver Spillers Indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        SumButton = Button(self.root, text="Liste Over Alle Indbetalinger", command=lambda: sumWindowClass(self))
        SumButton.pack(padx=20, pady=10, side=LEFT)

        #todo: tilføj knap til en liste med alle indsendte beløb for alle spillere (måske under "listbutton"/listWindow)

        # infinite loop
        mainloop()

    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("Gemt")

if __name__ == '__main__':
    main = mainWindow()