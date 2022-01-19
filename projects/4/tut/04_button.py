from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()
        self.count = 0


    def init_ui(self):
        '''
        button1 = Button(self, text="Submit")
        button1.grid(column=0,row=0)
        '''
        button1 = ttk.Button(self, text="Submit", command=self.button_click)
        button1.grid(column=1,row=0)

        self.label1 = ttk.Label(self, text="A new label")
        self.label1.grid(column=0, row=0)

    def button_click(self):
        self.count += 1
        self.label1.configure(text=self.count)

window = Root()
window.mainloop()