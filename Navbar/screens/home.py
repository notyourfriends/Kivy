from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.screenmanager import ScreenManager
from .profile import Profile
from .search import Search
from .bookmark import Bookmark

class Profile_scr(Profile):
    name = "profile"

class Search_scr(Search):
    name = "search"
    
class Bookmark_scr(Bookmark):
    name = "bookmark"

class MyNavbar(CommonElevationBehavior, MDFloatLayout):
    pass

class MyScreen(ScreenManager):
    pass

class Home(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/home.kv")
        super().__init__(**kwargs)
        #to avoid warning when clicked multiple times
        #temp data
        self.btn1 =0
        self.btn2 =0
        self.btn3 =0
    
    def search_btn(self):
        if self.btn1 == 0:
            self.ids.myscr.add_widget(Search_scr())
            self.btn1 +=1
        else:
            pass

    def bookmark_btn(self):
        if self.btn2 == 0:
            self.ids.myscr.add_widget(Bookmark_scr())
            self.btn2 +=1
        else:
            pass
        
    def profile_btn(self):
        if self.btn3 == 0:
            self.ids.myscr.add_widget(Profile_scr())
            self.btn3 +=1
        else:
            pass
        

    def navbar_click(self, instance):
        #check list on button
        #print(list(self.ids.keys())) 
        #check list on button by the index
        #print("clicked button", list(self.ids.values()).index(instance)) 
        #check the id of the button
        #print(list(self.ids.keys())[list(self.ids.values()).index(instance)])
        if instance in self.ids.values():
            current_id = list(self.ids.keys())[list(self.ids.values()).index(instance)]
            for i in range(4):
                if f'btn{i+1}'==current_id:
                    self.ids[f'btn{i+1}'].text_color = 1,0,0,1
                else:
                    self.ids[f'btn{i+1}'].text_color = 0,0,0,1