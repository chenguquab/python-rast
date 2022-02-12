from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(App):

    def build(self):
        layout = BoxLayout(orientation='horizontal')

        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")
        btn4 = Button(text="Button 4")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

BoxLayoutExample().run()