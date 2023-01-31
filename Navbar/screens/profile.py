from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Profile(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/profile.kv")
        super().__init__(**kwargs)