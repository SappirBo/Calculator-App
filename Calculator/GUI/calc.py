import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from src.MyCalculator import *

# Setting up size of the up
Window.size = (500, 700)
# Setting Up the kv file
Builder.load_file('calc.kv')


class myLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = ''

    # button pressing function
    def button_press(self, button):
        prev = self.ids.calc_input.text
        if prev == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text += f'{button}'
    def GCD(self):
        self.ids.calc_input.text = ''
        self.ids.calc_input.text = 'GCD: '
    def LCM(self):
        self.ids.calc_input.text = ''
        self.ids.calc_input.text = 'LCM: '


    def equal(self):
        input = self.ids.calc_input.text
        if 'GCD' in input and 'G' == input[0]:
            input = input[5:]
            input = input.split(',')
            ans = gcd(int(input[0]),int(input[1]))
            self.ids.calc_input.text = str(ans)
        elif 'LCM' in input and 'L' == input[0]:
            input = input[5:]
            input = input.split(',')
            ans = lcm(int(input[0]),int(input[1]))
            self.ids.calc_input.text = str(ans)
        else:
            pass


    def valid_check(self,num):
        pass
    pass


class clacApp(App):
    def build(self):
        return myLayout()


if __name__ == '__main__':
    clacApp().run()
