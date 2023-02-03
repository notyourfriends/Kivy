from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Calc(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/calc.kv')
        super().__init__( **kwargs)
    
    def clear(self):
        self.ids.calc_input.text= '0'
    
    def button_press(self, button):
        prior = self.ids.calc_input.text

        if 'ERROR' in prior:
            prior = ''
        
        if prior == '0':
            self.ids.calc_input.text = ' '
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def remove(self):
        prior = self.ids.calc_input.text

        prior = prior[:-1]
        self.ids.calc_input.text = prior
    
    def dot(self):
        prior = self.ids.calc_input.text

        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'.{prior}'
            self.ids.calc_input.text

    def math_sign(self, sign):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'
    
    def pos_neg(self):
        prior = self.ids.calc_input.text

        if '-' in prior:
            self.ids.calc_text = f'{prior.replace("-"," ")}'
        else:
            self.ids.calc_text = f'-{prior}'
