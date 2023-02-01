from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Calc(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/calc.kv')
        super().__init__( **kwargs)
    
    def clear(self):
        self.ids.calc_input.text= '0'