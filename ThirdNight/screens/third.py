from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Third(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/third.kv')
        super().__init__( **kwargs)