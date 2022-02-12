from kivy.app import App
from kivy.lang import Builder

my_kv = Builder.load_string('''
Label:
    text: "[b]Hello [color=#660730]World[/color] [/b]"
    markup: True
''')

class HelloWorld(App):
    def build(self):
        return my_kv

HelloWorld().run()