import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder



kivy.require('1.9.0')

Window.size=393,750


Builder.load_file('LenConverter.kv')


class CalCon_kv(GridLayout): 
    pass

class CalcGridlayout(GridLayout):
  # display function
    def update_display(self, text):
        self.display.text += text

#calculate function
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error' 


#drop_down menu
class Dropdown():
    dropdown = DropDown()
    for index in range(4):
        btn = Button(text ='Value % d' % index, size_hint_y = None, height = 40)
        btn.bind(on_release = lambda btn: dropdown.select(btn.text))
        mainbutton = Button(text ='Hello', size_hint =(None, None), pos =(350, 300))
        mainbutton.bind(on_release = dropdown.open)
        dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
        dropdown.add_widget(btn)



class ConverterGridlayout(GridLayout):
    def display(self):
        self.display.text+=text


class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(CalcGridlayout())
        self.add_widget(layout)

class ConverterScreen(Screen):
    def __init__(self,**kwargs):
        super(ConverterScreen,self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(ConverterGridlayout())
        self.add_widget(layout)
        
       

class MainScreen(Screen):
    pass

class CalConApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        sm.add_widget(ConverterScreen(name='length_converter'))
        return sm

    def switch_to_calculator(self):
        self.root.current = 'calculator'

    def switch_to_length_converter(self):
        self.root.current = 'length_converter'    

if __name__ == '__main__':
    CalConApp().run()

