import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button


kivy .require('1.9.0')

Config.set('graphics', 'width', '80')
Config.set('graphics', 'height', '400')

class CalcGridlayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display.text='Error'

class CalConApp(App):
    def build(self):
        return CalcGridlayout()

calcApp = CalConApp()
calcApp.run()

