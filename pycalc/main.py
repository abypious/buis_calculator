from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window

Window.size=393,750


Builder.load_file('LenConverter.kv')


class CalCon_kv(GridLayout): 
    pass


#Calcualator class
class CalcGridlayout(GridLayout):
    def update_display(self, text):
        self.display.text += text

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


from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class ConverterGridlayout(GridLayout):
    def __init__(self, **kwargs):
        super(ConverterGridlayout, self).__init__(**kwargs)
        self.cols = 2
        self.input_unit = TextInput(hint_text='Input', multiline=False)
        self.add_widget(self.input_unit)
        self.input_dropdown = DropDown()
        self.output_dropdown = DropDown()

        for unit in ['Millimeters', 'Centimeters', 'Meters', 'Kilometers']:
            input_button = Button(text=unit, size_hint_y=None, height=44)
            input_button.bind(on_release=lambda btn: self.input_dropdown.select(btn.text))
            self.input_dropdown.add_widget(input_button)

            output_button = Button(text=unit, size_hint_y=None, height=44)
            output_button.bind(on_release=lambda btn: self.output_dropdown.select(btn.text))
            self.output_dropdown.add_widget(output_button)

        self.input_unit_button = Button(text='Input', on_release=self.input_dropdown.open)
        self.add_widget(self.input_unit_button)

        self.output_unit_button = Button(text='Output', on_release=self.output_dropdown.open)
        self.add_widget(self.output_unit_button)

        self.input_dropdown.bind(on_select=lambda instance, x: setattr(self.input_unit_button, 'text', x))
        self.output_dropdown.bind(on_select=lambda instance, x: setattr(self.output_unit_button, 'text', x))

        # Define the output_unit TextInput widget
        self.output_unit = TextInput(hint_text='Output', multiline=False)
        self.add_widget(self.output_unit)

        self.convert_button = Button(text='Convert', on_press=self.convert)
        self.add_widget(self.convert_button)

    def convert(self, instance):
        try:
            input_value = float(self.input_unit.text)
            input_unit = self.input_unit_button.text
            output_unit = self.output_unit_button.text
            converted_value = self.perform_conversion(input_value, input_unit, output_unit)
            self.output_unit.text = str(converted_value)
        except ValueError:
            self.output_unit.text = 'Invalid input'

    def perform_conversion(self, input_value, input_unit, output_unit):
        conversion_factors = {
            'Millimeters': 0.001,
            'Centimeters': 0.01,
            'Meters': 1,
            'Kilometers': 1000
        }

        input_in_meters = input_value * conversion_factors[input_unit]
        output_value = input_in_meters / conversion_factors[output_unit]

        return output_value


class ConverterScreen(Screen):
    def __init__(self, **kwargs):
        super(ConverterScreen, self).__init__(**kwargs)
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
        sm.add_widget(CurrencyConverterScreen(name='currency_converter'))
        return sm
#Home Screen navigation Buttons functions
    def switch_to_calculator(self):
        self.root.current = 'calculator'

    def switch_to_length_converter(self):
        self.root.current = 'length_converter'

if __name__ == '__main__':
    CalConApp().run()
