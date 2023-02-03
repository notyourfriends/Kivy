from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.screenmanager import ScreenManager
from .settings import Setting
from .calc import Calc
from .login import Login

class Login_scr(Login):
    name = 'login'

class Calc_scr(Calc):
    name = 'calc'

class Setting_scr(Setting):
    name = 'setting'

class Navbar(CommonElevationBehavior, MDFloatLayout):
    pass

class MyScreen(ScreenManager):
    pass

class Home(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/home.kv")
        super().__init__(**kwargs)
        self.btn1 = 0
        self.btn2 = 0
        self.btn3 = 0

    def setting_btn(self):
        if self.btn1 == 0:
            self.ids.myscr.add_widget(Setting_scr())
            self.btn1 += 1
        else:
            pass
    
    def calc_btn(self):
        if self.btn2 == 0:
            self.ids.myscr.add_widget(Calc_scr())
            self.btn2 += 1
        else:
            pass
    
    def login_btn(self):
        if self.btn3 == 0:
            self.ids.myscr.add_widget(Login_scr())
            self.btn3 += 1
        else:
            pass

    def navbar_click(self, instance):
        if instance in self.ids.values():
            current_id = list(self.ids.keys())[list(self.ids.values()).index(instance)]
        for i in range(3):
            if f'btn{i+1}'== current_id:
                self.ids[f'btn{i+1}'].text_color = 1,0,0,1
            else:
                self.ids[f'btn{i+1}'].text_color = 0,0,0,1
            