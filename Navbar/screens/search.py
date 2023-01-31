from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Search(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/search.kv")
        super().__init__(**kwargs)