from tkinter import *
from turtle import back

'''
class Root(Tk):
    pass

window = Root()
window.mainloop()
'''

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("hooloo accounting app")
        self.minsize(640,320)
        self.configure(background="#3d3d3d")

window = Root()
window.mainloop()