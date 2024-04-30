from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty





Config.set('graphics', 'resizable', 'True')


Builder.load_file('LenConverter.kv')
Builder.load_file('Currency.kv')

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

class CurrencyConverterGridlayout(GridLayout):
    pass

    

    '''
    
    Spinner_id_one = ObjectProperty()
    Spinner_id_two = ObjectProperty()
    currecy_ip = ObjectProperty()
    result_label = ObjectProperty()


    conversion_rates = {
            'USD': 1.0,
            'EUR': 0.85,  # Example conversion rate, you can add more
            'GBP': 0.75,
            'INR': 110.0,
        }

    def convert(self):
        try:
            input_value = float(self.display.text)
            input_currency = self.Spinner_id_one.values
            output_currency = self.Spinner_id_two.values 
            converted_value = self.perform_conversion(input_value, input_currency, output_currency)
            self.output_unit.text = str(converted_value)
        except ValueError:
            self.output_unit.text = 'Invalid input'


    def perform_conversion(self, input_value, input_currency, output_currency):
        # Define conversion rates
        conversion_rates = {
            'USD': 1.0,
            'EUR': 0.85,  # Example conversion rate, you can add more
            'GBP': 0.75,
            'INR': 110.0,
        }

        # Perform conversion
        input_in_usd = input_value / conversion_rates[input_currency]
        output_value = input_in_usd * conversion_rates[output_currency]

        return output_value
    
    def convert(self,values):
        from_currency = self.Spinner_id_one.values
        to_currency = self.Spinner_id_two.values  # Change to your desired target currency
        amount_str = self.amount_input.values

        try:
            amount = float(amount_str)
        except ValueError:
            self.result_label.values = "Invalid amount"
            return

        # Your currency conversion logic here
        # Replace this line with actual conversion logic
        converted_amount = amount * conversion_rates() # Example conversion rate for USD to EUR

        self.result_label.text =amount_str
'''
    
    

class ConverterGridlayout(GridLayout):
    pass
    '''
    def __init__(self, **kwargs):
        super(ConverterGridlayout, self).__init__(**kwargs)
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
        '''
    
class TempConverterGridlayout(GridLayout):
    pass
    
    '''
    conversion_rates = {
        'Celsius': {'Celsius': 1, 'Fahrenheit': 9/5, 'Kelvin': 1},
        'Fahrenheit': {'Celsius': 5/9, 'Fahrenheit': 1, 'Kelvin': 5/9},
        'Kelvin': {'Celsius': 1, 'Fahrenheit': 9/5, 'Kelvin': 1},
    }

    def __init__(self, **kwargs):
        super(TempConverterGridlayout, self).__init__(**kwargs)
        self.input_unit = TextInput(hint_text='Input', multiline=False)
        self.add_widget(self.input_unit)
        self.input_dropdown = DropDown()
        self.output_dropdown = DropDown()

        for unit in self.conversion_rates.keys():
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
            self.output_unit.text = str(round(converted_value, 2))  # Round to 2 decimal places
        except ValueError:
            self.output_unit.text = 'Invalid input'

    def perform_conversion(self, input_value, input_unit, output_unit):
        # Perform temperature conversion based on the conversion_rates dictionary
        input_in_base = input_value * self.conversion_rates[input_unit][output_unit]
        return input_in_base
    '''

class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(CalcGridlayout())
        self.add_widget(layout)

class ConverterScreen(Screen):
    def __init__(self, **kwargs):
        super(ConverterScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(ConverterGridlayout())
        self.add_widget(layout)
        
class CurrencyConverterScreen(Screen):
    def __init__(self, **kwargs):
        super(CurrencyConverterScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(CurrencyConverterGridlayout())
        self.add_widget(layout)

class TempConverterScreen(Screen):
    def __init__(self, **kwargs):
        super(TempConverterScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(TempConverterGridlayout())
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
        sm.add_widget(TempConverterScreen(name='temp_converter'))
        return sm
#Home Screen navigation Buttons objects

    def switch_to_calculator(self):
        self.root.current = 'calculator'

    def switch_to_length_converter(self):
        self.root.current = 'length_converter'

    def switch_to_currency_converter(self):
        self.root.current = 'currency_converter'

    def switch_to_temp_converter(self):
        self.root.current = 'temp_converter'

if __name__ == '__main__':
    CalConApp().run()
