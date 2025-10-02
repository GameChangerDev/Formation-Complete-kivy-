from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.factory import Factory

# Enregistrement de widgets customisés
#@Factory.register
class PrimaryButton(Button):
    background_normal = (0.2, 0.6, 1, 1)
Factory.register("PrimaryButton", cls=PrimaryButton)

#@Factory.register
class HeaderLabel(Label):
    font_size = 24
Factory.register('HeaderLabel', cls=HeaderLabel)
