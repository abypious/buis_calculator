import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.9.0')

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class CalcGridlayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'

class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(CalcGridlayout())
        self.add_widget(layout)

class MainScreen(Screen):
    pass

class CalConApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        return sm

if __name__ == '__main__':
    CalConApp().run()