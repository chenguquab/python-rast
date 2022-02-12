from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(App):

    def build(self):
        main_layout     = BoxLayout(orientation='vertical', padding=30)
        h_layout        = BoxLayout(orientation='horizontal')
        v_layout        = BoxLayout(orientation='vertical')
        main_layout.add_widget(h_layout)
        main_layout.add_widget(v_layout)


        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")
        h_layout.add_widget(btn1)
        h_layout.add_widget(btn2)
        h_layout.add_widget(btn3)

        btn4 = Button(text="Button 4")
        btn5 = Button(text="Button 5")
        btn6 = Button(text="Button 6")
        v_layout.add_widget(btn4)
        v_layout.add_widget(btn5)
        v_layout.add_widget(btn6)

        return main_layout

BoxLayoutExample().run()