from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder

# You could also put the following in your kv file...
kv = '''
<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragLabel:
        size_hint: 0.25, 0.2
        text: 'Drag me'
'''

# essai du TouchRippleButtonBehavior
element_kv ="""
<DragButton@TouchRippleButtonBehavior+Label>
    drag_rectangle: self.x, self.y, self.width, self.height
    ripple_color: (1, 0.1, 0.05, 1)
    on_press: print(f"{self.text} : préssé")
"""

Builder.load_string(element_kv)
from kivy.factory import Factory
btn = Factory.DragButton(text="franklin", size_hint=(0.10, 0.10), pos_hint={"top":0.5, "right": 0.5})
print(btn.drag_rectangle)

# essai du drag
class DragLabel(DragBehavior, Label):
    pass


class TestApp(App):
    def build(self):
        return btn


#TestApp().run()

# le DragBehavior est le comportement du toucher - déplacer combiné avec un widget il permet de le bourge

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior


class MyButton(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'atlas://data/images/defaulttheme/checkbox_on'
        else:
            self.source = 'atlas://data/images/defaulttheme/checkbox_off'


class SampleApp(App):
    def build(self):
        return MyButton()


SampleApp().run()
