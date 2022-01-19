from cgitb import text
from tkinter import *
from turtle import circle

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()

    def init_ui(self):

        self.username = StringVar()

        self.label = Label(self, text="Please enter username: ")
        self.label.grid(column=0, row=0)

        entry = Entry(self, textvariable=self.username)
        entry.grid(column=1, row=0)

        button = Button(self, text="Submit", command=self.submit_username)
        button.grid(column=2, row=0)

    def submit_username(self):
        self.label.configure(text = f"your username is: {self.username.get()}")


window = Root()
window.mainloop()