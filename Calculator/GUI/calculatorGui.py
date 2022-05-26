import kivy
from kivy.app import App
from kivy.uix import label
from kivy.uix import button
from kivy.uix import textinput
from kivy.uix import gridlayout
from kivy.uix.gridlayout import GridLayout


class main_calc(App):
    def build(self):
        return main_grid_layout()


class main_grid_layout(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        # Setting up the first layer.
        self.cols = 1
        self.to_grid = GridLayout()
        self.to_grid.cols = 2
        self.add_widget(self.to_grid)
        # Setting up the Second layer.


if __name__ == '__main__':
    main_calc().run()
