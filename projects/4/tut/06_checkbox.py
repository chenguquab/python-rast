from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()

    def init_ui(self):

        self.check1=IntVar()
        self.check2=IntVar()

        check1 = Checkbutton(self, text="Male", variable=self.check1)
        check2 = Checkbutton(self, text="female", variable=self.check2)

        check1.grid(column=0, row=0, sticky=W)
        check2.grid(column=0, row=1, sticky=W)

        button = Button(self, text="submit", command=self.checked)
        button.grid(column=0, row=2)

    def checked(self):
        print(self.check1.get())
        print(self.check2.get())

window = Root()
window.mainloop()