from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Login(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/login.kv')
        super().__init__( **kwargs)

    def logger(self):
        self.ids.welcome_label.text = f'Welcome {self.ids.user.text}'
        #self.ids.success_label.text = f'Welcome {self.ids.user.text}'

    def clear(self):
        self.ids.welcome_label.text = 'Log In'
        self.ids.user.text = ''
        self.ids.pw.text = ''