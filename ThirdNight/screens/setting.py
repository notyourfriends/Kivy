from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Setting(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/setting.kv')
        super().__init__( **kwargs)