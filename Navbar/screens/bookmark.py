from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Bookmark(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/bookmark.kv")
        super().__init__(**kwargs)