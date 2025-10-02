# Voir les descriptions dans Deepseek et grok apk
# 1. introduction au ColorPicker
# Instanciation de base:
from kivy.tools.pep8checker.pep8 import continued_indentation
from kivy.uix.colorpicker import ColorPicker, ColorWheel

color_picker = ColorPicker()

# 2. propriétés principales     # 3. Personnalisation avancée
# a. Modifier les propriétés graphiques:
color_picker = ColorPicker(
    color=(1, 0, 0, 1), # Couleur initiale (Rouge)
    size_hint=(0.5, 0.5)
)

from kivy.base import runTouchApp, async_runTouchApp
#runTouchApp(color_picker)

# b. Personnaliser la roue chromatique:
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter

class CustomWheel(ColorWheel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_color=self.affiche)
    def affiche(self, *args):
        print(f"R: {self.color[0]}, G: {self.color[1]}, B: {self.color[2]}, A: {self.color[3]}")

class Color(ColorPicker):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.btn = Button(text="Valider", pos_hint={"top":0.98, "right":0.90}, height=20, size_hint=(0.2, None), on_press=self.react)
    def on_color(self, instance, color):
        self.callback(self)
        self.btn.background_color = self.color
        if self.btn not in self.children:
            scat = Scatter()
            scat.add_widget(self.btn)
            self.add_widget(scat)

    def react(self, btn):
        print(self.parent)
        self.parent.remove_widget(self)

color = Color(callback=CustomWheel.affiche, wheel=CustomWheel)
#runTouchApp(color)


scat = Scatter()
scat.do_rotation=True
scat.do_scale = True
btn = Button(text="Merci", size=(100, 50))
scat.add_widget(btn)
#runTouchApp(scat)


# Modifier les sous-widgets en parcourant le children

from kivy.app import App
from kivy.uix.colorpicker import ColorPicker, ColorWheel
from kivy.uix.boxlayout import BoxLayout

class CustomColorPicker(ColorPicker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Accéder à la roue et la personnaliser
        for child in self.children:
            if isinstance(child, ColorWheel):
                child.background_color = [0.2, 0.2, 0.2, 1]     # Fond sombre
                break

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        picker = CustomColorPicker()
        layout.add_widget(picker)
        return layout
#
# if __name__ == '__main__':
#     MyApp().run()

# 4. Gestion des Evénements et buildings
from kivy.app import App
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        picker = ColorPicker()

        def on_color_change(instance, value):
            print(f"Couleur changée : {value}")
            if value[0] > 0.9 and value[1] < 0.1 and value[2] < 0.1:    # Rouge pur interdit
                Clock.schedule_once(lambda dt: setattr(picker, 'color', [0,0,0,1]), 0.1)

        picker.bind(color=on_color_change)

        layout.add_widget(picker)
        return layout

# if __name__ == '__main__':
#     MyApp().run()

# 5. integration avec d'autre widget kivy
# exemple d'intégration avec Canvas:

from kivy.app import App
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        picker = ColorPicker()

        with layout.canvas:
            color_instr = Color(1, 1, 1, 1)
            Rectangle(pos=layout.pos, size=layout.size)

        picker.bind(color=lambda inst, val: setattr(color_instr, 'rgba', val))

        layout.add_widget(picker)
        return layout

# if __name__ == '__main__':
#     MyApp().run()

# 6. Meilleures Pratique avancées
# ----|----


# Projets pratique : Editeur de palette de couleurs
import json
from kivy.app import App
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.clock import Clock

class PaletteColorPicker(ColorPicker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 18
        # Personnalisation de la roue
        for child in self.children:
            if hasattr(child, 'background_color'):
                child.background_color = [0.1, 0.1, 0.1, 1]

class PaletteEditor(BoxLayout):
    palette = ListProperty([])  # Listede couleurs RGBA

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.grid = GridLayout(cols=5, size_hint_y=0.3)
        self.add_widget(self.grid)

        btn_add =  Button(text="Ajouter Couleur")
        btn_add.bind(on_press=self.open_picker)
        self.add_widget(btn_add)

        btn_save = Button(text='Sauvegarder Couleur')
        btn_save.bind(on_press=self.save_palette)
        self.add_widget(btn_save)

        btn_load = Button(text="Charger une palette")
        btn_load.bind(on_press=self.load_palette)
        self.add_widget(btn_load)

    def open_picker(self, instance):
        picker = CustomColorPicker()
        preview = Button(text='Preview', size_hint=(1, 0.2))
        def prev(c):
            preview.background_color = c

        picker.bind(color=lambda inst, value: prev(value))#preview.setter('background_color'))

        content = BoxLayout(orientation='vertical')
        content.add_widget(picker)
        content.add_widget(preview)

        btn_confirm = Button(text='confirmer', size_hint_y=0.1)
        content.add_widget(btn_confirm)

        popup = Popup(title='Selectionner Couleur', content=content, size_hint=(0.8, 0.8))
        popup.open()

        def on_confirm(inst):
            color = picker.color
            if color[0] == 1 and color[1] == 0 and color[2] == 0:   # Validation exemple
                print(f"rouge pur interdit !")
                Clock.schedule_once(lambda dt: setattr(picker, 'color', [0, 0, 0, 1]), 0.1)
            else:
                self.palette.append(color)
                self.update_grid()
                popup.dismiss()

        btn_confirm.bind(on_press=on_confirm)

    def update_grid(self):
        self.grid.clear_widgets()
        for color in self.palette:
            btn = Button(background_color=color)
            self.grid.add_widget(btn)

    def save_palette(self, instance):
        with open("palette.json", 'w') as f:
            json.dump(self.palette, f, indent=3)
        print("Palette enregistrée !")

    def load_palette(self, instance):
        try:
            with open("palette.json", "r") as f:
                self.palette = json.load(f)
            self.update_grid()
            print("Palette chargée !")
        except FileNotFoundError:
            print(f"Aucune palette trouvée.")

class PaletteApp(App):
    def build(self):
        return PaletteEditor()

if __name__ == '__main__':
    PaletteApp().run()