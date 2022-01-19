from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("My_app")
        self.minsize(640,320)
        self.init_ui()

    def init_ui(self):
        label_frame = LabelFrame(self, text="section title goes here")
        label_frame.grid(column=0, row=0)

        Label(label_frame, text="Label 1").pack()
        Label(label_frame, text="Label 2").pack()
        Label(label_frame, text="Label 3").pack()


window = Root()
window.mainloop()