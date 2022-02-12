from kivy.app import App
from kivy.lang import Builder

my_kv = Builder.load_file('my_kv_file.kv')

class HelloWorld(App):
    def build(self):
        return my_kv

HelloWorld().run()