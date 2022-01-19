from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()


    def init_ui(self):
        label1 = Label(self, text="Hello Tk app", bg="#101010", fg="#d5d5d5")
        label2 = Label(self, text="Hello Tk app", bg="#101010", fg="#d5d5d5")
        
        '''
        label2.grid(column=0, row=1)
        label1.grid(column=0, row=0)
        '''
        label1.place(x=20, y=50)
        label2.place(x=20, y=150)

window = Root()
window.mainloop()