from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
Label:
    text: "[b]Hello [color=#660730]World[/color] [/b]"
    markup: True
'''))