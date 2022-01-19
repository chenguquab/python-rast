from tkinter import *
from turtle import back


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()


    def init_ui(self):
        label1 = Label(self, text="Hello Tk app", bg="#101010", fg="#d5d5d5")
        label1.grid(column=0, row=0)
        label2 = Label(self, text="Hello Tk app", bg="#101010", fg="#d5d5d5")
        label2.grid(column=0, row=1)

window = Root()
window.mainloop()